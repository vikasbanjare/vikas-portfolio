# Writes ../showcase.html from the same brand code as the app: logo, flowers, icons, banners and kolam come from
# source-design/generator, animation from ../app/screens.css, phones from v6/ (see capture6.mjs).
import sys,json,re,html,pathlib
HERE=pathlib.Path(__file__).resolve().parent;CS=HERE.parent
sys.path.insert(0,str(CS/'source-design'/'generator'))
import ui,system
from ui import T,LIGHT,DARK,gi,btn,promo,pill,kolam_svg,ajrakh,flower,petals,outline,spinner,TF
from pattern import field as pfield
from screens1 import mark,liveMark,bloomt
from icons import D as ICONS
T.clear();T.update({k:f'var(--t-{k})' for k in LIGHT})
e=html.escape
META=json.loads((lambda s:s[s.index('{'):s.rindex('}')+1])((CS/'app/meta.js').read_text()))
LIVE=json.loads((CS/'v6/live.json').read_text()) if (CS/'v6/live.json').exists() else {'LT':{},'DK':{}}
(CS/'v6/live.js').write_text('window.CR_LIVE='+json.dumps(LIVE,ensure_ascii=False,separators=(',',':'))+';')
NAMES={k:v['name'] for k,v in META['M'].items()}
TOTAL=sum(len(f['keys']) for f in META['F'])

def ph(k,s=None,cap=None,cls=''):
    st=f' style="--s:{s}"' if s else ''
    img=f'<img src="v6/lt/{k}.webp" data-shot="{k}" alt="{e(NAMES.get(k,k))} screen" loading="lazy" width="390" height="844">'
    fig=f'<div class="ph {cls}"{st}><div class="ph-in" data-live="{k}">{img}</div></div>'
    return f'<figure class="phf">{fig}<figcaption>{cap}</figcaption></figure>' if cap else fig
def cta(t,href,kind='solid',ic=''):
    x=' target="_blank" rel="noopener"' if href.startswith('http') else ''
    return f'<a class="cta {kind} pt-press" href="{href}"{x}>{ic}<span>{t}</span>{TF}</a>'
def head(eb,h,sub=''):
    return f'<header class="sh"><p class="eb">{eb}</p><h2>{h}</h2>'+(f'<p class="sub">{sub}</p>' if sub else '')+'</header>'
def sec(id,bg,body,cls=''):
    return f'<section id="{id}" class="sec {cls}" style="background:var(--t-{bg})"><div class="w">{body}</div></section>'
def tile(n,s=26):return f'<span class="tile">{gi(n,s)}</span>'
def live_lock(light=False,sz=64,font=44):
    c='rgba(42,66,184,.16)' if light else 'rgba(255,255,255,.15)'
    ptn=ajrakh(c,'',W=420,H=190,live='pt-st',order=lambda a,z:7-a+z*.5,g='--g:.07s;')
    return f'<div class="lock {"lock-l" if light else ""}" role="img" aria-label="Crestline logo with the flower pattern">{ptn}<div class="lockin">{liveMark(sz,"blue" if light else "white",9)}<span class="pt-up" style="--i:19;font-size:{font}px;font-weight:500;letter-spacing:-.025em">Crestline</span></div></div>'

# ───── Hero
hero_field=ajrakh('rgba(255,255,255,.1)','',W=1100,H=860,mask=(4,52),live='pt-sw')
HERO=f'''<section class="hero" id="top">{hero_field}
<div class="hero-t"><a class="back" href="../index.html"><span aria-hidden="true">←</span> All UI/UX work</a>
<div class="brandrow">{liveMark(58,"white",6)}<span class="brandname pt-up" style="--i:12">Crestline</span></div>
<h1>An investing app built around the moments people lose money.</h1>
<p class="lede">Stocks, funds, IPOs and F&amp;O for India, with every journey, every document check and every failure designed. I set the brief and designed it end to end.</p>
<div class="ctas">{cta("Open the working app","app/","white")}{cta("See all "+str(TOTAL)+" screens","#screens","ghost")}</div>
<p class="note">Self-initiated concept. The broker is fictional, all numbers are sample data and no money moves.</p></div>
<div class="hero-p" aria-hidden="true">{ph("Stock",cls="side")}{ph("Home",cls="mid")}{ph("KycHub",cls="side")}</div></section>'''

