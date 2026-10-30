"""Crestline v4 screens: the spec's blind spots and core redesigns. Run with CREST_THEME=v4."""
from gen import *
Z=[]
def B(t,k="ex"): return f'<span class="bdg b-{k}">{t}</span>'
def mode(on="w"): return f'<div style="display:flex;background:var(--elev);border-radius:99px;padding:3px;font-size:12px;font-weight:700"><span style="padding:6px 10px;border-radius:99px;{"background:var(--lime);color:#fff" if on=="w" else "color:var(--ink2)"}">Wealth</span><span style="padding:6px 10px;border-radius:99px;{"background:var(--lime);color:#fff" if on=="t" else "color:var(--ink2)"}">Trader</span></div>'
def head(on="w"): return f'<div class="row" style="height:52px"><b style="font-family:Manrope;font-size:15px;letter-spacing:.04em">CRESTLINE</b>{mode(on)}<span style="display:flex;gap:8px"><span class="ico" style="width:36px;height:36px">{ic("search",17)}</span><span class="ico" style="width:36px;height:36px;position:relative">{ic("bell",17)}<i style="position:absolute;top:6px;right:7px;width:7px;height:7px;border-radius:50%;background:var(--spark)"></i></span></span></div>'
def jag(): return f'<div style="background:var(--warnBg);border-radius:14px;padding:10px 12px;display:flex;gap:10px;align-items:flex-start;margin-bottom:10px"><span style="color:var(--warn);flex:0 0 auto">{ic("shield",16)}</span><div style="font-size:12px;line-height:1.4;color:var(--warn);flex:1"><b>SEBI investor notice.</b> Most individual F&amp;O traders lose money. Never act on stock tips from chat groups.</div><span style="color:var(--warn)">{ic("close",14)}</span></div>'
def idx3(): return '<div style="display:flex;gap:8px">'+''.join(f'<div style="flex:1;background:#fff;border:1px solid var(--line);border-radius:12px;padding:8px 10px"><div class="sub" style="font-weight:700;font-size:11px">{n}</div><div class="num" style="font-size:13px;margin-top:2px">{v}</div><div class="num {k}" style="font-size:11px">{c}</div></div>' for n,v,c,k in [("NIFTY 50","24,482.65","▲ 0.46%","up"),("SENSEX","80,142.10","▲ 0.42%","up"),("INDIA VIX","13.82","▼ 2.10%","dn")])+'</div>'
def task(dot,t,s,cta,c="var(--signal)"): return f'<div style="background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 14px;margin-top:8px"><div class="row" style="align-items:flex-start"><div style="display:flex;gap:10px"><i style="width:8px;height:8px;border-radius:50%;background:{dot};margin-top:6px;flex:0 0 auto"></i><div><b style="font-size:13.5px">{t}</b><div class="sub" style="margin-top:2px">{s}</div></div></div></div><div style="text-align:right;margin-top:6px;font-size:12.5px;font-weight:800;color:{c}">{cta} →</div></div>'
# V1W command home wealth
Z.append(phone("V1W · COMMAND HOME · WEALTH",pad(head("w")+jag()+idx3()+f'''
<div style="background:var(--lime);color:#fff;border-radius:18px;padding:14px 16px;margin-top:10px"><div class="row" style="font-size:11.5px;opacity:.8"><span>Net worth · stocks, funds, bank sync</span><span>{ic("eye",14,"#fff")}</span></div><div class="num" style="font-size:28px;margin:4px 0 2px">₹14,82,450.00</div><div class="row" style="font-size:12px"><span class="num" style="color:#6EE7B7">▲ ₹18,420 (1.26%) today</span><span style="opacity:.8">As of 10:42 AM</span></div>
<div style="margin-top:10px;padding-top:10px;border-top:1px solid rgba(255,255,255,.18);display:flex;justify-content:space-between;font-size:12px"><span>UPI trading block · HDFC ••4821</span><b class="num">₹2,50,000</b></div></div>
<div class="row" style="margin:12px 0 0"><b style="font-size:14px">Actions and deadlines</b><span class="bdg b-t0">2</span></div>
{task("var(--spark)","MTF pledge pending: 50 HAL","Authorise your CDSL pledge by 7:00 PM to keep the funded position.","Authorise pledge")}
{task("var(--dn)","Expiry tomorrow: NIFTY 24500 CE short","Extra 2% loss margin applies from 9:15 AM. Review or roll.","Review margin",'var(--dn)')}
'''),"home"))
# V1T command home trader
def trow(s,ex,b,ltp,ch,k): return f'<div style="display:grid;grid-template-columns:1fr auto auto;gap:8px;align-items:center;height:42px;border-bottom:1px solid var(--line);font-size:12.5px"><div><b>{s}</b> {B(ex)} {b}</div><span class="num" style="font-size:12.5px">{ltp}</span><span class="num {k}" style="font-size:12px;min-width:58px;text-align:right">{ch}</span></div>'
Z.append(phone("V1T · COMMAND HOME · TRADER",pad(head("t")+f'''
<div style="display:flex;gap:8px;margin-bottom:8px">{''.join(f'<div style="flex:1;background:#fff;border:1px solid var(--line);border-radius:8px;padding:6px 8px"><div class="sub" style="font-size:10.5px;font-weight:700">{n}</div><div class="num" style="font-size:12px">{v}</div></div>' for n,v in [("NIFTY","24,482.65 ▲"),("BANKNIFTY","52,310.40 ▲"),("VIX","13.82 ▼")])}</div>
<div class="row" style="font-size:12px;margin:4px 0"><b>Margin used</b><span class="num">₹3.42L of ₹4.00L · 85%</span></div>{hbar(85,"var(--spark)",6)}<div class="sub" style="margin-top:4px">Above 85% you risk a peak-margin penalty.</div>
<div class="row" style="margin:10px 0 2px"><b style="font-size:13px">Watchlist · Momentum</b><span class="sub">14 rows</span></div>
{trow("TCS","NSE",B("T+0","t0"),"3,412.30","+1.22%","up")}{trow("HAL","NSE",B("MTF 4x","mtf"),"4,812.10","+2.04%","up")}{trow("IDEA","NSE",B("ASM-I","asm"),"13.85","-0.72%","dn")}{trow("RELIANCE","NSE","","1,248.00","-0.31%","dn")}{trow("HDFCBANK","NSE",B("T+0","t0"),"1,544.20","+0.62%","up")}{trow("ZOMATO","BSE",B("STALE 4s","stale"),"212.45","+0.18%","up")}{trow("NIFTY 24500 CE","NFO",B("LOT 65"),"142.65","+6.1%","up")}{trow("BANKNIFTY FUT","NFO","","52,388.00","+0.33%","up")}
'''+'<div style="position:absolute;left:12px;right:12px;bottom:92px;background:var(--lime);color:#fff;border-radius:12px;padding:10px 12px;display:flex;justify-content:space-between;align-items:center;font-size:12.5px"><span>Open positions 3 · MTM <b class="num" style="color:#6EE7B7">+₹14,280.50</b></span><span style="background:#fff;color:var(--dn);border-radius:8px;padding:6px 10px;font-weight:800">Exit all</span></div>'),"home"))
# V3F feed failover
Z.append(phone("V3F · STOCK DETAIL · FEED FAILOVER",pad(hdr("TCS",ic("star",18))+f'''
<div style="background:var(--warnBg);color:var(--warn);border-radius:12px;padding:10px 12px;display:flex;gap:10px;align-items:center;font-size:12.5px"><span>{ic("alert",16)}</span><div style="flex:1"><b>NSE quote delayed 4s.</b> Showing BSE live.</div><b style="color:var(--brandInk)">Use NSE</b></div>
<div class="row" style="margin-top:12px"><div style="display:flex;gap:10px;align-items:center">{logo("TC","#2F6FE0",40)}<div><b style="font-size:17px">TCS</b> {B("BSE")} {B("T+0","t0")}<div class="sub">Tata Consultancy Services</div></div></div></div>
<div style="display:flex;gap:8px;margin-top:12px"><div style="flex:1;border:1px solid var(--line);border-radius:12px;padding:10px;background:#fff;opacity:.6"><div class="sub">NSE {B("STALE 4s","stale")}</div><div class="num" style="font-size:20px">₹3,412.30</div></div><div style="flex:1;border:2px solid var(--lime);border-radius:12px;padding:10px;background:#fff"><div class="sub">BSE · live</div><div class="num" style="font-size:20px">₹3,411.95</div></div></div>
<div class="num up" style="font-size:13px;margin-top:8px">▲ +41.10 (+1.22%) · BSE tick &lt;1s</div>
<div style="margin:8px -4px 0">{chart(series(40,5,1.6),330,100)}</div>
{card(f'<div class="row" style="font-size:12.5px"><span class="sub">Allowed band today</span><b class="num">₹3,071.10 – ₹3,753.50</b></div>',"padding:10px 14px;margin-top:8px")}
'''+bottom('<div style="display:flex;gap:12px"><div class="btn" style="flex:1;background:var(--dn)">Sell</div><div class="btn" style="flex:2;background:var(--up)">Buy on BSE</div></div>'))))
# V4M order pad MTF
def mrow(l,v,b=False): return f'<div class="row" style="padding:5px 0;font-size:12.5px"><span class="sub" style="font-size:12.5px">{l}</span><span class="num" style="font-size:12.5px;{"font-weight:700" if b else ""}">{v}</span></div>'
Z.append(phone("V4M · ADAPTIVE ORDER PAD · MTF",pad(f'''
<div class="row" style="height:46px"><span>{ic("back")}</span><b>Buy TCS</b><span class="sub">Depth · Chart</span></div>
<div class="row" style="font-size:12px"><span class="num">NSE ₹3,412.30 ●</span>{B("T+0 ELIGIBLE","t0")}</div>
<div class="seg" style="margin:10px 0 8px;font-size:12px"><span>Delivery 1x</span><span class="on">MTF 4x</span><span>Intraday 5x</span></div>
<div style="display:flex;gap:6px;margin-bottom:8px">{chip("Limit",True)}{chip("Market ±1%")}{chip("SL-L")}{chip("GTT")}</div>
<div style="display:flex;gap:8px"><div class="field" style="flex:1;margin:0"><small>Quantity</small><b class="num" style="font-size:16px">100</b></div><div class="field" style="flex:1;margin:0"><small>Limit · tick ₹0.05</small><b class="num" style="font-size:16px">₹3,412.00</b></div></div>
<div class="row" style="margin:10px 0 6px;font-size:13px"><b>Stop-loss and target (OCO)</b><span style="width:38px;height:22px;border-radius:99px;background:var(--lime);position:relative;display:block"><i style="position:absolute;top:3px;right:3px;width:16px;height:16px;border-radius:50%;background:#fff"></i></span></div>
{card('<div class="lbl" style="margin-bottom:4px">MTF 4x funding</div>'+mrow("Order value","₹3,41,200.00")+mrow("Your cash, 25% via UPI block","₹85,300.00",True)+mrow("Crestline funded, 75%","₹2,55,900.00")+mrow("Interest from T+2, 0.049%/day","₹125.39/day")+mrow("Charges (est.)","₹384.12")+mrow("Available UPI block and cash","₹2,50,000 · OK"),"padding:10px 14px")}
<div style="background:var(--signalSoft);color:var(--signal);border-radius:12px;padding:8px 12px;font-size:12px;margin-top:8px;font-weight:600">Authorise the CDSL pledge between 4 PM and 7 PM today.</div>
'''+bottom('<div style="height:54px;border-radius:16px;background:var(--lime);display:flex;align-items:center;padding:5px;color:#fff"><div style="width:44px;height:44px;border-radius:12px;background:#fff;display:grid;place-items:center;color:var(--ink)">›</div><div style="flex:1;text-align:center;font-weight:800;font-size:14px;margin-right:44px">Swipe to buy · ₹85,300 cash</div></div>'))))
# V4L surveillance lock
Z.append(phone("V4L · ORDER PAD · SURVEILLANCE LOCK",pad(f'''
<div class="row" style="height:46px"><span>{ic("back")}</span><b>Buy IDEA</b><span class="num sub">₹13.85</span></div>
<div style="display:flex;gap:6px">{B("NSE")}{B("ASM-I","asm")}{B("T2T-BE","asm")}</div>
<div class="seg" style="margin:12px 0 8px;font-size:12px"><span class="on">Delivery 1x</span><span style="opacity:.45">MTF ✕</span><span style="opacity:.45">Intraday ✕</span></div>
<div style="background:var(--warnBg);border-radius:14px;padding:12px 14px;color:var(--warn);font-size:12.5px;line-height:1.45"><b>Why some options are off.</b> The exchange has moved this stock to trade-to-trade and added surveillance. Every trade must settle by delivery, so intraday and MTF are not allowed.</div>
<div style="display:flex;gap:6px;margin:12px 0 8px">{chip("Limit",True)}<span class="chip" style="opacity:.45">Market ✕</span></div>
{field("Quantity","1,000")}{field("Limit price","₹13.85")}
{card(mrow("Order value","₹13,850.00")+mrow("Full payment needed","₹13,850.00",True)+mrow("Charges (est.)","₹18.40"),"padding:8px 14px")}
'''+bottom(btn("Review delivery order")))))
# SR10 reconciling
Z.append(phone("SR10 · ORDER RECONCILING",pad(f'''
<div style="text-align:center;margin-top:44px"><div style="width:76px;height:76px;border-radius:50%;background:var(--warnBg);display:grid;place-items:center;margin:0 auto;color:var(--warn)">{ic("refresh",34)}</div>
<div class="h1" style="font-size:24px;margin-top:18px">Checking with the exchange</div>
<p class="sub" style="font-size:14px;margin:8px 18px 0;line-height:1.5">Your connection dropped while we confirmed this order with NSE. <b style="color:var(--ink)">Do not place it again.</b> We are checking its status every 2 seconds.</p></div>
{card(mrow("Order","Buy 100 TCS @ ₹3,412.00")+mrow("Request sent","10:42:07.118")+mrow("Reference","CR-7F3A…91C2")+mrow("Last check","2 seconds ago"),"margin-top:20px;padding:8px 14px")}
<div style="margin-top:14px;display:flex;gap:10px;align-items:center;font-size:12.5px" class="sub">{ic("lock",15)} Buy is locked for this order until we know the result.</div>
'''+bottom(btn("Go to orders","ghost")))))
# C6R rejection analyzer
Z.append(phone("C6R · REJECTION ANALYZER",pad(hdr("Order not placed")+f'''
<div style="background:var(--dnBg);border-radius:14px;padding:12px 14px;color:var(--dn)"><b style="font-size:14px">Not enough margin</b><div style="font-size:12.5px;margin-top:4px;line-height:1.4">You need ₹42,000 more for 100 TCS at ₹3,412.00 (MTF). You were not charged.</div></div>
<div class="lbl" style="margin:16px 0 6px">Fix it in one tap</div>
{card(f'<div class="row"><div><b style="font-size:14px">Block ₹42,000 via UPI</b><div class="sub">From HDFC ••4821 · money stays in your bank</div></div><span class="mut">›</span></div>',"padding:12px 14px")}
<div style="height:8px"></div>{card(f'<div class="row"><div><b style="font-size:14px">Switch to Delivery for 25 shares</b><div class="sub">Fits your available ₹85,300</div></div><span class="mut">›</span></div>',"padding:12px 14px")}
<div style="height:8px"></div>{card(f'<div class="row"><div><b style="font-size:14px">Pledge holdings</b><div class="sub">Up to ₹1.2L collateral after haircut</div></div><span class="mut">›</span></div>',"padding:12px 14px")}
<div class="sub" style="margin-top:12px">Exchange code 16388 · margin shortfall</div>
''')))
# MTF07 pledge
Z.append(phone("MTF07 · CDSL PLEDGE",pad(hdr("Authorise pledge")+f'''
<div style="background:var(--signalSoft);color:var(--signal);border-radius:14px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center"><div><b>Due by 7:00 PM today</b><div style="font-size:12px;margin-top:2px">Window opened at 4:00 PM</div></div><b class="num" style="font-size:20px">02:14:36</b></div>
{card(mrow("Stock","HAL · 50 shares")+mrow("Funded by Crestline","₹1,42,000.00")+mrow("Pledge type","MTF margin pledge"),"margin-top:12px;padding:8px 14px")}
<div class="lbl" style="margin:16px 0 8px">Enter CDSL TPIN</div>
<div class="otp">{''.join('<div>•</div>' for _ in range(4))}<div></div><div></div></div>
<div class="sub" style="margin-top:10px">An OTP from CDSL follows. TPIN authorisation stays valid until the end of today.</div>
<div style="margin-top:14px;font-size:12.5px;color:var(--ink2);line-height:1.45">If you miss 7:00 PM and have enough cash, the position converts to delivery. Otherwise it is marked unpaid and may be sold next day.</div>
'''+bottom(btn("Continue to CDSL")))))
# TR03 option chain
def oc(oi,d,ltp,k,pltp,pd,poi,atm=False): return f'<div style="display:grid;grid-template-columns:1.1fr .6fr .8fr .9fr .8fr .6fr 1.1fr;gap:2px;padding:7px 0;border-bottom:1px solid var(--line);font-size:11px;{"background:var(--signalSoft)" if atm else ""}" class="num"><span>{oi}</span><span class="sub" style="font-size:11px">{d}</span><b>{ltp}</b><b style="text-align:center;font-family:Inter">{k}</b><b>{pltp}</b><span class="sub" style="font-size:11px">{pd}</span><span style="text-align:right">{poi}</span></div>'
Z.append(phone("TR03 · OPTION CHAIN 2026",pad(hdr("NIFTY 50",ic("layers",18))+f'''
<div class="row" style="font-size:12px"><span class="num">24,482.65 ▲ 0.46%</span><span class="sub">IV 13.4 · IVP 42%</span></div>
<div style="display:flex;gap:6px;margin:8px 0">{chip("3 Nov · Tue",True)}{chip("10 Nov")}{chip("24 Nov · monthly")}</div>
<div class="row sub" style="font-size:11.5px;margin-bottom:4px"><span>Lot size {B("65")}</span><span>OI shown as future equivalent</span></div>
<div style="display:grid;grid-template-columns:1.1fr .6fr .8fr .9fr .8fr .6fr 1.1fr;gap:2px;font-size:10px;font-weight:800;color:var(--ink3);padding-bottom:4px;border-bottom:1px solid var(--line)"><span>OI</span><span>Δ</span><span>CALL</span><span style="text-align:center">STRIKE</span><span>PUT</span><span>Δ</span><span style="text-align:right">OI</span></div>
{oc("22.1L",".58","208.15","24,400","98.40","-.42","41.8L")}{oc("31.0L",".52","172.90","24,450","118.25","-.48","52.4L")}{oc("64.2L",".46","142.65","24,500","141.80","-.54","58.9L",True)}{oc("48.9L",".39","114.20","24,550","169.45","-.61","29.2L")}{oc("72.5L",".32","89.75","24,600","201.10","-.68","19.4L")}
<div style="background:var(--lime);color:#fff;border-radius:14px;padding:12px 14px;margin-top:10px;font-size:12px"><b style="font-size:13px">Basket · short 24500 straddle</b><div class="row" style="margin-top:6px"><span>Margin</span><b class="num">₹1,48,200</b></div><div class="row"><span>On expiry day, +2% loss margin</span><b class="num" style="color:#FDBA74">₹1,80,020</b></div><div class="row"><span>Breakevens</span><b class="num">24,216 – 24,784</b></div></div>
'''+bottom('<div style="display:flex;gap:10px"><div class="btn ghost" style="flex:1">Payoff</div><div class="btn" style="flex:1.4">Place 2 legs</div></div>'))))
# TR06 kill switch
Z.append(phone("TR06 · KILL SWITCH",pad(hdr("Trading limits")+f'''
<div style="background:var(--dnBg);border-radius:18px;padding:16px;color:var(--dn)"><div class="row"><b style="font-size:16px">F&amp;O and intraday paused</b>{ic("lock",20)}</div><div style="font-size:12.5px;margin-top:6px;line-height:1.45">You reached today's loss limit of ₹10,000 at 11:18 AM. New F&amp;O and intraday orders stay off until tomorrow.</div><div class="num" style="font-size:22px;margin-top:10px">Resumes in 17:42:10</div></div>
<div class="lbl" style="margin:16px 0 6px">Still allowed</div>
{card(''.join(f'<div class="row" style="padding:8px 0;{"border-top:1px solid var(--line)" if i else ""};font-size:13.5px"><span>{t}</span><span class="up">{ic("check",16)}</span></div>' for i,t in enumerate(["Exit open positions","Delivery buys and SIPs","Mutual funds, bonds, gold"])),"padding:4px 14px")}
<div class="lbl" style="margin:16px 0 6px">Your limits</div>
{card(mrow("Daily max loss","₹10,000")+mrow("Max orders per day","40")+mrow("Cool-off after a limit hit","Until next session"),"padding:6px 14px")}
<div class="sub" style="margin-top:10px">You can lower a limit any time. Raising one takes effect tomorrow.</div>
''')))
# TR07 physical delivery
Z.append(phone("TR07 · PHYSICAL DELIVERY WARNING",pad(hdr("Expiry week")+f'''
<div style="background:var(--warnBg);color:var(--warn);border-radius:16px;padding:14px"><b style="font-size:14.5px">TCS 3400 CE is in the money</b><div style="font-size:12.5px;margin-top:6px;line-height:1.45">Stock options settle by delivery. If you hold to expiry you must take 175 shares, worth about ₹5.97L.</div></div>
<div class="lbl" style="margin:16px 0 8px">Margin rises each day to expiry</div>
{card(bars([20,35,55,80,100],["T-4","T-3","T-2","T-1","Expiry"],96,"var(--signal)")+'<div class="sub" style="margin-top:8px">Today you need 55% of contract value as margin.</div>',"padding:14px")}
<div class="lbl" style="margin:16px 0 6px">What you can do</div>
{card(f'<div class="row"><b style="font-size:14px">Exit the position</b><span class="mut">›</span></div>',"padding:12px 14px")}<div style="height:8px"></div>{card(f'<div class="row"><b style="font-size:14px">Roll to next month</b><span class="mut">›</span></div>',"padding:12px 14px")}<div style="height:8px"></div>{card(f'<div class="row"><div><b style="font-size:14px">Keep and add funds</b><div class="sub">Needs ₹5.97L by expiry</div></div><span class="mut">›</span></div>',"padding:12px 14px")}
''')))
# P02 diagnostics
Z.append(phone("P02 · PORTFOLIO DIAGNOSTICS",pad(hdr("Diagnostics",ic("refresh",18))+f'''
<div class="sub" style="margin-bottom:8px">Diagnostic maths only, not investment advice. Synced 2 min ago.</div>
{card(f'<div class="lbl">True return, 3 years</div><div style="display:flex;gap:14px;margin-top:8px">{stat("Your XIRR","14.20%")}{stat("Nifty 50 TRI","15.85%")}</div><div style="margin-top:8px;font-size:12.5px;color:var(--signal);font-weight:600">You trailed the index by 1.65% a year.</div>',"padding:12px 14px")}
<div style="height:10px"></div>{card(f'<div class="lbl">Concentration</div><div class="row" style="margin-top:8px;font-size:13px"><b>HDFC Bank</b><b class="num dn">19.4%</b></div><div style="margin-top:6px">{hbar(97,"var(--dn)",6)}</div><div class="sub" style="margin-top:6px">9.8% direct, 9.6% inside three funds you hold.</div>',"padding:12px 14px")}
<div style="height:10px"></div>{card(f'<div class="lbl">Tax this year</div>'+mrow("Long-term gains","₹94,200")+mrow("Short-term gains","₹42,000")+mrow("Losses you could harvest","-₹18,500"),"padding:10px 14px")}
<div style="height:10px"></div>{card(f'<div class="lbl">Overnight margin mix</div><div class="row" style="margin-top:6px;font-size:13px"><span>Cash 58% · collateral 42%</span><span class="up">{ic("check",16)}</span></div><div class="sub">At least half must be cash.</div>',"padding:10px 14px")}
'''),"port"))
# P15 FIFO
def lot(d,q,c,days,tag_,k): return f'<div class="row" style="padding:9px 0;border-top:1px solid var(--line);font-size:12.5px"><div><b class="num" style="font-size:12.5px">{d}</b><div class="sub">{q} sh @ ₹{c} · {days}</div></div><span class="bdg b-{k}">{tag_}</span></div>'
Z.append(phone("P15 · FIFO TAX LOTS",pad(hdr("TCS · tax lots")+f'''
<div class="sub" style="margin-bottom:8px">Sold first: the oldest lot (first in, first out).</div>
{card(lot("12 Jan 2018","10","2,540.00","grandfathered at ₹2,818","LTCG 12.5%","mtf")+lot("05 Mar 2024","20","3,960.00","2y 7m","LTCG 12.5%","mtf")+lot("02 Sep 2026","15","3,520.00","58 days","STCG 20%","t0")+lot("18 Oct 2026","5","3,610.00","12 days","STCL","ill"),"padding:2px 14px")}
<div class="lbl" style="margin:14px 0 6px">If you sell 30 shares today</div>
{card(mrow("Long-term gain","₹10,986")+mrow("Covered by ₹1.25L exemption","₹10,986")+mrow("Short-term loss used","—")+mrow("Estimated tax","₹0.00",True),"padding:8px 14px")}
<div class="sub" style="margin-top:10px">An estimate from your trades. Check with your tax adviser before filing.</div>
''')))
# P09 discrepant holding
Z.append(phone("P09 · FIX BUY AVERAGE",pad(hdr("Missing buy price")+f'''
<div style="background:var(--warnBg);color:var(--warn);border-radius:14px;padding:12px 14px;font-size:12.5px;line-height:1.45"><b>40 Infosys shares have no buy price.</b> They came in by an off-market transfer, so profit and tax cannot be worked out yet.</div>
{card(mrow("Received","12 Aug 2026 · gift")+mrow("Quantity","40")+mrow("Current value","₹76,188.00"),"margin-top:12px;padding:8px 14px")}
<div class="lbl" style="margin:16px 0 8px">Add the original purchase</div>
{field("Acquisition date","14 Jun 2021")}{field("Buy price per share","₹1,412.50")}
<div class="sub">For a gift, use the giver's original date and price. Keep the transfer statement for your records.</div>
'''+bottom(btn("Save buy price")))))
# MF04 fund order with cut-off
Z.append(phone("MF04 · FUND ORDER · CUT-OFF",pad(hdr("Parag Parikh Flexi Cap")+f'''
<div style="display:flex;gap:6px;flex-wrap:wrap">{B("FLEXI CAP")}{B("VERY HIGH RISK","ill")}{B("HELD IN DEMAT","mtf")}</div>
<div class="sub" style="margin-top:6px">NAV ₹84.6210 · 29 Oct · expense ratio 0.63%</div>
<div class="seg" style="margin:12px 0;font-size:12px"><span class="on">One-time</span><span>SIP</span><span>SWP / STP</span></div>
<div style="background:var(--signalSoft);border-radius:14px;padding:12px 14px;color:var(--signal)"><div class="row"><b style="font-size:13px">Today's NAV if paid in</b><b class="num" style="font-size:18px">01:18:42</b></div><div style="font-size:12px;margin-top:4px;line-height:1.4">Money must reach the clearing house before 3:00 PM. Net banking above ₹2L can take up to 2 hours.</div></div>
<div class="field" style="margin-top:12px"><small>Amount</small><b class="num" style="font-size:22px">₹25,000</b></div>
<div style="display:flex;gap:6px">{chip("+₹5,000")}{chip("+₹10,000")}{chip("+₹50,000")}</div>
{card(mrow("Stamp duty, 0.005%","₹1.25")+mrow("Net invested","₹24,998.75",True)+mrow("Exit load","2% within 365 days"),"margin-top:10px;padding:6px 14px")}
'''+bottom(btn("Pay ₹25,000 via UPI")))))
# FI02 bond checkout
Z.append(phone("FI02 · BOND CHECKOUT",pad(hdr("REC 7.85% 2029")+f'''
<div style="display:flex;gap:6px;flex-wrap:wrap">{B("PSU · SECURED")}{B("AAA / STABLE","mtf")}{B("T+1")}</div>
<div class="sub" style="margin-top:6px">ISIN INE020B08427 · listed NSE and BSE</div>
{card(mrow("Yield to maturity","7.78% a year",True)+mrow("Coupon","7.85%, paid 15 Mar")+mrow("Maturity","15 Mar 2029")+mrow("Call option","None"),"margin-top:12px;padding:6px 14px")}
<div class="lbl" style="margin:14px 0 6px">10 units</div>
{card(mrow("Clean price","₹1,00,184.00")+mrow("Accrued interest, 229 days","₹4,925.07")+mrow("Stamp duty and fees","₹10.50")+'<div style="height:1px;background:var(--line);margin:4px 0"></div>'+mrow("Total payable","₹1,05,119.57",True),"padding:6px 14px")}
<div class="sub" style="margin-top:10px;line-height:1.45">Ratings are not guarantees. Selling before maturity depends on demand and rates. Interest is taxed at your slab.</div>
'''+bottom(btn("Pay ₹1,05,119.57 via UPI")))))
# FD01 UPI block
Z.append(phone("FD01 · UPI TRADING BLOCK",pad(hdr("UPI trading block")+f'''
<div style="background:var(--limeD);color:var(--brandInk);border-radius:16px;padding:14px;font-size:13px;line-height:1.45"><b>Trade without moving money.</b> We block an amount in your bank through UPI. It keeps earning savings interest until a trade settles.</div>
{card(f'<div class="row"><div style="display:flex;gap:10px;align-items:center"><span class="ico" style="width:38px;height:38px">{ic("bank",17)}</span><div><b>HDFC Bank ••4821</b><div class="sub">Primary · verified</div></div></div>{pill("Active","up")}</div>',"margin-top:12px;padding:12px 14px")}
<div class="field" style="margin-top:12px"><small>Block limit</small><b class="num" style="font-size:22px">₹2,50,000</b></div>
{card(mrow("Used today","₹85,300.00")+mrow("Available to trade","₹1,64,700.00",True)+mrow("Release now","₹1,64,700.00")+mrow("Mandate valid till","29 Oct 2027"),"padding:6px 14px")}
<div class="sub" style="margin-top:10px">Only your registered bank accounts can be used.</div>
'''+bottom(btn("Update block")))))
# FD03 withdrawable
Z.append(phone("FD03 · WHAT YOU CAN WITHDRAW",pad(hdr("Withdraw")+f'''
{card(f'<div class="sub">You can withdraw now</div><div class="num" style="font-size:28px;margin:2px 0 8px">₹44,200.00</div>{hbar(46,"var(--up)",8)}',"padding:14px")}
<div class="lbl" style="margin:14px 0 6px">Why not more</div>
{card(mrow("Cleared balance","₹44,200.00")+mrow("Sale money settling","₹27,456.00")+mrow("Today's intraday profit","₹1,284.00")+mrow("Blocked for open orders","₹40,920.00"),"padding:6px 14px")}
<div class="sub" style="margin-top:8px;line-height:1.45">Sale money and intraday profit become withdrawable after settlement. The exact date shows on each line in your ledger.</div>
{card(f'<div class="row"><span class="sub">Withdrawal status</span><b style="font-size:13px">Tracked live</b></div>',"margin-top:12px;padding:10px 14px")}
'''+bottom(btn("Withdraw ₹44,200")))))
# A11 activation pipeline
def st(t,s,state): 
    c={"done":("var(--up)",ic("check",13,"#fff")),"wait":("var(--spark)",ic("clock",13,"#fff")),"open":("var(--lime)",ic("lockopen",13,"#fff"))}[state]
    return f'<div style="display:flex;gap:12px;padding:10px 0;border-top:1px solid var(--line)"><span style="width:24px;height:24px;border-radius:50%;background:{c[0]};display:grid;place-items:center;flex:0 0 auto">{c[1]}</span><div><b style="font-size:14px">{t}</b><div class="sub">{s}</div></div></div>'
