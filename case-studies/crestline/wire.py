"""Low-fidelity wireframes for the Crestline v2 redesign. Run: python3 wire.py -> v2/wireframes.html"""
import pathlib
CSS="""*{box-sizing:border-box;margin:0}body{background:#EEF1F7;font-family:Manrope,system-ui,sans-serif;color:#1B2233;padding:44px}
h1{font-size:28px;letter-spacing:-.03em;margin-bottom:6px}.lead{color:#5F6B85;font-size:15px;margin-bottom:34px;max-width:720px;line-height:1.5}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,640px));gap:48px 40px;justify-content:center}
.item{display:grid;grid-template-columns:390px 1fr;gap:18px}.item.wide{grid-template-columns:390px}
.cap{font-size:12px;font-weight:800;letter-spacing:.08em;color:#5F6B85;margin-bottom:8px;text-transform:uppercase}
.fr{width:390px;height:844px;background:#fff;border:2px solid #1B2233;border-radius:30px;position:relative;overflow:hidden;padding:46px 16px 16px}
.fr:before{content:"";position:absolute;top:10px;left:50%;transform:translateX(-50%);width:110px;height:26px;border-radius:14px;background:#1B2233}
.b{background:#E9ECF3;border:1.5px solid #AAB3C7;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#5F6B85;position:relative}
.b.x{background:linear-gradient(to top right,transparent calc(50% - 1px),#AAB3C7,transparent calc(50% + 1px)),linear-gradient(to bottom right,transparent calc(50% - 1px),#AAB3C7,transparent calc(50% + 1px)),#F3F5FA}
.ln{height:9px;border-radius:5px;background:#CDD3E1;margin:7px 0}.ln.s{width:55%}.ln.m{width:78%}.ln.xs{width:32%}
.row{display:flex;gap:10px;align-items:center}.gap{margin-top:12px}.sp{justify-content:space-between}
.btn{height:50px;border-radius:14px;border:2px solid #1B2233;background:#1B2233;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:14px}.btn.o{background:#fff;color:#1B2233}
.row>.btn,.row>.b:not([style*="width"]){flex:1}
.chip{height:30px;padding:0 14px;border:1.5px solid #AAB3C7;border-radius:99px;font-size:12px;font-weight:700;color:#5F6B85;display:flex;align-items:center;background:#fff}.chip.on{background:#1B2233;color:#fff;border-color:#1B2233}
.tab{position:absolute;left:0;right:0;bottom:0;height:74px;border-top:1.5px solid #AAB3C7;background:#fff;display:flex;justify-content:space-around;padding-top:10px;font-size:10.5px;font-weight:700;color:#5F6B85}
.tab div{text-align:center}.tab i{display:block;width:24px;height:24px;border:1.5px solid #AAB3C7;border-radius:7px;margin:0 auto 4px}.tab .on{color:#1B2233}.tab .on i{background:#1B2233;border-color:#1B2233}
.circle{width:22px;height:22px;border-radius:50%;background:#3447F5;color:#fff;font-size:11px;font-weight:800;display:grid;place-items:center;position:absolute;right:-8px;top:-8px;z-index:3;border:2px solid #fff}
.notes{font-size:12.5px;line-height:1.45;color:#44506A;padding-top:26px}.notes b{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:#3447F5;color:#fff;font-size:10.5px;margin-right:8px}.notes p{margin-bottom:10px}
.list>div{display:flex;gap:10px;align-items:center;padding:10px 0;border-bottom:1.5px dashed #CDD3E1}.list .av{width:34px;height:34px;border-radius:50%;background:#E9ECF3;border:1.5px solid #AAB3C7;flex:0 0 auto}
.bar{height:46px;border:1.5px solid #AAB3C7;border-radius:12px;display:flex;align-items:center;padding:0 12px;font-size:12px;color:#8590A8;background:#fff;font-weight:700}"""
def n(i): return f'<span class="circle">{i}</span>'
def nav(t,l="‹",r=""): return f'<div class="row sp" style="height:40px"><b style="font-size:18px">{l}</b><b style="font-size:14px">{t}</b><span style="min-width:18px;font-weight:800">{r}</span></div>'
def box(h,l="",cls="",ann=None,st=""): return f'<div class="b {cls}" style="height:{h}px;{st}">{l}{n(ann) if ann else ""}</div>'
def lines(k=3): return ''.join(f'<div class="ln {c}"></div>' for c in (["","m","s","xs","m"][:k]))
def chips(ts,on=0): return '<div class="row" style="overflow:hidden">'+''.join(f'<span class="chip{" on" if i==on else ""}">{t}</span>' for i,t in enumerate(ts))+'</div>'
def lst(k,ann=None): return '<div class="list" style="position:relative">'+''.join('<div><span class="av"></span><div style="flex:1"><div class="ln m" style="margin:3px 0"></div><div class="ln xs" style="margin:3px 0"></div></div><div style="width:60px"><div class="ln" style="margin:3px 0"></div></div></div>' for _ in range(k))+(n(ann) if ann else '')+'</div>'
def tab(on=0): return '<div class="tab">'+''.join(f'<div class="{"on" if i==on else ""}"><i></i>{t}</div>' for i,t in enumerate(["Home","Markets","Portfolio","Orders","Account"]))+'</div>'
def btn(t,o=False,ann=None): return f'<div class="btn{" o" if o else ""}" style="position:relative">{t}{n(ann) if ann else ""}</div>'
def seg(ts,on=0): return '<div class="row" style="border:1.5px solid #AAB3C7;border-radius:99px;padding:4px">'+''.join(f'<span style="flex:1;text-align:center;font-size:12px;font-weight:800;padding:8px 0;border-radius:99px;{"background:#1B2233;color:#fff" if i==on else "color:#5F6B85"}">{t}</span>' for i,t in enumerate(ts))+'</div>'
def fr(inner,tb=None): return f'<div class="fr">{inner}{tab(tb) if tb is not None else ""}</div>'
def item(cap,inner,notes,tb=None):
    return f'<div><div class="cap">{cap}</div><div class="item"><div>{fr(inner,tb)}</div><div class="notes">'+''.join(f'<p><b>{i+1}</b>{t}</p>' for i,t in enumerate(notes))+'</div></div></div>'
