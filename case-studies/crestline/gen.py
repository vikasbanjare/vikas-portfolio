import re, math, pathlib, os
THEME = os.environ.get('CREST_THEME','v1')
UP,DN,LN=("#06784A","#C42A32","#E1E6F0") if THEME=='v2' else ("#0C8F52","#D13B3B","#E6E6E0")
BRAND="#3447F5" if THEME=='v2' else "#7A5CFF"
base = pathlib.Path("screens.html").read_text()
CSS = re.search(r"<style>(.*?)</style>", base, re.S).group(1)
SYM = re.search(r'(<svg width="0".*?</svg>)', base, re.S).group(1)
CSS += """
:root{--brandInk:#3C4A10;--brandLine:#DDF28A;--warn:#6B4B00;--warnBg:#FFF4D6;--upLine:#BFE6D0;--onlime:var(--ink)}
.btn.lime{color:var(--onlime)}.tab .on svg{color:var(--onlime)}
.sub{font-size:12px;color:var(--ink3)} .h2{font-size:20px;font-weight:700;letter-spacing:-.02em}
.field{background:#fff;border:1px solid var(--line);border-radius:16px;padding:12px 16px;margin-bottom:12px}
.field small{display:block;font-size:11px;color:var(--ink3);font-weight:600;letter-spacing:.04em;text-transform:uppercase}
.field b{font-size:17px;font-weight:600}
.dots{display:flex;gap:6px}.dots i{height:4px;flex:1;border-radius:4px;background:var(--line)}.dots i.on{background:var(--ink)}
.otp{display:flex;gap:10px}.otp div{flex:1;height:58px;border-radius:14px;border:1px solid var(--line);background:#fff;display:grid;place-items:center;font-size:24px;font-weight:600}
.ico{width:44px;height:44px;border-radius:14px;background:#fff;border:1px solid var(--line);display:grid;place-items:center;flex:0 0 auto}
.seg{display:flex;background:#fff;border:1px solid var(--line);border-radius:99px;padding:4px}.seg span{flex:1;text-align:center;padding:9px 6px;border-radius:99px;font-size:13px;font-weight:600;color:var(--ink2)}.seg span.on{background:var(--ink);color:#fff}
.tf{display:flex;justify-content:space-between;margin-top:10px}.tf span{padding:6px 12px;border-radius:99px;font-size:12px;font-weight:600;color:var(--ink2)}.tf span.on{background:var(--ink);color:#fff}
.banner{border-radius:18px;padding:14px 16px;font-size:13px;line-height:1.45}
.lbl{font-size:11px;font-weight:700;letter-spacing:.06em;color:var(--ink3);text-transform:uppercase}
"""

