"""Portfolio pass: light by default, a shorter page in a clearer order, and the small fixes.
Runs at the end of rebuild.py. Every anchor is asserted, like R in rebuild.py."""
import base64, re
from pathlib import Path

POLISH_UUID = "7e3b91a4-6c2f-4d18-b5e0-93a1f4c7d260"
ROOT = Path(__file__).parent

# dark value -> light value, used for the injected components' own CSS
COLOURS = [("#04060d", "#f4f6fb"), ("#060a14", "#eef1f8"), ("#03050b", "#f4f6fb"), ("#f6f9ff", "#0a0f1e"), ("#f3f7ff", "#0c1222"),
           ("#eaf0ff", "#1c2740"), ("#cfe0ff", "#27365a"), ("#a9bcdd", "#42506c"), ("#8da0c4", "#4c5a75"), ("#5d6e8e", "#5b6980")]
HAS_COLOUR = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\(")
COLOUR_PROPS = ("color", "background", "background-color", "border", "border-color", "border-top", "border-bottom", "border-left", "border-right", "outline-color", "box-shadow")


def _map_value(prop, v):
    for a, b in COLOURS:
        v = re.sub(re.escape(a), b, v, flags=re.I)
    v = re.sub(r"rgba\(\s*255\s*,\s*255\s*,\s*255\s*,", "rgba(16,24,48,", v)
    v = re.sub(r"rgba\(\s*4\s*,\s*6\s*,\s*13\s*,", "rgba(244,246,251,", v)
    if prop == "color":   # lime text is unreadable on a light page; lime fills keep their dark text
        v = re.sub(r"#b6f500", "#4f7a00", v, flags=re.I)
    return v


def light_css(css):
    """Copy only the colour declarations of a dark stylesheet, mapped, under html.vb-light."""
    css = re.sub(r"</?style>", "", re.sub(r"</style>.*?<style>", "", css, flags=re.S))   # the work component's capture spans a preview-only block
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out, i, at = [], 0, re.compile(r"@[^{;]+\{")
    while True:   # @media rules keep their wrapper, or a desktop-only rule leaks onto phones; keyframes are dropped
        m = at.search(css, i)
        if not m:
            return "".join(out + _light_rules(css[i:]))
        out += _light_rules(css[i:m.start()])
        depth, j = 1, m.end()
        while depth:
            depth += {"{": 1, "}": -1}.get(css[j], 0)
            j += 1
        inner = _light_rules(css[m.end():j - 1])
        if inner and m.group(0).startswith(("@media", "@supports")):
            out.append(m.group(0) + "".join(inner) + "}")
        i = j


def _light_rules(css):
    out = []
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        sel = sel.strip()
        if not sel or sel.startswith("@") or re.match(r"^(from|to|\d+%)", sel):
            continue
        decls = []
        for d in body.split(";"):
            if ":" not in d:
                continue
            p, v = d.split(":", 1)
            p = p.strip().lower()
            if p in COLOUR_PROPS and HAS_COLOUR.search(v):
                nv = _map_value(p, v.strip())
                if nv != v.strip():
                    decls.append(f"{p}:{nv}")
        if decls:
            pre = ",".join("html.vb-light " + s.strip() for s in sel.split(","))
            out.append(pre + "{" + ";".join(decls) + "}")
    return out


def _section(tpl, sid):
    i = tpl.index(f'id="{sid}"')
    a = tpl.rfind("<section", 0, i)
    return a, tpl.index("</section>", i) + len("</section>")


HERO_REEL = """<div class="vbr" data-vbr><img class="vbr-f" src="assets/posters/-KFeN_snxTq.jpg" alt="" data-label="Podcast Videos"><img class="vbr-f" src="assets/posters/Ue5FrWQ22dv.jpg" alt="" data-label="Wealthy YT Ads"><img class="vbr-f" src="assets/posters/CfjDPnZeIzE.jpg" alt="" data-label="Trailer Video"><img class="vbr-f" src="assets/posters/It7qHBhrcqT.jpg" alt="" data-label="Wealthy YT Ads"><img class="vbr-f" src="assets/posters/Em7TeX2SqTn.jpg" alt="" data-label="Podcast Videos"><img class="vbr-f" src="assets/posters/WKC6FEWm7QR.jpg" alt="" data-label="Trailer Video"><img class="vbr-f" src="assets/posters/R94zxhnXTCH.jpg" alt="" data-label="Podcast Videos"><img class="vbr-f" src="assets/posters/JNLiwdqkjxh.jpg" alt="" data-label="Wealthy YT Ads"><div class="vbr-flash"></div><div class="vbr-shade"></div>
<div class="vbr-in"><div class="vbr-main"><p class="vbr-kick"><i></i>Performance creative lead &middot; Mumbai &middot; works remote</p>
<h2 class="vbr-h">Vikas Banjare</h2>
<p class="vbr-p">Ads that earn their spend.</p>
<p class="vbr-s">I make fintech app ads with AI, learn what people respond to, and make the next round better.</p>
<div class="vbr-btns"><a href="#work">See the work &rarr;</a><a href="performance/">See what worked &rarr;</a></div></div>
<div class="vbr-side"><span class="vbr-now" data-vbr-now><b>01</b> / 08 &middot; Podcast Videos</span><div class="vbr-bars"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div></div></div>
</div>"""

CSS = """
body{font-family:'Onest',system-ui,sans-serif}
[data-hero] a{white-space:nowrap}
[data-hero] a[href="#work"],[data-hero] a[href="#contact"]{flex:none}
[data-chrome="header"] a[href="#contact"]{display:inline-flex!important;white-space:nowrap}
#experience [data-vbexp]{margin-top:0}
.vw2-more{display:none}
[data-vbwork2] .vw2-more.on{display:inline-flex;align-items:center;gap:8px;min-height:46px;margin-top:22px;padding:0 22px!important;border-radius:100px;background:#b6f500!important;color:#06140a!important;font-size:15px;font-weight:600}
@media (max-width:1040px){[data-vbrail]{display:none!important}}
@media (max-width:760px){
  [data-hero] p{max-width:none!important}
  [data-hero-fg]>div{right:20px!important;width:auto!important;max-width:none!important}
  [data-hero]>div:nth-child(3){display:none}
  [data-hero]>div:nth-child(2){opacity:.28}
  [data-hero] a[href="#work"],[data-hero] a[href="#contact"]{padding:13px 20px!important;font-size:14.5px!important}
  [data-chrome="header"] a[href="#contact"]{padding:9px 13px!important;font-size:13px!important}
  [data-chrome="theme-btn"]{display:none!important}
  #results>div:first-of-type,#results [style*="repeat(auto-fit"]{gap:10px}
}
/* ---- one grid for every section: 72px edges, even rhythm, cards that line up ---- */
#results,#work,#tools,#clients,#experience,#studio{padding-top:clamp(56px,9vh,104px)!important;padding-bottom:clamp(56px,9vh,104px)!important}
#contact{padding-top:clamp(56px,9vh,104px)!important}
[data-vbux] .vux-card{display:flex;flex-direction:column}
[data-vbux] .vux-body{display:flex;flex-direction:column;flex:1;padding:18px 0 0}
[data-vbux] .vux-foot{margin-top:auto}
@media (max-width:700px){#tools div:has(>[data-vbpipe]){display:none}}   /* at phone width the pipeline was a sideways strip of 8px labels; the cards below say the same */
/* these brand files carry wide empty margins, so their marks read tiny next to the rest */
#clients img[alt="DataFlow Group"]{transform:scale(2.3)}#clients img[alt="Purple Finance"]{transform:scale(1.9)}
#clients img[alt="i30 Learning Centre"]{transform:scale(2)}#clients img[alt="The Hub Bengaluru"]{transform:scale(1.5)}
html.vb-light [data-vbgal] h3{color:#f6f9ff!important}
html.vb-light [data-vbgal] h3~*,html.vb-light [data-vbgal] div>span{color:#a9bcdd}
html.vb-light #experience{background:#f4f6fb!important}
html.vb-light #experience h2{color:#0a0f1e!important}
html.vb-light #experience p{color:#4c5a75}
html.vb-light #tools [style*="rgba(12, 23, 54"]{background:#fff!important}
html.vb-light #contact a[href^="mailto"],html.vb-light #contact a[href*="linkedin"],html.vb-light #contact a[href*="behance"]{color:#4f7a00!important}
html.vb-light [data-hero] [data-hero-fg]>div>div:first-child,html.vb-light [data-hero] [data-hero-fg]>div>span:first-child{color:#34415c!important}
html.vb-light,html.vb-light body{background:#f4f6fb}
html.vb-light [data-chrome="loader"]{background:#f4f6fb!important}
html.vb-light [data-chrome="loader"] *{color:#1c2740!important}
html.vb-light [data-hero]{background:radial-gradient(55% 65% at 72% 48%,#E2EAFF 0%,rgba(226,234,255,0) 70%),radial-gradient(30% 35% at 88% 80%,rgba(182,245,0,.10) 0%,rgba(182,245,0,0) 70%),#F4F6FB!important;color:#1c2740!important}
html.vb-light [data-hero]>div:nth-child(1),html.vb-light [data-hero]>div:nth-child(2),html.vb-light [data-hero]>div:nth-child(3){display:none!important}
html.vb-light [data-hero] h1,html.vb-light [data-hero] h1 span{color:#0a0f1e!important}
html.vb-light [data-hero] p{color:#34415c!important}
html.vb-light [data-hero] p:first-of-type{color:#4f7a00!important}
html.vb-light [data-hero] a[href="#contact"]{color:#0a0f1e!important;background:#fff!important;border-color:rgba(16,24,48,.16)!important}
html.vb-light [data-hero] a[href="#work"]{box-shadow:none!important}
html.vb-light [data-hero] span{color:#34415c!important;background-color:transparent}
html.vb-light [data-hero] [data-vbhint]{display:none!important}
html.vb-light [data-vbwork2] .vw2-viewer{background:#e6ebf4;box-shadow:0 40px 60px -44px rgba(20,35,80,.45)}
html.vb-light [data-vbwork2] .vw2-viewer::after{box-shadow:inset 0 0 0 1px rgba(16,24,48,.08)}
html.vb-light [data-vbwork2] .vw2-item:not(.vw2-on) .vw2-meta,html.vb-light [data-vbwork2] .vw2-item:not(.vw2-on) .vw2-num{color:#5b6980}
html.vb-light [data-vbux] .vux-img{background:#e6ebf4;border-color:rgba(16,24,48,.08)}
html.vb-light [data-chrome="menu"]{color:#1c2740}
html.vb-motion.vb-light [data-hero-fg]>div>*{opacity:0}
html.vb-ready.vb-light [data-hero-fg]>div>*{animation:vbUp .9s cubic-bezier(.16,1,.3,1) both}
html.vb-ready.vb-light [data-hero-fg]>div>:nth-child(2){animation-delay:.08s}html.vb-ready.vb-light [data-hero-fg]>div>:nth-child(3){animation-delay:.16s}
html.vb-ready.vb-light [data-hero-fg]>div>:nth-child(4){animation-delay:.24s}html.vb-ready.vb-light [data-hero-fg]>div>:nth-child(n+5){animation-delay:.32s}
/* ---- hero: a showreel. Real stills from the films cut together with slow camera moves; name and buttons over a dark shade ---- */
.vbr{display:none}
html.vb-light [data-hero-fg]{display:none!important}
html.vb-light [data-hero]{background:#05070d!important}
html.vb-light .vbr{position:absolute;inset:0;z-index:4;display:block;overflow:hidden;font-family:'Onest',system-ui,sans-serif}
.vbr-f{position:absolute;inset:0;width:100%;height:100%;max-width:none;object-fit:cover;opacity:0;transform:scale(1.08)}
.vbr-f.on{opacity:1;animation:vbKenA 2.8s linear both}.vbr-f.on.alt{animation-name:vbKenB}
@keyframes vbKenA{from{transform:scale(1.08) translate(-1.2%,.6%)}to{transform:scale(1.2) translate(1.2%,-.8%)}}
@keyframes vbKenB{from{transform:scale(1.2) translate(1%,-.6%)}to{transform:scale(1.08) translate(-1%,.8%)}}
.vbr-flash{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none}.vbr-flash.go{animation:vbFlash .28s ease-out}
@keyframes vbFlash{0%{opacity:.18}100%{opacity:0}}
.vbr-shade{position:absolute;inset:0;background:linear-gradient(0deg,rgba(5,7,13,.94) 0%,rgba(5,7,13,.55) 42%,rgba(5,7,13,.25) 70%,rgba(5,7,13,.6) 100%),radial-gradient(120% 90% at 50% 45%,rgba(5,7,13,0) 55%,rgba(5,7,13,.55) 100%)}
.vbr-in{position:absolute;left:clamp(20px,5vw,72px);right:clamp(20px,5vw,72px);bottom:clamp(28px,7vh,72px);display:flex;align-items:flex-end;justify-content:space-between;gap:40px}
html.vb-light [data-hero] .vbr .vbr-kick{display:flex;align-items:center;gap:10px;margin:0 0 18px;font:600 13px/1 'Space Grotesk',sans-serif;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.78)!important}
html.vb-light [data-hero] .vbr .vbr-kick i{width:8px;height:8px;border-radius:50%;background:#ff3b30!important;animation:vbBlink 1.6s ease-in-out infinite}
@keyframes vbBlink{50%{opacity:.25}}
html.vb-light [data-hero] .vbr .vbr-h{margin:0;font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:clamp(52px,9vw,148px);line-height:.92;letter-spacing:-.05em;color:#fff!important}
html.vb-light [data-hero] .vbr .vbr-p{margin:18px 0 0;max-width:30ch;font-family:'Instrument Serif',serif;font-style:italic;font-size:clamp(22px,2.3vw,34px);line-height:1.15;color:#d9f99d!important}
html.vb-light [data-hero] .vbr .vbr-s{margin:12px 0 0;max-width:52ch;font-size:clamp(15px,1.2vw,18px);line-height:1.45;color:rgba(255,255,255,.86)!important}
.vbr-btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.vbr-btns a{display:inline-flex;align-items:center;min-height:50px;padding:0 26px;border-radius:100px;font:600 15px/1 'Space Grotesk',sans-serif;text-decoration:none;white-space:nowrap}
html.vb-light [data-hero] .vbr .vbr-btns a:first-child{background:#b6f500!important;color:#06140a!important}
html.vb-light [data-hero] .vbr .vbr-btns a+a{background:rgba(255,255,255,.14)!important;color:#fff!important;backdrop-filter:blur(10px)}
.vbr-side{flex:0 0 260px;text-align:right}
html.vb-light [data-hero] .vbr .vbr-now{display:block;font:600 12px/1.4 'Space Grotesk',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.7)!important}
html.vb-light [data-hero] .vbr .vbr-now b{color:#fff!important;font-weight:600}
.vbr-bars{display:flex;gap:4px;margin-top:12px}
html.vb-light [data-hero] .vbr .vbr-bars span{position:relative;flex:1;height:3px;border-radius:2px;background:rgba(255,255,255,.22)!important;overflow:hidden}
.vbr-bars span:after{content:"";position:absolute;inset:0;background:#fff;transform:scaleX(0);transform-origin:left}
.vbr-bars span.done:after{transform:scaleX(1)}.vbr-bars span.on:after{animation:vbBar 2.8s linear both}
@keyframes vbBar{to{transform:scaleX(1)}}
html.vb-motion.vb-light .vbr-in>*{opacity:0}
html.vb-ready.vb-light .vbr-in>*{animation:vbUp 1s cubic-bezier(.16,1,.3,1) both}
html.vb-ready.vb-light .vbr-in>.vbr-side{animation-delay:.25s}
/* over the reel the header goes clear with white type; it returns to the frosted bar once the hero is scrolled past */
html.vb-light.vb-ontop [data-chrome="header"]{background:transparent!important;border-bottom-color:transparent!important;backdrop-filter:none!important}
html.vb-light.vb-ontop [data-chrome="header"] a:not([href="#contact"]),html.vb-light.vb-ontop [data-chrome="header"] a:not([href="#contact"]) *,html.vb-light.vb-ontop [data-chrome="header"] button,html.vb-light.vb-ontop [data-chrome="header"] button *{color:#fff!important}
html.vb-light.vb-ontop [data-chrome="header"] button{background:rgba(255,255,255,.14)!important;border-color:rgba(255,255,255,.2)!important}
html.vb-light.vb-ontop [data-chrome="header"] svg [stroke]{stroke:#fff}
html.vb-light.vb-ontop [data-chrome="bar1"],html.vb-light.vb-ontop [data-chrome="bar2"]{background:#fff!important}
@media (max-width:760px){html.vb-light [data-hero] .vbr .vbr-kick{font-size:11px;letter-spacing:.06em;white-space:nowrap}}
@media (max-width:760px){.vbr-in{flex-direction:column;align-items:stretch;gap:26px}.vbr-side{flex:none;text-align:left}.vbr-btns a{padding:0 20px;font-size:14.5px;min-height:48px}}
@media (prefers-reduced-motion:reduce){.vbr-f.on,.vbr-bars span.on:after,.vbr-kick i{animation:none}.vbr-flash{display:none}}
@keyframes vbUp{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){html.vb-light [data-hero]{animation:none!important}html.vb-light [data-hero-fg]>div>*{animation:none!important;opacity:1!important}}
"""

JS = r"""
(function () {
  var KEY = 'vb-theme';
  var saved = null;
  try { saved = localStorage.getItem(KEY); if (!saved) { localStorage.setItem(KEY, 'light'); saved = 'light'; } } catch (e) { saved = 'light'; }
  var root = document.documentElement;

  // hero motion: hold the entrance until the loader has gone
  (function () {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) { return; }
    root.classList.add('vb-motion');
    var n = 0;
    (function ready() {
      var l = document.querySelector('[data-chrome="loader"]'), cs = l && getComputedStyle(l);
      if (!l || cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity < 0.1 || n++ > 60) { root.classList.add('vb-ready'); return; }   // ponytail: 6s cap so a stuck loader never hides the hero
      setTimeout(ready, 100);
    })();
  })();
  // showreel: hard cuts between film stills every 2.8s, each with its own slow camera move; starts once the loader has gone
  (function () {
    var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    (function bind(k) {
      var box = document.querySelector('[data-vbr]');
      if (!box) { if (k < 100) { setTimeout(function () { bind(k + 1); }, 100); } return; }
      var f = box.querySelectorAll('.vbr-f'), bars = box.querySelectorAll('.vbr-bars span'), now = box.querySelector('[data-vbr-now]'), flash = box.querySelector('.vbr-flash'), i = -1;
      function pad(v) { return v < 10 ? '0' + v : '' + v; }
      function cut() {
        var prev = i;
        i = (i + 1) % f.length;
        if (prev > -1) { f[prev].className = 'vbr-f'; }
        f[i].className = 'vbr-f on' + (i % 2 ? ' alt' : '');
        for (var j = 0; j < bars.length; j++) { bars[j].className = j < i ? 'done' : (j === i ? 'on' : ''); }
        now.innerHTML = '<b>' + pad(i + 1) + '</b> / ' + pad(f.length) + ' &middot; ' + f[i].getAttribute('data-label');
        if (prev > -1 && !still) { flash.className = 'vbr-flash'; void flash.offsetWidth; flash.className = 'vbr-flash go'; }
      }
      var hero = document.querySelector('[data-hero]');
      function top() { if (hero && window.pageYOffset < hero.offsetHeight - 80) { root.classList.add('vb-ontop'); } else { root.classList.remove('vb-ontop'); } }
      top(); window.addEventListener('scroll', top, { passive: true });
      cut();
      if (still) { return; }
      (function go() { if (root.classList.contains('vb-ready')) { setInterval(cut, 2800); } else { setTimeout(go, 100); } })();
    })(0);
  })();
  function setClass(on) { if (on) { root.classList.add('vb-light'); } else { root.classList.remove('vb-light'); } }
  setClass(saved === 'light');

  var INK = [['rgb(246, 249, 255)', 'rgb(10, 15, 30)'], ['rgb(234, 240, 255)', 'rgb(28, 39, 64)'], ['rgb(207, 224, 255)', 'rgb(39, 54, 90)'], ['rgb(141, 160, 196)', 'rgb(76, 90, 117)'], ['rgb(93, 110, 142)', 'rgb(91, 105, 128)'],
             ['rgb(182, 245, 0)', 'rgb(79, 122, 0)'], ['rgb(127, 212, 255)', 'rgb(15, 110, 170)'], ['rgba(255, 255, 255,', 'rgba(16, 24, 48,'], ['rgb(4, 6, 13)', 'rgb(255, 255, 255)']];
  function conv(v) { for (var i = 0; i < INK.length; i++) { v = v.split(INK[i][0]).join(INK[i][1]); } return v; }
  // Cards in Tools and Experience are drawn by script after the host has themed the page, so they get their own pass.
  function themeLate(light) {
    var els = document.querySelectorAll('#tools [style], #experience [style], #tools svg *');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.tagName === 'IMG') { continue; }
      var st = el.getAttribute('style');
      if (el._vbS === undefined) { el._vbS = st ? undo(st) : st; el._vbF = el.getAttribute('fill'); el._vbK = el.getAttribute('stroke'); }
      if (light) {
        if (el._vbS) { el.setAttribute('style', conv(el.style && el._vbS ? cssRgb(el._vbS) : el._vbS)); }
        if (el._vbF) { el.setAttribute('fill', conv(cssRgb(el._vbF))); }
        if (el._vbK) { el.setAttribute('stroke', conv(cssRgb(el._vbK))); }
      } else {
        if (el._vbS) { el.setAttribute('style', el._vbS); }
        if (el._vbF) { el.setAttribute('fill', el._vbF); }
        if (el._vbK) { el.setAttribute('stroke', el._vbK); }
      }
    }
  }
  var BACK = [['rgb(10, 15, 30)', 'rgb(246, 249, 255)'], ['rgb(12, 18, 34)', 'rgb(243, 247, 255)'], ['rgb(16, 25, 46)', 'rgb(240, 245, 255)'], ['rgb(28, 39, 64)', 'rgb(234, 240, 255)'], ['rgb(39, 54, 90)', 'rgb(207, 224, 255)'], ['rgb(76, 90, 117)', 'rgb(141, 160, 196)'], ['rgb(96, 134, 0)', 'rgb(182, 245, 0)']];
  function undo(v) { for (var i = 0; i < BACK.length; i++) { v = v.split(BACK[i][0]).join(BACK[i][1]); } return v; }   // the host may have themed these before they were first seen
  var HEX = { '#f6f9ff': 'rgb(246, 249, 255)', '#eaf0ff': 'rgb(234, 240, 255)', '#cfe0ff': 'rgb(207, 224, 255)', '#8da0c4': 'rgb(141, 160, 196)', '#5d6e8e': 'rgb(93, 110, 142)', '#b6f500': 'rgb(182, 245, 0)', '#7fd4ff': 'rgb(127, 212, 255)', '#04060d': 'rgb(4, 6, 13)' };
  function cssRgb(s) { s = s.replace(/rgba\(\s*255\s*,\s*255\s*,\s*255\s*,/g, 'rgba(255, 255, 255,').replace(/#[0-9a-fA-F]{6}\b/g, function (h) { return HEX[h.toLowerCase()] || h; }); return s; }

  function minText() {   // nothing below 12px, including text scripts draw later
    var els = document.querySelectorAll('body span, body p, body a, body div, body li, body dt, body b');
    for (var i = 0; i < els.length; i++) {
      var e = els[i];
      if (e.children.length || !e.textContent.trim() || e.closest('[data-chrome="loader"]')) { continue; }
      if (parseFloat(getComputedStyle(e).fontSize) < 12) { e.style.fontSize = '12px'; }
    }
  }
  function tick(light) { themeLate(light); minText(); }

  var tries = 0;
  (function wait() {
    var btn = document.querySelector('[data-chrome="theme-btn"]');
    var nav = document.querySelector('[data-nav]');
    if (!btn || !nav) { if (tries++ < 120) { setTimeout(wait, 100); } return; }
    btn.addEventListener('click', function () {
      setTimeout(function () { var l = false; try { l = localStorage.getItem(KEY) === 'light'; } catch (e) {} setClass(l); tick(l); }, 30);
    });
    nav.parentElement.setAttribute('data-vbrail', '');
    var gone = document.querySelectorAll('[data-nav="os"],[data-nav="launches"]');
    for (var i = 0; i < gone.length; i++) { gone[i].style.display = 'none'; }
    var hints = document.querySelectorAll('[data-hero] *');
    for (i = 0; i < hints.length; i++) { if (!hints[i].children.length && /scroll to dive|drag to explore/i.test(hints[i].textContent)) { var p = hints[i].parentElement; while (p.parentElement && p.parentElement.textContent.trim().length < 60) { p = p.parentElement; } p.setAttribute('data-vbhint', ''); break; } }
    // The host only themes reliably through its own switch, so a light first visit goes through it too.
    (function firstPaint(n) {
      var res = document.getElementById('results');
      var want = false; try { want = localStorage.getItem(KEY) === 'light'; } catch (e) {}
      if (!want || !res) { return; }
      if (getComputedStyle(res).backgroundColor !== 'rgb(4, 6, 13)') { return; }
      btn.click();
      var still = false; try { still = localStorage.getItem(KEY) === 'light'; } catch (e) {}
      if (!still) { btn.click(); }
      if (n > 0) { setTimeout(function () { firstPaint(n - 1); }, 300); }
    })(5);
    function now() { var l = false; try { l = localStorage.getItem(KEY) === 'light'; } catch (e) {} tick(l); }
    setTimeout(now, 500); setTimeout(now, 1500); setTimeout(now, 4000);
  })();
})();
"""


def apply(tpl, manifest, head_anchor, dark_css):
    def sub(a, b, n=-1):
        nonlocal tpl
        assert a in tpl, f"polish anchor missing: {a[:50]}"
        tpl = tpl.replace(a, b, n) if n > 0 else tpl.replace(a, b)

    # copy
    sub("Every craft in orbit.", "Films, design and AI for fintech and edtech brands.")
    sub("Creative lead · 8 years · Video · Design · AI", "Creative lead · Mumbai")
    sub("Bengaluru · working worldwide", "Mumbai · working worldwide")
    m = re.search(r'(<a href="#contact"[^>]*data-cursor="Talk"[^>]*>)[^<]*(</a>)', tpl)
    assert m, "header cta missing"
    tpl = tpl[:m.start()] + m.group(1) + "Work with me" + m.group(2) + tpl[m.end():]

    # shorter page: the node graph and launch pads repeat what the work list already shows
    for sid in ("os", "launches"):
        a, b = _section(tpl, sid)
        tpl = tpl[:a] + tpl[b:]
    # "A closer look" repeats four projects from the work list
    a = tpl.index("A closer look")
    a = tpl.rfind('<div style="position:relative; max-width:1400px; margin:clamp(64px,9vh,120px) auto 0;">', 0, a)
    assert a > 0, "closer look block missing"
    b = tpl.index("</section>", a)
    tpl = tpl[:a] + tpl[b:]

    # experience: cards instead of the hover-only career map
    a = tpl.index('<div data-chart="1"')
    b = tpl.index("<div data-vbexp")
    tpl = tpl[:a] + tpl[b:]
    sub('id="starchart"', 'id="experience"')
    sub("Hover a company to read what I owned there.", "What I owned at each company.")

    # one gutter: header, hero and brands used 56px and 90px against everyone else's 72px
    sub("clamp(20px,4vw,56px)", "clamp(20px,5vw,72px)")
    sub("max-width:1400px; margin:0 auto clamp(", "max-width:1440px; margin:0 auto clamp(")
    sub("padding:0 clamp(20px,5vw,90px)", "padding:0 clamp(20px,5vw,72px)")
    # monogram avatars: a tinted disc, not a lime ring
    sub("border:1px solid rgba(182,245,0,.35); background:rgba(182,245,0,.08)", "border:0; background:rgba(182,245,0,.16)")

    # the homepage leads with ads: UI/UX leaves the scroll and the menu; its row in the work list still opens case-studies/
    a, b = _section(tpl, "uiux")
    tpl = tpl[:a] + tpl[b:]
    tpl, n = re.subn(r'\s*<a href="#uiux" data-menu-link="1"[^>]*>.*?</a>', "", tpl, count=1, flags=re.S)
    assert n == 1, "uiux menu link missing"

    sub("Everyone sells<br>strategy. I ship<br>the thing.", "I make the ad,<br>read the data,<br>make the next one.")

    # results straight after the hero
    a, b = _section(tpl, "results")
    block = tpl[a:b]
    tpl = tpl[:a] + tpl[b:]
    at = tpl.index("<section data-vbwork2")
    tpl = tpl[:at] + block + tpl[at:]

    # the numbers on section labels could never match the menu, so the labels lose them
    tpl = re.sub(r">\d{2,3} — ([^<]{2,40}<)", r">\1", tpl)

    # menu in page order
    link = re.compile(r'<a href="#(\w+)" data-menu-link="1"[^>]*>.*?</a>', re.S)
    hits = list(link.finditer(tpl))
    by = {h.group(1): h.group(0) for h in hits}
    order = [k for k in ("results", "work", "tools", "studio", "contact") if k in by]
    assert len(order) == len(hits), f"menu changed: {list(by)}"
    start, end = hits[0].start(), hits[-1].end()
    sep = tpl[hits[0].end():hits[1].start()]
    def renum(s, n):
        return re.sub(r">0\d<", f">{n:02d}<", s, count=1)
    tpl = tpl[:start] + sep.join(renum(by[k], i + 1) for i, k in enumerate(order)) + tpl[end:]

    # hero showreel for the light page (the dark page keeps the host's orbit)
    h = re.search(r'<div ref="\{\{ hostRef \}\}"[^>]*></div>', tpl)
    assert h, "hero host missing"
    close = tpl.index("</section>", h.end())
    tpl = tpl[:close] + HERO_REEL + tpl[close:]

    manifest[POLISH_UUID] = {"mime": "text/javascript", "compressed": False, "data": base64.b64encode(JS.encode()).decode()}
    tpl = tpl.replace(head_anchor, head_anchor + f'\n<script src="{POLISH_UUID}"></script>', 1)
    tpl = tpl.replace("</head>", "<style>" + "".join(light_css(c) for c in dark_css) + CSS + "</style></head>", 1)
    return tpl
