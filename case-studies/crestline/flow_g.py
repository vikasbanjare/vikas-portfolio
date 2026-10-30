from gen import *
G=[]
def leg(a,c,n,side,q,p,t): return f'<div class="row" style="padding:13px 0;border-top:1px solid var(--line)"><div style="display:flex;gap:12px;align-items:center">{logo(a,c,38)}<div><b style="font-size:14.5px">{n}</b><div class="sub">{t} · {q} qty</div></div></div><div style="text-align:right"><span class="pill" style="background:{"var(--upBg)" if side=="Buy" else "var(--dnBg)"};color:{"var(--up)" if side=="Buy" else "var(--dn)"}">{side}</span><div class="num" style="font-size:13px;margin-top:4px">{p}</div></div></div>'
# G1 basket
body=pad(hdr("Basket",ic("plus",20))+f'''
<div class="row" style="margin:2px 0 6px"><div><b style="font-size:20px;letter-spacing:-.02em">Diwali picks</b><div class="sub">3 orders · saved</div></div>{pill("Ready","up")}</div>
{leg("TC","#2F6FE0","TCS","Buy",12,"₹3,410.00","Limit")}{leg("IN","#1B4F9C","Infosys","Buy",15,"Market","Market")}{leg("RE","#C9A24B","Reliance","Sell",5,"₹1,252.00","Limit")}
{card(kv("Funds needed","₹69,742.00",True)+kv("Funds from sale","₹6,260.00",True)+'<div style="height:1px;background:var(--line)"></div>'+kv("You need to add","₹0.00",True),"padding:4px 18px;margin-top:12px")}
{note("All three orders go out together. If one is rejected, the others still run.")}
'''+bottom(btn("Place 3 orders","lime"),'<div style="text-align:center;font-weight:700;font-size:14px;color:var(--ink2)">Save changes</div>'))
G.append(phone("G1 · BASKET",body))
# G2 bracket
body=pad(hdr("Bracket order")+f'''
<div class="row"><div style="display:flex;gap:10px;align-items:center">{logo("TC","#2F6FE0",38)}<b>Buy TCS</b></div><b class="num">₹3,412.30</b></div>
<div class="seg" style="margin:12px 0"><span>Delivery</span><span class="on">Intraday</span></div>
{field("Entry price","₹3,412.00")}
<div style="display:flex;gap:10px">{field("Target","₹3,480.00").replace('class="field"','class="field" style="flex:1"')}{field("Stop-loss","₹3,385.00").replace('class="field"','class="field" style="flex:1"')}</div>
{card(f'<div class="row" style="font-size:13px"><b class="up num">Reward ₹816</b><b class="dn num">Risk ₹324</b></div><div style="display:flex;height:12px;border-radius:9px;overflow:hidden;margin:10px 0 8px"><i style="width:72%;background:var(--up)"></i><i style="width:28%;background:var(--dn)"></i></div><div class="sub">Reward to risk is <b class="num" style="color:var(--ink)">2.5 : 1</b> for 12 shares.</div>',"padding:16px")}
<div class="row" style="margin-top:14px;font-size:14px"><span><b>Trailing stop-loss</b><div class="sub">Moves up as the price rises</div></span><span style="width:46px;height:28px;border-radius:99px;background:#CBD2E2;position:relative;display:block"><i style="position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff"></i></span></div>
'''+bottom(btn("Review order","lime")))
G.append(phone("G2 · BRACKET ORDER",body))
# G3 margin calc
body=pad(hdr("Margin calculator")+f'''
<div class="seg" style="margin:4px 0 12px"><span>Equity</span><span class="on">Futures</span><span>Options</span></div>
{field("Contract","NIFTY 28 Nov FUT")}
<div style="display:flex;gap:10px">{field("Lots","2").replace('class="field"','class="field" style="flex:1"')}{field("Product","Normal").replace('class="field"','class="field" style="flex:1"')}</div>
{card(f'<div class="sub">Margin required</div><div class="num" style="font-size:30px;margin:2px 0 12px">₹1,98,400</div>'+kv("SPAN","₹1,41,200",True)+kv("Exposure","₹57,200",True)+'<div style="height:1px;background:var(--line)"></div>'+kv("Available","₹52,310",True)+kv("Shortfall","₹1,46,090",True),"padding:16px 18px")}
{note("Pledge your holdings to unlock extra margin without selling.","brand")}
'''+bottom(btn("Pledge holdings","lime")))
G.append(phone("G3 · MARGIN CALCULATOR",body))
# G4 strategy payoff
pay='<svg width="100%" height="150" viewBox="0 0 330 150" preserveAspectRatio="none" style="display:block"><line x1="0" y1="82" x2="330" y2="82" stroke="#C3CAD9" stroke-dasharray="4 4"/><path d="M0,118 L110,118 L220,34 L330,34 L330,82 L0,82Z" fill="var(--upBg)" opacity=".0"/><path d="M0,118 L110,118 L220,34 L330,34" fill="none" stroke="var(--lime)" stroke-width="3" stroke-linejoin="round"/><circle cx="148" cy="82" r="5" fill="#fff" stroke="var(--ink)" stroke-width="2"/><text x="148" y="106" text-anchor="middle" font-size="11" fill="var(--ink3)">Breakeven</text></svg>'
body=pad(hdr("Strategy",ic("share",20))+f'''
<div class="row"><div><b style="font-size:19px;letter-spacing:-.02em">Bull call spread</b><div class="sub">NIFTY · 28 Nov expiry</div></div>{pill("Limited risk","up")}</div>
{card(f'<div class="sub" style="margin-bottom:6px">Profit or loss at expiry</div>{pay}<div class="row sub" style="margin-top:4px"><span>24,000</span><span>24,300</span><span>24,600</span></div>',"margin-top:12px;padding:16px")}
<div style="display:flex;gap:10px;margin-top:12px"><div style="flex:1;background:var(--upBg);border-radius:18px;padding:14px"><div class="sub">Max profit</div><b class="num up" style="font-size:19px">₹6,750</b></div><div style="flex:1;background:var(--dnBg);border-radius:18px;padding:14px"><div class="sub">Max loss</div><b class="num dn" style="font-size:19px">₹3,750</b></div></div>
{sec("Legs")}
{card(kv("Buy 24,200 CE","₹182.50",True)+kv("Sell 24,500 CE","₹92.50",True)+kv("Margin needed","₹11,900",True),"padding:4px 18px")}
'''+bottom(btn("Place strategy","lime")))
G.append(phone("G4 · STRATEGY BUILDER",body))
# G5 risk calc
body=pad(hdr("Risk calculator")+f'''
<div class="sub" style="margin-bottom:10px">Decide how many shares to buy based on what you can afford to lose.</div>
{field("Capital for this trade","₹1,00,000")}
<div style="display:flex;gap:10px">{field("Risk per trade","1%").replace('class="field"','class="field" style="flex:1"')}{field("Entry price","₹3,412").replace('class="field"','class="field" style="flex:1"')}</div>
{field("Stop-loss price","₹3,385")}
{card(f'<div class="sub">You can buy</div><div class="num" style="font-size:34px;margin:2px 0 4px">37 shares</div><div class="sub">If the stop-loss hits you lose about <b class="num dn">₹999</b>, which is 1% of your capital.</div><div style="margin-top:12px">{hbar(63,"var(--lime)",10)}</div><div class="row sub" style="margin-top:6px"><span>Position ₹1,26,244</span><span>Margin used 63%</span></div>',"margin-top:6px;padding:18px")}
'''+bottom(btn("Use 37 shares","lime")))
G.append(phone("G5 · RISK CALCULATOR",body))
# G6 pro chart
body=pad(f'''
<div class="row" style="height:50px"><span>{ic("back")}</span><div style="text-align:center"><b>TCS</b><div class="num up" style="font-size:12px">₹3,412.30 +0.84%</div></div><span>{ic("share",20)}</span></div>
<div style="display:flex;gap:8px;overflow:hidden;margin-bottom:8px">{chip("5m")}{chip("15m",True)}{chip("1h")}{chip("1D")}{ichip("candle","Candles")}{ichip("sliders","Indicators")}</div>
<div style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:8px 6px;position:relative">{candles(34,330,230)}<div style="position:absolute;top:10px;left:12px;font-size:11px" class="mut num">EMA 20 · 3,396 &nbsp; Vol 18.2L</div></div>
<div style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:10px 12px;margin-top:10px"><div class="row" style="font-size:12px"><b>RSI 14</b><b class="num">61.4</b></div><div style="margin-top:6px">{chart(series(40,12,.4),320,54,BRAND,False)}</div></div>
<div style="display:flex;justify-content:space-between;margin-top:14px">{''.join(f'<div style="text-align:center"><div class="ico" style="width:48px;height:48px">{ic(i,20)}</div><div class="sub" style="margin-top:4px;font-size:11px">{t}</div></div>' for i,t in [("trend","Trend line"),("layers","Fib"),("tag","Note"),("alert","Alert"),("more","More")])}</div>
'''+bottom('<div style="display:flex;gap:12px"><div class="btn" style="flex:1;background:var(--dn)">Sell</div><div class="btn" style="flex:1;background:var(--up)">Buy</div></div>'))
G.append(phone("G6 · PRO CHART",body))
# G7 AMO
body=pad(hdr("Buy TCS")+f'''
{note("Markets are closed. This order will be placed when trading opens at 9:15 AM tomorrow.","warn")}
<div class="seg" style="margin:14px 0"><span class="on">After-market order</span><span>Place now</span></div>
{field("Quantity","12")}
{field("Limit price","₹3,410.00")}
{card(kv("Order value","₹40,920.00",True)+kv("Funds blocked now","₹40,920.00",True)+kv("Order goes out","Tomorrow, 9:15 AM"),"padding:4px 18px;margin-top:4px")}
<div class="sub" style="margin-top:10px">You can cancel any time before 9:15 AM.</div>
'''+bottom(btn("Schedule order","lime")))
G.append(phone("G7 · AFTER-MARKET ORDER",body))
# G8 trade book
def tr(t,n,s,q,p,k): return f'<div class="row" style="padding:13px 0;border-top:1px solid var(--line)"><div><b style="font-size:14.5px">{n}</b><div class="sub">{t} · {s} {q}</div></div><div style="text-align:right"><div class="num" style="font-size:14px">{p}</div>{pill("Filled",k)}</div></div>'
body=pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:26px">Trades</div><span style="display:flex;gap:10px"><span class="ico">{ic("filter",20)}</span><span class="ico">{ic("download",20)}</span></span></div>
{tabs(["Orders","Trades","GTT","Baskets"],1,22)}
<div style="display:flex;gap:8px;margin:12px 0 4px">{chip("Today",True)}{chip("7 days")}{chip("This month")}{chip("Custom")}</div>
{tr("11:42 AM","TCS","Buy",12,"₹3,410.00","up")}{tr("10:05 AM","Reliance","Sell",5,"₹1,252.00","dn")}{tr("9:31 AM","Infosys","Buy",15,"₹1,903.40","up")}{tr("Yesterday","Canara Bank","Buy",148,"₹110.14","up")}
{note("Download a contract note for any trade from the trade detail screen.")}
''')
G.append(phone("G8 · TRADE BOOK",body,"ord"))
sheet("flow-g-trading-tools.html","Crestline v2 · Advanced trading tools",G)