W=[]
W.append(item("W1 · Home",
 f'<div class="row sp"><div class="row"><span class="b" style="width:38px;height:38px;border-radius:50%"></span><div><div class="ln" style="width:90px"></div><div class="ln xs"></div></div></div><span class="row"><span class="b" style="width:38px;height:38px"></span><span class="b" style="width:38px;height:38px"></span></span></div>'
 +'<div class="row gap" style="overflow:hidden">'+''.join('<div class="b" style="width:100px;height:60px;flex:0 0 auto"></div>' for _ in range(3))+'</div>'
 +box(190,"Portfolio card · value · day change · chart","","1","margin-top:12px")+f'<div class="row gap">{btn("Add money",False)}{btn("Withdraw",True)}</div>'
 +'<div class="row gap" style="gap:8px">'+''.join(box(52,"") for _ in range(4))+'</div>'+f'<div class="gap">{seg(["Gainers","Losers","Volume"])}</div>'+lst(2,"4"),
 ["Portfolio card is the anchor: value first, change second, chart as texture.","Index ticker keeps market context visible without leaving Home.","Quick actions: Stocks, F&O, Mutual funds, IPOs.","Top movers for fast discovery. Tabs swap Gainers, Losers, Volume."],0))
W.append(item("W2 · Markets",
 nav("Markets","","⌕")+chips(["India","Global","Commodities"])+box(150,"Index chart · status","","1","margin-top:12px")+'<div class="gap"><b style="font-size:13px">Sector heatmap</b></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:8px;position:relative">'+''.join(box(58,"") for _ in range(9))+n(2)+'</div>'+box(70,"Market breadth bar","","3","margin-top:12px"),
 ["Index with live market status (open or closed, time left).","Heatmap: colour is change, tap a tile to open the sector.","Breadth: how many stocks are up or down. Cheap to build, high value."],1))
