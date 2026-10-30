from gen import *
H=[]
def tog(on=True): return f'<span style="width:46px;height:28px;border-radius:99px;background:{"var(--lime)" if on else "#CBD2E2"};position:relative;display:block;flex:0 0 auto"><i style="position:absolute;top:3px;{"right" if on else "left"}:3px;width:22px;height:22px;border-radius:50%;background:#fff"></i></span>'
def trow(t,s,on=True): return f'<div class="row" style="padding:14px 0;border-top:1px solid var(--line);gap:14px"><div><b style="font-size:15px">{t}</b><div class="sub" style="margin-top:2px">{s}</div></div>{tog(on)}</div>'
def lrow(i,t,s=""): return f'<div class="row" style="padding:14px 0;border-top:1px solid var(--line)"><div style="display:flex;gap:14px;align-items:center"><span class="ico" style="width:40px;height:40px">{ic(i,18)}</span><div><b style="font-size:15px">{t}</b>{("<div class=sub style=margin-top:2px>"+s+"</div>") if s else ""}</div></div><span class="mut">›</span></div>'
# H1 welcome
body=f'''<div style="position:absolute;inset:0;background:var(--ink);color:#fff;padding:60px 24px 30px;display:flex;flex-direction:column">
<div style="width:56px;height:56px;border-radius:18px;background:var(--spark);display:grid;place-items:center;color:var(--ink)">{ic("up",28)}</div>
<div style="margin-top:44px;font-size:40px;line-height:1.05;font-weight:800;letter-spacing:-.04em">Invest with<br>clarity.</div>
<div style="margin-top:14px;font-size:16px;line-height:1.5;opacity:.78;max-width:290px">Stocks, funds and IPOs in one calm place. No jargon, no clutter.</div>
<div style="display:flex;gap:10px;margin-top:34px">{''.join(f'<div style="flex:1;background:rgba(255,255,255,.08);border-radius:18px;padding:14px 12px"><div class="num" style="font-size:20px;color:var(--spark)">{a}</div><div style="font-size:12px;opacity:.75;margin-top:2px">{b}</div></div>' for a,b in [("₹0","Account opening"),("Direct","Mutual funds"),("5 min","To get started")])}</div>
<div style="margin-top:auto;display:grid;gap:10px"><div style="height:56px;border-radius:18px;background:var(--spark);color:var(--ink);display:grid;place-items:center;font-weight:800;font-size:16px">Open an account</div><div style="height:56px;border-radius:18px;border:1.5px solid rgba(255,255,255,.28);display:grid;place-items:center;font-weight:700;font-size:16px">I already have an account</div></div></div>'''
H.append(phone("H1 · WELCOME",body))
# H2 first trade checklist
def step(n,t,s,done,cur=False): return f'<div style="display:flex;gap:14px;padding:14px 0;border-top:1px solid var(--line);align-items:center"><span style="width:32px;height:32px;border-radius:50%;display:grid;place-items:center;flex:0 0 auto;font-weight:800;font-size:13px;{"background:var(--up);color:#fff" if done else ("background:var(--lime);color:#fff" if cur else "background:var(--line);color:var(--ink3)")}">{ic("check",16,"#fff") if done else n}</span><div style="flex:1"><b style="font-size:15px">{t}</b><div class="sub">{s}</div></div>{"<span style=font-size:13px;font-weight:800;color:var(--brandInk)>Start</span>" if cur else ""}</div>'
body=pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:26px">Your first trade</div></div>
<div class="sub">You are 3 steps in. Finish the rest at your own pace.</div>
<div style="margin:10px 0 4px">{hbar(60,"var(--lime)",10)}</div><div class="row sub"><span>3 of 5 done</span><span>About 4 minutes left</span></div>
{step(1,"Account verified","Done on 12 Oct",True)}{step(2,"Add money","₹25,000 added",True)}{step(3,"Pick a stock to follow","Added 6 to your watchlist",True)}{step(4,"Set a price alert","Get a nudge when it moves",False,True)}{step(5,"Place a practice order","Try it with virtual money first",False)}
{note("Practice orders use virtual money, so nothing real is at stake.")}
''')
H.append(phone("H2 · FIRST-TRADE GUIDE",body,"home"))
# H3 practice mode
body=pad(hdr("Practice mode")+f'''
<div style="background:var(--ink);color:#fff;border-radius:26px;padding:20px;margin-top:6px"><div style="font-size:12.5px;opacity:.72">Virtual balance</div><div class="num" style="font-size:32px;margin:4px 0 2px">₹10,00,000</div><div class="num" style="font-size:13px;color:#7CF2B8">+₹4,210 (+0.42%) since you started</div><div style="margin-top:14px;display:flex;gap:10px"><span class="pill" style="background:rgba(255,255,255,.14);color:#fff">Not real money</span></div></div>
<div class="row" style="margin-top:16px;padding:14px 16px;background:#fff;border-radius:18px;border:1px solid var(--line)"><div><b>Use practice mode</b><div class="sub">Orders stay virtual</div></div>{tog(True)}</div>
{sec("Practice positions")}
{mv("TC","#2F6FE0","TCS","₹3,412.30","+0.84%",series(12,5,1.4),"up","10 shares")}{mv("RE","#C9A24B","Reliance","₹1,248.00","-0.31%",series(12,6,-1),"dn","20 shares")}
{note("You can switch practice mode off at any time. Your real account is not affected.")}
''')
H.append(phone("H3 · PRACTICE MODE",body,"port"))
# H4 tax P&L
body=pad(hdr("Tax report",ic("download",20))+f'''
<div class="row" style="margin:2px 0 10px">{chip("FY 2026-27",True)}{chip("FY 2025-26")}</div>
{card(f'<div class="sub">Realised profit this year</div><div class="num up" style="font-size:30px;margin:2px 0 14px">+₹21,400</div><div style="display:flex;gap:10px"><div style="flex:1;background:var(--limeD);border-radius:16px;padding:12px"><div class="sub">Short-term</div><b class="num" style="font-size:17px">₹6,800</b></div><div style="flex:1;background:var(--limeD);border-radius:16px;padding:12px"><div class="sub">Long-term</div><b class="num" style="font-size:17px">₹14,600</b></div></div>',"padding:16px")}
{sec("Breakdown")}
{card(kv("Intraday","₹1,240",True)+kv("Delivery, held under 1 year","₹5,560",True)+kv("Delivery, held over 1 year","₹14,600",True)+kv("Dividends received","₹1,840",True)+kv("Charges and taxes paid","₹1,102",True),"padding:4px 18px")}
{note("Review before you file. Crestline reports are a guide, not tax advice.","warn")}
'''+bottom(btn("Download statement","lime")))
H.append(phone("H4 · TAX REPORT",body))
# H5 family
def mem(a,c,n,rel,v,k): return f'<div class="row" style="padding:13px 0;border-top:1px solid var(--line)"><div style="display:flex;gap:12px;align-items:center">{avatar(a,c,40)}<div><b style="font-size:15px">{n}</b><div class="sub">{rel}</div></div></div><div style="text-align:right"><div class="num" style="font-size:14.5px">{v}</div>{pill(k[0],k[1])}</div></div>'
body=pad(hdr("Family",ic("plus",20))+f'''
{card(f'<div class="sub">Family portfolio</div><div class="num" style="font-size:30px;margin:2px 0 6px">₹2,41,880</div><div class="num up" style="font-size:13px">+₹3,106 today</div>',"padding:18px")}
{sec("Members","3")}
{mem("AM","var(--ink)","Aarav Mehta","You","₹1,03,256",("Owner","ink"))}{mem("NM","#7A5CFF","Nisha Mehta","Spouse","₹88,420",("View only","up"))}{mem("RM","#0E9A8A","Rohan Mehta","Son · 19","₹50,204",("Can trade","wait"))}
{note("Each person keeps their own account and login. You choose what others can see.")}
'''+bottom(btn("Invite a family member","lime")))
H.append(phone("H5 · FAMILY",body))
# H6 refer
body=pad(hdr("Refer a friend")+f'''
<div style="background:var(--limeD);border-radius:28px;padding:26px 20px;text-align:center;margin-top:6px"><div style="width:64px;height:64px;border-radius:22px;background:var(--lime);color:#fff;display:grid;place-items:center;margin:0 auto">{ic("gift",32)}</div><div style="font-size:24px;font-weight:800;letter-spacing:-.03em;margin-top:14px">Invite a friend</div><div style="font-size:14.5px;line-height:1.5;color:var(--ink2);margin-top:6px">When they place their first trade, you both get <b>₹100</b> in your account.</div></div>
<div class="row" style="margin-top:16px;padding:14px 16px;background:#fff;border:1px dashed var(--line);border-radius:16px"><div><div class="sub">Your code</div><b class="num" style="font-size:18px;letter-spacing:.06em">AARAV-CR204</b></div><b style="color:var(--brandInk)">Copy</b></div>
{sec("Your invites")}
{card(kv("Joined","3",True)+kv("Placed a first trade","2",True)+kv("Earned","₹200",True),"padding:4px 18px")}
'''+bottom(btn("Share invite link","lime")))
H.append(phone("H6 · REFER AND EARN",body))
# H7 security center
body=pad(hdr("Security")+f'''
<div style="background:var(--upBg);border-radius:20px;padding:16px;display:flex;gap:14px;align-items:center"><span class="ico" style="background:var(--up);border-color:transparent;color:#fff">{ic("shield",22)}</span><div><b style="color:var(--up);font-size:16px">Your account is well protected</b><div class="sub">4 of 4 checks on</div></div></div>
{sec("Sign-in")}
{trow("Face ID","Unlock the app and confirm orders")}{trow("Two-step verification","Code from your authenticator app")}{trow("PIN on every order","Extra check before each trade",False)}
{sec("Devices")}
{lrow("phone","This iPhone","Active now · Mumbai")}{lrow("phone","Chrome on Mac","Last used 2 days ago")}
<div style="text-align:center;margin-top:16px;font-weight:800;font-size:14px;color:var(--dn)">Sign out of all other devices</div>
''')
H.append(phone("H7 · SECURITY CENTRE",body,"acc"))
# H8 privacy
body=pad(hdr("Privacy")+f'''
{card(f'<div class="row"><div style="display:flex;gap:12px;align-items:center"><span class="ico">{ic("eyeoff",20)}</span><div><b>Hide balances</b><div class="sub">Shows ••••• until you tap</div></div></div>{tog(True)}</div>',"padding:14px 16px;margin-top:6px")}
<div style="margin-top:14px;background:var(--ink);color:#fff;border-radius:24px;padding:20px"><div style="font-size:12.5px;opacity:.72">Portfolio value</div><div class="num" style="font-size:32px;margin-top:4px;letter-spacing:.12em">• • • • • •</div><div style="font-size:12.5px;opacity:.72;margin-top:6px">Tap to show for 10 seconds</div></div>
{sec("App lock")}
{trow("Lock when I leave the app","Ask for Face ID after 1 minute")}{trow("Hide in app switcher","Blur the screen in recent apps")}{trow("Block screenshots","Stops capture inside the app",False)}
''')
H.append(phone("H8 · PRIVACY",body,"acc"))
# H9 notification prefs
body=pad(hdr("Notifications")+f'''
<div class="sub" style="margin-bottom:4px">Choose what is worth a buzz.</div>
{sec("Trading")}
{trow("Order updates","Filled, rejected or cancelled")}{trow("Price alerts","When a stock hits your target")}{trow("Margin calls","Before positions are squared off")}
{sec("Money")}
{trow("Funds and withdrawals","Credits, debits and failures")}{trow("Dividends and IPOs","Ex-dates, allotments, refunds")}
{sec("Learning")}
{trow("Market summary","One note after the close",False)}{trow("Tips and offers","Occasional, never more than weekly",False)}
''')
H.append(phone("H9 · NOTIFICATION SETTINGS",body,"acc"))
# H10 accessibility
body=pad(hdr("Display & access")+f'''
<div class="lbl" style="margin:6px 0 8px">Text size</div>
{card(f'<div class="row" style="font-size:13px"><span style="font-size:13px">A</span><span style="font-size:22px">A</span></div><div style="height:6px;border-radius:6px;background:var(--line);margin:12px 0;position:relative"><i style="position:absolute;left:0;width:55%;top:0;bottom:0;background:var(--lime);border-radius:6px"></i><i style="position:absolute;left:55%;top:-9px;width:24px;height:24px;border-radius:50%;background:#fff;border:2px solid var(--lime);margin-left:-12px"></i></div><div class="num" style="font-size:19px">₹3,412.30</div>',"padding:16px")}
{sec("Theme")}
<div class="seg"><span class="on">System</span><span>Light</span><span>Dark</span></div>
{sec("Gain and loss")}
{card(f'<div class="row" style="padding:6px 0"><span style="font-weight:700">Show arrows and signs</span>{tog(True)}</div><div class="sub" style="margin:2px 0 10px">Never rely on colour alone.</div><div style="display:flex;gap:10px"><div style="flex:1;background:var(--upBg);border-radius:14px;padding:12px" class="num up">▲ +0.84%</div><div style="flex:1;background:var(--dnBg);border-radius:14px;padding:12px" class="num dn">▼ −0.31%</div></div>',"padding:14px 16px")}
{trow("Reduce motion","Replace animations with fades",False)}
''')
H.append(phone("H10 · DISPLAY AND ACCESS",body,"acc"))
# H11 widgets / live activity
body=pad(f'''
<div class="row" style="height:54px"><div class="h1" style="font-size:24px">Widgets</div></div>
<div class="sub" style="margin-bottom:12px">Check the market without opening the app.</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
<div style="background:var(--ink);color:#fff;border-radius:26px;padding:16px;aspect-ratio:1"><div style="font-size:12px;opacity:.7">Portfolio</div><div class="num" style="font-size:19px;margin-top:6px">₹1,03,256</div><div class="num" style="font-size:12px;color:#7CF2B8">▲ +1.26%</div><div style="margin-top:8px">{spark(series(14,3,1.6),110,32,"#7CF2B8")}</div></div>
<div style="background:#fff;border:1px solid var(--line);border-radius:26px;padding:16px;aspect-ratio:1"><div class="sub" style="font-weight:700">NIFTY 50</div><div class="num" style="font-size:19px;margin-top:6px">24,310</div><div class="num up" style="font-size:12px">▲ +0.42%</div><div style="margin-top:8px">{spark(series(14,9,1.2),110,32)}</div></div></div>
{sec("Order tracker on your lock screen")}
<div style="background:var(--ink);color:#fff;border-radius:34px;padding:16px 18px;display:flex;align-items:center;gap:14px"><span style="width:42px;height:42px;border-radius:50%;background:var(--spark);color:var(--ink);display:grid;place-items:center;flex:0 0 auto">{ic("clock",20)}</span><div style="flex:1"><b style="font-size:15px">Buy TCS · 12</b><div style="font-size:12.5px;opacity:.72">Waiting at ₹3,410.00</div></div><b class="num" style="color:var(--spark)">₹3,412</b></div>
{note("Tap the lock-screen tracker to open the order. It disappears once the order is filled.")}
''')
H.append(phone("H11 · WIDGETS AND LIVE ACTIVITY",body))
# H12 support tracker
def tkt(t,s,st,k): return f'<div style="padding:14px 0;border-top:1px solid var(--line)"><div class="row"><b style="font-size:15px">{t}</b>{pill(st,k)}</div><div class="sub" style="margin-top:4px">{s}</div></div>'
body=pad(hdr("Help",ic("plus",20))+f'''
<div class="field" style="display:flex;gap:10px;align-items:center;padding:12px 14px">{ic("search",18,"var(--ink3)")}<span class="mut">Search help</span></div>
<div style="display:flex;gap:10px;margin:2px 0 6px"><div style="flex:1;background:#fff;border:1px solid var(--line);border-radius:18px;padding:14px"><div class="ico" style="margin-bottom:8px">{ic("book",20)}</div><b style="font-size:14px">Guides</b></div><div style="flex:1;background:#fff;border:1px solid var(--line);border-radius:18px;padding:14px"><div class="ico" style="margin-bottom:8px">{ic("phone",20)}</div><b style="font-size:14px">Chat with us</b></div></div>
{sec("Your requests")}
{tkt("Withdrawal not received","Opened 28 Oct · Reply in about 4 hours","In progress","wait")}{tkt("Update nominee details","Opened 20 Oct","Resolved","up")}
{note("Need to raise a formal complaint? Go to Grievance redressal in the Account menu.")}
''')
H.append(phone("H12 · HELP AND REQUESTS",body,"acc"))
sheet("flow-h-trust-growth.html","Crestline v2 · Trust, learning and growth",H)
