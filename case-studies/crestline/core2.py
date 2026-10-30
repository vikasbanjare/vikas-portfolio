from gen import *
S=[]
def idx(n,v,c,k): return f'<div style="flex:0 0 auto;background:#fff;border:1px solid var(--line);border-radius:16px;padding:10px 14px"><div class="sub" style="font-weight:700">{n}</div><div class="num" style="font-size:15px;margin-top:2px">{v}</div><div class="num {k}" style="font-size:12px">{c}</div></div>'
def mv(a,c,n,p,ch,sp,k="up"):
    return f'<div class="row" style="padding:12px 0;border-top:1px solid var(--line)"><div style="display:flex;gap:12px;align-items:center;min-width:0">{logo(a,c,38)}<div><b style="font-size:14.5px">{n}</b><div class="sub">NSE</div></div></div><div>{spark(sp,64,24,UP if k=="up" else DN)}</div><div style="text-align:right;min-width:78px"><div class="num" style="font-size:14.5px">{p}</div><div class="num {k}" style="font-size:12px">{ch}</div></div></div>'
# 1 HOME
S.append(phone("V1 · HOME", pad(f'''
<div class="row" style="height:54px"><div style="display:flex;gap:12px;align-items:center">{avatar("AM","var(--ink)",40)}<div><div class="sub">Good afternoon</div><b style="font-size:16px">Aarav</b></div></div><div style="display:flex;gap:10px"><span class="ico">{ic("search",20)}</span><span class="ico" style="position:relative">{ic("bell",20)}<i style="position:absolute;top:9px;right:10px;width:8px;height:8px;border-radius:50%;background:var(--dn);border:2px solid #fff"></i></span></div></div>
<div style="display:flex;gap:10px;margin:6px -20px 0;padding:0 20px;overflow:hidden">{idx("NIFTY 50","24,310.55","+0.42%","up")}{idx("SENSEX","79,880.10","+0.38%","up")}{idx("BANK NIFTY","52,104.30","-0.12%","dn")}</div>
<div style="background:var(--ink);color:#fff;border-radius:26px;padding:20px;margin-top:14px;position:relative;overflow:hidden">
<div style="font-size:12.5px;opacity:.72">Portfolio value</div><div class="num" style="font-size:32px;margin:4px 0 2px">₹1,03,255.60</div>
<div class="num" style="font-size:13px;color:#7CF2B8">+₹1,284.00 (+1.26%) today</div>
<div style="margin:12px -6px 8px">{chart(series(40,3,1.6),310,70,"#7CF2B8")}</div>
<div style="display:flex;gap:10px"><div style="flex:1;background:var(--spark);color:var(--ink);border-radius:14px;height:44px;display:grid;place-items:center;font-weight:800;font-size:14px">Add money</div><div style="flex:1;background:rgba(255,255,255,.12);border-radius:14px;height:44px;display:grid;place-items:center;font-weight:700;font-size:14px">Withdraw</div></div></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:16px">
{''.join(f'<div style="text-align:center"><div class="ico" style="width:100%;height:56px;border-radius:18px;margin-bottom:6px">{ic(i,22)}</div><div style="font-size:11.5px;font-weight:700">{t}</div></div>' for i,t in [("trend","Stocks"),("layers","F&O"),("coins" if False else "wallet","Mutual funds"),("bolt","IPOs")])}</div>
{sec("Top movers","See all")}
<div class="seg" style="margin-bottom:4px"><span class="on">Gainers</span><span>Losers</span><span>Volume</span></div>
{mv("TA","#E0A82E","Tata Motors","₹1,018.40","+3.82%",series(12,1,2))}{mv("SB","#2F6FE0","SBI","₹812.15","+2.64%",series(12,2,2))}{mv("IN","#1B4F9C","Infosys","₹1,904.70","+1.97%",series(12,4,1.6))}
'''),"home"))
# 2 MARKETS OVERVIEW
sectors=[("IT",1.8),("Banks",-0.6),("Auto",2.9),("Pharma",0.7),("FMCG",-1.1),("Metals",3.6),("Energy",0.2),("Realty",-2.4),("Infra",1.2)]
S.append(phone("V2 · MARKETS", pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:26px">Markets</div><span class="ico">{ic("search",20)}</span></div>
<div style="display:flex;gap:8px;margin-bottom:12px">{ichip("globe","India",True)}{ichip("trend","Global")}{ichip("coins" if False else "wallet","Commodities")}</div>
{card(f'<div class="row"><div><div class="sub">NIFTY 50</div><div class="num" style="font-size:28px;margin-top:2px">24,310.55</div><div class="num up" style="font-size:13px">+101.20 (+0.42%)</div></div><div style="text-align:right"><div class="sub">Market status</div><div style="display:inline-flex;gap:6px;align-items:center;font-weight:700;font-size:13px;margin-top:4px"><i style="width:8px;height:8px;border-radius:50%;background:var(--up)"></i>Open · closes 3:30 PM</div></div></div><div style="margin:10px -4px 0">{chart(series(46,9,1.2),330,96)}</div>','padding:16px 16px 10px')}
{sec("Sector heatmap","Full map")}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">{''.join(tile(n,p) for n,p in sectors)}</div>
<div class="sub" style="margin-top:8px">Tile colour shows today's change. Tap a sector to see its stocks.</div>
{sec("Market breadth")}
{card(f'<div class="row"><b class="up num">1,742 up</b><b class="dn num">1,010 down</b></div><div style="display:flex;height:10px;border-radius:9px;overflow:hidden;margin-top:10px"><i style="width:63%;background:var(--up)"></i><i style="width:37%;background:var(--dn)"></i></div><div class="row sub" style="margin-top:8px"><span>52-week highs 38</span><span>52-week lows 11</span></div>','padding:16px')}
'''),"watch"))
# 3 STOCK DETAIL (tabs + depth teaser)
S.append(phone("V3 · STOCK DETAIL", pad(f'''
<div class="row" style="height:50px"><span>{ic("back")}</span><span style="display:flex;gap:18px">{ic("bell",20)}{ic("star",20)}{ic("share",20)}</span></div>
<div style="display:flex;gap:12px;align-items:center">{logo("TC","#2F6FE0",44)}<div><b style="font-size:19px;letter-spacing:-.02em">TCS</b><div class="sub">NSE · Tata Consultancy Services</div></div></div>
<div class="row" style="align-items:flex-end;margin-top:12px"><div><div class="num" style="font-size:34px">₹3,412.30</div><div class="num up" style="font-size:14px">+₹28.40 (+0.84%) today</div></div><span class="pill" style="background:var(--limeD);color:var(--brandInk)">Live</span></div>
<div style="margin:8px -4px 0">{chart(series(44,5,1.7),350,120)}</div>
<div class="tf"><span>1D</span><span>1W</span><span class="on">1M</span><span>1Y</span><span>5Y</span><span>All</span></div>
<div style="display:flex;gap:22px;font-weight:700;font-size:14px;margin:14px 0 0;border-bottom:1px solid var(--line)"><span style="padding-bottom:9px;border-bottom:3px solid var(--ink)">Overview</span><span class="mut">Chart</span><span class="mut">Financials</span><span class="mut">Holders</span><span class="mut">News</span></div>
{card(f'<div style="display:flex;gap:14px">{stat("Day range","3,376 – 3,420")}{stat("52-week","3,060 – 4,592")}</div><div style="display:flex;gap:14px;margin-top:14px">{stat("Market cap","₹12.3L Cr")}{stat("P/E","29.4")}{stat("Volume","18.2L")}</div>','margin-top:14px;padding:16px')}
<div style="margin-top:12px;background:var(--limeD);border-radius:18px;padding:14px 16px;display:flex;gap:12px;align-items:center">{ic("calendar",20,"var(--brandInk)")}<div style="font-size:13px;line-height:1.4"><b>Dividend ex-date on 5 Nov</b><div class="mut">₹27 per share. Hold before the date to qualify.</div></div></div>
'''+bottom('<div style="display:flex;gap:12px"><div class="btn" style="flex:1;background:var(--dn)">Sell</div><div class="btn" style="flex:2;background:var(--up)">Buy</div></div>'))))
# 4 ORDER PAD v2
S.append(phone("V4 · ORDER PAD", pad(f'''
<div class="row" style="height:50px"><span>{ic("close")}</span><b>Buy TCS</b><span class="sub" style="font-weight:700">₹3,412.30</span></div>
<div class="seg" style="margin:4px 0 14px"><span class="on">Delivery</span><span>Intraday</span><span>MTF</span></div>
<div style="display:flex;gap:8px;margin-bottom:14px">{chip("Market")}{chip("Limit",True)}{chip("SL")}{chip("SL-M")}</div>
<div class="field" style="display:flex;justify-content:space-between;align-items:center"><div><small>Quantity</small><b class="num" style="font-size:22px">12</b></div><div style="display:flex;gap:10px"><span class="ico">{ic("minus",18)}</span><span class="ico">{ic("plus",18)}</span></div></div>
<div class="field"><small>Limit price</small><b class="num" style="font-size:22px">₹3,410.00</b><div class="sub" style="margin-top:2px">Last traded price ₹3,412.30</div></div>
{card(kv("Order value","₹40,920.00",True)+kv("Charges (est.)","₹32.60",True)+f'<div style="height:1px;background:var(--line)"></div>'+kv("Total required","₹40,952.60",True)+kv("Available to trade","₹52,310.40",True),'padding:4px 18px;margin-top:4px')}
<div class="sub" style="margin-top:10px;display:flex;gap:8px;align-items:center">{ic("info",15)} Valid for today. The order cancels if not filled by 3:30 PM.</div>
'''+bottom('<div style="height:60px;border-radius:20px;background:var(--lime);position:relative;display:flex;align-items:center;padding:6px"><div style="width:48px;height:48px;border-radius:16px;background:#fff;display:grid;place-items:center;color:var(--ink)">'+ic("back",20).replace('d="M15 5l-7 7 7 7"','d="M9 5l7 7-7 7"')+'</div><div style="flex:1;text-align:center;color:#fff;font-weight:800;font-size:15px;margin-right:48px">Swipe to buy 12 shares</div></div>'))))
# 5 PORTFOLIO v2
S.append(phone("V5 · PORTFOLIO", pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:26px">Portfolio</div><span class="ico">{ic("eye",20)}</span></div>
<div class="seg"><span class="on">Holdings · 6</span><span>Positions · 2</span></div>
{card(f'<div style="display:flex;gap:16px;align-items:center">{donut([(62,"var(--ink)"),(24,"var(--lime)"),(14,"#B9C2D6")],112,16)}<div style="flex:1"><div class="sub">Current value</div><div class="num" style="font-size:22px;margin:2px 0">₹1,03,255.60</div><div class="num up" style="font-size:13px">+₹5,226.72 (+5.33%)</div><div class="sub" style="margin-top:6px">XIRR <b class="num" style="color:var(--ink)">16.2%</b></div></div></div><div style="display:flex;gap:14px;margin-top:12px;font-size:12px" class="mut"><span>● Stocks 62%</span><span style="color:var(--brandInk)">● Funds 24%</span><span>● Other 14%</span></div>','margin-top:12px;padding:16px')}
{sec("By sector","Details")}
{card(''.join(f'<div style="margin:10px 0"><div class="row" style="font-size:13px"><b>{n}</b><span class="num">{p}%</span></div><div style="margin-top:6px">{hbar(p*2,c)}</div></div>' for n,p,c in [("Energy",27,"var(--ink)"),("IT",20,"var(--lime)"),("Banks",32,"#7A86A8")]),"padding:6px 16px")}
{sec("Holdings","Sort: Value")}
{srow("R","#C9A24B","Reliance","22 shares · avg ₹1,209.73","₹27,456.00","+3.16%")}{srow("TC","#2F6FE0","TCS","6 shares · avg ₹3,120.00","₹20,472.60","+9.36%")}
'''),"port"))
# 6 WATCHLIST v2
S.append(phone("V6 · WATCHLIST", pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:26px">Watchlist</div><span style="display:flex;gap:10px"><span class="ico">{ic("search",20)}</span><span class="ico">{ic("sliders",20)}</span></div>
<div style="display:flex;gap:8px;margin-bottom:6px;overflow:hidden">{chip("My picks",True)}{chip("Nifty 50")}{chip("F&O")}{chip("Funds")}{chip("+ New list")}</div>
<div class="row sub" style="margin:8px 0 2px"><span>6 stocks · sorted by day change</span><span style="display:flex;gap:4px;align-items:center">{ic("swap",14)} Sort</span></div>
{mv("TA","#E0A82E","Tata Motors","₹1,018.40","+3.82%",series(12,1,2))}{mv("SB","#2F6FE0","SBI","₹812.15","+2.64%",series(12,2,2))}{mv("HD","#1B4F9C","HDFC Bank","₹1,544.20","+0.62%",series(12,3,1))}{mv("TC","#2F6FE0","TCS","₹3,412.30","+0.84%",series(12,5,1.4))}{mv("RE","#C9A24B","Reliance","₹1,248.00","-0.31%",series(12,6,-1),"dn")}{mv("IT","#0E9A8A","ITC","₹468.55","-1.12%",series(12,7,-1.6),"dn")}
<div class="sub" style="text-align:center;margin-top:14px">Press and hold a stock to reorder or set an alert.</div>
'''),"watch"))
tf_=""
sheet("core-v2.html","Crestline v2 · core screens",S)
