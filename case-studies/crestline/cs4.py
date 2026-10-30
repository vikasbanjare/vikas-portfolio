"""Crestline v4 case study: self-contained (screens and wireframes inline, no image files).
Run from case-studies/crestline:  python3 cs4.py  -> v4/case-study.html"""
import os, sys, re, importlib, pathlib, html as H
os.environ['CREST_THEME']='v4'
HERE=pathlib.Path(__file__).parent; os.chdir(HERE); sys.path.insert(0,str(HERE))
import gen
CAP={}
def _cap(fn,title,screens):
    out=[]
    for s in screens:
        for a,b in gen.COPY_V4: s=s.replace(a,b)
        out.append(s)
    CAP[fn]=out
gen.sheet=_cap
for m in ['flow_a','flow_b','flow_c','flow_d','flow_e','core2','flow_f','flow_g','flow_h','flow_v4']:
    importlib.import_module(m)
import cs1, cs2, cs3
from cs1 import sec, tbl, tag, flow, cards, note, esc

# ---------- scoped screen CSS
def scope(css,root):
    out=[]
    for rule in css.split('}'):
        if '{' not in rule: continue
        sel,dec=rule.split('{',1)
        sels=[]
        for s in sel.split(','):
            s=s.strip()
            if not s: continue
            if s in (':root','body','html'): sels.append(root)
            elif s=='*': sels.append(root+' *')
            else: sels.append(root+' '+s)
        out.append(','.join(sels)+'{'+dec+'}')
    return '\n'.join(out)
APP_CSS=scope(gen.CSS+gen.V4_CSS,'.app')+'\n.app{padding:0!important;background:none!important;display:block}\n.app.gal{display:flex!important;flex-wrap:wrap;gap:6px 4px}'
def gal(screens,zoom=.5):
    return '<div class="app gal">'+''.join(f'<div class="scr" style="zoom:{zoom}">{s}</div>' for s in screens)+'</div>'
def pick(fn,ids): 
    out=[]
    for s in CAP[fn]:
        cid=re.search(r'class="cap">([^ <]+)',s).group(1)
        if cid in ids: out.append(s)
    return out
# wireframes inline
wf=pathlib.Path('v2/wireframes.html').read_text()
WF_CSS=scope(re.search(r'<style>(.*?)</style>',wf,re.S).group(1),'.wf')+'\n.wf{padding:0!important;background:none!important}'
WF_GRID=re.search(r'(<div class="grid">.*)</body>',wf,re.S).group(1)

V2TOV4=[('#3447F5','#0F2942'),('#06784A','#057A55'),('#C42A32','#C81E1E'),('#E3F5EC','#DEF7EC'),('#FDECEC','#FDE8E8'),('#E9ECFF','#E0F2FE'),('#1E2C9E','#0C4A6E'),('#D7FF3F','#EA580C')]
def v4ify(h):
    for a,b in V2TOV4: h=h.replace(a,b)
    return h
CSS=v4ify(cs1.CSS).replace('font-family:Manrope,system-ui,sans-serif;line-height:1.6','font-family:Inter,system-ui,sans-serif;line-height:1.6')
CSS+='''
h1,h2,h3,.toc b{font-family:Manrope,system-ui,sans-serif}
.gal{display:flex;flex-wrap:wrap;gap:6px 4px;margin:18px 0}.gal .scr{flex:0 0 auto}
.gal .cap{font-size:12px!important}
pre.ascii{background:#0F1626;color:#E2E8F0;border-radius:16px;padding:18px;overflow:auto;font:12px/1.45 'JetBrains Mono',monospace;margin:14px 0;max-width:100%}
pre.code{background:#F1F5F9;border:1px solid var(--line);border-radius:14px;padding:16px;overflow:auto;font:12.5px/1.5 'JetBrains Mono',monospace;color:#0A1120}
.fx{font:15px/1.7 'JetBrains Mono',monospace;background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 18px;margin:10px 0;overflow-x:auto;color:#0A1120}
.bdgs{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}
.wfwrap{overflow-x:auto;margin:16px 0}.wfwrap .wf{zoom:.62;min-width:1300px}
'''
def B(t,k): return f'<span class="bdg b-{k}" style="font-size:12px;padding:5px 8px">{t}</span>'

