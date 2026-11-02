#!/usr/bin/env python3
"""Patch the source design bundle into Crestline: v4 tokens, type, wordmark. Writes /tmp/crestline-{light,dark}.html"""
import re,json,base64,gzip,zlib,pathlib,sys
SRC=pathlib.Path(__file__).parent.parent/'source-design/hifi-artifact.html'
s=SRC.read_text(encoding='utf-8',errors='ignore')
tm=re.search(r'(<script type="__bundler/template">)(.*?)(</script>)',s,re.S)
mm=re.search(r'(<script type="__bundler/manifest">)(.*?)(</script>)',s,re.S)
tpl=json.loads(tm.group(2)); man=json.loads(mm.group(2))
NAVY='#0F2942'
def recolor(t):
    t=t.replace('get(/Time/i)','get(/^Time/i)')  # source bug: /Time/ also matched "One-time amount", giving Infinity
    t=re.sub(r"#C8FF00",'var(--accent)',t,flags=re.I)
    t=re.sub(r'rgba\(200, ?255, ?0, ?([.\d]+)\)',lambda m:f'rgba(15,41,66,{min(float(m.group(1)),.14)})',t)
    return t
for k,v in man.items():
    if not (v['mime'].startswith('text/html') or v['mime'].endswith('javascript')): continue
    d=base64.b64decode(v['data'])
    if v.get('compressed'):
        try:d=gzip.decompress(d)
        except Exception:d=zlib.decompress(d,-15)
    t=d.decode('utf8'); o=t
    if 'React.createElement' in t[:400] and '@license' in t[:80]: continue
    if t.startswith('// GENERATED from dc-runtime'): continue
    if t.startswith('(function(){ var A={"assets/icons'):
        for a,b in (('#C8FF00','#1B3A5C'),('#c8ff00','#1B3A5C'),('#A3D100','#0F2942'),('#a3d100','#0F2942'),('#7FA300','#0A1E33'),('#7fa300','#0A1E33')): t=t.replace(a,b)
    else:
        t=recolor(t)
    if 'function Wordmark' in t:
        t,n=re.subn(r'"P", /\*#__PURE__\*/React\.createElement\("span", \{\s*"aria-hidden": "true".*?"CKET"\)','"CRESTLINE")',t,count=1,flags=re.S)
        assert n==1,'wordmark'
        t=t.replace('"aria-label": "Pocket"','"aria-label": "Crestline"')
    if t!=o:
        v['data']=base64.b64encode(t.encode()).decode(); v['compressed']=False