V2_CSS = """
:root{--bg:#F4F6FB;--card:#fff;--ink:#0B1220;--ink2:#44506A;--ink3:#5F6B85;--line:#E1E6F0;--lime:#3447F5;--limeD:#E9ECFF;--up:#06784A;--upBg:#E3F5EC;--dn:#C42A32;--dnBg:#FDECEC;--brandInk:#1E2C9E;--brandLine:#C9D0FF;--warn:#8A5300;--warnBg:#FFF1D6;--upLine:#BFE6D0;--onlime:#fff;--spark:#D7FF3F}
body{background:#D9DEEA;font-family:Manrope,system-ui,sans-serif}
.num{font-family:Manrope,system-ui,sans-serif;font-weight:800;letter-spacing:-.025em;font-variant-numeric:tabular-nums}
.lime,[style*="var(--lime)"]{color:#fff}
.sub{font-size:12.5px}.lbl{font-size:11.5px}
.chip{white-space:nowrap}
.tab div{font-size:11.5px}
.btn{border-radius:18px;height:56px;font-weight:700}
.phone{box-shadow:0 30px 60px -20px rgba(11,18,32,.35)}
.card{border-radius:22px}
"""
FONTS_V1='<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">'
FONTS_V2='<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
IC = {"back":"M15 5l-7 7 7 7","bell":"M6 17V11a6 6 0 0 1 12 0v6l2 2H4zM10 21h4","search":"M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-4-4","shield":"M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z","cam":"M4 8h3l2-3h6l2 3h3v11H4zM12 11a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7z","bank":"M3 9l9-5 9 5M5 10v8M10 10v8M14 10v8M19 10v8M3 20h18","doc":"M7 3h7l4 4v14H7zM14 3v5h5M10 13h5M10 17h5","gear":"M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6zM12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2","help":"M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7M12 17v.5M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z","out":"M10 4H5v16h5M14 8l5 4-5 4M19 12H9","plus":"M12 5v14M5 12h14","check":"M5 12l4 4 10-10","star":"M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z","lock":"M6 11h12v9H6zM8 11V8a4 4 0 0 1 8 0v3","wifi":"M3 9a14 14 0 0 1 18 0M6 12.5a9 9 0 0 1 12 0M9 16a4.5 4.5 0 0 1 6 0M12 19.5v.1","user":"M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM4 21c1-4 4-6 8-6s7 2 8 6","bulb":"M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z","news":"M4 5h13v14H6a2 2 0 0 1-2-2zM17 9h3v8a2 2 0 0 1-2 2M7 9h7M7 13h7","trend":"M3 17l6-6 4 4 8-9"}
def ic(n,s=22,c="currentColor"): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{IC[n]}"/></svg>'
_SMALL={"a","an","the","and","or","nor","but","for","yet","so","to","of","in","on","at","by","with","from","as"}
def tcase(t):
    if not t or "<" in t: return t
    ws=t.split(" "); out=[]
    for i,w in enumerate(ws):
        if w=="" or any(c.isdigit() for c in w) or w.isupper() or "&" in w or w in "·-–": out.append(w)
        elif i not in (0,len(ws)-1) and w.lower() in _SMALL: out.append(w.lower())
        else: out.append(w[:1].upper()+w[1:])
    return " ".join(out)
def sb(): return '<div class="sb">9:41<i></i><b></b></div>'
def top(t,r=''): return f'<div class="pad row" style="height:50px"><span>{ic("back")}</span><b>{tcase(t)}</b><span style="min-width:22px;text-align:right;font-size:13px;font-weight:600">{r}</span></div>'
def tabbar(on):
    it=[("home","Home","i-home"),("watch","Markets" if THEME=="v2" else "Watchlist","i-bars" if THEME=="v2" else "i-eye"),("port","Portfolio","i-pie"),("ord","Orders","i-list"),("acc","Account","i-user")]
    return '<div class="tab">'+''.join(f'<div class="{"on" if k==on else ""}"><svg><use href="#{i}"/></svg>{l}</div>' for k,l,i in it)+'</div>'
EXTRA={}
def phone(cap,inner,tab=None):
    ex=EXTRA.get(cap.split(' ')[0],'')
    if ex: inner=inner.replace('padding-bottom:90px','padding-bottom:0')+ex
    return f'<div><div class="cap">{cap}</div><div class="phone">{sb()}{inner}{tabbar(tab) if tab else ""}</div></div>'
def pad(x,st=''): return f'<div class="pad" style="{st}">{x}</div>'
def bottom(*b): return '<div style="position:absolute;left:20px;right:20px;bottom:30px;display:flex;flex-direction:column;gap:10px">'+''.join(b)+'</div>'
def btn(t,c=''): return f'<div class="btn {c}">{t}</div>'
def card(x,st=''): return f'<div class="card" style="{st}">{x}</div>'
def kv(l,v,mono=False): return f'<div class="row" style="padding:10px 0"><span class="mut">{l}</span><b class="{"num" if mono else ""}" style="font-size:14px">{v}</b></div>'
def chip(t,on=False): return f'<span class="chip{" on" if on else ""}">{t}</span>'
def pill(t,k="up"):
    m={"up":"background:var(--upBg);color:var(--up)","dn":"background:var(--dnBg);color:var(--dn)","wait":"background:var(--warnBg);color:var(--warn)","ink":"background:var(--line);color:var(--ink)"}[k]
    return f'<span class="pill" style="{m}">{t}</span>'
