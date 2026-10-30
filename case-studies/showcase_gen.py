#!/usr/bin/env python3
"""Generates one showcase.html per case study from shared CSS + per-project data.
Run: python3 case-studies/showcase_gen.py
All copy below is taken from the source material (Mohit's pages, the supplied HTML files,
the Crestline screens). Nothing here is a metric or claim that is not on a source page.
"""
import os, html as H
ROOT = os.path.dirname(os.path.abspath(__file__))
esc = H.escape

CSS = r"""
:root{--bg:%(bg)s;--bg2:%(bg2)s;--surface:%(surface)s;--line:%(line)s;--text:%(text)s;--mut:%(mut)s;--mut2:%(mut2)s;--accent:%(accent)s;--accent-ink:%(accent_ink)s;--ease:cubic-bezier(.2,.7,.3,1)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:%(sans)s;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{display:block;max-width:100%%}a{color:inherit}
.wrap{width:100%%;max-width:1200px;margin:0 auto;padding:0 24px}
.serif{font-family:%(serif)s;font-style:italic;font-weight:400}
.eyebrow{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);font-weight:600}
.nav{position:absolute;top:0;left:0;right:0;z-index:5;padding:22px 0}
.nav .wrap{display:flex;justify-content:space-between;align-items:center}
.nav a{text-decoration:none;font-size:14px;font-weight:600;color:var(--mut)}.nav a:hover{color:var(--text)}
.hero{position:relative;padding:120px 0 0;background:%(herobg)s;overflow:hidden}
.hero .top{text-align:center}
.hero h1{font-size:clamp(46px,9vw,132px);line-height:.94;letter-spacing:-.04em;font-weight:800;margin-top:18px}
.hero h1 .serif{color:var(--accent);letter-spacing:-.02em}
.hero .lede{max-width:600px;margin:22px auto 0;color:var(--mut);font-size:clamp(16px,2vw,19px)}
.stage{position:relative;margin-top:54px}
.stage.phones{height:clamp(420px,58vw,700px)}
.phone{position:absolute;bottom:-60px;left:50%%;width:clamp(170px,26vw,320px);aspect-ratio:750/1624;border-radius:clamp(26px,4vw,46px);background:#05070f;padding:clamp(5px,.9vw,10px);box-shadow:0 0 0 1px rgba(255,255,255,.14),0 40px 80px rgba(0,0,0,.5);transition:transform .9s var(--ease)}
.phone img{width:100%%;height:100%%;border-radius:clamp(21px,3.3vw,37px);object-fit:cover;object-position:top}
.p1{transform:translateX(-142%%) rotate(-7deg) translateY(30px)}.p2{transform:translateX(-50%%) translateY(60px);z-index:2}.p3{transform:translateX(42%%) rotate(7deg) translateY(30px)}
.stage.in .p1{transform:translateX(-118%%) rotate(-6deg)}.stage.in .p2{transform:translateX(-50%%)}.stage.in .p3{transform:translateX(18%%) rotate(6deg)}
.herofig{border-radius:28px 28px 0 0;overflow:hidden;box-shadow:0 -10px 80px rgba(0,0,0,.35);max-height:clamp(260px,46vw,640px)}
.herofig img{width:100%%;object-fit:cover;object-position:top}
.meta{background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);position:relative;z-index:3}
.meta .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;padding-top:34px;padding-bottom:34px}
.meta b{display:block;font-size:17px;margin-top:6px;font-weight:700}
section{padding:clamp(70px,10vw,130px) 0}
.band{background:var(--bg2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
h2{font-size:clamp(32px,5vw,58px);letter-spacing:-.03em;line-height:1.04;font-weight:800;margin-top:14px}
h2 .serif{color:var(--accent)}
.p{color:var(--mut);font-size:17px;max-width:640px;margin-top:20px}
.intro{display:grid;grid-template-columns:1.1fr 1fr;gap:60px;align-items:start}
.facts{display:grid;gap:14px}
.fact{background:var(--surface);border-radius:20px;padding:22px 24px;display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:start}
.fact i{font-style:normal;font-family:%(serif)s;font-size:34px;line-height:1;color:var(--accent)}
.fact b{display:block;font-size:16px;margin-bottom:3px}.fact span{color:var(--mut);font-size:14.5px}
.spread{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,6vw,90px);align-items:center}
.spread.flip .shot{order:2}
.shot{position:relative;display:grid;place-items:center;padding:clamp(24px,4vw,50px);border-radius:36px;background:var(--surface);overflow:hidden}
.shot .ph{width:min(100%%,300px);aspect-ratio:750/1624;border-radius:38px;background:#05070f;padding:8px;box-shadow:0 30px 60px rgba(8,14,36,.4),0 0 0 1px rgba(255,255,255,.12)}
.shot .ph img{width:100%%;height:100%%;border-radius:30px;object-fit:cover;object-position:top}
.shot.wide{padding:clamp(18px,3vw,36px)}
.shot img.flat{width:100%%;border-radius:14px;box-shadow:0 24px 60px rgba(0,0,0,.35)}
.num{font-family:%(serif)s;font-style:italic;font-size:clamp(64px,9vw,110px);line-height:.8;color:var(--accent)}
.spread h3{font-size:clamp(26px,3.4vw,42px);letter-spacing:-.03em;line-height:1.06;font-weight:800;margin:14px 0 0}
.spread ul{list-style:none;margin-top:24px;display:grid;gap:15px}
.spread li{display:grid;grid-template-columns:28px 1fr;gap:12px;color:var(--mut);font-size:16px}
.spread li::before{content:"";width:10px;height:10px;border-radius:50%%;background:var(--accent);margin-top:9px;margin-left:4px}
.spread li b{color:var(--text);font-weight:700}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:24px}
.tag{font-size:12.5px;font-weight:600;padding:7px 13px;border-radius:99px;background:var(--surface);color:var(--mut)}
.band .tag{background:var(--bg)}
.gap{height:clamp(60px,8vw,110px)}
/* scroll frames */
.frame{border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 30px 70px rgba(0,0,0,.4),0 0 0 1px rgba(255,255,255,.1)}
.frame .bar{display:flex;gap:7px;padding:12px 16px;background:#E9E9EE}
.frame .bar i{width:11px;height:11px;border-radius:50%%;background:#C9C9D2}
.frame .scroll{max-height:clamp(380px,62vw,720px);overflow-y:auto;overscroll-behavior:contain;background:#fff}
.frame .scroll img{width:100%%}
.hint{margin-top:12px;font-size:12.5px;color:var(--mut2);text-align:center}
.mframe{width:min(100%%,330px);margin:0 auto;border-radius:44px;background:#05070f;padding:9px;box-shadow:0 30px 70px rgba(0,0,0,.45),0 0 0 1px rgba(255,255,255,.12)}
.mframe .scroll{height:clamp(500px,110vw,660px);overflow-y:auto;border-radius:36px;background:#fff;overscroll-behavior:contain}
.mframe img{width:100%%}
.duo{display:grid;grid-template-columns:2.2fr 1fr;gap:clamp(24px,4vw,56px);align-items:start;margin-top:50px}
/* screen strip */
.strip{display:grid;grid-template-columns:repeat(%(cols)s,1fr);gap:18px;margin-top:46px}
.strip figure{position:relative}
.strip .ph{aspect-ratio:750/1624;border-radius:30px;background:#05070f;padding:6px;box-shadow:0 20px 40px rgba(0,0,0,.35),0 0 0 1px rgba(255,255,255,.1)}
.strip .ph img{width:100%%;height:100%%;border-radius:24px;object-fit:cover;object-position:top}
.strip figcaption{margin-top:12px;font-size:13px;font-weight:600;color:var(--mut);text-align:center}
.strip.flat .ph{background:transparent;padding:0;box-shadow:none}
.strip.flat .ph img{border-radius:0;object-fit:contain}
/* steps */
.steps{display:grid;grid-template-columns:repeat(%(stepcols)s,1fr);gap:16px;margin-top:46px}
.step{background:var(--surface);border-radius:24px;padding:26px}
.step i{font-style:normal;font-family:%(serif)s;font-size:40px;color:var(--accent);line-height:1}
.step b{display:block;font-size:17px;margin:12px 0 6px}.step span{color:var(--mut);font-size:14.5px}
.lists{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:46px}
.lcard{background:var(--surface);border-radius:24px;padding:28px}
.lcard h4{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700;margin-bottom:14px}
.lcard li{list-style:none;color:var(--mut);padding:9px 0;border-top:1px solid var(--line);font-size:15px}
.ba{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:46px}
.ba>div{border-radius:26px;padding:30px}
.ba .b{background:var(--surface)}.ba .a{background:var(--accent);color:var(--accent-ink)}
.ba h4{font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin-bottom:14px;opacity:.8}
.ba li{list-style:none;padding:10px 0;border-top:1px solid rgba(127,127,127,.25);font-weight:600}
/* system */
.swatches{display:grid;grid-template-columns:repeat(%(swn)s,1fr);gap:14px;margin-top:44px}
.sw{border-radius:22px;padding:20px;min-height:170px;display:flex;flex-direction:column;justify-content:flex-end}
.sw b{font-size:16px}.sw span{font-size:12.5px;opacity:.9;font-weight:500;letter-spacing:.04em}
.sys{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px}
.card{background:var(--surface);border-radius:28px;padding:30px}
.band .card{background:var(--bg)}
.card h4{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);font-weight:600}
.type .big{font-size:clamp(40px,6vw,72px);letter-spacing:-.03em;line-height:1;margin-top:18px}
.type .rows{margin-top:22px;display:grid;gap:12px;color:var(--mut)}
.type .rows div{display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:12px;font-size:14px}
.type .rows b{color:var(--text)}
.quote{font-family:%(serif)s;font-style:italic;font-size:clamp(28px,4.4vw,52px);line-height:1.15;max-width:900px;margin:0 auto;text-align:center}
.credit{margin-top:44px;display:inline-flex;gap:12px;align-items:center;background:var(--surface);border-radius:99px;padding:10px 20px 10px 12px;font-size:14px;color:var(--mut);text-decoration:none}
.credit b{color:var(--text)}.credit i{width:30px;height:30px;border-radius:50%%;background:var(--accent);display:grid;place-items:center;color:var(--accent-ink);font-style:normal;font-weight:800;font-size:13px}
.outro{text-align:center}.outro h2{margin-left:auto;margin-right:auto;max-width:760px}
.cta{display:inline-block;margin-top:32px;background:var(--accent);color:var(--accent-ink);font-weight:700;text-decoration:none;padding:16px 28px;border-radius:99px;transition:transform .3s var(--ease)}.cta:hover{transform:translateY(-3px)}
.cta.ghost{background:transparent;color:var(--text);box-shadow:inset 0 0 0 1.5px var(--line);margin-left:10px}
footer{padding:30px 0 50px;color:var(--mut2);font-size:13px;text-align:center}
.rv{opacity:0;transform:translateY(34px);transition:opacity .8s var(--ease),transform .8s var(--ease)}.rv.in{opacity:1;transform:none}
@media (max-width:900px){
 .meta .wrap{grid-template-columns:1fr 1fr}.intro,.spread,.sys,.duo,.ba,.lists{grid-template-columns:1fr}
 .spread.flip .shot{order:0}.swatches{grid-template-columns:repeat(2,1fr)}
 .strip{grid-template-columns:repeat(2,1fr)}.steps{grid-template-columns:1fr 1fr}
 .stage.in .p1{transform:translateX(-104%%) rotate(-5deg)}.stage.in .p3{transform:translateX(4%%) rotate(5deg)}
}
@media (max-width:560px){.steps{grid-template-columns:1fr}.cta.ghost{margin:12px 0 0}}
@media (prefers-reduced-motion:reduce){.rv,.phone{transition:none}.rv{opacity:1;transform:none}}
"""

