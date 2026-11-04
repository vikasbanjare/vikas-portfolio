// New covers for the portfolio from the live page: assets/uiux/crestline.jpg and the first tile of work-mosaic.jpg.
import {spawn} from 'node:child_process';import fs from 'node:fs';import path from 'node:path';
const ROOT=path.resolve(import.meta.dirname,'../../..');const PROFILE=process.env.CR_PROFILE||'/tmp/cr-capture';
const chrome=spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',['--headless=new','--remote-debugging-port=9334','--user-data-dir='+PROFILE,'--no-first-run','--hide-scrollbars','about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let tgt;for(let i=0;i<40&&!tgt;i++){await sleep(250);try{tgt=(await (await fetch('http://127.0.0.1:9334/json')).json()).find(t=>t.type==='page')}catch{}}
const ws=new WebSocket(tgt.webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const wait=new Map();ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&wait.has(m.id)){wait.get(m.id)(m);wait.delete(m.id)}};
const cmd=(method,params={})=>new Promise((res,rej)=>{const i=++id;wait.set(i,m=>m.error?rej(new Error(m.error.message)):res(m.result));ws.send(JSON.stringify({id:i,method,params}))});
const js=async x=>{const r=await cmd('Runtime.evaluate',{expression:x,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw new Error(JSON.stringify(r.exceptionDetails).slice(0,300));return r.result.value};
await cmd('Page.enable');await cmd('Runtime.enable');
const shot=async(w,h,mid,side,q=86)=>{
  await cmd('Emulation.setDeviceMetricsOverride',{width:w,height:h,deviceScaleFactor:2,mobile:false});
  await cmd('Page.navigate',{url:'http://localhost:4173/case-studies/crestline/showcase.html'});await sleep(3500);
  await js(`(function(){var s=document.createElement('style');s.textContent='*{animation:none!important;transition:none!important}.hero-t,.tabs,main,.foot{display:none!important}body{padding:0;overflow:hidden}.hero{margin:0!important;border-radius:0!important;min-height:0!important;height:100vh;grid-template-columns:1fr!important}.hero-p .mid{--s:${mid}!important}.hero-p{padding:0!important;align-items:flex-start!important;margin-top:${Math.round(h*.09)}px;overflow:visible!important;height:auto!important}.hero-p .side{--s:${side}!important;margin-top:${Math.round(h*.09)}px!important;transform:none!important;display:block!important}';document.head.appendChild(s);document.querySelectorAll('.hero-p .side').forEach(function(p){p.style.margin=''});scrollTo(0,0)})()`);
  await sleep(900);
  return (await cmd('Page.captureScreenshot',{format:'jpeg',quality:q})).data};
fs.writeFileSync(ROOT+'/assets/uiux/crestline.jpg',Buffer.from(await shot(1200,750,.86,.62),'base64'));
const tile=await shot(532,447,.62,.46,90);
await cmd('Emulation.setDeviceMetricsOverride',{width:1600,height:900,deviceScaleFactor:1,mobile:false});
await js(`new Promise(function(r){document.documentElement.setAttribute('style','background:#000');document.body.innerHTML='<img id=a style="position:fixed;left:0;top:0;width:1600px;height:900px"><img id=b style="position:fixed;left:0;top:0;width:532px;height:447px">';var a=document.getElementById('a'),b=document.getElementById('b'),n=0,d=function(){if(++n==2)r()};a.onload=d;b.onload=d;a.src='/assets/uiux/work-mosaic.jpg?'+Date.now();b.src='data:image/jpeg;base64,${tile}'})`);
await sleep(300);
fs.writeFileSync(ROOT+'/assets/uiux/work-mosaic.jpg',Buffer.from((await cmd('Page.captureScreenshot',{format:'jpeg',quality:88})).data,'base64'));
ws.close();chrome.kill();process.exit(0);