# ───────── sections
def hero():
    n_v4=len(CAP['flow-v4-new.html']); n_all=sum(len(v) for v in CAP.values())
    return f'''<div class="hero"><div class="eyebrow">Case study · Crestline v4 · Concept</div><h1>A broking app that <em>never lies</em> about money.</h1>
<p class="lede">Version 4 follows the master specification: fifteen real-world blind spots, an institutional navy and signal-orange system, three typefaces with one job each, two density modes, honest state machines instead of hard-coded promises, and a 128-screen map.</p>
<div class="chips"><span class="chip">{n_all} screens designed</span><span class="chip">{n_v4} new in v4</span><span class="chip">128-screen inventory</span><span class="chip">15 blind spots</span><span class="chip">Self-contained page, no image files</span><span class="chip">Concept · fictional broker</span></div></div>'''
def summary():
    body=cards([("What v2 got wrong","Lime was illegible as text and read as a gaming app. Ultramarine buttons fought green Buy and red Sell. One heavy font blurred dense tables. Screens promised timings the system could not guarantee."),
      ("What v4 does","Navy for calm authority, orange only for focus and deadlines. Manrope for wealth, Inter for UI, JetBrains Mono for data. Wealth and Trader density modes. Live states for orders, pledges, withdrawals and activation."),
      ("Read this first","Regulatory details (SEBI rules, margins, tax rates, cut-offs) come from the v4 specification and are dated 2026. Verify every figure with compliance before any real use.")],3)
    show=gal(pick('flow-v4-new.html',{'V1W','V1T','V4M','TR03'}),.5)
    return sec("00","summary","Summary","Four of the new screens, then the detail.",body+show)
def blind():
    R=[("Physical delivery on stock F&amp;O","Margin climbs from T-4 to full contract value; positions can be squared off or default on delivery","Expiry-week warning with margin ladder and exit, roll or fund options","TR07"),
       ("UPI block for trading","Money sits idle in a broker wallet","Trade from a bank block that keeps earning interest","FD01, V1W"),
       ("50% cash-collateral rule","Pledged shares alone cannot carry overnight margin","Cash and collateral mix shown with a pass or fail","P02"),
       ("CDSL TPIN and DDPI","Selling is delayed by OTP steps while a price falls","Pre-authorisation prompt and DDPI option in onboarding","MTF07, A18"),
       ("Surveillance and trade-to-trade","Intraday or market orders get rejected","Badges and locked products before the tap","V4L, W6T"),
       ("Illiquid strikes and freak trades","Market orders fill far from the price","Protected market order, limit at LTP ± a cap; ILLIQUID badge","V4M, W6T"),
       ("2026 F&amp;O structure","Lot sizes, single weekly expiry, expiry-day margin","Option chain with lot 65, future-equivalent OI, expiry margin preview","TR03"),
       ("Corporate actions break orders","GTTs and strikes become wrong after splits and bonuses","Adjusted-strike flag and one-tap GTT recalculation","Spec CA01"),
       ("Holdings with no buy price","P&amp;L and tax show nothing for gifted or transferred shares","Fix buy average flow","P09"),
       ("Multi-bank routing","Deposits from unregistered banks fail","Registered banks only, primary bank for payouts","FD01"),
       ("Peak-margin penalty","Mid-day margin spikes cost penalties","Margin-used meter that warns at 85%","V1T"),
       ("Mutual fund cut-offs","People miss same-day NAV without knowing why","Live countdown to the 3:00 PM realisation cut-off, holding mode badge","MF04"),
       ("Feed outages","A frozen price looks like a broken app","Dual-exchange failover, stale badge, service status page","V3F, SR01"),
       ("Tax lots and grandfathering","A PDF does not explain what selling will cost","FIFO lot inspector with a sell-now estimate","P15"),
       ("Overtrading tilt","Losses compound after a bad morning","Daily loss kill switch that still allows exits","TR06")]
    return sec("01","blind","Fifteen blind spots","Real mechanics where Indian investors and traders lose money or get stuck, and what the design does about each.",tbl(["Blind spot","What goes wrong","Design response","Screens"],[[f'<b>{a}</b>',b,c,tag(d,"b")] for a,b,c,d in R]))
