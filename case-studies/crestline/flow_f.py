from gen import *
F=[]
# F1 top movers
F.append(phone("F1 · TOP MOVERS", pad(hdr("Top movers",ic("filter",20))+f'''
{tabs(["Gainers","Losers","Volume","52-wk high"],0,18)}
<div style="display:flex;gap:8px;margin:12px 0 4px">{chip("Nifty 50",True)}{chip("Nifty 500")}{chip("F&O stocks")}</div>
{mv("TA","#E0A82E","Tata Motors","₹1,018.40","+3.82%",series(12,1,2))}{mv("SB","#2F6FE0","SBI","₹812.15","+2.64%",series(12,2,2))}{mv("IN","#1B4F9C","Infosys","₹1,904.70","+1.97%",series(12,4,1.6))}{mv("BA","#0E9A8A","Bajaj Auto","₹9,812.00","+1.74%",series(12,8,1.5))}{mv("LT","#7A5CFF","L&T","₹3,640.25","+1.52%",series(12,9,1.4))}{mv("TI","#C9A24B","Titan","₹3,288.60","+1.31%",series(12,10,1.2))}{mv("AX","#C42A32","Axis Bank","₹1,121.90","+1.10%",series(12,11,1.1))}
'''),"watch"))
# F2 sector detail
F.append(phone("F2 · SECTOR", pad(hdr("Auto",ic("star",20))+f'''
<div class="num" style="font-size:30px">14,208.40</div><div class="num up" style="font-size:14px">+2.90% today</div>
<div style="margin:6px -4px 0">{chart(series(44,4,1.9),350,110)}</div>
<div class="tf"><span>1D</span><span class="on">1W</span><span>1M</span><span>1Y</span><span>5Y</span></div>
{sec("Biggest movers in Auto")}
{card(''.join(f'<div class="row" style="padding:9px 0;{"border-top:1px solid var(--line)" if i else ""}"><span style="font-weight:700;font-size:14px">{n}</span><div style="flex:1;margin:0 14px">{hbar(w,UP,6)}</div><b class="num up" style="font-size:13px">{c}</b></div>' for i,(n,w,c) in enumerate([("Tata Motors",90,"+3.82%"),("Bajaj Auto",50,"+1.74%"),("Mahindra",44,"+1.52%"),("Maruti",30,"+0.88%")])),"padding:6px 16px")}
{sec("Stocks","24")}
{mv("TA","#E0A82E","Tata Motors","₹1,018.40","+3.82%",series(12,1,2))}{mv("BA","#0E9A8A","Bajaj Auto","₹9,812.00","+1.74%",series(12,8,1.5))}
'''),"watch"))
# F3 screener builder
FLT=card(f'''<div class="lbl" style="margin-bottom:10px">Filters · 3 on</div>
<div style="margin:12px 0"><div class="row" style="font-size:13px"><b>Market cap</b><span class="num">₹20,000 Cr +</span></div><div style="height:8px;border-radius:8px;background:var(--line);margin-top:8px;position:relative"><i style="position:absolute;left:30%;right:0;top:0;bottom:0;background:var(--lime);border-radius:8px"></i></div></div>
<div style="margin:16px 0"><div class="row" style="font-size:13px"><b>P/E ratio</b><span class="num">5 – 25</span></div><div style="height:8px;border-radius:8px;background:var(--line);margin-top:8px;position:relative"><i style="position:absolute;left:10%;right:55%;top:0;bottom:0;background:var(--lime);border-radius:8px"></i></div></div>
<div style="margin:16px 0 4px"><div class="row" style="font-size:13px"><b>Dividend yield</b><span class="num">2% +</span></div><div style="height:8px;border-radius:8px;background:var(--line);margin-top:8px;position:relative"><i style="position:absolute;left:35%;right:0;top:0;bottom:0;background:var(--lime);border-radius:8px"></i></div></div>''',"padding:16px")
F.append(phone("F3 · SCREENER", pad(hdr("Screener",ic("refresh",20))+f'''
<div class="sub" style="margin-bottom:8px">Start with an idea, then fine-tune.</div>
<div style="display:flex;gap:8px;overflow:hidden;margin-bottom:14px">{ichip("coins" if False else "wallet","Dividend payers",True)}{ichip("shield","Low debt")}{ichip("flame","Momentum")}</div>
{FLT}
<div class="row" style="margin-top:14px"><span style="font-weight:700;font-size:14px">+ Add filter</span><span class="sub">ROE · Debt · Growth · Promoter holding</span></div>
'''+bottom(btn("Show 18 stocks","lime")))))
# F4 screener results
F.append(phone("F4 · RESULTS", pad(hdr("18 stocks",ic("download",20))+f'''
<div style="display:flex;gap:8px;overflow:hidden;margin-bottom:10px">{chip("Market cap 20,000 Cr+")}{chip("P/E 5–25")}{chip("Yield 2%+")}</div>
<div class="row sub" style="padding:8px 0;border-bottom:1px solid var(--line)"><span>Stock</span><span style="display:flex;gap:26px"><span>P/E</span><span>Yield</span><span>1Y</span></span></div>
{''.join(f'<div class="row" style="padding:13px 0;border-bottom:1px solid var(--line)"><div style="display:flex;gap:10px;align-items:center">{logo(a,c,34)}<div><b style="font-size:14px">{n}</b><div class="sub">₹{p}</div></div></div><span class="num" style="display:flex;gap:22px;font-size:13px"><span>{pe}</span><span>{y}</span><b class="up">{r}</b></span></div>' for a,c,n,p,pe,y,r in [("IT","#0E9A8A","ITC","468.55","24.1","3.1%","+12%"),("CI","#1B4F9C","Coal India","402.30","7.4","5.8%","+22%"),("PG","#C9A24B","Power Grid","318.90","18.2","3.6%","+31%"),("ON","#7A5CFF","ONGC","262.10","7.9","4.5%","+9%"),("HU","#2F6FE0","Hindustan Zinc","524.00","19.5","4.2%","+17%")])}
'''),"watch"))
# F5 market depth
def dep(q,p,w,k): return f'<div style="position:relative;display:flex;justify-content:space-between;padding:7px 8px;font-size:13px"><i style="position:absolute;{"right" if k=="up" else "left"}:0;top:0;bottom:0;width:{w}%;background:{"var(--upBg)" if k=="up" else "var(--dnBg)"};border-radius:6px"></i><span class="num" style="position:relative">{q if k=="up" else p}</span><b class="num {k}" style="position:relative">{p if k=="up" else q}</b></div>'
F.append(phone("F5 · MARKET DEPTH", pad(hdr("TCS · Depth",ic("refresh",20))+f'''
<div class="row"><div class="num" style="font-size:26px">₹3,412.30</div><span class="pill" style="background:var(--limeD);color:var(--brandInk)">Live</span></div>
{tabs(["Overview","Depth","Chart","News"],1)}
<div style="display:flex;gap:10px;margin-top:14px">
<div style="flex:1"><div class="row sub" style="padding:0 8px 4px"><span>Qty</span><span>Bid</span></div>{dep("1,240","3,412.20",95,"up")}{dep("860","3,412.10",70,"up")}{dep("2,010","3,412.00",100,"up")}{dep("420","3,411.90",40,"up")}{dep("990","3,411.80",62,"up")}</div>
<div style="flex:1"><div class="row sub" style="padding:0 8px 4px"><span>Offer</span><span>Qty</span></div>{dep("540","3,412.40",45,"dn")}{dep("1,100","3,412.50",78,"dn")}{dep("730","3,412.60",56,"dn")}{dep("1,820","3,412.70",100,"dn")}{dep("310","3,412.80",26,"dn")}</div></div>
<div class="row" style="margin-top:10px;padding:10px 8px;background:#fff;border-radius:14px;font-size:13px"><span>Total bids <b class="num up">5,520</b></span><span>Total offers <b class="num dn">4,500</b></span></div>
{card(f'<div style="display:flex;gap:14px">{stat("Open","3,390")}{stat("High","3,420")}{stat("Low","3,376")}{stat("Prev close","3,383.90")}</div><div style="display:flex;gap:14px;margin-top:14px">{stat("Upper circuit","3,722.30")}{stat("Lower circuit","3,045.50")}</div>',"margin-top:12px;padding:14px 16px")}
'''),"watch"))
# F6 financials
F.append(phone("F6 · FINANCIALS", pad(hdr("TCS · Financials")+f'''
{tabs(["Overview","Financials","Holders","News"],1)}
<div class="seg" style="margin:14px 0"><span class="on">Revenue</span><span>Profit</span><span>EPS</span></div>
{card(f'<div class="sub">Revenue, last 4 quarters (₹ Cr)</div><div class="num" style="font-size:24px;margin:4px 0 12px">63,973</div>{bars([60,61,62,64],["Q1","Q2","Q3","Q4"],100)}',"padding:16px")}
{sec("Key ratios")}
{card(kv("Net profit margin","19.4%",True)+kv("Return on equity","46.2%",True)+kv("Debt to equity","0.08",True)+kv("Dividend yield","1.2%",True),"padding:2px 18px")}
{note("Figures update after each quarterly result. Last updated 12 Oct.")}
'''),"watch"))
# F7 holders
F.append(phone("F7 · SHAREHOLDING", pad(hdr("TCS · Holders")+f'''
{tabs(["Overview","Financials","Holders","News"],2)}
{card(f'<div style="display:flex;gap:16px;align-items:center">{donut([(72,"var(--ink)"),(12,"var(--lime)"),(9,"#7A86A8"),(7,"#C3CAD9")],120,18)}<div style="flex:1;font-size:13px;display:grid;gap:8px"><div class="row"><span>Promoters</span><b class="num">72.3%</b></div><div class="row"><span style="color:var(--brandInk)">FIIs</span><b class="num">12.4%</b></div><div class="row"><span>DIIs</span><b class="num">8.9%</b></div><div class="row"><span>Public</span><b class="num">6.4%</b></div></div></div>',"margin-top:14px;padding:16px")}
{sec("Change in the last quarter")}
{card(''.join(f'<div class="row" style="padding:10px 0;{"border-top:1px solid var(--line)" if i else ""}"><span style="font-size:14px">{n}</span><b class="num {k}" style="font-size:14px">{c}</b></div>' for i,(n,c,k) in enumerate([("Promoters","0.0%","mut"),("FIIs","-0.4%","dn"),("DIIs","+0.5%","up"),("Public","-0.1%","dn")])),"padding:4px 18px")}
{note("Shareholding is reported each quarter by the company.")}
'''),"watch"))
# F8 news feed
def news(src,t,time,tick,k="up",c="+0.8%"): return f'<div style="padding:14px 0;border-top:1px solid var(--line)"><div class="sub" style="font-weight:700">{src} · {time}</div><div style="font-weight:700;font-size:15px;line-height:1.35;margin:5px 0 8px">{t}</div><div style="display:flex;gap:8px">{chip(tick+" "+c)}</div></div>'
F.append(phone("F8 · NEWS", pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:26px">News</div><span class="ico">{ic("search",20)}</span></div>
{tabs(["For you","Markets","My stocks","IPOs"],0,18)}
<div style="margin-top:12px;background:var(--ink);color:#fff;border-radius:22px;padding:18px"><div style="font-size:12px;opacity:.7">In short · 2 min read</div><div style="font-weight:800;font-size:19px;line-height:1.25;margin:8px 0 12px">Nifty ends higher as IT and auto stocks lead the gains</div><div style="display:flex;gap:8px"><span class="pill" style="background:rgba(255,255,255,.14);color:#fff">NIFTY +0.42%</span><span class="pill" style="background:rgba(255,255,255,.14);color:#fff">TCS +0.84%</span></div></div>
{news("Market wire","Rate decision keeps banks in focus ahead of next week's results","1h","HDFCBANK","dn","-0.2%")}
{news("Business desk","Navkar Foods IPO opens for bids, price band set at ₹312–329","3h","IPO","up","Open")}
{news("Company filings","TCS board approves interim dividend of ₹27 per share","5h","TCS")}
'''),"watch"))
# F9 article
F.append(phone("F9 · ARTICLE", pad(hdr("",ic("share",20))+f'''
<div class="sub" style="font-weight:700">Company filings · 5h ago</div>
<h1 class="h1" style="font-size:24px;line-height:1.2;margin:8px 0 14px">TCS board approves interim dividend of ₹27 per share</h1>
{note("<b>In short.</b> Shareholders on record as of 5 Nov receive ₹27 per share. Payment follows in about two weeks.")}
<p style="font-size:15.5px;line-height:1.6;margin:16px 0;color:var(--ink2)">The board met on Tuesday and approved the payout. The record date is 5 November, which means you must hold the shares before the market opens that day to qualify.</p>
{card(f'<div class="row"><div style="display:flex;gap:10px;align-items:center">{logo("TC","#2F6FE0",38)}<div><b>TCS</b><div class="sub">₹3,412.30</div></div></div><b class="num up">+0.84%</b></div>',"padding:14px 16px")}
'''+bottom('<div style="display:flex;gap:12px"><div class="btn ghost" style="flex:1">Set alert</div><div class="btn" style="flex:1;background:var(--lime)">Buy TCS</div></div>'))))
# F10 calendar
def ev(d,m,t,s,k): return f'<div style="display:flex;gap:14px;padding:12px 0;border-top:1px solid var(--line);align-items:center"><div style="width:48px;text-align:center;background:#fff;border:1px solid var(--line);border-radius:12px;padding:6px 0"><div class="num" style="font-size:18px">{d}</div><div class="sub" style="font-size:11px">{m}</div></div><div style="flex:1"><b style="font-size:14.5px">{t}</b><div class="sub">{s}</div></div>{pill(k[0],k[1])}</div>'
F.append(phone("F10 · CALENDAR", pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:26px">Calendar</div><span class="ico">{ic("calendar",20)}</span></div>
<div style="display:flex;gap:8px;margin-bottom:6px;overflow:hidden">{chip("All",True)}{chip("Results")}{chip("Dividends")}{chip("IPOs")}{chip("Holidays")}</div>
{sec("This week")}
{ev("30","Oct","Kaveri Power IPO closes","Mainboard · last day to bid",("IPO","wait"))}{ev("31","Oct","Navkar Foods IPO closes","Apply with UPI",("IPO","wait"))}{ev("2","Nov","Infosys quarterly results","After market hours",("Results","ink"))}{ev("5","Nov","TCS ex-dividend","₹27 per share · you hold 6",("Dividend","up"))}{ev("14","Nov","Market holiday","Exchanges closed",("Holiday","dn"))}
'''),"watch"))
# F11 compare
F.append(phone("F11 · COMPARE", pad(hdr("Compare")+f'''
<div style="display:flex;gap:10px;margin:4px 0 12px"><div style="flex:1;background:#fff;border:1px solid var(--line);border-radius:16px;padding:12px"><div style="display:flex;gap:8px;align-items:center">{logo("TC","#2F6FE0",30)}<b>TCS</b></div></div><div style="flex:1;background:#fff;border:1px solid var(--line);border-radius:16px;padding:12px"><div style="display:flex;gap:8px;align-items:center">{logo("IN","#1B4F9C",30)}<b>Infosys</b></div></div></div>
{card(f'<div style="display:flex;gap:14px;margin-bottom:8px;font-size:12px"><b style="color:var(--lime)">● TCS +18.4%</b><b class="mut">● Infosys +24.9%</b></div>'+chart2(series(40,5,1.7),series(40,8,2.2))+'<div class="tf"><span>1M</span><span>6M</span><span class="on">1Y</span><span>3Y</span></div>',"padding:14px 12px 8px")}
{sec("Side by side")}
{card(''.join(f'<div class="row" style="padding:11px 0;{"border-top:1px solid var(--line)" if i else ""}"><span class="mut" style="width:96px;font-size:13px">{l}</span><b class="num" style="font-size:14px;flex:1;text-align:center">{a}</b><b class="num" style="font-size:14px;flex:1;text-align:right">{b}</b></div>' for i,(l,a,b) in enumerate([("Price","₹3,412","₹1,905"),("1Y return","+18.4%","+24.9%"),("P/E","29.4","26.8"),("Dividend","1.2%","2.4%"),("Debt/equity","0.08","0.11")])),"padding:2px 18px")}
'''),"watch"))
# F12 ETFs & gold
def coll(i,t,s): return f'<div style="background:#fff;border:1px solid var(--line);border-radius:20px;padding:16px;display:flex;gap:14px;align-items:center"><span class="ico" style="background:var(--limeD);border-color:transparent;color:var(--brandInk)">{ic(i,22)}</span><div style="flex:1"><b>{t}</b><div class="sub">{s}</div></div><span class="mut">›</span></div>'
F.append(phone("F12 · ETFs, GOLD, BONDS", pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:26px">Invest</div><span class="ico">{ic("search",20)}</span></div>
<div style="display:grid;gap:10px">{coll("layers","ETFs","Track an index in one buy")}{coll("coins" if False else "wallet","Digital gold","Start from ₹10")}{coll("bank","Bonds and G-secs","Fixed income, lower risk")}{coll("target","Fixed deposits","Partner banks, tenures 7 days to 10 years")}{coll("book","Mutual funds","Direct plans, no commission")}</div>
{sec("Popular ETFs")}
{mv("N5","#1B4F9C","Nifty 50 ETF","₹254.20","+0.41%",series(12,3,1))}{mv("GO","#C9A24B","Gold ETF","₹62.80","+0.22%",series(12,5,.8))}
'''),"home"))
# F13 bonds
F.append(phone("F13 · BONDS", pad(hdr("Bonds & G-secs",ic("filter",20))+f'''
<div style="display:flex;gap:8px;margin-bottom:10px">{chip("All",True)}{chip("G-secs")}{chip("Corporate")}{chip("Tax-free")}</div>
{''.join(card(f'<div class="row"><div><b>{n}</b><div class="sub">{iss}</div></div>{pill(r,"ink")}</div><div style="display:flex;gap:14px;margin-top:12px">{stat("Yield",y)}{stat("Maturity",m)}{stat("Min. invest",mi)}</div>',"margin-bottom:10px;padding:16px") for n,iss,r,y,m,mi in [("7.10% GOI 2034","Government of India","Sovereign","7.02%","Apr 2034","₹10,000"),("8.25% Corporate 2029","Rated AA+","AA+","8.31%","Aug 2029","₹10,000")])}
{note("Bond prices move with interest rates. Returns are paid only if you hold to maturity.","warn")}
'''),"home"))
sheet("flow-f-discover.html","Crestline v2 · Discover and research",F)