# ───── At a glance
GLANCE=[('All',str(TOTAL),'screens, in light and dark'),('Stocks',str(len(META['F'])),'areas, from sign-in to tax reports'),('ID card','Own KYC','for each product, with its own documents'),('Trading API','3 builds','web, a private iPhone app, a private Android app'),('Profile','0','real users so far, and I say so below')]
glance='<div class="glance">'+''.join(f'<div class="card gl">{tile(i)}<b>{n}</b><span>{t}</span></div>' for i,n,t in GLANCE)+'</div>'

# ───── Problem, on Rose: this app keeps Rose for risk and failure
BRIEFS=[('FoGate','F&amp;O losses','Leverage is one toggle away, and the possible loss is rarely on screen at that moment.','A check before F&amp;O, and the most you can lose shown on the order.'),
('OrderTypes','Confusing order types','Limit, GTT, SL-M and AMO are exchange words, not choices a new investor can weigh.','Plain names with one line each.'),
('KycHub','Slow, unclear KYC','A long form hides how much is left, and failures rarely say what to do next.','Short steps, and each product lists exactly what it needs.'),
('Charges','Hidden charges','The price on the button is rarely what leaves the account.','The total before the order, and a full breakdown one tap away.')]
briefs='<div class="briefs">'+''.join(f'<article class="card brief"><div class="brief-p">{ph(k,.42)}</div><div><h3>{t}</h3><p>{p}</p><p class="ans"><b>My answer</b>{a}</p></div></article>' for k,t,p,a in BRIEFS)+'</div>'
PERS=[('Aarav','27, first-time investor','Wants to understand before acting, and fears the wrong tap.'),('Meera','41, long-term SIP investor','Checks weekly and needs tax clarity at filing time.'),('Rahul','33, active F&amp;O trader','Opens the app many times a day and wants margin and depth at a glance.'),('Savitri','62, careful and low in confidence','Needs readable text, and signals that are not colour alone.')]
pers='<div class="four">'+''.join(f'<div class="card pers"><span class="av">{n[0]}</span><b>{n}</b><span class="dim">{a}</span><p>{t}</p></div>' for n,a,t in PERS)+'</div>'
PROBLEM=sec('story','bgRose',f'''<div class="big"><p class="eb">The problem</p><p class="num">91%</p><h2>of individual F&amp;O traders made a net loss in FY25.</h2>
<p class="sub">Together they lost ₹1,05,603 crore, up about 41% in a year. The apps they used are fast and polished. I wanted to know what an investing app looks like if it keeps that speed and stops hiding the consequences.</p>
<p class="src">SEBI study, July 2025, reported by <a href="https://www.business-standard.com/markets/news/net-losses-of-traders-in-fo-widens-in-fy25-sebi-study-125070701221_1.html" target="_blank" rel="noopener">Business Standard</a> and <a href="https://moneylife.in/article/91-percentage-of-retail-traders-lost-money-in-derivatives-losses-in-fo-surged-41-percentage-to-rs105-lakh-crore-in-fy25-sebi-study/77613.html" target="_blank" rel="noopener">Moneylife</a>.</p></div>
<h3 class="h3">Four complaints became four design briefs.</h3><p class="sub s2">Desk research: competitor apps, what investors and traders say on X, Quora and Reddit, and data from NSE, SEBI and AMFI.</p>{briefs}
<h3 class="h3">Who I designed for</h3>{pers}<p class="sub s2">These four are proto-personas written from desk research, not from interviews.</p>''')

# ───── Role
ROLE=sec('role','bgCloud',head('Role and limits','A concept is only as credible as its constraints.')+f'''<div class="three">
<div class="card plain"><h3>What I did</h3><ul><li>Framed the research and set the direction</li><li>Made the product decisions below</li><li>Directed the flows, brand, system and screens</li><li>Reviewed and tested across rounds</li></ul></div>
<div class="card plain"><h3>Rules I held to</h3><ul><li>Real Indian products: delivery, intraday, MTF, GTT, IPO, SIP, F&amp;O</li><li>Risk wording on order screens</li><li>No pattern or motion behind a money figure</li><li>Sample data, always labelled</li></ul></div>
<div class="card plain"><h3>What I did not have</h3><ul><li>Real users or analytics</li><li>Engineers or a backend</li><li>A compliance review</li><li>A client or a brief. I set my own</li></ul></div></div>''')

