/* Offline Trace proof draft generation. Never sends mail or changes order state. */
(function (root) {
  'use strict';
  const LABELS = {
    'order number': 'order', 'customer name': 'customer', 'customer email': 'email',
    'runner name': 'runner', 'race name': 'race', 'date': 'date', 'distance': 'distance',
    'location': 'location', 'official time': 'finishTime', 'style': 'style',
    'accent': 'accent', 'piece reference': 'piece', 'unit number': 'unit'
  };
  const LIMIT = 20_000_000;

  function unwrap(value) {
    const text = value.trim();
    for (const marker of ['**', '__', '`']) {
      if (text.length >= marker.length * 2 && text.startsWith(marker) && text.endsWith(marker)) {
        return text.slice(marker.length, -marker.length).trim();
      }
    }
    return text;
  }

  function parseOrder(markdown) {
    if (typeof markdown !== 'string') throw new Error('Order file must contain text.');
    const result = Object.fromEntries(Object.values(LABELS).map(key => [key, '']));
    const seen = new Set();
    let fence = false;
    for (const line of markdown.split(/\r?\n/)) {
      if (/^\s*(```|~~~)/.test(line)) { fence = !fence; continue; }
      if (fence) continue;
      let label, value;
      const table = line.match(/^\s*\|\s*([^|]+)\|\s*([^|]*)\|\s*$/);
      const pair = line.match(/^\s*(?:[-*+]\s+)?(.+?):\s*(.*?)\s*$/);
      if (table) [, label, value] = table;
      else if (pair) [, label, value] = pair;
      else continue;
      label = label.trim();
      // Handle **Label:** value without treating a mismatched value marker as formatting.
      for (const marker of ['**', '__']) {
        if (label.startsWith(marker) && !label.endsWith(marker) && value.startsWith(marker)) {
          label = label.slice(marker.length);
          value = value.slice(marker.length).trim();
          break;
        }
      }
      label = unwrap(label).toLowerCase().replace(/:$/, '');
      const key = LABELS[label];
      if (!key) continue;
      if (seen.has(key)) throw new Error('Duplicate ' + label + ': use one piece per order file.');
      seen.add(key);
      result[key] = unwrap(value);
    }
    if (!seen.size) throw new Error('No recognized order fields found.');
    return result;
  }

  function clean(value, label, required) {
    if (value !== undefined && value !== null && typeof value !== 'string' && typeof value !== 'number') {
      throw new Error(label + ' must be text.');
    }
    const text = String(value == null ? '' : value).trim();
    if (/[\x00-\x1f\x7f]/.test(String(value == null ? '' : value))) throw new Error(label + ' must be a single line.');
    if (required && !text) throw new Error(label + ' is required.');
    if (required && /<[^<>]*>/.test(text)) throw new Error(label + ' contains an unresolved placeholder.');
    if (text.length > 500) throw new Error(label + ' is too long.');
    return text;
  }

  function checkedFields(fields) {
    if (!fields || typeof fields !== 'object') throw new Error('Order details are required.');
    const required = new Set(['order', 'customer', 'email', 'piece', 'unit', 'version', 'runner', 'race', 'style', 'accent']);
    const result = {};
    for (const key of [...Object.values(LABELS), 'version']) result[key] = clean(fields[key], key, required.has(key));
    if (!/^[1-9]\d*$/.test(result.unit) || !Number.isSafeInteger(Number(result.unit))) throw new Error('Unit must be a positive whole number.');
    // One ASCII mailbox only: no display names, comments, multiple recipients or headers.
    if (!/^[A-Za-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+$/.test(result.email) || result.email.length > 254) {
      throw new Error('Enter one valid ASCII customer email address.');
    }
    return result;
  }

  function buildDraft(fields) {
    const f = checkedFields(fields);
    const identity = `order ${f.order}, piece ${f.piece}, unit ${f.unit}, proof ${f.version}`;
    const approval = `APPROVED FOR PRODUCTION — ${identity}`;
    const details = [
      `Runner: ${f.runner}`, `Race: ${f.race}`,
      ...(f.date ? [`Date: ${f.date}`] : []), ...(f.distance ? [`Distance: ${f.distance}`] : []),
      ...(f.location ? [`Location: ${f.location}`] : []), ...(f.finishTime ? [`Official time: ${f.finishTime}`] : []),
      `Style: ${f.style}`, `Accent: ${f.accent}`
    ].join('\n');
    return {
      subject: `Your Trace proof — ${f.order} · ${f.piece} · unit ${f.unit} · ${f.version}`,
      approval,
      body: `Hi ${f.customer},\n\nYour Trace proof is attached. I’m looking forward to bringing your route to life.\n\n${identity}\n\n${details}\n\nPlease review the attached proof carefully: route shape, name and spelling, race, date, distance, finish time (if included), layout, style and accent.\n\nPlease reply to this email within 48 hours with any changes, or copy this exact approval into your reply:\n\n${approval}\n\nApproval applies only to this piece and proof version. If you ordered more than one piece, each needs its own written approval. Silence does not count as approval, and production will not begin without it.\n\nProduction takes 8–10 business days after complete, usable intake and written proof approval. Shipping transit time is additional.\n\nYou can cancel for a full refund before written approval. After approval and before production, changes or cancellation are at my discretion; orders cannot be canceled once production starts.\n\nIf I don’t hear back, I’ll send a reminder after 48 hours and a final reminder on day 7. After 10 calendar days without a response to this proof request, the unapproved order will be canceled and fully refunded.\n\nThank you,\nCraig\nTeklo Studio\norders@teklostudio.com`
    };
  }

  function validateAttachments(attachments) {
    if (!Array.isArray(attachments) || !attachments.length) throw new Error('Attach at least one proof (PNG, JPEG or PDF).');
    let total = 0;
    return attachments.map((file, index) => {
      if (!file || !(file.bytes instanceof Uint8Array)) throw new Error('Attachment bytes are missing.');
      const b = file.bytes;
      total += b.byteLength;
      if (total > LIMIT) throw new Error('Combined attachments must be 20 MB or smaller.');
      let type, extension;
      if (b.length >= 8 && [137,80,78,71,13,10,26,10].every((v, i) => b[i] === v)) { type = 'image/png'; extension = 'png'; }
      else if (b.length >= 3 && b[0] === 255 && b[1] === 216 && b[2] === 255) { type = 'image/jpeg'; extension = 'jpg'; }
      else if (b.length >= 5 && [37,80,68,70,45].every((v, i) => b[i] === v)) { type = 'application/pdf'; extension = 'pdf'; }
      else throw new Error('Only files with a PNG, JPEG or PDF signature are accepted.');
      if (file.type && file.type !== type && file.type !== 'application/octet-stream') throw new Error('Attachment type does not match its file signature.');
      const raw = String(file.name || `proof-${index + 1}`).split(/[\\/]/).pop();
      const stem = raw.replace(/\.[^.]*$/, '').replace(/[^A-Za-z0-9._-]/g, '_').replace(/^\.+/, '').slice(0, 100) || `proof-${index + 1}`;
      return { name: `${stem}.${extension}`, type, bytes: b };
    });
  }

  function base64(bytes) {
    let binary = '';
    for (let i = 0; i < bytes.length; i += 8192) binary += String.fromCharCode(...bytes.subarray(i, i + 8192));
    return btoa(binary);
  }
  const utf8 = value => new TextEncoder().encode(value);
  const wrapped = value => value.match(/.{1,76}/g).join('\r\n');
  function encodedSubject(subject) {
    // Keep each RFC 2047 encoded word below 75 characters without splitting UTF-8 characters.
    const words = [];
    let chunk = '';
    for (const character of subject) {
      if (utf8(chunk + character).length > 42) { words.push(`=?UTF-8?B?${base64(utf8(chunk))}?=`); chunk = ''; }
      chunk += character;
    }
    if (chunk) words.push(`=?UTF-8?B?${base64(utf8(chunk))}?=`);
    return words.join('\r\n ');
  }

  function makeEml(fields, attachments) {
    const f = checkedFields(fields), draft = buildDraft(f), files = validateAttachments(attachments);
    // Base64 bodies cannot contain underscore, so this boundary cannot collide with content.
    const boundary = 'Trace_Proof_Draft_Boundary';
    const lines = [
      'From: Teklo Studio <orders@teklostudio.com>', `To: ${f.email}`,
      'Reply-To: orders@teklostudio.com', `Subject: ${encodedSubject(draft.subject)}`,
      'X-Unsent: 1', 'MIME-Version: 1.0', `Content-Type: multipart/mixed; boundary="${boundary}"`, '',
      `--${boundary}`, 'Content-Type: text/plain; charset=UTF-8', 'Content-Transfer-Encoding: base64', '',
      wrapped(base64(utf8(draft.body.replace(/\n/g, '\r\n'))))
    ];
    for (const file of files) lines.push(
      `--${boundary}`, `Content-Type: ${file.type}; name="${file.name}"`,
      `Content-Disposition: attachment; filename="${file.name}"`, 'Content-Transfer-Encoding: base64', '', wrapped(base64(file.bytes))
    );
    lines.push(`--${boundary}--`, '');
    return lines.join('\r\n');
  }
  const api = { parseOrder, buildDraft, validateAttachments, makeEml };
  root.TraceProof = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
