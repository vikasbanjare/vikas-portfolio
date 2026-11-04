(function(){
var AREAS="__AREAS__",root=document.documentElement,$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
function theme(){return root.getAttribute('data-theme')==='dark'?'DK':'LT'}
// ───── Phones: swap the picture for the real screen, so its animation runs
var STAT='<div class="phstat"><span>9:41</span><i>Sample data</i></div>';
function fill(slot){var k=slot.getAttribute('data-live'),L=window.CR_LIVE&&CR_LIVE[theme()]&&CR_LIVE[theme()][k];if(!L||slot.classList.contains('playing'))return;slot.innerHTML=L+STAT;slot.setAttribute('data-th',theme())}
var seen=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){fill(x.target);x.target.setAttribute('data-near','1');seen.unobserve(x.target)}})},{rootMargin:'400px'});
function watch(){$$('[data-live]').forEach(function(s){seen.observe(s)})}
if(window.CR_LIVE)watch();else addEventListener('load',watch);
// ───── Animation only runs where you are looking
var far=new IntersectionObserver(function(es){es.forEach(function(x){x.target.classList.toggle('off',!x.isIntersecting)})},{rootMargin:'120px'});
$$('.sec,.hero,.foot').forEach(function(s){far.observe(s)});
// ───── Tab bar follows the page
var tabs=$$('.tabs a'),byId={};tabs.forEach(function(a){byId[a.getAttribute('data-t')]=a});
var mark=new IntersectionObserver(function(es){es.forEach(function(x){if(!x.isIntersecting)return;tabs.forEach(function(a){a.removeAttribute('aria-current')});var a=byId[x.target.id==='role'?'story':x.target.id];if(a){a.setAttribute('aria-current','true');var i=a.querySelector('svg'),c=i.cloneNode(true);i.replaceWith(c)}})},{rootMargin:'-45% 0px -50% 0px'});
$$('.sec').forEach(function(s){mark.observe(s)});
// ───── Light and dark, same as the app
var tb=$('#theme'),tl=$('#themel');
function paint(){var d=theme()==='DK';tb.setAttribute('aria-pressed',d);tb.setAttribute('aria-label',d?'Switch to light mode':'Switch to dark mode');tl.textContent=d?'Light':'Dark';
  $$('img[data-shot]').forEach(function(i){var w='v6/'+(d?'dk':'lt')+'/'+i.getAttribute('data-shot')+'.webp';if(i.getAttribute('src')!==w)i.setAttribute('src',w)});
  $$('[data-live][data-near]').forEach(fill);
  var f=$('#appslot iframe');if(f)try{f.contentWindow.CR_APP.setTheme(d?'DK':'LT')}catch(e){}
  if(lbi.getAttribute('data-k'))show(cur)}
tb.addEventListener('click',function(){var d=theme()!=='DK';root.setAttribute('data-theme',d?'dark':'light');try{localStorage.setItem('cr.page',d?'dark':'light')}catch(e){}paint()});
// ───── The real app, inside the phone
var st=$('#startapp');st.addEventListener('click',function(){var s=$('#appslot');s.classList.add('playing');s.innerHTML='<iframe title="Crestline working app" src="app/#Home"></iframe>';st.remove();
  var f=s.firstChild;f.addEventListener('load',function(){if(theme()==='DK')setTimeout(function(){try{f.contentWindow.CR_APP.setTheme('DK')}catch(e){}},600)})});
// ───── Filter and viewer for all screens
var chips=$$('.fchip'),ths=$$('.th'),vis=ths;
chips.forEach(function(c){c.addEventListener('click',function(){chips.forEach(function(x){x.removeAttribute('data-on')});c.setAttribute('data-on','1');var f=c.getAttribute('data-f');ths.forEach(function(t){t.hidden=f!=='all'&&t.getAttribute('data-a')!==f});vis=ths.filter(function(t){return !t.hidden});wall.classList.remove('lim');if(more)more.remove()})});
var wall=$('#wall'),more=$('#more');more.addEventListener('click',function(){wall.classList.remove('lim');more.remove();more=null});
var lb=$('#lb'),lbi=$('#lbi'),cur=0;
function show(i){cur=(i+vis.length)%vis.length;var t=vis[cur],k=t.getAttribute('data-k');lbi.setAttribute('data-k',k);lbi.src='v6/'+(theme()==='DK'?'dk':'lt')+'/'+k+'.webp';lbi.alt=t.getAttribute('aria-label')+' screen';$('#lbt').textContent=t.getAttribute('aria-label');$('#lba').textContent=AREAS[t.getAttribute('data-a')];$('#lbo').href='app/#'+k}
ths.forEach(function(t){t.addEventListener('click',function(){show(vis.indexOf(t));lb.showModal()})});
$('#lbc').addEventListener('click',function(){lb.close()});$('#lbp').addEventListener('click',function(){show(cur-1)});$('#lbn').addEventListener('click',function(){show(cur+1)});
lb.addEventListener('click',function(e){if(e.target===lb||e.target.classList.contains('lbin'))lb.close()});
lb.addEventListener('close',function(){lbi.removeAttribute('data-k')});
addEventListener('keydown',function(e){if(!lb.open)return;if(e.key==='ArrowLeft')show(cur-1);if(e.key==='ArrowRight')show(cur+1)});
// Sample controls in the brand kit go nowhere
document.addEventListener('click',function(e){var a=e.target.closest('a[href="#"]');if(a)e.preventDefault()});
if(theme()==='DK')paint();
// ───── Sections rise in, the same small move as the app
if(!matchMedia('(prefers-reduced-motion:reduce)').matches){var up=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');up.unobserve(x.target)}})},{rootMargin:'0px 0px -6% 0px'});
  $$('.card,.dec,.mo,.kol,.sh,.big').forEach(function(n){n.classList.add('rv');up.observe(n)})}
})();