# ───── Decisions
DEC=[('Put the risk before the switch','F&amp;O is off by default. Turning it on starts with the risk, not the benefits.','One toggle in settings, or a tick box inside a long agreement.','The biggest loss in this category sits behind this one action, so this is the one place where added friction helps.','Share of people who turn on F&amp;O and trade in their first week, against how many read the risk screen.',['FoGate']),
('A full-screen pad, not a swipe','Quantity and price are typed, so the keypad is the layout.','Swipe-to-buy on every order.','A gesture is quick to learn but does not help someone check an order.','Time to a first order, and how often people edit an order straight after placing it.',['Buy','Review']),
('Placed is not filled','A limit order gets its own waiting screen. Waiting, part-filled and filled are different states with different money.','One "Order successful" screen for every outcome.','"Success" suggests the shares are already yours.','Support contacts asking "where are my shares", and repeat orders placed by mistake.',['Waiting','PartFilled','Filled']),
('Profit after charges','Booked profit is net of brokerage, STT and fees, so it matches the contract note.','The gross figure, with charges on a separate statement.','A number that differs from the contract note reads as a mistake, even when the arithmetic is right.','Tickets about a profit figure that does not match the statement.',['Sold','Charges']),
('One number leads the portfolio','Value first. Each holding takes two lines.','A dense table for people watching holdings hourly.','I expect most visits to ask one question: how am I doing?','Time to answer "how much am I up today" in a moderated test.',['Portfolio']),
('Mobile number first','Sign-in leads with a mobile number and code. Client ID is a second link.','Client ID and password first, the older broker pattern.','People coming from other Indian apps already expect this, and a client ID is easy to forget.','Sign-in success on the first try, and use of the Client ID link.',['Welcome']),
('Green means Buy, whatever the brand does','Buy is green and Sell is red, always with the word. Blue is the brand.','Buy in the brand colour.','A trade button should not change meaning with the brand, and colour alone fails people who cannot tell the two apart.','Wrong-side orders corrected within a minute.',['Stock']),
('Each product asks for its own checks','One KYC opens the account. Funds, IPOs, F&amp;O, bonds, deposits and loans then ask only for what each one needs.','One long form that asks everyone for everything.','People see why a document is needed at the moment they want that product.','Drop-off at each check, and how many people finish a check they started.',['KycHub'])]
def dec(i,d):
    t,l,a,b,m,sc=d;fl=flower(0,0,'var(--t-kghost)','',0,6)
    s=.62 if len(sc)==1 else (.5 if len(sc)==2 else .42)
    return f'''<article class="dec {"rev" if i%2 else ""}"><div class="dec-p"><svg class="dec-f" aria-hidden="true" viewBox="-110 -110 220 220">{fl}</svg>{"".join(ph(k,s) for k in sc)}</div>
<div class="dec-t"><span class="n">{i+1:02d}</span><h3>{t}</h3><p class="lead">{l}</p><dl><div><dt>Instead of</dt><dd>{a}</dd></div><div><dt>Because</dt><dd>{b}</dd></div><div><dt>I would measure</dt><dd>{m}</dd></div></dl></div></article>'''
DECISIONS=sec('decisions','pagebg',head('Decisions','Eight calls, what I passed on, and how I would test each.')+''.join(dec(i,d) for i,d in enumerate(DEC)))

# ───── Brand
def logos():
    TL=[('Blue with pattern','pattern','For the app icon and splash.'),('Blue gradient','plain','For small sizes, where a pattern blurs.'),('White','white','For blue backgrounds.'),('Ink','ink','For quiet, formal documents.'),('Yellow','haldi','Kept as an option.')]
    return '<div class="logos">'+''.join(f'<div class="card lg {"lg-b" if s=="white" else ""}"><span class="lab">{n}</span>{mark(92,s)}<div class="sizes">{mark(44,s)}{mark(30,s)}{mark(20,s)}</div><p>{w}</p></div>' for n,s,w in TL)+'</div>'
COL=[('Neel','#2A42B8','Actions, brand','#FFF'),('Neel light','#4C6AE8','Secondary, charts','#FFF'),('Neel tint','#EDEFFA','Soft surfaces','#2A42B8'),('Syahi','#171A22','Text','#FFF'),('Slate','#5F6475','Quiet text','#FFF'),('Haldi','#E9A820','One accent, rarely','#171A22'),('Khadi','#F6F5F2','Background','#171A22'),('Surface','#FFFFFF','Cards','#171A22'),('Up','#0B7A52','Gains, Buy','#FFF'),('Down','#C2332B','Losses, Sell','#FFF'),('Up tint','#E6F4EE','Success surface','#075E3F'),('Down tint','#FBEAE8','Error surface','#9B241D')]
cols='<div class="swatches">'+''.join(f'<div class="sw"><div class="chip" style="background:{h};color:{f}">{h}</div><b>{n}</b><span>{u}</span></div>' for n,h,u,f in COL)+'</div>'
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)];c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c];return .2126*c[0]+.7152*c[1]+.0722*c[2]
def ratio(a,b):
    x,y=sorted((lum(a),lum(b)),reverse=True);return (x+.05)/(y+.05)