JS = """(function(){var els=document.querySelectorAll('.rv,.stage');
if(!('IntersectionObserver' in window)){for(var i=0;i<els.length;i++)els[i].classList.add('in');return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
for(var i=0;i<els.length;i++)io.observe(els[i]);
setTimeout(function(){var s=document.querySelector('.stage.phones');if(s)s.classList.add('in')},250)})();"""

# ---------- component helpers ----------
def tags(ts): return '<div class="tags">'+''.join(f'<span class="tag">{esc(t)}</span>' for t in ts)+'</div>' if ts else ''
def lis(items): return ''.join(f'<li><span><b>{esc(a)}</b> {esc(b)}</span></li>' if b else f'<li><span>{esc(a)}</span></li>' for a,b in items)

def hero_phones(imgs):
    return '<div class="wrap"><div class="stage phones">'+''.join(f'<div class="phone p{i+1}"><img src="{s}" alt="" loading="eager"></div>' for i,s in enumerate(imgs))+'</div></div>'
def hero_fig(img, alt=''):
    return f'<div class="wrap"><div class="stage"><div class="herofig"><img src="{img}" alt="{esc(alt)}"></div></div></div>'

def meta(items):
    return '<div class="meta"><div class="wrap">'+''.join(f'<div><span class="eyebrow">{esc(a)}</span><b>{esc(b)}</b></div>' for a,b in items)+'</div></div>'

