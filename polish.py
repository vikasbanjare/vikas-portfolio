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
    out = []
    css = re.sub(r"</?style>", "", re.sub(r"</style>.*?<style>", "", css, flags=re.S))   # the work component's capture spans a preview-only block
    for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", re.sub(r"/\*.*?\*/", "", css, flags=re.S)):
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
    return "".join(out)


def _section(tpl, sid):
    i = tpl.index(f'id="{sid}"')
    a = tpl.rfind("<section", 0, i)
    return a, tpl.index("</section>", i) + len("</section>")


def _cover(slug):
    return sorted((ROOT / "assets" / "img" / slug).glob("cover.*"))[0].relative_to(ROOT).as_posix()


HERO_TILES = [("case-studies/crestline/showcase.html", "assets/uiux/crestline.jpg", "Crestline app"), ("#work", _cover("podcast-videos"), "Podcast videos"),
              ("case-studies/purple-finance/showcase.html", "assets/uiux/purple-finance.jpg", "Purple Finance website"), ("#work", _cover("wealthy-yt-ads"), "Wealthy YouTube ads"),
              ("case-studies/leadsquared/showcase.html", "assets/uiux/leadsquared.jpg", "LeadSquared concept"), ("#work", _cover("trailer-video"), "Trailer videos")]
HERO_VIS = '<div class="vbh-vis">' + "".join(f'<a class="vbh-t" href="{h}"><img src="{s}" alt="{a}" loading="lazy"></a>' for h, s, a in HERO_TILES) + "</div>"

CSS = """
body{font-family:'Onest',system-ui,sans-serif}
[data-hero] a{white-space:nowrap}
[data-hero] a[href="#work"],[data-hero] a[href="#contact"]{flex:none}
.vbh-vis{display:none}
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
/* ---- light ---- */
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
html.vb-light [data-hero]{background:linear-gradient(160deg,#E9EFFF 0%,#F5F7FD 52%,#FFFFFF 100%)!important;color:#1c2740!important}
html.vb-light [data-hero]>div:nth-child(1),html.vb-light [data-hero]>div:nth-child(2),html.vb-light [data-hero]>div:nth-child(3){display:none!important}
html.vb-light [data-hero] h1,html.vb-light [data-hero] h1 span{color:#0a0f1e!important}
html.vb-light [data-hero] p{color:#34415c!important}
html.vb-light [data-hero] p:first-of-type{color:#4f7a00!important}
html.vb-light [data-hero] a[href="#contact"]{color:#0a0f1e!important;background:#fff!important;border-color:rgba(16,24,48,.16)!important}
html.vb-light [data-hero] a[href="#work"]{box-shadow:none!important}
html.vb-light [data-hero] span{color:#34415c!important;background-color:transparent}
html.vb-light [data-hero] [data-vbhint]{display:none!important}
html.vb-light .vbh-vis{position:absolute;z-index:3;right:clamp(20px,5vw,90px);top:50%;transform:translateY(-50%);display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;width:min(46vw,88vh,720px);pointer-events:auto}
html.vb-light .vbh-t{position:relative;display:block;overflow:hidden;aspect-ratio:16/10;border-radius:16px;background:#e6ebf5;box-shadow:0 22px 44px -28px rgba(20,35,80,.5);transition:translate .5s cubic-bezier(.2,.7,.3,1)}
html.vb-light .vbh-t img{position:absolute;inset:0;display:block;width:100%;height:100%;max-width:none;object-fit:cover}
@media (hover:hover){html.vb-light .vbh-t:hover{translate:0 -5px}}
html.vb-light [data-vbwork2] .vw2-mon-in,html.vb-light [data-vbwork2] .vw2-viewer{background:#fff}
html.vb-light [data-vbux] .vux-card{background:#fff}
html.vb-light [data-chrome="menu"]{color:#1c2740}
@media (max-width:1040px){html.vb-light .vbh-vis{top:auto;bottom:18px;left:20px;right:20px;width:auto;transform:none;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}html.vb-light .vbh-t{aspect-ratio:16/10;border-radius:10px}html.vb-light .vbh-t:nth-child(n+4){display:none}}
@media (max-height:760px) and (max-width:760px){html.vb-light .vbh-vis{display:none}}
"""

JS = r"""
(function () {
  var KEY = 'vb-theme';
  var saved = null;
  try { saved = localStorage.getItem(KEY); if (!saved) { localStorage.setItem(KEY, 'light'); saved = 'light'; } } catch (e) { saved = 'light'; }
  var root = document.documentElement;
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
    sub("Every craft in orbit.", "Creative lead for fintech and edtech brands.")
    sub("Creative lead · 8 years · Video · Design · AI", "8 years · Video · Design · AI")
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
    order = [k for k in ("results", "work", "uiux", "tools", "studio", "contact") if k in by]
    assert len(order) == len(hits), f"menu changed: {list(by)}"
    start, end = hits[0].start(), hits[-1].end()
    sep = tpl[hits[0].end():hits[1].start()]
    def renum(s, n):
        return re.sub(r">0\d<", f">{n:02d}<", s, count=1)
    tpl = tpl[:start] + sep.join(renum(by[k], i + 1) for i, k in enumerate(order)) + tpl[end:]

    # hero picture for the light page
    h = re.search(r'<div ref="\{\{ hostRef \}\}"[^>]*></div>', tpl)
    assert h, "hero host missing"
    close = tpl.index("</section>", h.end())
    tpl = tpl[:close] + HERO_VIS + tpl[close:]

    manifest[POLISH_UUID] = {"mime": "text/javascript", "compressed": False, "data": base64.b64encode(JS.encode()).decode()}
    tpl = tpl.replace(head_anchor, head_anchor + f'\n<script src="{POLISH_UUID}"></script>', 1)
    tpl = tpl.replace("</head>", "<style>" + "".join(light_css(c) for c in dark_css) + CSS + "</style></head>", 1)
    return tpl