PAIRS=[('#171A22','#FFFFFF','Text on a card'),('#5F6475','#FFFFFF','Quiet text on a card'),('#FFFFFF','#2A42B8','White on a main button'),('#FFFFFF','#0B7A52','White on Buy'),('#FFFFFF','#C2332B','White on Sell'),('#F1F2F5','#101218','Dark mode text'),('#9DB0FF','#20232D','Dark mode blue on a card')]
cont='<div class="pairs">'+''.join(f'<div class="pair"><span class="aa" style="background:{b};color:{a}">Aa</span><span>{t}</span><b>{ratio(a,b):.2f}:1</b></div>' for a,b,t in PAIRS)+'</div>'
GR=[('Neel Dawn','linear-gradient(180deg,#E4EBFF,#F1F4FE 45%,#F8F8F7)','Main pages: home, markets, portfolio',0),('Neel Deep','linear-gradient(115deg,#1E2F95,#2A42B8 55%,#4C6AE8)','Hero, splash, main banner',1),('Neel Press','linear-gradient(180deg,#3350CC,#2A42B8)','Main buttons',1),('Cloud','linear-gradient(165deg,#EDF1FF,#FAFBFF 55%,#FFFFFF)','Steps and forms: buying, KYC, records',0),('Sky','linear-gradient(115deg,#123E8A,#1E5FBF 60%,#2F7FDB)','Learn banners',1),('Sea','linear-gradient(115deg,#0A4F58,#0E6A6C 55%,#128078)','Refer and earn',1),('Leaf','linear-gradient(115deg,#0A5A3D,#0B7A52 60%,#159069)','Funds and SIP banners',1),('Mint','linear-gradient(135deg,#DDF3E7,#F7FCF9)','Every success',0),('Mist','linear-gradient(135deg,#DFE6FF,#F8FAFF)','Waiting and loading',0),('Rose','linear-gradient(135deg,#F8E9E6,#FDF9F8)','Failure and risk',0),('Deepavali','linear-gradient(115deg,#3F1A63,#6E2257 55%,#A5332F)','Diwali only',1),('Night','linear-gradient(180deg,#1A2140,#14182A 45%,#101218)','Dark mode background',1)]
grads='<div class="grads">'+''.join(f'<div><div class="gchip" style="background:{g};color:{"#FFF" if d else "#171A22"}">{n}</div><span>{u}</span></div>' for n,g,u,d in GR)+'</div>'
def motions():
    W,H=393,190
    svg=lambda x:f'<svg class="fit" aria-hidden="true" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">{x}</svg>'
    wht='rgba(255,255,255,.26)';blu='rgba(42,66,184,.3)'
    tapb=f'<button class="tapdemo pt-press pt-tb" type="button">Explore funds<svg class="fit" aria-hidden="true" viewBox="0 0 170 56"><g transform="translate(85 28)"><g class="pt-ta">'+''.join(f'<ellipse cy="-15" rx="4.5" ry="10" fill="rgba(255,255,255,.55)" transform="rotate({k*45})"/>' for k in range(8))+f'</g></g></svg>{TF}</button>'
    spin=f'<div class="spins"><span class="spinbox">{spinner(50)}</span>{spinner(34,"var(--t-br)")}{spinner(22,"var(--t-br)")}<span class="spinbtn">{spinner(20)}Placing</span></div>'
    M=[('Bloom','One flower opens, petal by petal, on empty pages.',svg(petals(W/2,H/2,'rgba(255,255,255,.9)',2.9)),'heroG'),
    ('Block print','Stamped line by line, the way a printer works by hand. On the refer invitation.',svg(pfield(W,H,wht,'pt-st',lambda a,z:z*7+a,'--g:.05s;')),'heroG'),
    ('Ripple','Flowers open outward from the logo, on the opening animation.',svg(pfield(W,H,blu,'pt-ri',lambda a,z:round(((28+56*a-W/2)**2+(28+56*z-H/2)**2)**.5/56,1),'--g:.12s;'))+f'<div class="on">{mark(56)}</div>','pagebg'),
    ('Turning flowers','Each flower turns one step, neighbours in opposite directions, on long waits.',svg(pfield(W,H,wht,'pt-tu',lambda a,z:(a+z)*.5,'--g:.06s;',True)),'heroG'),
    ('Soft light','A slow light passes over the flowers, on Welcome and the main banners.',f'<div class="on wide">{ui.banner("Refer and earn","Invest with a friend","You both get ₹250 after their first trade","ajrakh",124)}</div>','pagebg'),
    ('Hand drawn','Each petal drawn with one line, on Help and Start here.',svg(''.join(outline(84+112*a,50+90*z,'var(--t-br)',1.45,(a+z*3)*8) for a in range(3) for z in range(2))),'bgCloud'),
    ('Petal loader','Light travels around the eight petals. Small enough for a button.',f'<div class="on">{spin}</div>','pagebg'),
    ('App icon','Flowers open in the tile, then the C draws itself, on sign-in.',f'<div class="on">{liveMark(118)}</div>','pagebg'),
    ('Tap bloom','A flower opens from what you press. Press this one. Never on Buy or Sell.',f'<div class="on">{tapb}</div>','pagebg')]
    return '<div class="motions">'+''.join(f'<figure><div class="mo" style="background:var(--t-{b})">{a}</div><figcaption><b>{i+1}. {n}</b>{w}</figcaption></figure>' for i,(n,w,a,b) in enumerate(M))+'</div>'