def system():
    def lum(h):
        h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
        f=lambda c: c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
        return .2126*f(r)+.7152*f(g)+.0722*f(b)
    def cr(a,b):
        la,lb=lum(a),lum(b); la,lb=max(la,lb),min(la,lb); return (la+.05)/(lb+.05)
    T=[("surface/canvas","#F8FAFC","#070B14"),("surface/card","#FFFFFF","#0F1626"),("surface/elevated","#F1F5F9","#1E293B"),("text/primary","#0A1120","#F1F5F9"),("text/secondary","#334155","#CBD5E1"),("text/muted","#475569","#94A3B8"),("border/subtle","#E2E8F0","#1E293B"),("brand/primary","#0F2942","#38BDF8"),("brand/soft","#E0F2FE","#0C4A6E"),("accent/signal","#EA580C","#FB923C"),("accent/signal-text","#C2410C","#FB923C"),("accent/soft","#FFEDD5","#431407"),("trade/buy","#057A55","#10B981"),("trade/buy-tint","#DEF7EC","#064E3B"),("trade/sell","#C81E1E","#F43F5E"),("trade/sell-tint","#FDE8E8","#4C0519"),("status/warn","#B45309","#FBBF24"),("status/warn-tint","#FEF3C7","#451A03")]
    sw='<div class="sw">'+''.join(f'<div style="background:{l};color:{"#fff" if lum(l)<.3 else "#0A1120"}"><b>{n}</b><span>{l} · dark {d}</span></div>' for n,l,d in T)+'</div>'
    C=[("text/muted on canvas","#475569","#F8FAFC","7.1"),("text/secondary on canvas","#334155","#F8FAFC","10.4"),("Buy text on white","#057A55","#FFFFFF","5.48"),("Sell text on white","#C81E1E","#FFFFFF","5.86"),("Warn on white","#B45309","#FFFFFF","5.02"),("Signal orange #EA580C on white","#EA580C","#FFFFFF","4.6"),("Signal orange on canvas","#EA580C","#F8FAFC","4.62"),("Corrected orange text #C2410C on white","#C2410C","#FFFFFF","—"),("Buy on its tint","#057A55","#DEF7EC","—"),("Sell on its tint","#C81E1E","#FDE8E8","—"),("White on navy button","#FFFFFF","#0F2942","—"),("Ink on orange button","#0A1120","#EA580C","—"),("Dark: sell on card","#F43F5E","#0F1626","6.4")]
    def cell(a,b):
        r=cr(a,b); return f'<span class="num">{r:.2f}:1</span> '+tag("Pass AA" if r>=4.5 else ("UI only, 3:1" if r>=3 else "Fail"),"up" if r>=4.5 else ("w" if r>=3 else "dn"))
    ct=tbl(["Pair","Spec says","Measured"],[[n,s if s!="—" else "not stated",cell(a,b)] for n,a,b,s in C])
    fix=note("<b>Correction to the spec.</b> Signal orange #EA580C measures 3.4 to 3.56:1 on light surfaces, not 4.6:1. It passes for focus rings, icons and large text (3:1) but not for small text. Orange text and badges therefore use #C2410C (5.18:1). Buttons in orange use dark ink text (5.3:1).")
    ty=tbl(["Tier","Typeface","Use","Rule"],[["1 · Wealth and titles","Manrope 600–800","Net worth, screen titles, section headers","Tabular figures, -0.025em"],["2 · UI and prose","Inter 400–700","Labels, inputs, articles, disclosures","Body 14.5/21, labels 13.5/18, captions 11.5/15"],["3 · Data","JetBrains Mono 500–700","Live prices, option chain, depth, IDs, timestamps","Every character the same width so decimals align"]])
    sample='<div class="cols c3"><div class="card"><h4 style="margin-top:0">Tier 1</h4><div style="font:800 30px Manrope;letter-spacing:-.025em">₹14,82,450</div></div><div class="card"><h4 style="margin-top:0">Tier 2</h4><div style="font:500 15px/1.5 Inter">Authorise your CDSL pledge by 7:00 PM to keep the funded position.</div></div><div class="card"><h4 style="margin-top:0">Tier 3</h4><div style="font:600 14px/1.6 \'JetBrains Mono\'">  3,412.05<br>18,920.80<br>   142.65</div></div></div>'
    dens=tbl(["Property","Wealth mode","Trader mode"],[["Row height","64 px, full name and sector","42 px, symbol, badges, LTP, change"],["Card radius","16 px","8 px"],["Card padding","18–20 px","10–12 px"],["Rows above the fold","7–8 plus net worth","14–16 plus MTM strip"],["Order confirmation","Swipe, charges expanded","One tap with a 2 s undo on far limits"]])
    bd='<div class="bdgs">'+B("NSE","ex")+B("BSE","ex")+B("T+0","t0")+B("MTF 4x","mtf")+B("ASM-I","asm")+B("T2T-BE","asm")+B("ILLIQUID","ill")+B("STALE · 14s","stale")+'</div><p>Monospace 10 px badges, 4 px radius. Surveillance badges open a sheet explaining which products are blocked and why.</p>'
    gov='<ul class="l"><li><b>Banned in lists:</b> flame, bolt and trophy icons. They read as stock tips. v4 maps them to neutral icons.</li><li><b>Never colour alone:</b> every gain or loss carries ▲ or ▼ and a sign.</li><li><b>Orange is rationed:</b> focus, deadlines and the active mode only.</li></ul>'
    return sec("02","system","Design system v4","Institutional navy and signal orange, checked against the spec's own contrast claims.",'<h3>Tokens, light and dark</h3>'+sw+'<h3>Contrast: the spec checked</h3>'+ct+fix+'<h3>Three typefaces, one job each</h3>'+sample+ty+'<h3>Two density modes</h3>'+dens+'<h3>Instrument badges</h3>'+bd+'<h3>Icon governance</h3>'+gov)
