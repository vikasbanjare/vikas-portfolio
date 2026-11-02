// node capture.mjs <theme> <outDir> [onlyIdsCsv|all] [mode] -> screenshots each frame and writes manifest
import {spawn} from 'node:child_process';import fs from 'node:fs';
const [theme,outDir,only='all',mode='']=process.argv.slice(2);
const CH='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';const port=9100+Math.floor(Math.random()*500);
const p=spawn(CH,['--headless=new','--disable-gpu',`--remote-debugging-port=${port}`,`--user-data-dir=/tmp/cdp-${port}`,'--hide-scrollbars','about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let tgt;for(let i=0;i<80;i++){try{tgt=(await (await fetch(`http://127.0.0.1:${port}/json`)).json()).find(t=>t.type==='page');if(tgt)break}catch(e){}await sleep(300)}
const ws=new WebSocket(tgt.webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const pend={};ws.onmessage=m=>{const d=JSON.parse(m.data);if(d.id&&pend[d.id]){pend[d.id](d);delete pend[d.id]}};
const send=(method,params={},to=90000)=>Promise.race([new Promise(r=>{const i=++id;pend[i]=r;ws.send(JSON.stringify({id:i,method,params}))}),sleep(to).then(()=>({timeout:true}))]);
const ev=async e=>{const r=await send('Runtime.evaluate',{expression:e,returnByValue:true,awaitPromise:true});if(r.result?.exceptionDetails)console.log('JSERR',JSON.stringify(r.result.exceptionDetails).slice(0,400));return r.result?.result?.value};
await send('Emulation.setDefaultBackgroundColorOverride',{color:{r:0,g:0,b:0,a:0}});
await send('Emulation.setDeviceMetricsOverride',{width:2200,height:1200,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:`file:///tmp/crestline-${theme}.html`});await sleep(26000);
await ev(fs.readFileSync(new URL('../source-design/scrub.js',import.meta.url),'utf8'));
const SETUP=fs.readFileSync(new URL('./pass.js',import.meta.url),'utf8');
await ev(SETUP);
const frames=JSON.parse(await ev('JSON.stringify(window.__frames())'));
console.log('frames',frames.length);
fs.mkdirSync(outDir,{recursive:true});
const want=only==='all'?null:new Set(only.split(','));
const out=[];
for(const f of frames){
  if(want&&!want.has(f.id))continue;
  const info=JSON.parse(await ev(`JSON.stringify(window.__prep(${f.i},${JSON.stringify(mode)}))`));
  if(!info||!info.w){console.log('skip',f.id);continue}
  await sleep(120);
  const r=await send('Page.captureScreenshot',{format:'webp',quality:84,captureBeyondViewport:true,clip:{x:info.x,y:info.y,width:info.w,height:info.h,scale:2}});
  if(r.result){fs.writeFileSync(`${outDir}/${f.id}.webp`,Buffer.from(r.result.data,'base64'));out.push({...f,...info});}else console.log('FAIL',f.id);
}
console.log('leftovers',await ev(`window.REP.filter(r=>document.body.innerText.search(r[0])>-1).map(r=>String(r[0])).join(' ')`));
fs.writeFileSync(`${outDir}/manifest.json`,JSON.stringify(out));console.log('done',out.length);
ws.close();p.kill();process.exit(0);