BN=[('ipo','IPO','Lalithaa Jewellery','Closes at 5 pm','Soft light over the flower pattern'),('sip','SIP','Small amounts add up','From ₹100 a month','Bars grow, month by month'),('fund','Mutual funds','Find your first fund','Sorted by risk and cost','Bandhani dots twinkle'),('fo','F&amp;O','Trade options the simple way','Read the risk first','Leheriya waves drift'),('stock','Stocks','Your first share','Start to finish, 3 min','Candles breathe'),('bond','Bonds','Steady income','Paid twice a year','Light passes behind a jali'),('gold','Gold','Own gold without the locker','From ₹500','A coin turns and shines'),('etf','ETFs','The whole index in one buy','From ₹70','Bandhani dots on teal'),('refer','Refer and earn','Invest with a friend','You both get ₹250','Block print, stamped by hand'),('learn','Learn','What happens in an IPO','2 min video','The icon itself moves'),('basket','Baskets','Stocks picked together','One tap to buy them all','The icon itself moves'),('diwali','Diwali · 8 Nov','Muhurat trading','One hour this evening','Rangoli turns slowly. Diwali only')]
banners='<div class="banners">'+''.join(f'<figure>{promo(k,a,b,d)}<figcaption>{w}</figcaption></figure>' for k,a,b,d,w in BN)+'</div>'
icons='<div class="icons">'+''.join(f'<div class="ic" style="--d:{i%10*.09:.2f}s">{tile(n,30)}<span>{n}</span></div>' for i,n in enumerate(ICONS))+'</div>'
KO=[('ok','bgMint','Order filled','The line completes around its dots.'),('wait','bgMist','Waiting','A light travels along the line.'),('part','bgMist','Part filled','The line stops part of the way.'),('bad','bgRose','Failed','Only the dots. The line is never drawn on a failure.')]
kolam='<div class="four">'+''.join(f'<div class="kol" style="background:var(--t-{b})">{kolam_svg(k,{"ok":"var(--t-up)","bad":"var(--t-gr)"}.get(k,"var(--t-tintfg)"),"var(--t-kghost)",128)}<b>{n}</b><span>{w}</span></div>' for k,b,n,w in KO)+'</div>'
RULES=[('One touch per screen','Never two patterns or animations together. Icons and the logo do not count.'),('Never on a money figure','No pattern behind a balance, price or order detail.'),('Ajrakh-inspired flowers for invitations','The logo, opening animation, Welcome, banners and the small loader.'),('Kolam after the order is placed','Plays once. Never on a failure: there, only the dots appear.'),('Rangoli for Diwali only','Other festivals get their own motif, or none.'),('Real objects for icons','Torana for IPOs, a bell for alerts, a potli for money. Each has one short motion.'),('No gold, no saffron clichés','A deep blue leads, an echo of indigo.'),('Words stay simple','Lakh and crore, ₹, and Indian languages from the first screen.')]
rules='<div class="rules">'+''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in RULES)+'</div>'
TY=[('Display','34','₹1,03,250.56',34),('Title','26','Your first share',26),('Section','17','Top movers today',17),('Body','15','Banks lifted the market today.',15),('Small','13','Sent to +91 98••• ••421',13)]
typ='<div class="type">'+''.join(f'<div><span>{n} · {d}</span><b style="font-size:{z}px;font-weight:{500 if z>15 else 400}">{x}</b></div>' for n,d,x,z in TY)+'</div>'
comp=system.Components()
comp=re.sub(r'^<div style="padding:32px"><h1.*?</h1><p.*?</p>','<div>',comp,flags=re.S)
comp=comp.replace('display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:26px 22px;align-items:start','display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,262px),1fr));gap:30px 22px;align-items:start')
comp=re.sub(r'<div style="margin-top:26px;width:390px.*</div></div>$','</div>',comp,flags=re.S) if 'width:390px' in comp else comp
BRAND=sec('brand','bgCloud',head('The brand','Deep blue, Ajrakh flowers, and colour that always means something.','Everything on this page is the app’s own code: the same logo, the same animation, the same icons. Press and watch; these loop here so you can see them, and in the app each plays once at its moment.')+f'''
<div class="two">{live_lock()}{live_lock(True)}</div>
<h3 class="h3">Logo</h3><p class="sub s2">A C under one straight line. The flowers inside the tile come from Ajrakh block printing.</p>{logos()}
<h3 class="h3">The flower, in motion</h3><p class="sub s2">Nine movements, each with one job. Only one moves on a screen, never behind a money figure.</p>{motions()}
<h3 class="h3">Banners, one look per product</h3><p class="sub s2">Each product has its own colour, pattern and quiet motion, so people can tell them apart before they read a word.</p>{banners}
<h3 class="h3">Icons, all {len(ICONS)}, each with its own motion</h3><p class="sub s2">The bell swings, money drops into the potli, bars grow and lines draw.</p>{icons}
<h3 class="h3">Kolam tells you how an order ended</h3><p class="sub s2">One line drawn around dots without lifting the hand, the way a kolam is drawn at a doorway.</p>{kolam}
<h3 class="h3">Colour</h3><p class="sub s2">Blue and white do most of the work. Green and red only ever mean up and down.</p>{cols}
<h3 class="h3">Gradients</h3><p class="sub s2">Each section of the app has its own light gradient, and a result always wins: a success is Mint and a failure is Rose, wherever it happens. This page follows the same map.</p>{grads}
<div class="two tp"><div><h3 class="h3 t0">Type</h3><p class="sub s2">Satoshi, by Indian Type Foundry. Anek Devanagari, by Ek Type, for Indian scripts.</p>{typ}<p lang="hi" class="hindi">आपका ऑर्डर सुबह 9:41 बजे एक्सचेंज तक पहुँच गया।</p></div>
<div><h3 class="h3 t0">Measured contrast</h3><p class="sub s2">Worked out from the colour values. WCAG AA asks for 4.5:1 on small text.</p>{cont}</div></div>
<h3 class="h3">How I use Indian tradition</h3><p class="sub s2">Rare, meaningful and never in the way of money.</p>{rules}
<h3 class="h3">Components and states</h3><p class="sub s2">The parts every screen is built from. Cards use a soft shadow, never a coloured edge.</p><div class="kit">{comp}</div>''')

