'use strict';
const labels = {order:'Order number',customer:'Customer name',email:'Order email',piece:'Piece reference',unit:'Unit number',runner:'Runner display name',race:'Race / event',date:'Event date',distance:'Distance',location:'Location',finishTime:'Finish time (or Not displayed)',style:'Finish / style',accent:'Route accent'};
const inputs = {};
for (const [key,label] of Object.entries(labels)) {
  const wrapper=document.createElement('label'); wrapper.textContent=label;
  const input=document.createElement('input'); input.id=key; input.autocomplete='off';
  input.type=key==='email'?'email':'text';
  if(key==='unit') input.inputMode='numeric';
  wrapper.append(input); document.getElementById('fields').append(wrapper); inputs[key]=input;
}
const el=id=>document.getElementById(id);
let attachments=[],urls=[],draft=null,loadToken=0;
function values(){return {...Object.fromEntries(Object.entries(inputs).map(([k,v])=>[k,v.value.trim()])),version:el('version').value.trim()};}
function resetReview(){el('review').checked=false; refresh();}
function refresh(){
  draft=null;
  try {
    draft=TraceProof.buildDraft(values());
    el('subject').textContent='To: '+values().email+' | Subject: '+draft.subject;
    el('preview').textContent=draft.body;
    TraceProof.validateAttachments(attachments);
    el('status').textContent='Ready for your review. The 48-hour reply window starts when you send the proof.';
  } catch(error){el('status').textContent=error.message; if(!draft){el('subject').textContent='';el('preview').textContent='Complete the order and proof details to preview the email.';}}
  let valid=false; try{TraceProof.validateAttachments(attachments);valid=Boolean(draft);}catch{}
  el('download').disabled=!(valid&&el('review').checked);el('copy').disabled=!draft;
}
for(const input of [...Object.values(inputs),el('version')])input.addEventListener('input',resetReview);
el('review').addEventListener('change',refresh);
function clearFiles(){attachments=[];urls.forEach(URL.revokeObjectURL);urls=[];el('files').replaceChildren();el('proofFiles').value='';}
el('orderFile').addEventListener('change',async()=>{
  const token=++loadToken;const file=el('orderFile').files[0];
  for(const input of Object.values(inputs))input.value='';
  el('version').value='';clearFiles();resetReview();if(!file)return;
  try{if(file.size>1000000)throw new Error('Order file is too large. Choose the single-piece order.md record.');const parsed=TraceProof.parseOrder(await file.text());if(token!==loadToken)return;for(const [k,v]of Object.entries(parsed))if(inputs[k])inputs[k].value=v;resetReview();}catch(error){if(token===loadToken)el('status').textContent=error.message;}
});
async function loadFiles(files){
  const token=++loadToken;clearFiles();resetReview();
  try{
    if(!files.length)throw new Error('Choose at least one proof.');
    if(files.reduce((n,f)=>n+f.size,0)>20000000)throw new Error('Proof attachments must total 20 MB or less.');
    const loaded=await Promise.all(files.map(async file=>({name:file.name,type:file.type,bytes:new Uint8Array(await file.arrayBuffer())})));
    if(token!==loadToken)return;
    TraceProof.validateAttachments(loaded);attachments=loaded;
    for(const file of loaded){const p=document.createElement('p');p.textContent=file.name+' ('+Math.ceil(file.bytes.length/1024)+' KB)';el('files').append(p);if(/image\/(png|jpeg)/.test(file.type)){const img=document.createElement('img');const url=URL.createObjectURL(new Blob([file.bytes],{type:file.type}));urls.push(url);img.src=url;img.alt='Selected proof: '+file.name;el('files').append(img);}}
    resetReview();
  }catch(error){if(token===loadToken){clearFiles();el('status').textContent=error.message;}}
}
el('proofFiles').addEventListener('change',e=>loadFiles([...e.target.files]));
for(const kind of ['dragenter','dragover'])el('drop').addEventListener(kind,e=>{e.preventDefault();el('drop').classList.add('over');});
el('drop').addEventListener('dragleave',()=>el('drop').classList.remove('over'));
el('drop').addEventListener('drop',e=>{e.preventDefault();el('drop').classList.remove('over');return loadFiles([...e.dataTransfer.files]);});
el('download').addEventListener('click',()=>{
  try{if(!el('review').checked)throw new Error('Review the recipient and proof before downloading.');const message=TraceProof.makeEml(values(),attachments);const url=URL.createObjectURL(new Blob([message],{type:'message/rfc822'}));const a=document.createElement('a');a.href=url;a.download=('Trace-'+values().order+'-'+values().piece+'-'+values().unit+'-'+values().version).replace(/[^a-zA-Z0-9_-]/g,'_')+'.eml';a.click();setTimeout(()=>URL.revokeObjectURL(url),30000);el('status').textContent='Email file prepared. Open it in your mail app, verify its attachments and send when ready. Nothing has been sent or recorded as delivered.';}catch(error){el('status').textContent=error.message;}
});
el('copy').addEventListener('click',async()=>{try{const d=TraceProof.buildDraft(values());await navigator.clipboard.writeText('To: '+values().email+'\nSubject: '+d.subject+'\n\n'+d.body);el('status').textContent='Text copied. Attach the original proofs manually before sending.';}catch{el('status').textContent='Clipboard unavailable. Select and copy the email preview below.';}});