TOK='''
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style id="crestline-v4">
:root{--pk-lime-50:#FFF7ED;--pk-lime-100:#FFEDD5;--pk-lime-200:#FED7AA;--pk-lime-300:#FDBA74;--pk-lime-400:#EA580C;--pk-lime-500:#C2410C;--pk-lime-600:#9A3412;--pk-lime-800:#0F2942;--pk-lime-900:#0A1E33;
--font-display:'Manrope',system-ui,sans-serif;--stretch-display:100%;--font-sans:'Inter',system-ui,sans-serif;--stretch-sans:100%;--font-mono:'JetBrains Mono',ui-monospace,monospace;--font-wordmark:'Manrope',system-ui,sans-serif;--stretch-wordmark:100%;
--bg-app:#070B14;--surface-1:#0F1626;--surface-2:#1E293B;--surface-hover:#27364B;--surface-sunken:#070B14;--border-subtle:#1E293B;--border-default:#334155;--text-primary:#F1F5F9;--text-secondary:#CBD5E1;--text-tertiary:#94A3B8;--text-disabled:#64748B;--text-on-accent:#070B14;--accent:#38BDF8;--accent-hover:#7DD3FC;--accent-pressed:#0EA5E9;--accent-tint:rgba(56,189,248,.14);--accent-text:#38BDF8;--accent-ring:transparent;--gain:#10B981;--gain-tint:rgba(16,185,129,.14);--loss:#FB7185;--loss-tint:rgba(244,63,94,.14);--on-loss:#070B14;--warning:#FBBF24;--info:#38BDF8;--ring-focus:0 0 0 3px rgba(251,146,60,.5);
--grad-accent:linear-gradient(135deg,#38BDF8,#7DD3FC);--grad-accent-soft:linear-gradient(135deg,rgba(56,189,248,.18),rgba(56,189,248,.06));--grad-card:linear-gradient(180deg,#14203A 0%,#0F1626 100%);--grad-page:#070B14;--grad-sheet:linear-gradient(180deg,#14203A,#0F1626 40%);--grad-chart-accent-from:rgba(56,189,248,.28);--grad-chart-accent-to:rgba(56,189,248,0);--grad-chart-gain-from:rgba(16,185,129,.26);--grad-chart-gain-to:rgba(16,185,129,0);--grad-chart-loss-from:rgba(251,113,133,.24);--grad-chart-loss-to:rgba(251,113,133,0)}
[data-theme="light"]{--bg-app:#FFFFFF;--surface-1:#F1F5F9;--surface-2:#E2E8F0;--surface-hover:#E2E8F0;--surface-sunken:#F8FAFC;--border-subtle:#E2E8F0;--border-default:#CBD5E1;--text-primary:#0A1120;--text-secondary:#334155;--text-tertiary:#475569;--text-disabled:#94A3B8;--text-on-accent:#FFFFFF;--accent:#0F2942;--accent-hover:#1B3A5C;--accent-pressed:#0A1E33;--accent-tint:rgba(15,41,66,.08);--accent-text:#0F2942;--accent-ring:transparent;--gain:#057A55;--gain-tint:rgba(5,122,85,.10);--loss:#C81E1E;--loss-tint:rgba(200,30,30,.09);--on-loss:#FFFFFF;--warning:#B45309;--info:#0369A1;--ring-focus:0 0 0 3px rgba(234,88,12,.45);
--grad-accent:linear-gradient(135deg,#0F2942,#1B3A5C);--grad-accent-soft:linear-gradient(135deg,rgba(15,41,66,.10),rgba(15,41,66,.03));--grad-card:linear-gradient(180deg,#FFFFFF 0%,#F1F5F9 100%);--grad-page:#F8FAFC;--grad-sheet:linear-gradient(180deg,#FFFFFF,#F8FAFC 40%);--grad-chart-accent-from:rgba(15,41,66,.20);--grad-chart-accent-to:rgba(15,41,66,0);--grad-chart-gain-from:rgba(5,122,85,.20);--grad-chart-gain-to:rgba(5,122,85,0);--grad-chart-loss-from:rgba(200,30,30,.18);--grad-chart-loss-to:rgba(200,30,30,0)}
#__claude_design_branding{display:none!important}
</style></head>'''
def imp(m):
    body=re.sub(r';',' !important;',m.group(2).rstrip().rstrip(';')+';')
    return m.group(1)+'{'+body+'}'
TOK=re.sub(r'(:root|\[data-theme="light"\])\{([^}]*)\}',imp,TOK)
TOK=TOK.replace('--pk-lime-50:','--pk-paper:#F1F5F9 !important;--pk-ink-100:#E2E8F0 !important;--pk-lime-50:',1)
for theme in ('light','dark'):
    t=tpl.replace('&quot;default&quot;:&quot;dark&quot;',f'&quot;default&quot;:&quot;{theme}&quot;')
    t=recolor(t).replace('</head>',TOK,1)
    out=s[:mm.start(2)]+json.dumps(man,separators=(',',':'))+s[mm.end(2):]
    tm2=re.search(r'(<script type="__bundler/template">)(.*?)(</script>)',out,re.S)
    out=out[:tm2.start(2)]+json.dumps(t).replace('/','\\u002F')+out[tm2.end(2):]
    pathlib.Path(f'/tmp/crestline-{theme}.html').write_text(out); print('wrote',theme,len(out)//1024,'KB')