def ia():
    shell='''<div class="card" style="font-size:13.5px"><div style="display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap"><b style="font:800 15px Manrope;letter-spacing:.05em">CRESTLINE</b><span style="background:#F1F5F9;border-radius:99px;padding:3px"><span style="background:#0F2942;color:#fff;border-radius:99px;padding:5px 12px;font-weight:700">Wealth</span><span style="padding:5px 12px;font-weight:700;color:#334155">Trader</span></span><span style="color:#475569">Search or type a command · Alerts 2</span></div>
<div style="background:#FEF3C7;color:#B45309;border-radius:12px;padding:10px 12px;margin:12px 0;font-weight:600">SEBI investor notice, shown on alternate days until read.</div>
<div style="background:#F8FAFC;border:1px dashed #CBD5E1;border-radius:12px;padding:30px;text-align:center;color:#475569">Active screen</div>
<div style="background:#0F2942;color:#fff;border-radius:12px;padding:10px 12px;margin-top:12px;display:flex;justify-content:space-between"><span>Trader mode only: open positions 3 · MTM +₹14,280.50</span><b>Exit all</b></div>
<div style="display:flex;justify-content:space-around;margin-top:12px;font-weight:700;color:#334155"><span>Home</span><span>Markets</span><span>Portfolio</span><span>Orders</span><span>Account</span></div></div>'''
    cmd=tbl(["You type","What happens"],[["Nifty 24500","Shows both options with Buy, Sell and Option chain inline"],["Tax report or Capital gains","Opens the FIFO tax harvester"],["Pledge or TPIN","Opens the CDSL pledge hub"],["Gold","Opens the gold selector: ETF, SGB, fund, commodity"],["Kill switch or Stop trading","Opens trading limits"]])
    return sec("03","ia","Navigation","Five tabs stay. A mode switch and a command search handle the sprawl.",shell+'<h3>Command search</h3>'+cmd)
def machines():
    a='<h3>Smart onboarding router</h3>'+flow([("Welcome and disclosure","s"),("Client type","n"),("Mobile, OTP, email","n"),("PAN and DOB","n"),("KRA lookup","n")])+'<p><b>Branches</b></p>'+flow([("KRA validated","o"),("Skip documents (A13)","n")])+flow([("New, on hold or mismatch","d"),("DigiLocker and video KYC","n"),("Assisted KYC for accessibility","n")])+flow([("NRI","d"),("FEMA, FATCA, passport route","n")])+flow([("Bank via ₹1 penny-drop","n"),("Offer UPI trading block","n"),("Segments and DDPI","n"),("Nominees, up to 10","n"),("Activation pipeline (A11)","o")])
    b='<h3>Order that never double-fires</h3>'+flow([("Tap Buy","s"),("Pre-checks: stale quote, circuit band, freeze limit, funds","n"),("Idempotency key, button locked","n"),("Send","n")])+flow([("Ack under 400 ms","o"),("Open, partly filled, filled","o")])+flow([("Network drop","d"),("Reconciling, re-order blocked (SR10)","n"),("Poll every 2 s","n")])+flow([("RMS or exchange reject","d"),("Plain reason, one-tap fix (C6R)","n")])
    c='<h3>MTF and pledge lifecycle</h3>'+flow([("MTF 4x on order pad","s"),("Cost drawer: 25% cash, 75% funded, daily interest","n"),("Fill","n"),("Pledge window 4–7 PM","n")])+flow([("Pledged","o"),("Carry forward, interest accrues","o")])+flow([("Missed, cash available","d"),("Convert to delivery","n")])+flow([("Missed, no cash","d"),("Marked unpaid, may be sold next day","n")])
    return sec("04","machines","State machines","Every money promise is a state the backend confirms, never a sentence on screen.",a+b+c+note("Removed hard-coded promises: 'Credited in 1 working day', 'Tomorrow, 9:15 AM', 'Released in 3 days' and 'You're all set'. Each now shows a live status.","b"))
