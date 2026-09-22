const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const root = path.join(__dirname, '../tools/proof-email');
function harness() {
  class Element {
    constructor(){this.value='';this.checked=false;this.disabled=false;this.files=[];this.children=[];this.events={};this.classList={add(){},remove(){}};}
    append(...nodes){this.children.push(...nodes);}
    replaceChildren(){this.children=[];}
    addEventListener(name,fn){this.events[name]=fn;}
    click(){}
  }
  const elements = new Map();
  const get = id => {if(!elements.has(id))elements.set(id,new Element());return elements.get(id);};
  const document={getElementById:get,createElement:()=>new Element()};
  const context=vm.createContext({document,console,TextEncoder,Uint8Array,btoa,Blob,URL:{createObjectURL:()=> 'blob:test',revokeObjectURL(){}},setTimeout(){},navigator:{clipboard:{writeText:async()=>{}}}});
  vm.runInContext(fs.readFileSync(path.join(root,'core.js'),'utf8'),context);
  vm.runInContext(fs.readFileSync(path.join(root,'app.js'),'utf8'),context);
  for(const label of get('fields').children){const input=label.children[0];elements.set(input.id,input);}
  return {get,async order(text){get('orderFile').files=[{size:text.length,text:async()=>text}];await get('orderFile').events.change();},async proof(bytes){await get('drop').events.drop({preventDefault(){},dataTransfer:{files:[{name:'proof.png',type:'image/png',size:bytes.length,arrayBuffer:async()=>bytes.buffer}]}});}};
}
const sample=fs.readFileSync(path.join(root,'sample-order.md'),'utf8');
const png=new Uint8Array([137,80,78,71,13,10,26,10,0]);
test('order import, proof selection and recipient edits cannot reuse prior review',async()=>{
 const h=harness();await h.order(sample);assert.equal(h.get('email').value,'sample@example.invalid');assert.equal(h.get('download').disabled,true);
 h.get('version').value='v1';h.get('version').events.input();await h.proof(png);
 assert.equal(h.get('download').disabled,true);h.get('review').checked=true;h.get('review').events.change();assert.equal(h.get('download').disabled,false);
 h.get('email').value='changed@example.invalid';h.get('email').events.input();assert.equal(h.get('review').checked,false);assert.equal(h.get('download').disabled,true);
 await h.order(sample.replace('DEMO-PIECE','SECOND-PIECE'));assert.equal(h.get('version').value,'');assert.equal(h.get('files').children.length,0);assert.equal(h.get('download').disabled,true);
});
test('invalid replacement proof discards previously selected attachment',async()=>{
 const h=harness();await h.order(sample);h.get('version').value='v1';await h.proof(png);h.get('review').checked=true;h.get('review').events.change();assert.equal(h.get('download').disabled,false);
 await h.proof(new Uint8Array([1,2,3]));assert.equal(h.get('download').disabled,true);assert.equal(h.get('files').children.length,0);assert.match(h.get('status').textContent,/signature/);
});
