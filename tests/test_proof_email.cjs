const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { parseOrder, buildDraft, makeEml, validateAttachments } = require('../tools/proof-email/core.js');
const fields = { order: '#TEST-1', customer: 'Zoë 测试', email: 'test@example.com', runner: 'Zoë', race: 'Test Marathon', date: '2026-09-22', distance: '26.2 mi', location: 'Houston', finishTime: '', style: 'Nocturne', accent: 'Match My Medal Color', piece: 'A', unit: '1', version: 'v1' };
const png = { name: 'render.png', type: 'image/png', bytes: Uint8Array.from([137,80,78,71,13,10,26,10,0,1,2]) };
test('canonical Markdown labels and tables populate only recognized fields', () => {
  const result = parseOrder('# Order\n- **Order Number:** #TEST-1\n**Customer Name**: Zoë\n| Customer Email | test@example.com |\n- Piece Reference: A\nUnit Number: 1\nRandom: ignored\n```\nDate: ignored\n```');
  assert.equal(result.order, '#TEST-1'); assert.equal(result.customer, 'Zoë'); assert.equal(result.email, 'test@example.com'); assert.equal(result.date, '');
});
test('duplicate fields, including multiple-piece records, fail rather than choosing a value', () => {
  assert.throws(() => parseOrder('Piece Reference: A\nPiece Reference: B'), /Duplicate/);
  assert.throws(() => parseOrder('Date: 2026\nDate: 2026'), /Duplicate/);
  assert.throws(() => parseOrder('unrelated'), /No recognized/);
});
test('bundled canonical order sample produces a valid draft without Markdown wrappers', () => {
  const sample = fs.readFileSync(path.join(__dirname, '../tools/proof-email/sample-order.md'), 'utf8');
  const order = parseOrder(sample);
  assert.equal(order.email, 'sample@example.invalid');
  assert.equal(order.unit, '1');
  assert.match(buildDraft({ ...order, version: 'v1' }).approval, /piece DEMO-PIECE, unit 1, proof v1$/);
});
test('only matching formatting wrappers are removed; required placeholders cannot generate drafts', () => {
  assert.equal(parseOrder('Customer Name: **Sample Customer**').customer, 'Sample Customer');
  assert.equal(parseOrder('**Customer Name:** **Sample Customer**').customer, 'Sample Customer');
  assert.equal(parseOrder('Customer Name: **Sample Customer').customer, '**Sample Customer');
  assert.equal(parseOrder('Customer Name: `Sample Customer').customer, '`Sample Customer');
  assert.throws(() => buildDraft({ ...fields, piece: '<piece reference>' }), /unresolved placeholder/);
});
test('recipient and order header injection, missing facts and invalid units are rejected', () => {
  for (const email of ['x@example.com\r\nBcc: theft@example.com', 'a@example.com,b@example.com', 'Name <a@example.com>', 'é@example.com', 'a@-example.com']) assert.throws(() => buildDraft({ ...fields, email }));
  for (const unit of ['0', '-1', '1.5', '1 and 2']) assert.throws(() => buildDraft({ ...fields, unit }));
  assert.throws(() => buildDraft({ ...fields, order: '#1\nInjected' }), /single line/);
  assert.throws(() => buildDraft({ ...fields, runner: '' }), /required/);
});
test('written approval identifies the exact piece, unit and proof; no optional time is invented', () => {
  const a = buildDraft(fields), b = buildDraft({ ...fields, piece: 'B', unit: 2, version: 'v2' });
  assert.equal(a.approval, 'APPROVED FOR PRODUCTION — order #TEST-1, piece A, unit 1, proof v1');
  assert.match(b.approval, /piece B, unit 2, proof v2$/); assert.notEqual(a.subject, b.subject);
  assert.doesNotMatch(a.body, /Official time:/); assert.match(a.body, /Silence does not count as approval/);
  assert.match(a.body, /48 hours/); assert.match(a.body, /8–10 business days/);
});
test('EML preserves Unicode, exact recipient, attachment bytes and safe MIME filenames', () => {
  const eml = makeEml(fields, [{ ...png, name: '../../proof"\r\nBcc-evil.png' }]);
  assert.match(eml, /^From: Teklo Studio <orders@teklostudio.com>\r\nTo: test@example.com\r\n/);
  assert.match(eml, /X-Unsent: 1\r\n/); assert.doesNotMatch(eml, /\r\nBcc:/);
  const subjectHeader = eml.match(/Subject: ([\s\S]*?)\r\nX-Unsent:/)[1];
  const subject = [...subjectHeader.matchAll(/=\?UTF-8\?B\?([^?]+)\?=/g)].map(m => Buffer.from(m[1], 'base64').toString('utf8')).join('');
  assert.equal(subject, buildDraft(fields).subject);
  const parts = eml.split('--Trace_Proof_Draft_Boundary');
  const body = Buffer.from(parts[1].split('\r\n\r\n')[1].trim(), 'base64').toString('utf8');
  assert.equal(body, buildDraft(fields).body.replace(/\n/g, '\r\n'));
  const attachment = Buffer.from(parts[2].split('\r\n\r\n')[1].trim(), 'base64');
  assert.deepEqual(attachment, Buffer.from(png.bytes));
  assert.match(parts[2], /filename="proof___Bcc-evil.png"/);
});
test('file signatures, MIME mismatch, size cap and missing render are enforced', () => {
  assert.throws(() => makeEml(fields, []), /Attach at least/);
  assert.throws(() => validateAttachments([{ ...png, bytes: new TextEncoder().encode('<script>no</script>') }]), /signature/);
  assert.throws(() => validateAttachments([{ ...png, type: 'application/pdf' }]), /does not match/);
  const big = new Uint8Array(20_000_000); big.set(png.bytes);
  assert.equal(validateAttachments([{ ...png, bytes: big }])[0].bytes.length, 20_000_000);
  assert.throws(() => validateAttachments([{ ...png, bytes: big }, png]), /20 MB/);
  assert.equal(validateAttachments([{ name: 'proof.pdf', bytes: new TextEncoder().encode('%PDF-1.7\n') }])[0].type, 'application/pdf');
  assert.equal(validateAttachments([{ name: 'proof.jpg', bytes: Uint8Array.from([255,216,255,224]) }])[0].type, 'image/jpeg');
});