def intro(eyebrow, h2html, para, facts):
    f=''.join(f'<div class="fact"><i>{i+1}</i><div><b>{esc(a)}</b><span>{esc(b)}</span></div></div>' for i,(a,b) in enumerate(facts))
    return f'<section><div class="wrap intro"><div class="rv"><div class="eyebrow">{esc(eyebrow)}</div><h2>{h2html}</h2><p class="p">{esc(para)}</p></div><div class="facts rv">{f}</div></div></section>'

def phone_vis(img, bg=''):
    return f'<div class="shot" style="{bg}"><div class="ph"><img src="{img}" alt="" loading="lazy"></div></div>'
def flat_vis(img, bg=''):
    return f'<div class="shot wide" style="{bg}"><img class="flat" src="{img}" alt="" loading="lazy"></div>'

def spread(n, title, items, tg, vis, flip=False):
    return (f'<div class="spread rv{" flip" if flip else ""}">{vis}<div><div class="num">{n}</div><h3>{title}</h3><ul>{lis(items)}</ul>{tags(tg)}</div></div>')

def browser_frame(img, hint='Scroll inside the frame to see the full page'):
    return f'<div class="frame"><div class="bar"><i></i><i></i><i></i></div><div class="scroll"><img src="{img}" alt="" loading="lazy"></div></div><div class="hint">{esc(hint)}</div>'
