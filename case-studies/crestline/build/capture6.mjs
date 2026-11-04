// Pictures and live copies of the real app, for showcase.html. Run with the site served on :4173.
// node build/capture6.mjs [Screen ...]   writes v6/lt, v6/dk and v6/live.json
import {spawn} from 'node:child_process';import fs from 'node:fs';import path from 'node:path';
const ROOT=path.resolve(import.meta.dirname,'..');const PROFILE=process.env.CR_PROFILE||'/tmp/cr-capture';
const LIVE=['Welcome','Home','Stock','KycHub','Buy','Review','Filled','Waiting','PartFilled','NotPlaced','Sold','Charges','Portfolio','FoGate','FoProof','OptionSimple','OrderTypes','KycReady','KycFail','KycReview','MoneyFail','HoldEmpty','Festive','Segments','Otp','Markets','FundsHome','IpoList'];
const chrome=spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',['--headless=new','--remote-debugging-port=9333','--user-data-dir='+PROFILE,'--no-first-run','--hide-scrollbars','--force-device-scale-factor=1','about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let tgt;for(let i=0;i<40&&!tgt;i++){await sleep(250);try{tgt=(await (await fetch('http://127.0.0.1:9333/json')).json()).find(t=>t.type==='page')}catch{}}
const ws=new WebSocket(tgt.webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const wait=new Map();ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&wait.has(m.id)){wait.get(m.id)(m);wait.delete(m.id)}};
const cmd=(method,params={})=>new Promise((res,rej)=>{const i=++id;const t=setTimeout(()=>rej(new Error('timeout '+method)),30000);wait.set(i,m=>{clearTimeout(t);m.error?rej(new Error(m.error.message)):res(m.result)});ws.send(JSON.stringify({id:i,method,params}))});
const js=async x=>{const r=await cmd('Runtime.evaluate',{expression:x,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw new Error(JSON.stringify(r.exceptionDetails).slice(0,400));return r.result.value};
await cmd('Page.enable');await cmd('Runtime.enable');
await cmd('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:false});
await cmd('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'},{name:'prefers-color-scheme',value:'light'}]});
await cmd('Page.navigate',{url:'http://localhost:4173/case-studies/crestline/app/'});await sleep(2500);
const only=process.argv.slice(2);const names=await js(`Object.keys(CR_LT.S)`);const todo=only.length?only:names;
const live=fs.existsSync(ROOT+'/v6/live.json')&&only.length?JSON.parse(fs.readFileSync(ROOT+'/v6/live.json')):{LT:{},DK:{}};
const go=k=>js(`(function(){var S=CR_APP.S;S.seen.RELIANCE=1;clearTimeout(S.auto);S.stock=null;S.stack=[];CR_APP.nav('Home',{fade:1});S.stack=['Home'];document.body.classList.remove('panel-open');CR_APP.nav(${JSON.stringify(k)},{fade:1});clearTimeout(S.auto);return document.body.getAttribute('data-screen')})()`);
const FREEZE=`(function(){var s=document.getElementById('frz');if(!s){s=document.createElement('style');s.id='frz';s.textContent='*,*::before,*::after{animation:none!important;transition:none!important}';document.head.appendChild(s)}})()`;
const MELT=`(function(){var s=document.getElementById('frz');if(s)s.remove()})()`;
let bad=[];
for(const [th,dir] of [['LT','lt'],['DK','dk']]){
  await js(`CR_LT&&0`);
  if(th==='DK'&&!(await js(`!!window.CR_DK`))){await js(`new Promise(function(r){var s=document.createElement('script');s.src='screens-dk.js';s.onload=r;document.head.appendChild(s)})`)}
  await js(`CR_APP.S.theme=${JSON.stringify(th)};document.documentElement.setAttribute('data-theme',${JSON.stringify(th==='DK'?'dark':'light')})`);
  await sleep(300);
  for(const k of todo){try{
    await js(MELT);const got=await go(k);await sleep(LIVE.includes(k)?500:160);
    if(got!==k)bad.push(th+':'+k+'->'+got);
    if(LIVE.includes(k))live[th][k]=await js(`(function(){var l=[].slice.call(document.querySelectorAll('#view .layer')).pop();var c=l.cloneNode(true);[].forEach.call(l.querySelectorAll('canvas'),function(a,i){var b=c.querySelectorAll('canvas')[i],m=new Image();m.src=a.toDataURL();m.style.cssText=a.style.cssText;b.replaceWith(m)});return c.outerHTML})()`);
    await js(FREEZE+";document.getElementById('clock').textContent='9:41'");await sleep(40);
    const r=await cmd('Page.captureScreenshot',{format:'webp',quality:80});
    fs.writeFileSync(`${ROOT}/v6/${dir}/${k}.webp`,Buffer.from(r.data,'base64'));
  }catch(e){bad.push(th+':'+k+' '+e.message)}}
  console.log(th,'done');
}
fs.writeFileSync(ROOT+'/v6/live.json',JSON.stringify(live));
console.log('problems',bad.length,bad.join(' | '));
ws.close();chrome.kill();process.exit(0);