def field(l,v): return f'<div class="field"><small>{l}</small><b>{v}</b></div>'
def dots(n,t): return '<div class="dots">'+''.join(f'<i class="{"on" if i<n else ""}"></i>' for i in range(t))+'</div>'
def h1(t,s=28): return f'<div class="h1" style="font-size:{s}px">{t}</div>'
def logo(a,c,s=40): return f'<span class="logo" style="background:{c};width:{s}px;height:{s}px;font-size:{s//3}px">{a}</span>'
def srow(a,c,n,sub,p,ch):
    cl="up" if ch.startswith("+") else "dn"
    return f'<div class="row" style="padding:13px 0;border-top:1px solid var(--line)"><div style="display:flex;gap:12px;align-items:center">{logo(a,c)}<div style="font-weight:700;font-size:15px">{n}<div class="mut" style="font-weight:400;font-size:12px;margin-top:2px">{sub}</div></div></div><div style="text-align:right"><div class="num" style="font-size:15px">{p}</div><div class="{cl} num" style="font-size:12px">{ch}</div></div></div>'
def series(n,seed,tr):
    return [100+tr*i/n*40+10*math.sin(i*.55+seed)+5*math.sin(i*1.3+seed*2) for i in range(n)]
def chart(vals,w=350,h=150,col=None,fill=True):
    col=col or UP
    lo,hi=min(vals),max(vals); pts=[(i*w/(len(vals)-1),h-8-(v-lo)/(hi-lo)*(h-24)) for i,v in enumerate(vals)]
    d="M"+" L".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    a=f'<path d="{d} L{w},{h} L0,{h} Z" fill="{col}" opacity=".10"/>' if fill else ""
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display:block"><line x1="0" y1="{h-1}" x2="{w}" y2="{h-1}" stroke="{LN}"/>{a}<path d="{d}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round"/><circle cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="4.5" fill="{col}"/></svg>'
def candles(n=34,w=350,h=210):
    s="";o=100
    for i in range(n):
        c=o+9*math.sin(i*.6)+3*math.sin(i*1.7)+(i-n/2)*.18; hi=max(o,c)+4+3*abs(math.sin(i)); lo=min(o,c)-4-3*abs(math.cos(i)); col=UP if c>=o else DN
        x=6+i*(w-12)/n; y=lambda v:h-10-(v-70)*(h-30)/70
        s+=f'<line x1="{x+4}" x2="{x+4}" y1="{y(hi):.1f}" y2="{y(lo):.1f}" stroke="{col}" stroke-width="1.4"/><rect x="{x}" y="{y(max(o,c)):.1f}" width="8" height="{max(2,abs(y(o)-y(c))):.1f}" rx="1.5" fill="{col}"/>'; o=c
    ma="M"+" L".join(f"{6+i*(w-12)/n+4:.1f},{h-10-(100+(i-n/2)*.18-70)*(h-30)/70:.1f}" for i in range(n))
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{s}<path d="{ma}" fill="none" stroke="{BRAND}" stroke-width="1.6" stroke-dasharray="3 3"/></svg>'
def sheet(fn,title,screens):
    v2=THEME=='v2'; css=CSS+(V2_CSS if v2 else ''); fonts=FONTS_V2 if v2 else FONTS_V1
    html=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>{fonts}<style>{css}</style></head><body>{SYM}<div class="grid">{"".join(screens)}</div></body></html>'
    out=pathlib.Path('v2')/fn if v2 else pathlib.Path(fn); out.parent.mkdir(exist_ok=True); out.write_text(html); print(out,len(screens),"screens")