def mobile_frame(img, hint='Scroll inside the phone'):
    return f'<div class="mframe"><div class="scroll"><img src="{img}" alt="" loading="lazy"></div></div><div class="hint">{esc(hint)}</div>'

def strip(imgs, caps=None, flat=False):
    figs=''.join(f'<figure class="rv"><div class="ph"><img src="{s}" alt="" loading="lazy"></div>'+(f'<figcaption>{esc(caps[i])}</figcaption>' if caps else '')+'</figure>' for i,s in enumerate(imgs))
    return f'<div class="strip{" flat" if flat else ""}">{figs}</div>'

def steps(items,cols=None):
    return f'<div class="steps"{f" style=\"grid-template-columns:repeat({cols},1fr)\"" if cols else ""}>'+''.join(f'<div class="step rv"><i>{n}</i><b>{esc(a)}</b><span>{esc(b)}</span></div>' for n,a,b in items)+'</div>'

def lists3(cols):
    return '<div class="lists">'+''.join(f'<div class="lcard rv"><h4>{esc(t)}</h4><ul>'+''.join(f'<li>{esc(x)}</li>' for x in xs)+'</ul></div>' for t,xs in cols)+'</div>'

def beforeafter(b, a):
    return ('<div class="ba rv"><div class="b"><h4>Before</h4><ul>'+''.join(f'<li>{esc(x)}</li>' for x in b)+'</ul></div><div class="a"><h4>After</h4><ul>'+''.join(f'<li>{esc(x)}</li>' for x in a)+'</ul></div></div>')