def newscreens():
    return sec("05","new","New in v4","Twenty-three screens built from the specification.",gal(CAP['flow-v4-new.html'],.5))
def wires():
    asc=pathlib.Path('/Users/vikas/Downloads/crestline_v4_master_specification_complete_fix_blueprint.md')
    pres=''
    if asc.exists():
        t=asc.read_text()
        blocks=re.findall(r'### (Wireframe \d+:[^\n]*)\n```\n(.*?)```',t,re.S)
        pres=''.join(f'<h3>{esc(h.replace("`",""))}</h3><pre class="ascii">{esc(b)}</pre>' for h,b in blocks)
    return sec("06","wireframes","Wireframes","Twelve low-fidelity screens, followed by the six annotated wireframes from the specification. All inline, nothing to load.",f'<div class="wfwrap"><div class="wf">{WF_GRID}</div></div>'+pres)
def formulas():
    f='''<h3>Portfolio returns</h3><div class="fx">Unrealised P&amp;L = Σ (Qty<sub>i</sub> × LTP<sub>i</sub>) − Σ (Qty<sub>i</sub> × BuyAvg<sub>i, FIFO</sub>)</div><div class="fx">XIRR: solve r where Σ C<sub>k</sub> / (1 + r)<sup>(d<sub>k</sub> − d<sub>0</sub>) / 365</sup> = 0</div><p>Guardrail: under one year, show absolute return and label XIRR an annualised estimate, so a 2% gain in three days never reads as 1,100%.</p>
<h3>Margin and MTF</h3><div class="fx">Daily MTF interest = max(0, Funded − Free ledger credit) × APR / 365</div><div class="fx">Required cash = 0.50 × (SPAN + Exposure + Expiry ELM)<br>Cash shortfall = max(0, Required cash − (UPI block used + Cash equivalents))</div><div class="fx">Equity ratio = (Qty × LTP − Funded) / (Qty × LTP)<br>Below haircut → shortfall warning · at or below 0.15 → liquidation alert</div>
<h3>Bonds</h3><div class="fx">Dirty price = Clean price + Face value × Coupon × Days since last coupon / Days in coupon year</div><div class="fx">YTM: solve y where Dirty price = Σ CF<sub>t</sub> / (1 + y)<sup>w<sub>t</sub></sup> + M / (1 + y)<sup>w<sub>n</sub></sup></div><p>Callable bonds above par show yield to call and highlight the lower as yield to worst.</p>
<h3>Cost basis after corporate actions</h3><ul class="l"><li><b>Bonus A:B:</b> original lots keep their price. Bonus shares are a new lot at ₹0 dated on the ex-bonus date.</li><li><b>Split F<sub>old</sub> → F<sub>new</sub>:</b> quantity × F<sub>old</sub>/F<sub>new</sub>, price ÷ the same, original dates kept for long-term gains.</li></ul>'''
    return sec("07","formulas","Calculation engine","Exact formulas so engineering never guesses how a number is derived.",f)
