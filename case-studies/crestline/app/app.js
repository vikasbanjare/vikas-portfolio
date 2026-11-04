// Crestline working prototype. Screens come from the generator; this file makes them behave.
(function(){
'use strict';
var META=window.CR_META,M=META.M,STOCKS=META.STOCKS,C=window.CR_CALC;
var $=function(q,r){return(r||document).querySelector(q)},$$=function(q,r){return[].slice.call((r||document).querySelectorAll(q))};
var view=$('#view'),RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
var IDX={'Nifty 50':24812.30,'Sensex':80912.65,'Bank Nifty':52104.60,'FinNifty':23560.15};
var FAMILY={Stock:1,Chart:1,Depth:1,StockAbout:1,Holding:1,Buy:1,BuyPrice:1,Review:1,Placing:1,Filled:1,Sell:1,SellReview:1,Sold:1,WatchAdd:1,Alerts:1,OrderTypes:1,Waiting:1,LoadStock:1};
var AUTO={Splash:['Language',3000],LoadHome:['Home',1300],LoadStock:['Stock',850],Placing:['Filled',1700]};
var SHEETS={ScreenFilters:1,Charges:1,CancelAsk:1,SipStop:1,SignOut:1,ExitAll:1,WatchAdd:1,OrderTypes:1,ShareSheet:1,ChartTools:1,RiskPopup:1};
var TABS={Home:1,Markets:1,Portfolio:1,AllProducts:1};
var FLT0={pe:100,roe:0,ret:-30,div:0};
var S={theme:'LT',stack:[],stock:null,logo:'',seen:{},tf:'1 day',ctype:'Candles',ind:{Volume:1},scr:{preset:'All',sort:'mcap',flt:Object.assign({},FLT0),off:{}},charts:[],timer:0};
function D(){return window['CR_'+S.theme]}
function T(){return D().T}
// ───── Sample stock context
function stockFrom(a){var t=a.textContent;for(var i=0;i<STOCKS.length;i++){var x=STOCKS[i];if(t.indexOf(x.short)>=0||t.indexOf(x.name)>=0)return x}return null}
function subst(key,h){if(key==='IndexDetail'&&S.idx&&S.idx!=='Nifty 50'){var f=IDX[S.idx]/24812.30;h=h.replace(/Nifty 50/g,S.idx).replace(/>(\d\d,\d{3}\.\d\d)</g,function(m,n){return'>'+C.inr(parseFloat(n.replace(',',''))*f,2)+'<'})}var c=S.stock;if(!c||c.short==='Reliance'||!FAMILY[key])return h;
  var cut=h.indexOf('<!--noscale-->'),tail='';if(cut>=0){tail=h.slice(cut);h=h.slice(0,cut)}
  var r=c.price/1248;
  h=h.replace(/Reliance Industries/g,c.name).replace(/Reliance/g,c.short);
  h=h.replace(/₹([\d,]+(?:\.\d+)?)(?![\d,.]*\s*(?:lakh|crore))/g,function(m,n){var v=parseFloat(n.replace(/,/g,''))*r;return'₹'+C.inr(v,n.indexOf('.')>=0?2:0)});
  if(key==='Depth')h=h.replace(/>(\d,\d{3}\.\d\d)</g,function(m,n){return'>'+C.inr(parseFloat(n.replace(',',''))*r,2)+'<'});
  return h+tail}
function stockFacts(root){var c=S.stock,sm=$$('[data-sim]',root);if(sm.length){var me=c||{sym:'RELIANCE',sector:'Energy'},n=0;sm.forEach(function(x){var ok=x.getAttribute('data-sim')===me.sector&&x.getAttribute('data-sim-sym')!==me.sym&&n<3;if(ok)n++;x.hidden=!ok});var hd=sm[0].closest('div[style*="margin"]');if(hd&&hd.previousElementSibling)hd.hidden=hd.previousElementSibling.hidden=!n}
  if(!c||c.short==='Reliance')return;
  var R1=rng(hash(c.sym)),rets=[c.ret*.08+(R1()-.5)*6,c.ret*.5+(R1()-.5)*10,c.ret,c.ret*1.7+18+R1()*10,c.ret*2.4+40+R1()*25];$$('[data-rt]',root).forEach(function(e,i){var v=rets[i];e.textContent=(v>=0?'+':'−')+Math.abs(v).toFixed(1)+'%';e.style.color=v>=0?T().up:T().dn});
  var l=$('[data-logo]',root);if(l&&S.logo)l.innerHTML=S.logo;
  var s=$('[data-sector]',root);if(s)s.textContent=c.sector;
  var a=$('[data-about]',root);if(a)a.textContent=c.about;
  var chg=$('[data-tk="s"] [data-c]',root);if(chg){chg.textContent=(c.chg>=0?'+':'−')+Math.abs(c.chg).toFixed(2)+'%';chg.style.color=c.chg>=0?T().up:T().dn}
  $$('div',root).forEach(function(d){if(d.children.length===2&&d.firstElementChild.tagName==='SPAN'){var k=d.firstElementChild.textContent,v=d.lastElementChild;
    if(k==='Market value')v.textContent='₹'+(c.mcap>=1e5?(c.mcap/1e5).toFixed(2)+' lakh crore':C.inr(c.mcap)+' crore');if(k==='P/E ratio')v.textContent=c.pe||'Not meaningful';if(k==='Return on equity')v.textContent=c.roe+'%';if(k==='Dividend yield')v.textContent=c.div+'%';if(k==='Debt to equity')v.textContent=c.de}})}
// ───── Chart: candles, line or area, with volume, an average, RSI and MACD. Prices are simulated.
function hash(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
function rng(a){return function(){a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
var TF={'1D':[75,.0011,5],'1W':[70,.002,30],'1M':[60,.006,1440],'6M':[90,.009,2880],'1Y':[100,.012,5040],'3Y':[110,.018,14400],'5Y':[120,.02,20160],'All':[150,.024,40320],'5 min':[72,.0012,5],'15 min':[72,.0018,15],'1 hour':[72,.003,60],'1 day':[90,.011,1440],'1 week':[80,.022,10080]};
function series(seed,n,last,vol){var R=rng(seed),a=new Array(n),c=last,drift=(R()-.42)*vol*.5;
  for(var i=n-1;i>=0;i--){var o=c*(1-drift+(R()-.5)*vol*2),hi=Math.max(o,c)*(1+R()*vol*.7),lo=Math.min(o,c)*(1-R()*vol*.7);a[i]={o:o,h:hi,l:lo,c:c,v:.25+R()};c=o}return a}
function sma(a,n){var o=[],s=0;for(var i=0;i<a.length;i++){s+=a[i].c;if(i>=n)s-=a[i-n].c;o.push(i>=n-1?s/n:null)}return o}
function rsi(a,n){var o=[],g=0,l=0;for(var i=0;i<a.length;i++){if(!i){o.push(null);continue}var d=a[i].c-a[i-1].c;if(i<=n){g+=Math.max(d,0);l+=Math.max(-d,0);o.push(i===n?100-100/(1+g/(l||1e-9)):null);continue}g=(g*(n-1)+Math.max(d,0))/n;l=(l*(n-1)+Math.max(-d,0))/n;o.push(100-100/(1+g/(l||1e-9)))}return o}
function ema(v,n){var k=2/(n+1),o=[],p=v[0];v.forEach(function(x){p=x*k+p*(1-k);o.push(p)});return o}
function macd(a){var c=a.map(function(x){return x.c}),f=ema(c,12),s=ema(c,26),m=f.map(function(x,i){return x-s[i]}),sg=ema(m,9);return{m:m,s:sg,h:m.map(function(x,i){return x-sg[i]})}}
function stamp(i,n,step){var d=new Date(Date.UTC(2026,10,3,10,0)-(n-1-i)*step*6e4),mo=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][d.getUTCMonth()];
  if(step<1440)return d.getUTCDate()+' '+mo+', '+('0'+d.getUTCHours()).slice(-2)+':'+('0'+d.getUTCMinutes()).slice(-2);return d.getUTCDate()+' '+mo+' '+d.getUTCFullYear()}
function Chart(host,kind,seedTxt,tf,last){
  var cv=document.createElement('canvas'),ctx=cv.getContext('2d'),me=this,W=0,H=0,cross=-1,prog=1,raf=0,data,bench,spec;
  cv.setAttribute('role','img');cv.setAttribute('aria-label',kind==='full'?'Interactive price chart':'Price chart');cv.style.cssText='display:block;width:100%;height:100%;touch-action:pan-y';host.appendChild(cv);
  this.tf=tf;this.ctype=kind==='full'?S.ctype:'Area';
  function load(){spec=TF[me.tf]||TF['1Y'];data=series(hash(seedTxt+me.tf),spec[0],last,spec[1]);if(kind==='compare')bench=series(hash('nifty'+me.tf),spec[0],100,spec[1]*.7);me.play()}
  this.play=function(){if(RM){prog=1;draw();return}var t0=performance.now();cancelAnimationFrame(raf);(function step(t){prog=Math.min(1,(t-t0)/620);prog=1-Math.pow(1-prog,3);draw();if(prog<1)raf=requestAnimationFrame(step)})(t0)};
  this.set=function(k,v){me[k]=v;if(k==='tf')load();else draw()};this.redraw=function(){draw()};
  this.nudge=function(r){var x=data[data.length-1];x.c*=1+r;x.h=Math.max(x.h,x.c);x.l=Math.min(x.l,x.c);draw()};this.kill=function(){cancelAnimationFrame(raf)};
  function size(){var r=host.getBoundingClientRect(),d=window.devicePixelRatio||1;W=host.clientWidth||r.width;H=host.clientHeight||r.height;cv.width=W*d;cv.height=H*d;ctx.setTransform(d,0,0,d,0,0)}
  function txt(s,x,y,c,al,sz){ctx.fillStyle=c;ctx.font=(sz||11)+'px Satoshi,sans-serif';ctx.textAlign=al||'left';ctx.fillText(s,x,y)}
  function draw(){if(!W)size();var t=T();ctx.clearRect(0,0,W,H);var n=data.length,show=Math.max(2,Math.ceil(n*prog)),full=kind==='full';
    var ind=S.ind,subs=full?(ind.RSI?1:0)+(ind.MACD?1:0):0,subH=62,pr=full?50:2,pt=full?10:6,pb=full?18:2,mainB=H-pb-subs*subH,bw=(W-pr)/n;
    var hi=-1e18,lo=1e18;data.forEach(function(d){hi=Math.max(hi,d.h);lo=Math.min(lo,d.l)});if(kind==='compare'){var rA=data[0].c,rB=bench[0].c;hi=-1e18;lo=1e18;data.forEach(function(d,i){var a=d.c/rA,b=bench[i].c/rB;hi=Math.max(hi,a,b);lo=Math.min(lo,a,b)})}
    var pad=(hi-lo)*.06;hi+=pad;lo-=pad;var volH=full&&ind.Volume?(mainB-pt)*.18:0,top=pt,bot=mainB-volH-(full?4:0);
    var Y=function(v){return top+(hi-v)/(hi-lo)*(bot-top)},X=function(i){return(i+.5)*bw};
    if(full){ctx.strokeStyle=t.ln;ctx.lineWidth=1;for(var g=0;g<4;g++){var v=lo+(hi-lo)*(g+.5)/4,y=Math.round(Y(v))+.5;ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();txt(C.inr(v,v<100?2:0),W-4,y-3,t.gr,'right')}
      var q=Math.floor(n/3);for(var j=1;j<3;j++)txt(stamp(j*q,n,spec[2]).replace(/ 20\d\d$/,''),X(j*q),H-5-subs*0,t.gr,'center',10.5)}
    var up=data[show-1].c>=data[0].c,col=kind==='compare'?t.br:(up?t.up:t.dn);
    if(volH){var mv=Math.max.apply(null,data.map(function(d){return d.v}));for(var i=0;i<show;i++){var d=data[i],h=d.v/mv*volH;ctx.globalAlpha=.32;ctx.fillStyle=d.c>=d.o?t.up:t.dn;ctx.fillRect(X(i)-bw*.33,mainB-h,bw*.66,h)}ctx.globalAlpha=1}
    if(kind==='compare'){line(bench.slice(0,show).map(function(d){return d.c/rB}),t.gr,1.3);line(data.slice(0,show).map(function(d){return d.c/rA}),t.br,1.9,true)}
    else if(me.ctype==='Candles'){for(var i2=0;i2<show;i2++){var a=data[i2],c2=a.c>=a.o?t.up:t.dn,x=X(i2);ctx.strokeStyle=c2;ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x,Y(a.h));ctx.lineTo(x,Y(a.l));ctx.stroke();ctx.fillStyle=c2;var ya=Y(Math.max(a.o,a.c));ctx.fillRect(x-bw*.34,ya,bw*.68,Math.max(1,Y(Math.min(a.o,a.c))-ya))}}
    else line(data.slice(0,show).map(function(d){return d.c}),col,1.7,me.ctype==='Area');
    if(full&&ind.Average){var m=sma(data,20);ctx.strokeStyle=t.br;ctx.lineWidth=1.3;ctx.beginPath();var st=0;for(var i3=0;i3<show;i3++){if(m[i3]==null)continue;st++?ctx.lineTo(X(i3),Y(m[i3])):ctx.moveTo(X(i3),Y(m[i3]))}ctx.stroke()}
    var lastp=data[show-1];if(kind!=='compare'){if(full){var yl=Y(lastp.c);ctx.setLineDash([3,3]);ctx.strokeStyle=col;ctx.beginPath();ctx.moveTo(0,yl);ctx.lineTo(W-pr,yl);ctx.stroke();ctx.setLineDash([]);ctx.fillStyle=col;rr(W-pr,yl-9,pr-1,18,5);ctx.fill();txt(C.inr(lastp.c,lastp.c<100?2:0),W-pr/2-.5,yl+4,'#FFF','center',11)}
      else{ctx.fillStyle=col;ctx.beginPath();ctx.arc(X(show-1),Y(lastp.c),3.2,0,7);ctx.fill()}}
    var yS=mainB+(full?16:0);
    if(subs){var sTop=H-pb-subs*subH+6;if(ind.RSI){var r=rsi(data,14);sub(sTop,subH-14,'RSI 14',[0,100],function(){[30,70].forEach(function(l){var yy=sTop+(100-l)/100*(subH-14);ctx.strokeStyle=t.ln;ctx.beginPath();ctx.moveTo(0,yy);ctx.lineTo(W-pr,yy);ctx.stroke()});ctx.strokeStyle=t.br;ctx.lineWidth=1.3;ctx.beginPath();var st2=0;for(var i4=0;i4<show;i4++){if(r[i4]==null)continue;var yy=sTop+(100-r[i4])/100*(subH-14);st2++?ctx.lineTo(X(i4),yy):ctx.moveTo(X(i4),yy)}ctx.stroke()});sTop+=subH}
      if(ind.MACD){var mc=macd(data),mx=Math.max.apply(null,mc.m.concat(mc.s).map(Math.abs))||1,hh=subH-14,YM=function(v,tp){return tp+hh/2-v/mx*hh/2},tp0=sTop;sub(tp0,hh,'MACD',null,function(){for(var i5=0;i5<show;i5++){var v5=mc.h[i5];ctx.fillStyle=v5>=0?t.up:t.dn;ctx.globalAlpha=.5;var y0=YM(0,tp0),y1=YM(v5,tp0);ctx.fillRect(X(i5)-bw*.3,Math.min(y0,y1),bw*.6,Math.max(1,Math.abs(y1-y0)))}ctx.globalAlpha=1;ctx.strokeStyle=t.br;ctx.lineWidth=1.2;ctx.beginPath();for(var i6=0;i6<show;i6++){i6?ctx.lineTo(X(i6),YM(mc.m[i6],tp0)):ctx.moveTo(X(i6),YM(mc.m[i6],tp0))}ctx.stroke()})}}
    if(cross>=0&&cross<n){var cx=data[cross],xc=X(cross);ctx.strokeStyle=t.gr;ctx.lineWidth=1;ctx.setLineDash([3,3]);ctx.beginPath();ctx.moveTo(xc,0);ctx.lineTo(xc,H-pb);ctx.stroke();ctx.setLineDash([]);
      var lab=kind==='compare'?['You '+((cx.c/data[0].c-1)*100).toFixed(1)+'%','Nifty 50 '+((bench[cross].c/bench[0].c-1)*100).toFixed(1)+'%']:full&&me.ctype==='Candles'?['O '+C.inr(cx.o,2)+'   H '+C.inr(cx.h,2),'L '+C.inr(cx.l,2)+'   C '+C.inr(cx.c,2)]:['₹'+C.inr(cx.c,2)];
      lab.unshift(stamp(cross,n,spec[2]));ctx.font='11.5px Satoshi,sans-serif';var tw=Math.max.apply(null,lab.map(function(s){return ctx.measureText(s).width}))+18,th=lab.length*15+9,bx=Math.min(Math.max(2,xc-tw/2),W-tw-2);
      ctx.fillStyle=t.ink;rr(bx,1,tw,th,8);ctx.fill();lab.forEach(function(s,i){txt(s,bx+9,16+i*15,t.card,'left',11.5)})}
    function line(v,c,w,area){ctx.beginPath();v.forEach(function(p,i){i?ctx.lineTo(X(i),Y(p)):ctx.moveTo(X(i),Y(p))});ctx.strokeStyle=c;ctx.lineWidth=w;ctx.lineJoin='round';ctx.stroke();if(area){ctx.lineTo(X(v.length-1),bot);ctx.lineTo(X(0),bot);ctx.closePath();var g=ctx.createLinearGradient(0,top,0,bot);g.addColorStop(0,c+'2E');g.addColorStop(1,c+'00');ctx.fillStyle=g;ctx.fill()}}
    function sub(y,h,name,rng_,fn){ctx.save();fn();ctx.restore();txt(name,4,y+10,t.gr,'left',10.5)}
    function rr(x,y,w,h,r){ctx.beginPath();ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath()}
  }
  function pos(e){var r=cv.getBoundingClientRect(),n=data.length,pr=kind==='full'?50:2;return Math.max(0,Math.min(n-1,Math.floor((e.clientX-r.left)*(cv.offsetWidth/r.width)/((W-pr)/n))))}
  cv.addEventListener('pointermove',function(e){cross=pos(e);draw()});cv.addEventListener('pointerdown',function(e){cross=pos(e);draw();e.stopPropagation()});
  cv.addEventListener('pointerleave',function(){cross=-1;draw()});cv.addEventListener('click',function(e){e.preventDefault();e.stopPropagation()});
  size();load()}
// ───── Pick controls: chips, tabs, ranges
function setupPick(p){var kids=[].slice.call(p.children);var on=kids.filter(function(k){return k.hasAttribute('data-on')})[0],off=kids.filter(function(k){return!k.hasAttribute('data-on')})[0];p._on=on?on.style.cssText:'';
  if(off)p._off=off.style.cssText;else{var c=on.cloneNode(false);c.style.background=T().card;c.style.color=T().ink;c.style.fontWeight='400';p._off=c.style.cssText}}
function setOn(p,k,v){k.style.cssText=v?p._on:p._off;if(v)k.setAttribute('data-on','1');else k.removeAttribute('data-on')}
function pickByText(p,txts){[].slice.call(p.children).forEach(function(k){setOn(p,k,txts.indexOf(k.textContent.trim())>=0)})}
function picked(p){return[].slice.call(p.children).filter(function(k){return k.hasAttribute('data-on')}).map(function(k){return k.textContent.trim()})}
function screenRoot(el){return el.closest('[data-root]')}
function onPick(p,txt,root){var ch=S.charts;
  if(p.hasAttribute('data-tabs')){var g=p.getAttribute('data-tabs'),i=[].slice.call(p.children).findIndex(function(k){return k.hasAttribute('data-on')});$$('[data-panel^="'+g+':"]',root).forEach(function(x){x.hidden=x.getAttribute('data-panel')!==g+':'+i});layout(root);stagger(root)}
  if(p.hasAttribute('data-ranges')){var host=p.parentElement.parentElement.querySelector('[data-host]')||root.querySelector('[data-host]');if(host&&host._chart)host._chart.set('tf',txt)}
  if(p.hasAttribute('data-tf')){S.tf=txt;ch.forEach(function(c){c.set('tf',txt)})}
  if(p.hasAttribute('data-ctype')){S.ctype=txt;ch.forEach(function(c){c.set('ctype',txt)})}
  if(p.hasAttribute('data-ind')){S.ind={};picked(p).forEach(function(k){S.ind[k]=1});ch.forEach(function(c){c.redraw()})}
  if(p.hasAttribute('data-filter')){$$('[data-tag]',root).forEach(function(r){r.hidden=txt!=='All'&&r.getAttribute('data-tag').split('|').indexOf(txt)<0});layout(root)}
  if(p.hasAttribute('data-preset')){S.scr.preset=txt;screener(root)}
  if(p.hasAttribute('data-sectors')){S.scr.off={};[].slice.call(p.children).forEach(function(k){if(!k.hasAttribute('data-on'))S.scr.off[k.textContent.trim()]=1});fcount(root)}
  if(p.hasAttribute('data-theme-seg')){setTheme(txt==='Dark'?'DK':txt==='Light'?'LT':(matchMedia('(prefers-color-scheme:dark)').matches?'DK':'LT'),txt)}
  if(p.hasAttribute('data-opt'))recalc(p.closest('[data-calc]'));
  var am=$('[data-amt]',root);if(am&&/^(All |Max )?₹?[\d,]+$/.test(txt)){am.textContent=txt.replace(/^(All|Max) /,'');var sub=am.nextElementSibling,qty=parseInt(am.textContent.replace(/\D/g,''));if(sub&&/^About ₹/.test(sub.textContent)&&am.textContent.charAt(0)!=='₹')sub.textContent=sub.textContent.replace(/^About ₹[\d,]+/,'About ₹'+C.inr(qty*(S.stock?S.stock.price:1248)))}
  if(/^FY /.test(txt)||p.hasAttribute('data-rescale')){var i2=[].slice.call(p.children).findIndex(function(k){return k.hasAttribute('data-on')});$$('span,div',root).forEach(function(e){if(e.children.length||p.contains(e))return;var v=e.textContent.trim();if(!/^[+−-]?₹?[\d,]+\.\d\d$|^₹[\d,]+$/.test(v))return;if(!e.hasAttribute('data-b'))e.setAttribute('data-b',v);var b=e.getAttribute('data-b'),n=parseFloat(b.replace(/[^\d.]/g,''))*(1+i2*.23),dec=b.indexOf('.')>=0?2:0;e.textContent=b.replace(/[\d,]+(\.\d+)?/,C.inr(n,dec))})}}
// ───── Screener
function match(x){var f=S.scr.flt,p=S.scr.preset;if(S.scr.off[x.sector])return false;
  if(f.pe<100&&(!x.pe||x.pe>f.pe))return false;if(x.roe<f.roe||x.ret<f.ret||x.div<f.div)return false;
  return p==='All'||(p==='Quality'&&x.roe>=18&&x.de<=1)||(p==='Value'&&x.pe>0&&x.pe<=20)||(p==='Momentum'&&x.ret>=20)||(p==='Dividend'&&x.div>=2)||(p==='Low debt'&&x.de<=.2)}
function plural(n){return n+(n===1?' stock':' stocks')}
function screener(root){var box=$('[data-st]',root);if(!box)return;var list=box.parentElement,s=S.scr.sort,rows=$$('[data-st]',list),by={};STOCKS.forEach(function(x){by[x.sym]=x});
  rows.sort(function(a,b){var x=by[a.getAttribute('data-st')],y=by[b.getAttribute('data-st')];return s==='pe'?((x.pe||1e9)-(y.pe||1e9)):y[s]-x[s]}).forEach(function(r){list.appendChild(r);r.hidden=!match(by[r.getAttribute('data-st')])});
  var c=STOCKS.filter(match).length;$('[data-scount]',root).textContent=plural(c);layout(root)}
function fcount(root){var c=$('[data-fcount]',root);if(c)c.textContent=plural(STOCKS.filter(match).length)+' match'}
// ───── Calculators and sliders
function fmtv(f,v){return f==='inr'?'₹'+C.inr(v):f==='pct'?v+'%':f==='yr'?v+(v===1?' year':' years'):f==='n'?C.inr(v):String(v)}
function paint(r){r.style.setProperty('--f',((r.value-r.min)/(r.max-r.min)*100)+'%')}
function recalc(box){var v={};$$('.rg',box).forEach(function(r){v[r.getAttribute('data-k')]=+r.value});var o=$('[data-opt]',box);if(o)v.opt=picked(o)[0];var res=C[box.getAttribute('data-calc')](v);$('[data-o="r"]',box).textContent=res.r;$('[data-o="s"]',box).textContent=res.s}
// ───── Live-looking prices
function num(t){var m=t.match(/[\d,]+\.\d+/);return m?parseFloat(m[0].replace(/,/g,'')):null}
function tick(){var layer=topLayer();if(!layer||document.hidden)return;var root=$('[data-root]',layer),key=S.stack[S.stack.length-1];
  var all=$$('[data-tk]',root).filter(function(e){return e.offsetParent!==null&&num($('[data-p]',e).textContent)!==null});
  if(key==='Home')all=all.filter(function(e){return!/shares/.test(e.parentElement.textContent)});
  if(!/^(Home|Markets|Watchlist|Search|Movers|Screener|Stock|Chart|Depth|FoWatch|IndexDetail|Gold|EtfList)$/.test(key))return;
  for(var i=0;i<Math.min(3,all.length);i++){var e=all[Math.floor(Math.random()*all.length)],stock=e.getAttribute('data-tk')==='s',p=$('[data-p]',e),c=$('[data-c]',e),old=num(p.textContent),dr=(Math.random()-.47)*.0012,nv=old*(1+dr),pre=p.textContent.charAt(0)==='₹'?'₹':'';
    p.textContent=pre+C.inr(nv,2);
    if(c){var m=c.textContent.match(/([+−-])([\d.]+)%/);if(m){var cv=(m[1]==='+'?1:-1)*parseFloat(m[2])+dr*100;c.textContent=(cv>=0?'+':'−')+Math.abs(cv).toFixed(2)+'%';c.style.color=cv>=0?T().up:T().dn}}
    if(!RM)p.animate([{color:dr>=0?T().up:T().dn},{color:getComputedStyle(p).color}],{duration:700,easing:'ease-out'});
    if(stock){S.charts.forEach(function(ch){ch.nudge(dr)});break}}
  if(key==='Depth')$$('[data-root] span',layer).forEach(function(s){if(/^\d[\d,]*$/.test(s.textContent)&&Math.random()<.18)s.textContent=C.inr(Math.max(50,Math.round(parseInt(s.textContent.replace(/,/g,''))*(.9+Math.random()*.2))))})}
// ───── Screen mounting
function topLayer(){var l=$$('.layer',view);return l[l.length-1]}
function layout(root){var layer=root.closest('.layer');if(!layer)return;var dock=$('.dock',layer),vh=layer.clientHeight,dh=0;
  $$(':scope > *',dock).forEach(function(c){if(c.classList.contains('fade'))return;var b=parseFloat(getComputedStyle(c).bottom)||0;dh=Math.max(dh,c.offsetHeight+b)});
  root.style.height='auto';var flow=root.offsetHeight,ab=0;
  $$(':scope > *',root).forEach(function(c){var s=getComputedStyle(c);if(s.position==='absolute'&&s.bottom!=='auto')ab=Math.max(ab,c.offsetHeight+parseFloat(s.bottom))});
  var need=flow+Math.max(dh,ab)+(dh||ab?10:0);root.style.height=Math.max(vh,need)+'px';
  var f=$('.fade',dock);if(f){f.style.height=(dh+18)+'px';f.style.display=need>vh&&dh?'block':'none'}}
function stagger(root){if(RM)return;$$('[data-l]',root).slice(0,10).forEach(function(r,i){if(r.offsetParent)r.animate([{opacity:0,transform:'translateY(6px)'},{opacity:1,transform:'none'}],{duration:280,delay:i*28,easing:'ease-out',fill:'backwards'})})}
function enhance(root,key){
  $$('[data-pick]',root).forEach(setupPick);stockFacts(root);
  $$('svg[data-chart]',root).forEach(function(svg){var kind=svg.getAttribute('data-chart'),host=document.createElement('div');host.setAttribute('data-host','');
    host.style.cssText=svg.style.cssText;host.style.height=svg.getAttribute('height')+'px';host.style.width=kind==='full'?'auto':'100%';svg.replaceWith(host);
    var hasR=host.parentElement.querySelector('[data-ranges]'),tf=kind==='full'?S.tf:hasR?picked(hasR)[0]:'1Y',last=S.stock&&FAMILY[key]?S.stock.price:key==='Stock'||key==='Chart'?1248:key==='IndexDetail'?(IDX[S.idx]||24812.3):key==='Gold'?72450:103250;
    var ch=new Chart(host,kind,key+(S.stock?S.stock.sym:'RELIANCE')+svg.getAttribute('data-seed'),tf,last);host._chart=ch;S.charts.push(ch)});
  var tfP=$('[data-tf]',root);if(tfP){pickByText(tfP,[S.tf]);pickByText($('[data-ctype]',root),[S.ctype]);pickByText($('[data-ind]',root),Object.keys(S.ind))}
  if(key==='ChartTools')$$('[data-sw]',root).forEach(function(sw){var n=sw.previousElementSibling.textContent.trim().replace('Moving average','Average');flip(sw,!!S.ind[n])});
  if(key==='Appearance'){var seg=$('[data-theme-seg]',root);pickByText(seg,[S.themeLabel||(S.theme==='DK'?'Dark':'Light')])}
  var pre=$('[data-preset]',root);if(pre){pickByText(pre,[S.scr.preset]);var so=$('[data-ssort]',root);so.value=S.scr.sort;so.addEventListener('change',function(){S.scr.sort=so.value;screener(root)});screener(root)}
  if(key==='ScreenFilters'){$$('[data-flt]',root).forEach(function(r){r.value=S.scr.flt[r.getAttribute('data-k')];paint(r);$('[data-v="'+r.getAttribute('data-k')+'"]',root).textContent=fmtv(r.getAttribute('data-fmt'),+r.value)});var sc=$('[data-sectors]',root);[].slice.call(sc.children).forEach(function(k){setOn(sc,k,!S.scr.off[k.textContent.trim()])});fcount(root)}
  $$('[data-calc]',root).forEach(recalc);
  var srch=$('[data-search]',root);if(srch){var run=function(){var q=srch.value.trim().toLowerCase();$$('[data-sr]',root).forEach(function(r){r.hidden=!q||r.getAttribute('data-sr').indexOf(q)<0});var sec=$('[data-sec]',root);if(sec)sec.hidden=q.length>0&&!/nip|fund|etf|pay|mtf|sma/.test(q);if(!window.CR_HTML){var rows=$$('[data-sr]',root),any=false,boxes=[];rows.forEach(function(r){if(boxes.indexOf(r.parentElement)<0)boxes.push(r.parentElement)});boxes.forEach(function(b){var on=rows.some(function(r){return r.parentElement===b&&!r.hidden});any=any||on;b.hidden=!on;var h=b.previousElementSibling;if(h&&$('h2',h))h.hidden=!on});var none=$('.nomatch',root);if(!none){none=document.createElement('p');none.className='nomatch';none.style.color=T().gr;root.appendChild(none)}none.hidden=!q||any||!!(sec&&!sec.hidden);none.textContent='Nothing matches "'+q+'". Try a company name or a feature such as IPO.'}layout(root)};srch.addEventListener('input',run);run()}
  $$('[data-snap]',root).forEach(function(sn){var dots=$$('[data-sdot]',root);if(!dots.length)return;sn.addEventListener('scroll',function(){var i=Math.round(sn.scrollLeft/sn.clientWidth);dots.forEach(function(d,j){d.style.background=j===i?T().br:T().track})},{passive:true})});
  $$('.rg',root).forEach(function(r){r.addEventListener('input',function(){paint(r);var v=$('[data-v="'+r.getAttribute('data-k')+'"]',root);if(v)v.textContent=fmtv(r.getAttribute('data-fmt'),+r.value);var b=r.closest('[data-calc]');if(b)recalc(b);if(r.hasAttribute('data-flt')){S.scr.flt[r.getAttribute('data-k')]=+r.value;fcount(root)}})});
}
function mount(key,cls){var d=D().S[key],layer=document.createElement('div'),sc=document.createElement('div'),root=document.createElement('div'),dock=document.createElement('div');
  layer.className='layer '+(cls||'');sc.className='scroll';dock.className='dock';var end=(d[1].match(/#[0-9A-Fa-f]{6}(?![\s\S]*#[0-9A-Fa-f]{6})/)||[T().bg])[0];layer.style.background=end;
  root.setAttribute('data-root','');root.style.cssText='position:relative;overflow:hidden;background:'+d[1]+';color:'+T().ink+';font-family:Satoshi,"Anek Devanagari",sans-serif;-webkit-font-smoothing:antialiased';root.innerHTML=subst(key,d[0]);
  var fade=document.createElement('div');fade.className='fade';fade.style.background='linear-gradient(transparent,'+end+' 40%)';dock.appendChild(fade);
  $$('[data-cta]',root).forEach(function(c){dock.appendChild(c)});sc.appendChild(root);layer.appendChild(sc);layer.appendChild(dock);view.appendChild(layer);
  sc.addEventListener('scroll',function(){document.body.classList.toggle('scrolled',sc.scrollTop>6)},{passive:true});
  if(key==='Festive')root.style.paddingTop='50px';
  layout(root);enhance(root,key);layout(root);return layer}
function anim(el,frames,dur,done){if(RM){if(done)done();return}var a=el.animate(frames,{duration:dur||280,easing:'cubic-bezier(.2,.8,.2,1)'});if(done)a.onfinish=done}
function clearCharts(){S.charts.forEach(function(c){c.kill()});S.charts=[]}
function show(key,mode){var prev=$$('.layer',view);clearInterval(S.timer);document.body.classList.remove('scrolled');
  if(mode==='sheet'){var bk=document.createElement('div');bk.className='backdrop';view.appendChild(bk);var sh=mount(key,'sheet');anim(bk,[{opacity:0},{opacity:1}],220);anim(sh,[{transform:'translateY(100%)'},{transform:'none'}],320)}
  else{clearCharts();$$('.backdrop',view).forEach(function(b){b.remove()});var n=mount(key);var kill=function(){prev.forEach(function(p){p.remove()})};
    if(mode==='fade'||!prev.length){kill();anim(n,[{opacity:0},{opacity:1}],200)}
    else if(mode==='back'){prev.forEach(function(p){p.style.zIndex=3;anim(p,[{transform:'none'},{transform:'translateX(100%)'}],260,kill)});if(RM)kill();else anim(n,[{transform:'translateX(-22%)'},{transform:'none'}],260)}
    else if(mode==='none')kill();
    else{anim(n,[{transform:'translateX(100%)'},{transform:'none'}],300,kill);if(RM)kill();else prev.forEach(function(p){anim(p,[{transform:'none'},{transform:'translateX(-22%)'}],300)})}}
  document.body.setAttribute('data-screen',key);document.documentElement.setAttribute('data-app-theme',S.theme);panel(key);
  try{history.replaceState(null,'','#'+key)}catch(e){}
  var a=AUTO[key];if(a){clearTimeout(S.auto);S.auto=setTimeout(function(){if(S.stack[S.stack.length-1]===key){S.stack.pop();nav(a[0],{replace:1})}},a[1])}
  $('#status').hidden=key==='Splash'}
function isSheet(k){return!!SHEETS[k]}
function nav(key,o){o=o||{};if(!D().S[key])return;
  var st=S.stack,cur=st[st.length-1];
  if(key==='Stock'&&cur!=='LoadStock'&&!S.seen[S.stock?S.stock.sym:'RELIANCE']){S.seen[S.stock?S.stock.sym:'RELIANCE']=1;key='LoadStock'}
  if(!o.replace&&st.length>1&&st[st.length-2]===key)return pop();
  if(TABS[key]&&o.tab){S.stack=[key];if(key!=='Home'||1)S.stock=null;return show(key,'fade')}
  if(cur&&isSheet(cur)&&!isSheet(key)){$$('.backdrop',view).forEach(function(b){b.remove()});st.pop();st.push(key);return show(key,'push')}
  st.push(key);show(key,isSheet(key)&&cur?'sheet':o.replace?'none':o.fade?'fade':'push')}
function pop(){var st=S.stack;if(st.length<2)return;var was=st.pop(),key=st[st.length-1];
  if(isSheet(was)){var ls=$$('.layer',view),t=ls[ls.length-1],bk=$$('.backdrop',view);var fin=function(){t.remove();bk.forEach(function(b){b.remove()})};
    clearCharts();$$('.layer',view).slice(0,-1).forEach(function(l){var r=$('[data-root]',l);var n=mount(key,'');l.replaceWith(n);view.insertBefore(n,bk[bk.length-1]||t)});
    if(RM)fin();else{anim(t,[{transform:'none'},{transform:'translateY(100%)'}],240,fin);bk.forEach(function(b){anim(b,[{opacity:1},{opacity:0}],240)})}
    panel(key);document.body.setAttribute('data-screen',key);try{history.replaceState(null,'','#'+key)}catch(e){}return}
  show(key,'back')}
function flip(sw,on){var k=sw.firstElementChild;sw.style.background=on?T().br:T().track;k.style.left=on?'auto':'3px';k.style.right=on?'3px':'auto';if(on)sw.setAttribute('data-on','1');else sw.removeAttribute('data-on')}
function toast(m){var o=$('#toast');if(o)o.remove();var d=document.createElement('div');d.id='toast';d.setAttribute('role','status');d.textContent=m;$('#phone').appendChild(d);if(!RM)d.animate([{opacity:0,transform:'translateY(8px)'},{opacity:1,transform:'none'}],{duration:200,easing:'ease-out'});setTimeout(function(){d.remove()},1900)}
// ───── Keypad
function keypad(lab,root,key){var boxes=$$('[data-otp]',root),dots=$$('[data-dot]',root),am=$('[data-amt]',root);
  var next=function(){var g=M[key].go[0];if(g)setTimeout(function(){nav(g[1])},180)};
  if(boxes.length){var f=boxes.filter(function(b){return b.textContent.trim()});if(lab==='Delete'){if(f.length)f[f.length-1].textContent=''}else{var b=boxes[f.length];if(b){b.textContent=lab;if(!RM)b.animate([{transform:'scale(.86)'},{transform:'none'}],140);if(f.length+1===boxes.length)next()}}return}
  if(dots.length){var on=dots.filter(function(d){return d.hasAttribute('data-on')});if(lab==='Delete'){if(on.length){var l=on[on.length-1];l.removeAttribute('data-on');l.style.background=T().track}}else{var d=dots[on.length];if(d){d.setAttribute('data-on','1');d.style.background=T().br;if(!RM)d.animate([{transform:'scale(.6)'},{transform:'none'}],160);if(on.length+1===dots.length)next()}}return}
  if(key==='WrongOtp'){var bx=$$('span',root).filter(function(e){return /^\d$/.test(e.textContent.trim())&&!e.children.length});if(lab==='Delete'){var la=bx[bx.length-1];if(la)la.textContent=''}else{nav('Otp')}return}
  if(am){var v=am.textContent.replace(/[^\d.]/g,'');v=lab==='Delete'?v.slice(0,-1):(v==='0'?'':v)+lab;if(v.replace(/\D/g,'').length>9)return;am.textContent='₹'+(v?C.inr(parseFloat(v),v.indexOf('.')>=0?2:0):'0')}}
// ───── Clicks
view.addEventListener('click',function(e){var t=e.target,root=screenRoot(t)||(t.closest('.layer')&&$('[data-root]',t.closest('.layer')));
  if(t.closest('.backdrop')){e.preventDefault();return pop()}
  if(t.closest('canvas')||t.closest('summary')||t.closest('select')||t.closest('input'))return;
  var key=S.stack[S.stack.length-1];
  var ch=t.closest('[data-pick] > *');
  if(ch&&!ch.hasAttribute('href')&&ch.tagName!=='A'){var p=ch.parentElement;e.preventDefault();if(p.hasAttribute('data-multi'))setOn(p,ch,!ch.hasAttribute('data-on'));else [].slice.call(p.children).forEach(function(k){setOn(p,k,k===ch)});if(!RM)ch.animate([{transform:'scale(.95)'},{transform:'none'}],150);return onPick(p,ch.textContent.trim(),root||view)}
  var lg=t.closest('[data-lang]');if(lg){$$('[data-sel]',root).forEach(function(x){x.hidden=x.parentElement!==lg});return}
  var kb=t.closest('button[aria-label]');if(kb){var lb=kb.getAttribute('aria-label');if(/^(\d|\.|Delete)$/.test(lb)){e.preventDefault();return keypad(lb,root,key)}}
  if(kb&&kb.getAttribute('aria-label')==='Copy'||(t.closest('button')&&!t.closest('a[href]')&&t.closest('button').textContent.trim()==='Copy')){var cb=t.closest('button');var old=cb.innerHTML;cb.textContent='Copied';setTimeout(function(){cb.innerHTML=old},1200);toast('Copied');return}
  if(kb&&kb.getAttribute('aria-label')==='Pro mode'){S.pro=!S.pro;toast(S.pro?'Pro mode on':'Pro mode off');return}
  var a=t.closest('a[href]'),sw=t.closest('[data-sw]')||((t.closest('div')||{}).querySelector&&!a&&t.closest('div').querySelector(':scope > [data-sw]'));
  if(sw&&!a){flip(sw,!sw.hasAttribute('data-on'));if(key==='ChartTools'){var n=sw.previousElementSibling.textContent.trim().replace('Moving average','Average');if(sw.hasAttribute('data-on'))S.ind[n]=1;else delete S.ind[n]}return}
  if(!a)return;var href=a.getAttribute('href');e.preventDefault();if(!href||href==='#')return;var m=href.match(/^S(.+)(Lt|Dk)\.dc\.html$/);if(!m)return;var to=m[1];
  var label=(t.closest('button')||a).textContent.trim();
  if(key==='Intro'&&!/skip/i.test(label)){var sn=$('[data-snap]',root);var i=Math.round(sn.scrollLeft/sn.clientWidth);if(i<2){sn.scrollTo({left:(i+1)*sn.clientWidth,behavior:RM?'auto':'smooth'});return}}
  if(key==='ScreenFilters'||key==='ScreenEmpty'){if(/reset|clear/i.test(label)){S.scr.flt=Object.assign({},FLT0);S.scr.off={};S.scr.preset='All'}else if(/show results/i.test(label)&&!STOCKS.filter(match).length){S.stack.pop();$$('.backdrop',view).forEach(function(b){b.remove()});return nav('ScreenEmpty',{fade:1})}}
  if(to==='IndexDetail'){var tx=a.textContent;S.idx=Object.keys(IDX).filter(function(n){return tx.indexOf(n)>=0})[0]||'Nifty 50'}
  var TM={'Add':'Added to watchlist','Save':'Saved','Apply':'Applied','Set alert':'Alert set','Remove':'Removed','Done':''};if(TM[label])setTimeout(function(){toast(TM[label])},260);
  if(TO_STOCK[to]){var f=stockFrom(a);if(f){S.stock=f;var lg=a.querySelector('svg')||a.querySelector('span');S.logo=lg?lg.outerHTML:''}}
  if(kb&&/^(Back|Close)$/.test(kb.getAttribute('aria-label'))&&S.stack.length>1)return pop();
  if(a.parentElement&&a.parentElement.hasAttribute('data-pick')){S.stack.pop();return nav(to,{fade:1})}
  nav(to,{tab:!!a.closest('nav')})});
view.addEventListener('pointerdown',function(e){var b=e.target.closest('button');if(b&&!RM)b.animate([{transform:'none'},{transform:'scale(.975)'},{transform:'none'}],{duration:220,easing:'ease-out'})});
var TO_STOCK={Stock:1,LoadStock:1,Holding:1};
// ───── Theme
function setTheme(th,label){S.themeLabel=label||(th==='DK'?'Dark':'Light');var go=function(){S.theme=th;var key=S.stack[S.stack.length-1],stack=S.stack;$$('.layer,.backdrop',view).forEach(function(l){l.remove()});clearCharts();show(key,'none');$$('[data-themebtn]').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-themebtn')===th?'true':'false')})};
  if(window['CR_'+th])return go();var s=document.createElement('script');s.src='screens-'+th.toLowerCase()+'.js';s.onload=go;document.head.appendChild(s)}
// ───── Side panel
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function panel(key){var m=M[key];$('#here').textContent=m.id+' · '+m.name;var layer=topLayer(),links={};if(layer)$$('a[href]',layer).forEach(function(a){var x=(a.getAttribute('href')||'').match(/^S(.+)(Lt|Dk)/);if(x)links[x[1]]=1});
  var seen={},alts=m.go.filter(function(g){if(links[g[1]]||seen[g[1]]||!D().S[g[1]])return false;seen[g[1]]=1;return true});
  $('#alts').innerHTML=alts.length?alts.map(function(g){return'<button type="button" data-jump="'+esc(g[1])+'">'+esc(g[0])+'</button>'}).join(''):'<p class="dim">Everything from here is on the screen.</p>'}
var list=$('#jump');list.innerHTML=META.F.map(function(f){return'<details><summary>'+esc(f.name)+' <span class="dim">'+f.keys.length+'</span></summary><div>'+f.keys.map(function(k){return'<button type="button" data-jump="'+k+'"><span class="dim">'+M[k].id+'</span> '+esc(M[k].name)+'</button>'}).join('')+'</div></details>'}).join('');
$('#find').addEventListener('input',function(){var q=this.value.trim().toLowerCase();$$('#jump details').forEach(function(d){var any=false;$$('button',d).forEach(function(b){var ok=!q||b.textContent.toLowerCase().indexOf(q)>=0;b.hidden=!ok;any=any||ok});d.hidden=!any;d.open=!!q&&any})});
document.addEventListener('click',function(e){var j=e.target.closest('[data-jump]');if(j){document.body.classList.remove('panel-open');var k=j.getAttribute('data-jump');S.stack=[];nav(k,{fade:1});return}
  var tb=e.target.closest('[data-themebtn]');if(tb)return setTheme(tb.getAttribute('data-themebtn'));
  if(e.target.closest('#restart')){S.stack=[];S.stock=null;S.seen={};S.scr={preset:'All',sort:'mcap',flt:Object.assign({},FLT0),off:{}};return nav('Splash',{fade:1})}
  if(e.target.closest('#more'))return document.body.classList.toggle('panel-open');
  if(e.target.closest('#closepanel'))document.body.classList.remove('panel-open')});
addEventListener('hashchange',function(){var h=location.hash.slice(1);if(D().S[h]&&h!==S.stack[S.stack.length-1]){S.stack=[];nav(h,{fade:1})}});
function fit(){var ph=$('#phone');if(innerWidth<760){ph.style.transform='';return}var s=Math.min(1,(innerHeight-28)/844);ph.style.transform='scale('+s+')';ph.parentElement.style.height=844*s+'px';ph.parentElement.style.width=390*s+'px'}
var rt=0;addEventListener('resize',function(){fit();clearTimeout(rt);rt=setTimeout(function(){var l=topLayer();if(l)layout($('[data-root]',l))},120)});
fit();setInterval(tick,1300);
var clock=function(){var d=new Date();$('#clock').textContent=d.getHours()%12+(d.getHours()%12?'':12)+':'+('0'+d.getMinutes()).slice(-2)};clock();setInterval(clock,3e4);
(document.fonts&&document.fonts.ready||Promise.resolve()).then(function(){var h=(location.hash||'').slice(1);S.stack=[];nav(D().S[h]?h:'Splash',{fade:1})});
// Screens were generated with a link inside a link in places. Browsers split those apart, which makes uneven rows, so keep one link per row.
function unnest(h){var re=/<(\/?)a\b([^>]*)>/g,parts=[],open=[],last=0,m;
  while((m=re.exec(h))){parts.push(h.slice(last,m.index));last=re.lastIndex;
    if(m[1]){var t=open.pop();parts.push(t==='span'?'</span>':'</a>');continue}
    if(!open.length){open.push(parts.length);parts.push(m[0]);continue}
    var to=m[2].match(/href="([^"]*)"/);if(to)parts[open[0]]=parts[open[0]].replace(/href="[^"]*"/,'href="'+to[1]+'"');
    open.push('span');parts.push('<span'+m[2].replace(/\s*href="[^"]*"/,'').replace(/\s*data-l="1"/,'')+'>')}
  parts.push(h.slice(last));return parts.join('')}
var subst0=subst;subst=function(k,h){return subst0(k,unnest(h))};
window.CR_APP={nav:nav,pop:pop,S:S,setTheme:setTheme};
})();