def swatches(sw):
    return '<div class="swatches rv">'+''.join(f'<div class="sw" style="background:{c};color:{t}"><b>{esc(n)}</b><span>{c}</span></div>' for n,c,t in sw)+'</div>'

def system(sw, type_big, type_style, rows, comp_title, comp_html):
    return (swatches(sw)+f'<div class="sys"><div class="card type rv"><h4>Typography</h4><div class="big" style="{type_style}">{esc(type_big)}</div><div class="rows">'
            +''.join(f'<div><span>{esc(a)}</span><b>{esc(b)}</b></div>' for a,b in rows)+f'</div></div><div class="card rv"><h4>{esc(comp_title)}</h4>{comp_html}</div></div>')

def section(inner, band=False, sid=''):
    return f'<section class="{"band" if band else ""}"{f" id={sid!r}".replace(chr(39),chr(34)) if sid else ""}><div class="wrap">{inner}</div></section>'

def heading(eyebrow, h2html, para=''):
    return f'<div class="rv"><div class="eyebrow">{esc(eyebrow)}</div><h2>{h2html}</h2>'+(f'<p class="p">{esc(para)}</p>' if para else '')+'</div>'

def outro(h2html, extra_links=''):
    return f'<section class="outro"><div class="wrap rv"><div class="eyebrow">Next</div><h2>{h2html}</h2><a class="cta" href="../index.html">All UI/UX work</a><a class="cta ghost" href="../../index.html">Back to portfolio</a>{extra_links}</div></section>'

def credit(initials, line, href=None):
    inner=f'<i>{esc(initials)}</i><span>{line}</span>'
    return f'<a class="credit" href="{href}" target="_blank" rel="noopener">{inner}</a>' if href else f'<div class="credit">{inner}</div>'

def page(p):
    theme=dict(bg=p['bg'],bg2=p['bg2'],surface=p['surface'],line=p.get('line','rgba(255,255,255,.1)'),text=p.get('text','#F4F7FF'),mut=p['mut'],mut2=p.get('mut2',p['mut']),
               accent=p['accent'],accent_ink=p['accent_ink'],sans=p.get('sans','"Plus Jakarta Sans",system-ui,sans-serif'),serif=p.get('serif','"Instrument Serif",serif'),
               herobg=p['herobg'],cols=p.get('cols',6),stepcols=p.get('stepcols',5),swn=p.get('swn',5))
    css=CSS%theme+p.get('extra_css','')
    nav='<header class="nav"><div class="wrap"><a href="../index.html">&larr; All UI/UX work</a><a href="'+p.get('nav_link','#')+'">'+esc(p.get('nav_label',''))+'</a></div></header>'
    hero=(f'<div class="hero"><div class="wrap top"><div class="eyebrow">{esc(p["kicker"])}</div><h1>{p["h1"]}</h1><p class="lede">{esc(p["lede"])}</p></div>{p["hero_vis"]}</div>')
    body=nav+hero+meta(p['meta'])+''.join(p['sections'])+outro(p['outro_h2'],p.get('outro_extra',''))+f'<footer>{p["footer"]}</footer>'
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(p["title"])}</title><meta name="description" content="{esc(p["desc"])}">'
            f'<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{p["fonts"]}" rel="stylesheet"><style>{css}</style></head><body>{body}<script>{JS}</script></body></html>')

def write(slug,p):
    with open(os.path.join(ROOT,slug,'showcase.html'),'w') as f: f.write(page(p))
    print('wrote',slug)

FONT_PJS='https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Instrument+Serif:ital@1&display=swap'

if __name__=='__main__':
    import projects
    for slug,p in projects.build().items(): write(slug,p)