# ───── Working app
STATES=[('NotPlaced','Not placed'),('Waiting','Waiting'),('PartFilled','Part filled'),('MoneyFail','Money did not arrive'),('KycFail','KYC needs a fix'),('HoldEmpty','Nothing here yet')]
states='<div class="rail">'+''.join(ph(k,None,c) for k,c in STATES)+'</div>'
STATE_SEC=sec('states','bgMist',head('States','Concepts usually stop at the happy path. Money apps cannot.','Most trust is won or lost when something goes wrong, so each failure says what happened, where the money is and what to do next.')+states)
NAT=[('kyc-hub','KYC and documents screen listing what each product asks for','Each product asks for its own checks'),('fo-proof','F&amp;O income proof screen with eight accepted documents','F&amp;O income proof, step by step'),('offline','Home screen as skeleton shapes with a no internet card','No internet: skeleton shapes, then saved numbers')]
nat=''.join(f'<figure class="phf"><div class="ph" ><div class="ph-in"><img src="v6/native/{k}.jpg" alt="{a}" loading="lazy" width="390" height="844"></div></div><figcaption>{c}</figcaption></figure>' for k,a,c in NAT)
APP=sec('app','pagebg',f'''<div class="appgrid"><div class="appph"><div class="ph frame" style="--s:.82"><div class="ph-in" data-live="Home" id="appslot"><img src="v6/lt/Home.webp" data-shot="Home" alt="Home screen" width="390" height="844" loading="lazy"></div></div><button class="startapp cta solid pt-press" id="startapp" type="button"><span>Start the app here</span>{TF}</button></div>
<div>{head('Working app','Every journey, in one app you can use.',str(TOTAL)+' screens across '+str(len(META['F']))+' areas, in light and dark. It covers the checks and documents each product needs, turning on F&amp;O, commodities and currency, NRI and family accounts, stock SIPs, deposits, pension and insurance. Prices and orders are simulated, and nothing you type leaves the page.')}
<div class="ctas">{cta("Open it full screen","app/")}</div>
<div class="builds"><div class="card plain"><h3>iPhone</h3><p>A native SwiftUI build that I run on my own phone. Private, not on the App Store. US prices come live through my own data key.</p></div><div class="card plain"><h3>Android</h3><p>A private install that matches the iPhone rules, works with no internet permission and carries sample data only.</p></div></div></div></div>
<div class="natgrid"><div><h3 class="h3">From the iPhone build</h3><p class="sub s2">Real pictures from my phone. The same design, rebuilt natively, with skeleton shapes when there is no internet and each product’s checks saved as you go.</p></div><div class="rail">{nat}</div></div>''')

