const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const base = process.env.TEKLO_PREVIEW_URL || 'http://127.0.0.1:9293';
const results = [];
const pass = (name) => results.push({ name, result: 'passed' });

async function html(path) {
  const response = await fetch(base + path);
  assert.equal(response.status, 200, path);
  const content = await response.text();
  assert.doesNotMatch(content, /Liquid (?:error|syntax error)|translation missing:/i, path);
  return content;
}

function testDrawerNavigation() {
  let click, closed = false, focused = false, scrolled = false, expanded;
  const summary = { setAttribute: (name, value) => { expanded = value; } };
  const drawer = { querySelector: () => summary, closeMenuDrawer: () => { closed = true; } };
  const target = { hasAttribute: () => false, setAttribute() {}, addEventListener() {}, focus: () => { focused = true; }, scrollIntoView: () => { scrolled = true; } };
  const location = new URL(base + '/');
  const context = {
    URL, document: { addEventListener: (name, handler) => { click = handler; }, getElementById: () => target },
    window: { location, setTimeout: (fn) => fn() }
  };
  vm.runInNewContext(fs.readFileSync('assets/teklo-navigation.js', 'utf8'), context);
  let prevented = false;
  const link = { href: base + '/#made-at-teklo', closest: () => drawer };
  click({ target: { closest: () => link }, button: 0, preventDefault: () => { prevented = true; } });
  assert(closed && focused && scrolled && prevented);
  assert.equal(expanded, 'false');
  assert.equal(location.hash, '#made-at-teklo');
  closed = false;
  link.href = base + '/pages/contact?view=custom-work';
  click({ target: { closest: () => link }, button: 0, preventDefault() {} });
  assert.equal(closed, false, 'ordinary page navigation stays native');
  pass('Mobile same-page navigation releases the drawer and focuses the story; ordinary links stay native');
}

(async () => {
  testDrawerNavigation();
  const home = await html('/');
  assert.equal((home.match(/<h1\b/g) || []).length, 1);
  assert.match(home, /teklo-hero-film--split/);
  assert.match(home, /data-teklo-media-toggle/);
  for (const id of ['teklo-trace']) assert(home.includes('id="' + id + '"'));
  for (const text of ['Designed through process.', 'A route worth remembering.', 'A finish for every memory.', '12.5 × 15 × 2.4 in', 'Have a problem worth making for?']) assert(home.includes(text));
  assert.match(home, /\/pages\/contact\?view=custom-work(?:&amp;|#|\")/);
  assert.doesNotMatch(home, /placeholder-hero-3d-print\.mp4/);
  pass('Homepage has one H1, split video hero, complete story sequence, inquiry navigation, and no missing fallback video');
  assert.doesNotMatch(home, /class="teklo-objects|class="teklo-featured-collection|Form changes when the light/);
  assert.match(home, /teklo-hero-film__eyebrow/);
  for(const text of ['A new way of thinking about things.','Purposeful objects for what moves you.','teklo-maker-seal','trace-wordmark','teklo-studio-horizontal','425BD1ED','DD2233B2','23C2B695']) assert(home.includes(text),text);
  assert.doesNotMatch(home,/placeholder-trace-section|Trace-Listing_Graphics|IMG-0423|11 × 14 in framed artwork/);
  assert.match(home,/header--middle-left/);
  const studio = await html('/pages/about-us?view=studio');
  assert.equal((studio.match(/<h1\b/g)||[]).length,1);
  for(const text of ['Curated objects','Design &amp; fabrication','Experiments','Ship-hull master mold','Tent-pole connector','Around the shop']) assert(studio.includes(text),text);
  assert.doesNotMatch(studio,/Previous professional project|Trace-Listing_Graphics|IMG-0423/);
  assert.equal((studio.match(/<img[^>]*src="[^"]*9A8B0F62[^"]*"/g)||[]).length,2,'Connector appears in exactly two Studio image slots');
  pass('Studio renders three offerings, two factual projects and personal shop introduction; unfinished professional project is hidden');
  const custom = await html('/pages/contact?view=custom-work');
  assert.equal((custom.match(/<h1\b/g) || []).length, 1);
  assert.doesNotMatch(custom, /class="teklo-custom-work__projects"/);
  const form = custom.match(/<form[^>]*class="teklo-custom-work__form"[\s\S]*?<\/form>/)?.[0];
  assert(form, 'Native custom inquiry form renders');
  assert.match(form, /name="form_type" value="contact"/);
  assert.match(form, /name="contact\[Inquiry type\]" value="Custom Work"/);
  assert.match(form, /name="return_to"/);
  for (const name of ['name', 'email', 'body']) assert(new RegExp('name="contact\\[' + name + '\\]"[^>]*required').test(form));
  for (const input of form.matchAll(/<(?:input|textarea)\b[^>]*id="([^"]+)"[^>]*>/g)) assert(form.includes('for="' + input[1] + '"'));
  assert.doesNotMatch(form, /type="file"/);
  pass('Custom Work renders labeled native contact fields, required inputs and return destination; empty project proof is hidden');
  const collection = await html('/collections/all');
  assert.match(collection, /\/products\//);
  await html('/products/boho-wall-planter-a-touch-of-nature-elevated');
  await html('/products/birch-moody-accent-pendant-light-calm-lighting-for-dining-living-spaces-eco-friendly-decor');
  await html('/search?q=planter&type=product');
  await html('/cart');
  pass('Catalog, linked products, search and cart routes render without Liquid or translation errors');
  const assets = [...home.matchAll(/(?:src|href)="([^"]*\/(?:teklo-navigation\.js|teklo-media\.js|teklo-studio-refresh\.css)[^"]*)"/g)];
  assert.equal(assets.length, 3);
  for (const match of assets) {
    const url = new URL(match[1].replaceAll('&amp;', '&'), base);
    const response = await fetch(url);
    assert.equal(response.status, 200, url.pathname);
  }
  pass('New navigation, playback, and design stylesheet assets are served');
  fs.writeFileSync('review/studio-refresh-verification.json', JSON.stringify({ date: new Date().toISOString(), base, results, notTested: ['Browser visual and keyboard verification', 'Real inquiry delivery', 'Checkout transaction', 'Populated project examples'] }, null, 2) + '\n');
  console.log(results.map(x => 'PASS ' + x.name).join('\n'));
})().catch(error => { console.error(error); process.exitCode = 1; });