def contracts():
    c1='''interface PortfolioHoldingV4 {
  isin: string; symbol: string; exchange_primary: "NSE" | "BSE";
  instrument_series: "EQ" | "BE" | "BZ" | "SM" | "ST" | "SGB" | "ETF";
  surveillance_stage: "NONE" | "ASM_STAGE_1" | "ASM_STAGE_4" | "GSM_STAGE_2";
  quantities: { total_demat_qty; free_salable_qty; pledged_for_margin_qty;
                mtf_funded_unpledged_qty; unpaid_cuspa_qty; locked_in_qty };
  authorization_state: { ddpi_enabled; cdsl_tpin_authorized_today; tpin_expiry_timestamp? };
  valuation_and_cost: { fifo_avg_buy_price: number | null; is_discrepant_holding;
                        ltp; ltp_timestamp_ms; is_quote_stale; gross_unrealized_pnl;
                        estimated_sell_charges; net_realizable_pnl };
  tax_lots_fifo: Array<{ lot_id; acquisition_date; quantity; cost_per_share;
                         grandfathered_jan2018_fmv?; holding_days; tax_classification }>;
}'''
    c2='''interface ClientCapitalStateV4 {
  as_of_timestamp_ms: number;
  upi_trading_block: { mandate_status: "ACTIVE" | "PENDING_NPCI" | "EXPIRED" | "NOT_SETUP";
                       linked_bank_masked; total_blocked_limit; utilized_for_trades_today;
                       available_to_trade_block; instant_releasable_amount };
  broker_ledger: { opening_cleared_balance; unsettled_t1_sale_proceeds;
                   intraday_realized_profits; withdrawable_free_cash; next_quarterly_settlement_date };
  margin_and_collateral: { cash_and_cash_equivalents; non_cash_equity_collateral;
                           effective_50_50_usable_collateral; excess_collateral_subject_to_interest;
                           span_margin_used; exposure_margin_used; expiry_day_additional_elm;
                           peak_margin_utilization_pct };
}'''
    return sec("08","contracts","Data contracts","The two contracts every money screen reads from. Types abbreviated; full versions are in the specification.",f'<pre class="code">{esc(c1)}</pre><pre class="code">{esc(c2)}</pre>')
def inventory():
    D=[("Core and command",8,"V1–V6, S01, S08","V1W, V1T, V3F, V4M, V4L, V1–V6"),("Smart KYC and account lifecycle",26,"A1–A26","A1–A11, A13, A19"),("Equities, research and discovery",21,"B1–B10, F1–F11, S05","B1–B10, F1–F13"),("Orders, baskets and MTF",26,"C1–C7, G1–G8, S06, MTF01–10","C1–C7, C6R, G1–G8, SR10, MTF07"),("F&amp;O risk and physical delivery",10,"TR01–TR10","TR03, TR06, TR07"),("Portfolio, tax and corporate actions",26,"D1–D8, P01–P15, CA01–05","D1–D8, P02, P09, P15"),("Multi-asset: MF, gold, bonds, partners",38,"MF01–12, AS01–08, FI01–10, PT01–08","MF04, FI02, F12, F13"),("Funds, security and grievance",26,"FD01–08, E1–E9, H2–H11, SR01–10","FD01, FD03, E1–E9, H1–H12, SR01")]
    rows=[[f'<b>{a}</b>',f'<span class="num">{n}</span>',c,d] for a,n,c,d in D]
    return sec("09","inventory","The 128-screen map","Eight domain packages. The right column lists what is drawn in hi-fi today; the rest is specified and ready to design.",tbl(["Domain","Screens","IDs in the specification","Designed in hi-fi"],rows)+note("Designed screens cover every P0 item. The remaining screens in partner, commodity, corporate-action and grievance packages are specified but not yet drawn."))
def checklist():
    P=[("P0","No broken image dependencies","Done: this page embeds every screen"),("P0","Investor notice on Home","Designed: V1W"),("P0","Replace hard-coded promises with live states","Done: copy pass and A11, FD03, G7"),("P0","UPI block and T+0 order pad","Designed: FD01, V4M"),("P0","2026 F&amp;O rules engine","Designed: TR03, TR07; rest specified"),("P0","MTF and CDSL pledge flow","Designed: V4M, MTF07"),("P0","Smart KRA onboarding","Designed: A13, A19, A11"),("P1","Explainable diagnostics and FIFO tax","Designed: P02, P15, P09"),("P1","Fund cut-off timers and demat SWP/STP","Designed: MF04"),("P1","Bonds with clean and dirty price","Designed: FI02"),("P1","Kill switch, reconciliation and failover","Designed: TR06, SR10, V3F, SR01"),("P2","Specialised investment funds gate","Specified"),("P2","Regulated partner collars","Specified")]
    k=lambda s:"up" if s.startswith(("Done","Designed")) else "g"
    return sec("10","checklist","Release gates","Where each gate from the specification stands.",tbl(["Gate","Item","Status"],[[f'<b>{a}</b>',b,tag(c,k(c))] for a,b,c in P]))