# ───── All screens
ch='<button class="fchip pt-press" data-on="1" data-f="all" type="button">All '+str(TOTAL)+TF+'</button>'+''.join(f'<button class="fchip pt-press" data-f="{f["code"]}" type="button">{e(f["name"],quote=False).replace("&amp;amp;","&amp;")} {len(f["keys"])}{TF}</button>' for f in META['F'])
wall=''.join(f'<button class="th" type="button" data-k="{k}" data-a="{f["code"]}" aria-label="{e(NAMES.get(k,k))}"><img src="v6/lt/{k}.webp" data-shot="{k}" alt="" loading="lazy" width="390" height="844"><span>{e(NAMES.get(k,k))}</span></button>' for f in META['F'] for k in f['keys'])
SCREENS=sec('screens','bgCloud',head('Everything','All '+str(TOTAL)+' screens.','Pictures from the working app, by area. Switch to dark at the bottom of the page and they change with it. Open any one to read it, then jump into the app on that screen.')+f'<div class="fchips">{ch}</div><div class="wall lim" id="wall">{wall}</div><button class="cta ghost2 pt-press more" id="more" type="button"><span>Show all {TOTAL} screens</span>{TF}</button>')

# ───── Proof and outcome
PROOF=sec('proof','bgMist',head('What is proven, and what is not','Nothing here has met a real user yet.')+f'''<div class="four">
<div class="card plain pf"><span class="lab">Virtual Android phone</span><b>{TOTAL} screens</b><p>Every screen, light and dark, at two phone sizes: no layout problems. 72 text boxes on 44 screens stayed clear of the keyboard.</p></div>
<div class="card plain pf"><span class="lab">Followed from the main tabs</span><b>No dead ends</b><p>Earlier, 106 of 312 screens could not be reached at all. A link check missed that. I now follow every link from the main tabs in the Android build.</p></div>
<div class="card plain pf"><span class="lab">Earlier direction</span><b>26 of 32 tasks</b><p>A simulated test with 8 personas, plus eight rounds of expert audit, shaped the flows. That was before this brand, and simulated people are not people.</p></div>
<div class="card plain pf"><span class="lab">Not done</span><b>Real people</b><p>Still to do: a study with real investors, a compliance review, a physical Android phone, and a first run with real Indian prices.</p></div></div>
<div class="card lesson"><div><h3>Testing on a phone still found what a browser could not.</h3><p>Black bars on Android, a keyboard covering the number box, and rows split unevenly by a link inside a link only showed up once I ran the app on a phone and looked. On an earlier pass, two tabs I had called done turned out to be dead, which is why I now tap through instead of trusting a checker.</p></div>{bloomt("Research")}</div>''')
OUTCOME=sec('outcome','bgMint',head('If it shipped','What I expect to change, and how I would know.')+'''<div class="four">
<div class="card plain"><h3>Wrong-assumption tickets</h3><p>"Where are my shares", "why does my profit differ". Fewer, per 1,000 orders.</p></div>
<div class="card plain"><h3>First order</h3><p>Share of funded accounts placing an order, and how often it is edited at once.</p></div>
<div class="card plain"><h3>F&amp;O activation</h3><p>Deliberately lower is fine. Watch early losses per new F&amp;O user instead.</p></div>
<div class="card plain"><h3>KYC completion</h3><p>Drop-off at each step, and recovery after a failure.</p></div></div>
<p class="sub s2">No baselines exist, so I have set no targets. These are the measures, not results.</p>
<p class="closing">I set out to design a broker. The real work was writing what happens after the tap, and the next step is to watch real people use it before I add a single screen.</p>''')
FOOT=f'''<footer class="foot"><div class="w">{live_lock(False,48,34)}
<div class="credits"><h3>Credits and how this was made</h3><p>Concept, research framing and design direction by Vikas Banjare. I set the brief, the research framing and the design direction. Screens, specifications and code were produced with AI assistance and directed and reviewed by me.</p><p>Crestline is fictional. Figures are sample data. Company names appear only to make the examples realistic, with no affiliation implied. This is not investment advice.</p>{cta("Back to all work","../index.html","ghost")}</div></div></footer>'''
TABS=[('Story','#story','Learn'),('Decisions','#decisions','Research'),('Brand','#brand','Gain'),('App','#app','Play'),('Screens','#screens','All')]
NAV='<nav class="tabs" aria-label="Sections">'+''.join(f'<a href="{h}" data-t="{h[1:]}">{gi(i,22)}<span>{n}</span></a>' for n,h,i in TABS)+f'<button id="theme" type="button" aria-pressed="false" aria-label="Switch to dark mode">{gi("Clock",22) if 0 else ""}<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 3.5a8.500 8.500 0 0 1 0 17z" fill="currentColor"/></svg><span id="themel">Dark</span></button></nav>'
LB=f'''<dialog id="lb" aria-label="Screen"><div class="lbin"><button class="lbx" id="lbp" type="button" aria-label="Previous screen">{gi("Back",22) if "Back" in ICONS else "←"}</button><figure><img id="lbi" alt="" width="390" height="844"><figcaption><b id="lbt"></b><span id="lba"></span><a class="cta solid pt-press" id="lbo" href="app/"><span>Open in the app</span>{TF}</a><button class="cta ghost2 pt-press" id="lbc" type="button"><span>Close</span>{TF}</button></figcaption></figure><button class="lbx" id="lbn" type="button" aria-label="Next screen">→</button></div></dialog>'''