W.append(item("W3 · Stock detail",
 nav("","‹","☆ ⤴")+'<div class="row"><span class="b" style="width:44px;height:44px;border-radius:50%"></span><div><div class="ln" style="width:70px"></div><div class="ln m"></div></div></div>'+'<div class="gap" style="position:relative"><div class="ln" style="width:140px;height:18px"></div>'+n(1)+'</div>'+box(130,"Price chart","x","2","margin-top:10px")+f'<div class="gap">{chips(["1D","1W","1M","1Y","5Y"],2)}</div>'+'<div class="row gap" style="gap:18px;font-size:12px;font-weight:800;border-bottom:1.5px solid #CDD3E1;padding-bottom:8px;position:relative"><span>Overview</span><span style="color:#8590A8">Chart</span><span style="color:#8590A8">Financials</span><span style="color:#8590A8">Holders</span>'+n(3)+'</div>'+box(110,"Key stats grid","","","margin-top:12px")+f'<div class="row" style="position:absolute;left:16px;right:16px;bottom:16px">{btn("Sell",True)}<div style="flex:2">{btn("Buy",False,"4")}</div></div>',
 ["Price and day change are the first read.","Chart with one-tap timeframes.","Tabs hold depth of detail so Overview stays light.","Buy and Sell pinned at the bottom, always reachable by thumb."]))
W.append(item("W4 · Order pad",
 nav("Buy TCS","✕","₹3,412")+seg(["Delivery","Intraday","MTF"])+f'<div class="gap">{chips(["Market","Limit","SL","SL-M"],1)}</div>'+box(70,"Quantity  [ − ]  12  [ + ]","","1","margin-top:12px")+box(70,"Limit price","","2","margin-top:10px")+box(130,"Order value · charges · total · available","","3","margin-top:10px")+'<div class="ln m gap"></div><div class="b" style="position:absolute;left:16px;right:16px;bottom:16px;height:58px;border-radius:18px;background:#1B2233;color:#fff;font-size:14px">Swipe to buy 12 shares'+n(4)+'</div>',
 ["Quantity stepper plus keyboard entry.","Order types as chips: the common ones first.","Total required is shown before you commit, charges included.","Swipe confirms. It prevents accidental orders and feels deliberate."]))
W.append(item("W5 · Portfolio",
 '<div class="row sp"><b style="font-size:22px">Portfolio</b><span class="b" style="width:38px;height:38px"></span></div>'+f'<div class="gap">{seg(["Holdings","Positions"])}</div>'+'<div class="b gap" style="height:150px;position:relative;margin-top:12px">Donut · value · returns · XIRR'+n(1)+'</div>'+box(110,"By sector bars","","2","margin-top:12px")+'<div class="gap"><b style="font-size:13px">Holdings</b></div>'+lst(2,"3"),
 ["Allocation donut answers 'where is my money?'","Sector bars reveal concentration risk.","Holdings sorted by value, tap for the holding page."],2))
W.append(item("W6 · Watchlist",
 '<div class="row sp"><b style="font-size:22px">Watchlist</b><span class="row"><span class="b" style="width:38px;height:38px"></span><span class="b" style="width:38px;height:38px"></span></span></div>'+chips(["My picks","Nifty 50","F&O","+ New"],0)+'<div class="row sp gap" style="font-size:11.5px;color:#5F6B85;font-weight:700"><span>6 stocks · sorted by change</span><span>⇅ Sort</span></div>'+lst(6,"1"),
 ["Multiple lists as chips. Rows carry a sparkline for trend at a glance. Long-press to reorder or alert."],1))
W.append(item("W7 · Screener",
 nav("Screener","‹","↻")+chips(["Dividend payers","Low debt","Momentum"],0)+box(250,"Filters: market cap · P/E · yield (range sliders)","","1","margin-top:14px")+'<div class="ln m gap"></div><div class="b" style="position:absolute;left:16px;right:16px;bottom:16px;height:54px;border-radius:16px;background:#1B2233;color:#fff;position:absolute">Show 18 stocks'+n(2)+'</div>',
 ["Start from a preset idea, then fine-tune with sliders.","The result count lives on the button, so you know before you tap."],1))
