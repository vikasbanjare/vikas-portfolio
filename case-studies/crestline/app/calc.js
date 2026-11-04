// The sums behind every calculator. Pure, so they can be checked on their own (calc.test.mjs).
var CR_CALC=(function(){
  function inr(n,d){d=d||0;var neg=n<0,s=Math.abs(n).toFixed(d),p=s.split('.'),w=p[0];
    if(w.length>3){var t=w.slice(-3),h=w.slice(0,-3),o=[];while(h.length>2){o.unshift(h.slice(-2));h=h.slice(0,-2)}if(h)o.unshift(h);w=o.join(',')+','+t}
    return(neg?'−':'')+w+(p[1]?'.'+p[1]:'')}
  function money(n){var a=Math.abs(n);if(a>=1e7)return'₹'+(n/1e7).toFixed(2)+' crore';if(a>=1e5)return'₹'+(n/1e5).toFixed(2)+' lakh';return'₹'+inr(Math.round(n))}
  function sipFV(p,r,y,s){var m=r/1200,v=0,a=p,put=0;for(var i=0;i<y*12;i++){if(i&&i%12===0)a*=1+s/100;v=(v+a)*(1+m);put+=a}return{v:v,put:put}}
  function charges(q,b,c,intra){var bv=q*b,sv=q*c,br=intra?Math.min(20,bv*.0003)+Math.min(20,sv*.0003):0,stt=intra?sv*.00025:(bv+sv)*.001,ex=(bv+sv)*.0000297,seb=(bv+sv)*.000001,st=bv*(intra?.00003:.00015),gst=(br+ex+seb)*.18,t=br+stt+ex+seb+st+gst;return{t:t,keep:sv-bv-t}}
  return{inr:inr,money:money,sipFV:sipFV,charges:charges,
    sip:function(v){var o=sipFV(v.p,v.r,v.y,v.s);return{r:money(o.v),s:'You put in '+money(o.put)+' · estimated gain '+money(o.v-o.put)}},
    lump:function(v){var f=v.p*Math.pow(1+v.r/100,v.y);return{r:money(f),s:'Estimated gain '+money(f-v.p)}},
    goal:function(v){var m=v.r/1200,n=v.y*12,a=v.g/((Math.pow(1+m,n)-1)/m*(1+m));return{r:'₹'+inr(Math.round(a)),s:'You put in '+money(a*n)+' over '+v.y+' years'}},
    brok:function(v){var o=charges(v.q,v.b,v.c,v.opt==='Intraday');return{r:(o.keep<0?'−':'')+'₹'+inr(Math.abs(o.keep),2),s:'Total charges ₹'+inr(o.t,2)}},
    margin:function(v){var t=v.q*v.p,pay=t*v.m/100,f=t-pay;return{r:'₹'+inr(pay),s:'Crestline funds ₹'+inr(f)+' · interest about ₹'+inr(Math.round(f*.0004))+' a day'}},
    cagr:function(v){var g=(Math.pow(v.b/v.a,1/v.y)-1)*100;return{r:g.toFixed(1)+'% a year',s:(v.b>=v.a?'₹'+inr(v.b-v.a)+' gain':'₹'+inr(v.a-v.b)+' loss')+' in '+v.y+' years'}}}
})();
if(typeof module!=='undefined')module.exports=CR_CALC;