vars_lt=''.join(f'--t-{k}:{v};' for k,v in LIGHT.items());vars_dk=''.join(f'--t-{k}:{v};' for k,v in DARK.items())
CSS=(HERE/'present6.css').read_text().replace('/*LT*/',vars_lt).replace('/*DK*/',vars_dk)
JS=(HERE/'present6.js').read_text().replace('"__AREAS__"',json.dumps({f['code']:f['name'].replace('&amp;','&') for f in META['F']},ensure_ascii=False))
icon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1E2F95"/><stop offset=".6" stop-color="#2A42B8"/><stop offset="1" stop-color="#4C6AE8"/></linearGradient></defs><rect width="100" height="100" rx="23" fill="url(#g)"/><path d="M14 22H86M76 40H52C38 40 30 48 30 59S38 78 52 78H76" fill="none" stroke="#fff" stroke-width="9"/></svg>'
(CS/'v6/icon.svg').write_text(icon)
PAGE=f'''<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Crestline, a concept investing app · Vikas Banjare</title>
<meta name="description" content="Crestline is a concept investing app for India, designed around the moments people lose money: {TOTAL} screens, its own brand, and a working app.">
<meta property="og:title" content="Crestline, a concept investing app"><meta property="og:description" content="{TOTAL} screens, its own brand, and a working app. By Vikas Banjare."><meta property="og:image" content="https://vikasbanjare.github.io/vikas-portfolio/assets/uiux/crestline.jpg">
<link rel="icon" href="v6/icon.svg"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anek+Devanagari:wght@400;500&display=swap">
<link rel="stylesheet" href="app/screens.css"><style>{CSS}</style><script>try{{if(localStorage.getItem('cr.page')==='dark')document.documentElement.setAttribute('data-theme','dark')}}catch(e){{}}</script></head><body>
{HERO}<main><div class="w gw">{glance}</div>{PROBLEM}{ROLE}{DECISIONS}{BRAND}{STATE_SEC}{APP}{SCREENS}{PROOF}{OUTCOME}</main>{FOOT}{NAV}{LB}
<script src="v6/live.js" defer></script><script>{JS}</script></body></html>'''
(CS/'showcase.html').write_text(PAGE)
print('showcase.html',len(PAGE)//1024,'KB; live.js',(CS/'v6/live.js').stat().st_size//1024,'KB')
