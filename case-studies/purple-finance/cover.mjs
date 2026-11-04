// New covers from the live page: assets/uiux/purple-finance.jpg and the bottom-middle tile of work-mosaic.jpg. Needs the preview server on :4173.
import {spawn} from 'node:child_process';import fs from 'node:fs';import path from 'node:path';
const ROOT=path.resolve(import.meta.dirname,'../..');
const chrome=spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',['--headless=new','--remote-debugging-port=9348','--user-data-dir=/tmp/pf-cover','--no-first-run','--hide-scrollbars','about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let tgt;for(let i=0;i<40&&!tgt;i++){await sleep(250);try{tgt=(await (await fetch('http://127.0.0.1:9348/json')).json()).find(t=>t.type==='page')}catch{}}
const ws=new WebSocket(tgt.webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const wait=new Map();ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&wait.has(m.id)){wait.get(m.id)(m);wait.delete(m.id)}};
const cmd=(method,params={})=>new Promise((res,rej)=>{const i=++id;wait.set(i,m=>m.error?rej(new Error(m.error.message)):res(m.result));ws.send(JSON.stringify({id:i,method,params}))});
const js=async x=>{const r=await cmd('Runtime.evaluate',{expression:x,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw new Error(JSON.stringify(r.exceptionDetails).slice(0,300));return r.result.value};
await cmd('Page.enable');await cmd('Runtime.enable');
const shot=async(w,h,mid,side,pad,q=86)=>{
  await cmd('Emulation.setDeviceMetricsOverride',{width:w,height:h,deviceScaleFactor:2,mobile:false});
  await cmd('Page.navigate',{url:'http://localhost:4173/case-studies/purple-finance/showcase.html'});await sleep(3000);
  await js(`(function(){var s=document.createElement('style');s.textContent='*{animation:none!important;transition:none!important}.nav,.hero .w>div:first-child,main>:not(.hero),.w>.nums,.src,.cta,.foot,.band{display:none!important}body{background:#F3E9F5}.hero{padding:0;height:100vh;display:flex;align-items:center}.hero .w{display:block;max-width:none;width:100%;padding:0}.stage{min-height:100vh;border-radius:0;padding:${pad}px ${side}px ${pad}px ${pad}px}.stage .brow,.stage .ph{transform:none!important;opacity:1!important}.stage .ph{--w:${mid}px!important;right:${Math.round(pad*.7)}px;bottom:${Math.round(pad*.7)}px}';document.head.appendChild(s);scrollTo(0,0)})()`);
  await sleep(700);
  return (await cmd('Page.captureScreenshot',{format:'jpeg',quality:q})).data};
fs.writeFileSync(ROOT+'/assets/uiux/purple-finance.jpg',Buffer.from(await shot(1200,750,280,220,50),'base64'));
const tile=await shot(532,447,150,110,24,90);
await cmd('Emulation.setDeviceMetricsOverride',{width:1600,height:900,deviceScaleFactor:1,mobile:false});
await js(`new Promise(function(r){document.documentElement.setAttribute('style','background:#000');document.body.innerHTML='<img id=a style="position:fixed;left:0;top:0;width:1600px;height:900px"><img id=b style="position:fixed;left:535px;top:453px;width:530px;height:447px">';var a=document.getElementById('a'),b=document.getElementById('b'),n=0,d=function(){if(++n==2)r()};a.onload=d;b.onload=d;a.src='/assets/uiux/work-mosaic.jpg?'+Date.now();b.src='data:image/jpeg;base64,${tile}'})`);
await sleep(300);
fs.writeFileSync(ROOT+'/assets/uiux/work-mosaic.jpg',Buffer.from((await cmd('Page.captureScreenshot',{format:'jpeg',quality:88})).data,'base64'));
ws.close();chrome.kill();process.exit(0);