# ───────── extensions used by the v2 flows ─────────
IC.update({
 "minus":"M5 12h14",
 "eye":"M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z",
 "flame":"M12 3c1 3.5 4.5 5 4.5 9a4.5 4.5 0 0 1-9 0c0-1.8.7-3 2-4.2C9.5 10 11 8 12 3z",
 "filter":"M4 5h16l-6 8v6l-4-2v-4z","calendar":"M5 6h14v14H5zM5 10h14M9 3v4M15 3v4",
 "news":"M5 5h12v14H5zM17 8h3v9a2 2 0 0 1-2 2M8 9h6M8 13h6M8 16h4",
 "candle":"M8 3v3M8 18v3M6 6h4v12H6zM16 6v3M16 21v-3M14 9h4v9h-4z",
 "layers":"M12 3l9 5-9 5-9-5zM3 13l9 5 9-5","percent":"M6 18L18 6M8 8.5a1.5 1.5 0 1 0 .01 0M16 17a1.5 1.5 0 1 0 .01 0",
 "refresh":"M20 11a8 8 0 1 0-2 6M20 5v6h-6","share":"M12 3v12M8 7l4-4 4 4M5 12v8h14v-8",
 "eyeoff":"M3 3l18 18M10 6a9 9 0 0 1 11 6 9 9 0 0 1-3 4M6 8a9 9 0 0 0-3 4c2 4 6 7 9 7a8 8 0 0 0 3-.6",
 "key":"M8 14a4 4 0 1 1 3.5-6H21v3h-2v2h-3v-2h-4.5A4 4 0 0 1 8 14z",
 "users":"M9 11a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM2 20c0-3.5 3-6 7-6s7 2.5 7 6M17 5a3 3 0 0 1 0 6M20 20c0-2.5-1.5-4.5-4-5.5",
 "gift":"M4 10h16v10H4zM3 7h18v3H3zM12 7v13M12 7c-1-3-5-3-5 0M12 7c1-3 5-3 5 0",
 "download":"M12 4v11M8 11l4 4 4-4M5 20h14","sliders":"M4 7h10M18 7h2M4 17h2M10 17h10M14 5v4M6 15v4",
 "info":"M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 11v6M12 7.5v.01","tag":"M3 12V4h8l10 10-8 8zM7.5 8v.01",
 "up":"M3 17l6-6 4 4 8-8M15 7h6v6","down":"M3 7l6 6 4-4 8 8M15 17h6v-6","clock":"M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 7v5l3 2",
 "alert":"M12 3l10 18H2zM12 10v5M12 18v.01","grid":"M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z","bolt":"M13 2L4 14h7l-1 8 9-12h-7z",
 "globe":"M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18",
 "faceid":"M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3M9 10v1M15 10v1M12 10v3M9 16c1.5 1 4.5 1 6 0",
 "mail":"M3 6h18v12H3zM3 7l9 7 9-7","phone":"M7 3h10v18H7zM11 18h2","barchart":"M5 20V10M12 20V4M19 20v-7","list":"M8 6h12M8 12h12M8 18h12M4 6v.01M4 12v.01M4 18v.01",
 "swap":"M7 4L3 8l4 4M3 8h14M17 20l4-4-4-4M21 16H7","lockopen":"M6 11h12v9H6zM9 11V8a3 3 0 0 1 5.5-1.7","close":"M6 6l12 12M18 6L6 18","more":"M5 12v.01M12 12v.01M19 12v.01",
 "wallet":"M3 7h16v12H3zM3 7l12-3v3M16 13h3","target":"M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM12 12v.01",
 "book":"M5 4h10a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3zM8 20a3 3 0 0 1-3-3","moon":"M20 14A8 8 0 1 1 10 4a6.5 6.5 0 0 0 10 10z",
 "text":"M4 18l5-13 5 13M6 14h6M16 18l3-8 3 8M17 16h4","drag":"M8 6v.01M8 12v.01M8 18v.01M16 6v.01M16 12v.01M16 18v.01",
})
def spark(vals,w=70,h=26,col=None):
    col=col or UP; lo,hi=min(vals),max(vals); hi=hi if hi!=lo else lo+1
    pts=[(i*w/(len(vals)-1),h-3-(v-lo)/(hi-lo)*(h-6)) for i,v in enumerate(vals)]
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display:block"><path d="M{" L".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="none" stroke="{col}" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>'
def donut(parts,size=120,th=16):
    r=(size-th)/2; c=2*math.pi*r; off=0; s=""
    for v,col in parts:
        d=c*v/100; s+=f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{col}" stroke-width="{th}" stroke-dasharray="{d-2:.1f} {c-d+2:.1f}" stroke-dashoffset="{-off:.1f}" transform="rotate(-90 {size/2} {size/2})"/>'; off+=d
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">{s}</svg>'
def hbar(pct,col=None,h=8,bg=None): return f'<div style="height:{h}px;border-radius:9px;background:{bg or "var(--line)"};overflow:hidden"><i style="display:block;width:{pct}%;height:100%;background:{col or "var(--ink)"};border-radius:9px"></i></div>'
def tile(sym,pct,w=1):
    up=pct>=0; a=min(abs(pct),4)/4; bg=f"rgba(6,120,74,{.12+a*.78})" if up else f"rgba(196,42,50,{.12+a*.78})"; fg="#fff" if a>.45 else ("var(--up)" if up else "var(--dn)")
    return f'<div style="grid-column:span {w};background:{bg};color:{fg};border-radius:12px;padding:10px 8px;min-height:62px;display:flex;flex-direction:column;justify-content:space-between"><b style="font-size:12.5px">{sym}</b><span class="num" style="font-size:12px">{"+" if up else ""}{pct:.2f}%</span></div>'
def ichip(i,t,on=False): return f'<span class="chip{" on" if on else ""}" style="display:inline-flex;gap:6px;align-items:center">{ic(i,14)}{t}</span>'
def sec(t,r=""): return f'<div class="row" style="margin:20px 0 8px"><span class="lbl">{t}</span><span style="font-size:13px;font-weight:700;color:var(--lime)">{r}</span></div>' if THEME!="v2" else f'<div class="row" style="margin:22px 0 8px"><b style="font-size:15px;letter-spacing:-.01em">{t}</b><span style="font-size:13px;font-weight:700;color:var(--brandInk)">{r}</span></div>'
def stat(l,v): return f'<div style="flex:1"><div class="sub">{l}</div><div class="num" style="font-size:14.5px;margin-top:3px">{v}</div></div>'
def avatar(t,c="var(--ink)",s=40): return f'<span class="logo" style="background:{c};width:{s}px;height:{s}px;font-size:{s//3}px">{t}</span>'

def mv(a,c,n,p,ch,sp,k="up",sub="NSE"):
    return f'<div class="row" style="padding:12px 0;border-top:1px solid var(--line)"><div style="display:flex;gap:12px;align-items:center;min-width:0">{logo(a,c,38)}<div><b style="font-size:14.5px">{n}</b><div class="sub">{sub}</div></div></div><div>{spark(sp,64,24,UP if k=="up" else DN)}</div><div style="text-align:right;min-width:78px"><div class="num" style="font-size:14.5px">{p}</div><div class="num {k}" style="font-size:12px">{ch}</div></div></div>'
def tabs(items,on=0,gap=22):
    return f'<div style="display:flex;gap:{gap}px;font-weight:700;font-size:14px;border-bottom:1px solid var(--line);overflow:hidden">'+''.join(f'<span style="padding-bottom:9px;white-space:nowrap;{"border-bottom:3px solid var(--ink)" if i==on else "color:var(--ink3)"}">{t}</span>' for i,t in enumerate(items))+'</div>'
def hdr(t,r=""): return f'<div class="row" style="height:50px"><span>{ic("back")}</span><b>{tcase(t)}</b><span style="min-width:22px;display:flex;justify-content:flex-end">{r}</span></div>'
def note(t,kind="brand"):
    m={"brand":"background:var(--limeD);color:var(--brandInk)","warn":"background:var(--warnBg);color:var(--warn)","up":"background:var(--upBg);color:var(--up)","dn":"background:var(--dnBg);color:var(--dn)"}[kind]
    return f'<div class="banner" style="{m};margin-top:12px">{t}</div>'
def bars(vals,labels,h=90,col=None,w=300):
    col=col or "var(--ink)"; mx=max(vals); n=len(vals); bw=w/n
    return '<div style="display:flex;align-items:flex-end;gap:10px;height:%dpx">'%h+''.join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px;justify-content:flex-end;height:100%"><i style="display:block;width:100%;height:{max(6,v/mx*(h-26)):.0f}px;border-radius:8px 8px 3px 3px;background:{col if i==n-1 else "var(--line)"}"></i><span class="sub" style="font-size:11.5px">{l}</span></div>' for i,(v,l) in enumerate(zip(vals,labels)))+'</div>'

def chart2(a,b,w=330,h=130,ca=None,cb="#7A86A8"):
    ca=ca or BRAND
    def pts(v):
        lo,hi=min(min(a),min(b)),max(max(a),max(b)); return " L".join(f"{i*w/(len(v)-1):.1f},{h-8-(x-lo)/(hi-lo)*(h-24):.1f}" for i,x in enumerate(v))
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display:block"><line x1="0" y1="{h-1}" x2="{w}" y2="{h-1}" stroke="{LN}"/><path d="M{pts(b)}" fill="none" stroke="{cb}" stroke-width="2.2" stroke-linejoin="round"/><path d="M{pts(a)}" fill="none" stroke="{ca}" stroke-width="2.6" stroke-linejoin="round"/></svg>'

if THEME=='v2':
    import extras_v2