def review():
    F=[("P0","Visual · A11y","Lime as text and accent","1.08:1 on white and read as speculative","Removed. Orange rationed, navy for action","Fixed"),
       ("P0","A11y","Spec's signal orange as text","3.4–3.56:1, below 4.5:1","#C2410C for text and badges","Fixed"),
       ("P1","Visual","Ultramarine CTA beside green and red","Chromatic clash on dense screens","Navy primary, colour reserved for trade","Fixed"),
       ("P1","Visual","One heavy font everywhere","Option chains blur at small sizes","Three-tier type","Fixed"),
       ("P1","UX · H1","Promised timings","Screens stated outcomes the system cannot guarantee","Live states and status pages","Fixed"),
       ("P1","UX · H5","Error prevention for restricted stocks","Rejections after the tap","Badges and locked products before the tap","Fixed"),
       ("P2","UX · H7","Density","One layout for investors and traders","Wealth and Trader modes","Fixed"),
       ("P2","UX · H9","Network drop on order","Risk of double orders","Idempotent reconciling state","Fixed"),
       ("P2","Compliance","Regulatory figures","Dated rules can change","Verify with compliance before use","Open")]
    kk={"Fixed":"up","Open":"dn"}
    return sec("11","review","Design review v4","Findings on v2 that drove v4, and the status now.",tbl(["Sev","Area","Where","Issue","Fix","Status"],[[f'<b>{a}</b>',b,c,d,e,tag(f,kk[f])] for a,b,c,d,e,f in F]))
def everything():
    order=[('core-v2.html','Core'),('flow-a-account.html','A · Create an account'),('flow-b-markets.html','B · Markets and research'),('flow-c-orders.html','C · Orders'),('flow-d-portfolio.html','D · Portfolio and products'),('flow-e-account-system.html','E · Account and system'),('flow-f-discover.html','F · Discover'),('flow-g-trading-tools.html','G · Trading tools'),('flow-h-trust-growth.html','H · Trust and growth')]
    out=''.join(f'<h3>{t}</h3>'+gal(CAP[fn],.42) for fn,t in order)
    return sec("15","screens","Every flow in v4","All earlier flows re-themed with the v4 system and copy rules.",out)
SECTIONS=[("00","summary","Summary"),("01","blind","Fifteen blind spots"),("02","system","Design system v4"),("03","ia","Navigation"),("04","machines","State machines"),("05","new","New in v4"),("06","wireframes","Wireframes"),("07","formulas","Calculation engine"),("08","contracts","Data contracts"),("09","inventory","128-screen map"),("10","checklist","Release gates"),("11","review","Design review"),("12","research","Research plan"),("13","personas","Proto-personas"),("14","writing","UX writing"),("15","screens","Every flow"),("16","motion","Motion"),("17","next","Next steps")]
def build():
    renum=lambda h,old,new: h.replace(f'<div class="sn">{old}</div>',f'<div class="sn">{new}</div>',1)
    reused=renum(v4ify(cs1.research()),"03","12")+renum(v4ify(cs1.personas()),"04","13")+renum(v4ify(cs3.writing()),"12","14")
    tail=renum(v4ify(cs2.motion()),"11","16")+renum(v4ify(cs3.nxt()),"16","17")
    body=hero()+summary()+blind()+system()+ia()+machines()+newscreens()+wires()+formulas()+contracts()+inventory()+checklist()+review()+reused+everything()+tail
    toc='<nav class="toc" aria-label="Sections"><b>Crestline v4</b><small>Case study · concept</small>'+''.join(f'<a href="#{i}"><i>{n}</i>{t}</a>' for n,i,t in SECTIONS)+'<a href="../showcase.html" style="margin-top:18px;color:var(--brandInk)"><i>←</i>Back to showcase</a></nav>'
    doc=(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Crestline v4 · Case Study</title>'
         '<meta name="description" content="Crestline v4: an Indian broking app concept with fifteen blind spots designed, a navy and orange system, density modes, honest state machines and a 128-screen map.">'
         + gen.FONTS_V4 + f'<style>{CSS}\n{APP_CSS}\n{WF_CSS}</style></head><body>{gen.SYM}<div class="shell">{toc}<main>{body}</main></div></body></html>')
    pathlib.Path('v4/case-study.html').write_text(doc)
    print('v4/case-study.html',len(doc)//1024,'KB', sum(len(v) for v in CAP.values()),'screens inline')
if __name__=='__main__': build()