Z.append(phone("A11 · ACTIVATION PIPELINE",pad(f'''
<div class="h1" style="font-size:24px;margin-top:20px">Almost there, Aarav</div>
<div class="sub" style="font-size:14px;margin:6px 0 14px">We show each step as it happens. No guesses.</div>
{card(st("Application e-signed","Ref CR-88219 · 10:12 AM","done")+st("KRA validated","Fast-tracked from your existing record","done")+st("Exchange and depository activation","NSE, BSE and CDSL · usually 2 to 4 working hours","wait")+st("Unlocked now","Watchlists, screener, practice mode","open"),"padding:2px 14px")}
<div class="sub" style="margin-top:12px">We will notify you the moment trading opens for your account.</div>
'''+bottom(btn("Try practice mode"),btn("Explore markets","ghost")))))
# A13 KRA
Z.append(phone("A13 · KRA FAST-TRACK",pad(top("Identity","4 of 9")+f'''
<div style="margin:0 0 14px">{dots(4,9)}</div>
<div style="background:var(--upBg);border-radius:18px;padding:16px;color:var(--up)"><div class="row"><b style="font-size:16px">KYC already verified</b>{ic("shield",22)}</div><div style="font-size:13px;margin-top:6px;line-height:1.45;color:var(--ink2)">We found your record with the KYC registry. You can skip the Aadhaar and document upload steps.</div></div>
{card(mrow("Name","AARAV MEHTA")+mrow("PAN","ABCPM1234K")+mrow("Status","KRA validated")+mrow("Address","Andheri East, Mumbai"),"margin-top:12px;padding:6px 14px")}
<div class="sub" style="margin-top:10px">Something wrong? You can update it through the registry after opening.</div>
'''+bottom(btn("Confirm and continue")))))
# A19 nomination
def nom(n,r,p): return f'<div class="row" style="padding:11px 0;border-top:1px solid var(--line)"><div><b style="font-size:14px">{n}</b><div class="sub">{r}</div></div><b class="num">{p}</b></div>'
Z.append(phone("A19 · NOMINATION MANAGER",pad(top("Nominees","8 of 9")+f'''
<div style="margin:0 0 12px">{dots(8,9)}</div>
<div class="sub" style="font-size:13.5px">Add up to 10 people and split your holdings between them.</div>
{card(nom("Meera Mehta","Mother","50%")+nom("Nisha Mehta","Spouse","30%")+nom("Rohan Mehta","Son · minor · guardian Nisha","20%"),"margin-top:10px;padding:2px 14px")}
<div class="row" style="margin-top:8px;font-size:13px"><b>Total</b><b class="num up">100%</b></div>
<div style="margin-top:12px;font-weight:800;font-size:14px;color:var(--brandInk)">+ Add nominee</div>
<div class="sub" style="margin-top:12px">Prefer not to nominate? You can opt out with a video or OTP check.</div>
'''+bottom(btn("Save nominees"),btn("Opt out","ghost")))))
# W6T trader watchlist
Z.append(phone("W6T · WATCHLIST · TRADER DENSITY",pad(f'''
<div class="row" style="height:48px"><b style="font-family:Manrope;font-size:20px">Watchlist</b>{mode("t")}</div>
<div style="display:flex;gap:6px;margin-bottom:6px">{chip("F&O",True)}{chip("Momentum")}{chip("Banks")}</div>
<div style="display:grid;grid-template-columns:1fr auto auto;gap:8px;font-size:10px;font-weight:800;color:var(--ink3);padding:4px 0;border-bottom:1px solid var(--line)"><span>SYMBOL</span><span>LTP</span><span style="min-width:58px;text-align:right">CHG</span></div>
{trow("TCS","NSE",B("T+0","t0"),"3,412.30","+1.22%","up")}{trow("HAL","NSE",B("MTF 4x","mtf"),"4,812.10","+2.04%","up")}{trow("IDEA","NSE",B("ASM-I","asm"),"13.85","-0.72%","dn")}{trow("RELIANCE","NSE","","1,248.00","-0.31%","dn")}{trow("HDFCBANK","NSE",B("T+0","t0"),"1,544.20","+0.62%","up")}{trow("ZOMATO","BSE",B("STALE 4s","stale"),"212.45","+0.18%","up")}{trow("INFY","NSE","","1,904.70","+1.97%","up")}{trow("SBIN","NSE",B("MTF 4x","mtf"),"812.15","+2.64%","up")}{trow("TATAMOTORS","NSE","","1,018.40","+3.82%","up")}{trow("24600 CE","NFO",B("ILLIQUID","ill"),"3.10","-12.4%","dn")}{trow("ITC","NSE","","468.55","-1.12%","dn")}{trow("AXISBANK","NSE","","1,121.90","+1.10%","up")}
'''),"watch"))
# SR01 service status
Z.append(phone("SR01 · LIVE SERVICE STATUS",pad(hdr("Service status")+f'''
<div style="background:var(--warnBg);color:var(--warn);border-radius:14px;padding:12px 14px;font-size:12.5px"><b>NSE price feed is slow.</b> BSE prices are live. Orders on both exchanges work.</div>
{card(''.join(f'<div class="row" style="padding:10px 0;{"border-top:1px solid var(--line)" if i else ""};font-size:13.5px"><span>{t}</span><span style="display:flex;gap:6px;align-items:center;font-weight:700;font-size:12.5px;color:{c}"><i style="width:8px;height:8px;border-radius:50%;background:{c}"></i>{s}</span></div>' for i,(t,s,c) in enumerate([("NSE prices","Delayed 4s","var(--warn)"),("BSE prices","Live","var(--up)"),("Order placement","Working","var(--up)"),("UPI payments","Working","var(--up)"),("CDSL pledge","Working","var(--up)"),("Withdrawals","Working","var(--up)")])),"margin-top:12px;padding:4px 14px")}
<div class="lbl" style="margin:14px 0 6px">If prices freeze completely</div>
<div class="sub" style="line-height:1.45">Close-only mode keeps exits open while new orders pause. You will see a banner on every trading screen.</div>
''')))
sheet("flow-v4-new.html","Crestline v4 · new screens",Z)