W.append(item("W8 · Market depth",
 nav("TCS · Depth","‹","↻")+'<div class="ln" style="width:130px;height:16px"></div>'+f'<div class="gap">{chips(["Overview","Depth","Chart","News"],1)}</div>'+'<div class="row gap" style="align-items:flex-start;gap:10px;position:relative"><div style="flex:1">'+''.join(box(30,"Bid","","","margin-bottom:6px") for _ in range(5))+'</div><div style="flex:1">'+''.join(box(30,"Offer","","","margin-bottom:6px") for _ in range(5))+n(1)+'</div></div>'+box(40,"Total bids / offers","","2","margin-top:6px")+box(90,"Open · high · low · prev close · circuits","","3","margin-top:10px"),
 ["Five levels each side with quantity bars.","Totals show which side is heavier.","Circuit limits help avoid rejected orders."],1))
W.append(item("W9 · Basket",
 nav("Basket","‹","+")+'<div class="ln" style="width:140px;height:16px"></div>'+lst(3,"1")+box(100,"Funds needed · funds from sale · to add","","2","margin-top:12px")+'<div class="ln m gap"></div>'+f'<div style="position:absolute;left:16px;right:16px;bottom:16px">{btn("Place 3 orders",False,"3")}</div>',
 ["Each leg shows side, quantity, type, price.","Funds summary nets sales against purchases.","One tap places all legs."],3))
W.append(item("W10 · Create account step",
 nav("Verify PAN","‹","3/9")+'<div class="row" style="gap:5px">'+''.join(f'<span class="b" style="height:5px;flex:1;border-radius:3px;{"background:#1B2233" if i<3 else ""}"></span>' for i in range(9))+'</div><div class="gap"><div class="ln" style="width:200px;height:18px"></div></div>'+lines(2)+box(58,"PAN number","","1","margin-top:18px")+box(58,"Date of birth","","","margin-top:10px")+'<div class="ln m gap"></div><div class="ln gap" style="width:60%"></div>'+f'<div style="position:absolute;left:16px;right:16px;bottom:16px">{btn("Continue",False,"2")}</div>',
 ["One question per screen with live validation and a progress bar.","Continue stays disabled until the field is valid."]))
W.append(item("W11 · Funds",
 nav("Funds","‹")+box(110,"Available to trade · cash · pledged","","1")+f'<div class="row gap">{btn("+ Add money",False,"2")}{btn("Withdraw",True)}</div>'+'<div class="gap"><b style="font-size:13px">Recent</b></div>'+lst(4,"3"),
 ["Balance with a split of cash and pledged margin.","Add and Withdraw are equal weight, side by side.","Ledger with credits and debits."]))
W.append(item("W12 · Security",
 nav("Security","‹")+box(70,"Status: 4 of 4 checks on","","1")+'<div class="gap"><b style="font-size:13px">Sign-in</b></div>'+''.join('<div class="row sp" style="padding:12px 0;border-bottom:1.5px dashed #CDD3E1"><div><div class="ln" style="width:110px"></div><div class="ln xs"></div></div><span class="b" style="width:46px;height:26px;border-radius:99px"></span></div>' for _ in range(3))+'<div class="gap" style="position:relative"><b style="font-size:13px">Devices</b>'+n(2)+'</div>'+lst(2)+'<div class="gap" style="text-align:center;font-weight:800;font-size:13px;color:#C42A32">Sign out of other devices</div>',
 ["A single status line tells you if you are safe.","Devices list with a one-tap sign-out for all others."],4))
html=f'<!doctype html><html><head><meta charset="utf-8"><title>Crestline v2 · Wireframes</title><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&display=swap" rel="stylesheet"><style>{CSS}</style></head><body><h1>Crestline v2 wireframes</h1><p class="lead">Low-fidelity layouts for twelve key screens. Grey boxes show structure only. Numbers match the notes beside each screen.</p><div class="grid">{"".join(W)}</div></body></html>'
pathlib.Path("v2/wireframes.html").write_text(html);print("v2/wireframes.html",len(W),"wireframes")
