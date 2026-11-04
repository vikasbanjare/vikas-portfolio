#!/usr/bin/env python3
"""Crestline v5 presentation: device mockups, click-through prototype, showcase page.
Reads v5/screens/manifest.json (see capture.mjs). Run from anywhere: python3 present.py [mock] [proto] [page]
Writes v5/mockups/*.jpg, v5/prototype.html, ../showcase.html."""
import json, os, re, subprocess, sys, tempfile, html as H, pathlib
HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
V5 = ROOT / 'v5'
MAN = json.load(open(V5 / 'screens/manifest.json'))
BY = {m['id']: m for m in MAN}
esc = H.escape
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def need(i):
    assert i in BY, 'unknown screen ' + i
    return i


def shot(i, base='v5/screens'):
    return '%s/%s.webp' % (base, need(i))


# ── Mockups ──────────────────────────────────────────────────────────
def render(name, w, h, body, css=''):
    """Compose a scene in plain CSS, screenshot it in headless Chrome, save as jpeg."""
    page = ('<!doctype html><meta charset=utf-8><style>*{box-sizing:border-box;margin:0}html,body{width:%dpx;height:%dpx;overflow:hidden}'
            '.p{position:absolute;width:393px;border-radius:58px;padding:11px;background:#0B1220;box-shadow:0 0 0 1.5px #2A3650,0 50px 90px -24px rgba(4,10,24,.55)}'
            '.p img{display:block;width:100%%;border-radius:47px}%s</style>%s') % (w, h, css, body)
    out = V5 / 'mockups'
    out.mkdir(exist_ok=True)
    with tempfile.NamedTemporaryFile('w', suffix='.html', dir=V5, delete=False) as f:
        f.write(page)
    png = '/tmp/mock-%s.png' % name
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=%d,%d' % (w, h), '--virtual-time-budget=6000', '--screenshot=' + png, 'file://' + f.name],
                   stderr=subprocess.DEVNULL, check=True)
    os.unlink(f.name)
    subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '84', png, '--out', str(out / (name + '.jpg'))],
                   stdout=subprocess.DEVNULL, check=True)


def phone(i, x, y, s=1, r=0, base='screens', z=1):
    return ('<div class="p" style="left:%dpx;top:%dpx;transform:scale(%s) rotate(%sdeg);transform-origin:top left;z-index:%d">'
            '<img src="%s/%s.webp"></div>') % (x, y, s, r, z, base, need(i))


def mockups():
    # Hero: three phones, the trading journey from price to order to portfolio.
    hero = phone('stock_overview', 210, 150, .92, -4, z=1) + phone('home', 603, 70, 1.02, 0, z=3) + phone('buy_pad', 1020, 170, .92, 4, z=2)
    render('hero', 1600, 1040, hero, 'html,body{background:#0F2942}')
    # Wall: the breadth of the product, tilted columns.
    cols = [['sign_in', 'kyc_account_ready', 'funds'], ['watchlist', 'stock_depth', 'order_types'], ['portfolio', 'charges_breakdown', 'gtt_triggered'],
            ['mf_discover', 'calc_sip', 'sip_started'], ['option_chain', 'option_buy_pad', 'fo_turn_on'], ['ipo_list', 'taxes', 'save_tax']]
    wall = ''
    for c, col in enumerate(cols):
        for r, i in enumerate(col):
            wall += phone(i, 40 + c * 300, -220 + r * 590 + (c % 2) * 190, .68, 0)
    render('wall', 1600, 900, '<div style="position:absolute;inset:-60px;transform:rotate(-7deg) scale(1.1)">%s</div>' % wall, 'html,body{background:#E2E8F0}')
    # Isometric grid: states and edge cases.
    iso_ids = ['buy_rejected', 'bank_declined', 'order_placed', 'funds_zero', 'buy_partly_filled', 'gtt_empty', 'kill_switch', 'withdraw_on_way',
               'fo_review', 'report_delayed', 'sip_mandate_expired', 'mf_sip_missed']
    iso = ''.join(phone(i, (n % 4) * 460, (n // 4) * 940, 1) for n, i in enumerate(iso_ids))
    render('iso', 1600, 900, '<div style="position:absolute;left:50%%;top:50%%;width:1840px;height:2820px;margin:-1410px 0 0 -920px;transform:rotateX(50deg) rotateZ(-38deg) scale(.82)">%s</div>' % iso,
           'html,body{background:#070B14}')
    # Light and dark, split down the middle.
    pair = phone('home', 330, 40, 1) + phone('home', 877, 50, 1, base='dark')
    render('pair', 1600, 900, pair, 'html,body{background:linear-gradient(90deg,#F1F5F9 50%,#070B14 50%)}')
    # Thumbnail used by the portfolio card (16:10).
    cover = phone('stock_overview', 230, 120, .9, -4) + phone('home', 500, 50, 1, z=3) + phone('portfolio', 790, 130, .9, 4, z=2)
    render('cover', 1200, 750, cover, 'html,body{background:#0F2942}')


# ── Prototype ────────────────────────────────────────────────────────
# Each step is (screen id, words on the control that moves on). None = last screen of the journey.
JOURNEYS = [
    ('First trade', 'Sign in, find a stock and buy it. Watch "placed" become "filled".',
     [('sign_in', 'Get code'), ('otp', None), ('home', '^Stocks'), ('stock_overview', '^Buy$'), ('buy_pad', '^Buy 10'), ('order_placed', 'Track'), ('buy_partly_filled', 'Keep waiting'), ('buy_filled', 'See holding'), ('portfolio', None)]),
    ('When an order fails', 'A limit order outside the price band, and what the app says next.',
     [('buy_pad', '^Buy 10'), ('buy_rejected', 'Edit price'), ('buy_pad', None)]),
    ('Add money', 'UPI, including the wait when the bank has not confirmed.',
     [('funds', 'Add funds'), ('add_funds', 'Pay'), ('add_funds_upi', '^GPay'), ('add_funds_pending', 'Check status'), ('funds_added', None)]),
    ('Withdraw', 'What can leave today, and when it arrives.',
     [('withdraw', '^Withdraw ₹'), ('withdraw_confirm', None), ('withdraw_on_way', None)]),
    ('Start a SIP', 'From a fund page to AutoPay approved.',
     [('mf_fund', 'Start SIP'), ('mf_sip', 'Choose SIP date'), ('sip_date', 'Choose payment'), ('mf_sip_nominee', 'Continue'), ('sip_mandate', 'Set up AutoPay'), ('sip_mandate_pending', 'Open UPI'), ('sip_started', None)]),
    ('Option order', 'The chain, the most you can lose, then the order.',
     [('fo_home', '^NIFTY 50'), ('option_chain', '^98.60'), ('option_strike', '^Buy$'), ('option_buy_pad', '^Buy 2'), ('option_placed', None)]),
    ('IPO bid', 'A UPI block, not a payment, explained at each step.',
     [('ipo_list', '^Lalithaa'), ('ipo_detail', '^Apply'), ('ipo_apply', 'Apply with UPI'), ('ipo_upi_mandate', 'Open UPI'), ('ipo_status', None)]),
    ('Turn on F&O', 'Friction on purpose: the risk comes first.',
     [('fo_turn_on', 'understand'), ('fo_income_proof', 'Upload proof'), ('fo_review', None)]),
    ('Stop trading', 'The kill switch, with its consequences stated.',
     [('positions', 'Kill switch'), ('kill_switch', None)]),
]


def hotspot(i, words):
    """Find the button to tap from the rects measured during capture."""
    m = BY[need(i)]
    if words:
        for c in m['cta']:
            if re.search(words, c['t'], re.I):
                return [c['x'], c['y'], c['w'], c['h'], c['t']]
    # ponytail: no match means the page's Next control moves on, e.g. the OTP auto-read screen.
    return None


def prototype():
    data = []
    for name, why, steps in JOURNEYS:
        out = []
        for n, (i, words) in enumerate(steps):
            last = n == len(steps) - 1
            out.append({'id': i, 't': BY[i]['title'], 'h': None if last else hotspot(i, words)})
        data.append({'n': name, 'w': why, 's': out})
    page = PROTO.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
    (V5 / 'prototype.html').write_text(page)
    missing = [(d['n'], s['id']) for d in data for s in d['s'][:-1] if not s['h']]
    print('prototype journeys', len(data), 'steps', sum(len(d['s']) for d in data), 'no hotspot (uses Next):', missing)


PROTO = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Crestline prototype</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
<style>
:root{--ink:#0A1120;--ink2:#475569;--navy:#0F2942;--paper:#F1F5F9;--line:#E2E8F0;--signal:#C2410C}
*{box-sizing:border-box;margin:0}html,body{height:100%}body{font:15px/1.5 Inter,system-ui,sans-serif;color:var(--ink);background:var(--paper)}
.app{display:grid;grid-template-columns:minmax(0,320px) auto;gap:clamp(24px,5vw,72px);justify-content:center;align-items:start;padding:clamp(16px,3vw,36px)}
h1{font:800 22px/1.2 Manrope,sans-serif;letter-spacing:-.02em}.lead{color:var(--ink2);margin:6px 0 18px;font-size:14px}
.list{display:grid;gap:4px;list-style:none;padding:0}
.list button{width:100%;text-align:left;border:0;background:transparent;border-radius:12px;padding:11px 14px;font:600 14.5px Inter,sans-serif;color:var(--ink);cursor:pointer;min-height:44px}
.list button small{display:block;font-weight:400;font-size:13px;color:var(--ink2);margin-top:2px}
.list button:hover{background:#E2E8F0}.list button[aria-current=true]{background:var(--navy);color:#fff}.list button[aria-current=true] small{color:#CBD5E1}
button:focus-visible,a:focus-visible{outline:3px solid var(--signal);outline-offset:2px}
.stage{width:min(393px,calc(100vw - 32px))}
.phone{position:relative;border-radius:52px;padding:10px;background:#0B1220;box-shadow:0 40px 70px -28px rgba(4,10,24,.5)}
.screen{position:relative;border-radius:42px;overflow:hidden;aspect-ratio:393/852;background:#fff}
.screen img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top;animation:in .24s cubic-bezier(.2,.7,.3,1)}
@keyframes in{from{opacity:.2;transform:translateX(14px)}to{opacity:1;transform:none}}
.hot{position:absolute;border:0;background:transparent;border-radius:999px;cursor:pointer;padding:0}
.hot::after{content:"";position:absolute;inset:-3px;border-radius:inherit;box-shadow:0 0 0 3px rgba(234,88,12,.9);animation:pulse 1.6s infinite}
@keyframes pulse{0%,100%{opacity:.25}50%{opacity:1}}
.bar{display:flex;align-items:center;gap:10px;margin-top:14px}.bar .where{flex:1;font-size:13.5px;color:var(--ink2);min-width:0}.bar b{display:block;color:var(--ink);font-weight:600}
.ctl{min-width:44px;height:44px;padding:0 14px;border-radius:999px;border:0;background:#E2E8F0;color:var(--ink);font:600 14px Inter,sans-serif;cursor:pointer}.ctl:disabled{opacity:.4;cursor:default}.ctl.go{background:var(--navy);color:#fff}
.note{margin-top:18px;font-size:12.5px;color:var(--ink2)}
@media (max-width:760px){.app{grid-template-columns:minmax(0,1fr);justify-items:center}.side{width:100%;min-width:0}.list{grid-auto-flow:column;grid-auto-columns:max-content;overflow-x:auto;padding-bottom:6px}.list small{display:none!important}.note{display:none}}
@media (prefers-reduced-motion:reduce){.screen img,.hot::after{animation:none}.hot::after{opacity:1}}
</style></head><body><main class="app">
<div class="side"><h1>Crestline prototype</h1><p class="lead">Pick a journey. Tap the glowing control on the phone, or use Next and the arrow keys.</p>
<ul class="list" id="list"></ul><p class="note">A click-through of final screens, built to show flow. Sample data, fictional broker, no real orders.</p></div>
<div class="stage"><div class="phone"><div class="screen" id="screen" aria-live="polite"></div></div>
<div class="bar"><button class="ctl" id="back" aria-label="Previous screen">←</button><div class="where"><b id="t"></b><span id="c"></span></div><button class="ctl go" id="next">Next</button></div></div>
</main><script>
var J=__DATA__,j=0,s=0;var $=function(i){return document.getElementById(i)};
var pre={};function load(i){if(!pre[i]){pre[i]=new Image();pre[i].src='screens/'+i+'.webp'}}
function draw(){var d=J[j],st=d.s[s],sc=$('screen');sc.innerHTML='';var im=document.createElement('img');im.src='screens/'+st.id+'.webp';im.alt=st.t;sc.appendChild(im);
 if(st.h){var b=document.createElement('button');b.className='hot';var h=st.h;b.style.cssText='left:'+h[0]/3.93+'%;top:'+h[1]/8.52+'%;width:'+h[2]/3.93+'%;height:'+h[3]/8.52+'%';b.setAttribute('aria-label',h[4]||'Continue');b.onclick=go;sc.appendChild(b)}
 $('t').textContent=st.t;$('c').textContent=d.n+' · '+(s+1)+' of '+d.s.length;$('back').disabled=s===0;var end=s===d.s.length-1;$('next').textContent=end?'Restart':'Next';
 if(d.s[s+1])load(d.s[s+1].id);[].forEach.call($('list').children,function(li,i){li.firstChild.setAttribute('aria-current',i===j);if(i===j)$('list').scrollLeft=li.offsetLeft-16})}
function go(){s=s<J[j].s.length-1?s+1:0;draw()}function back(){if(s>0){s--;draw()}}
J.forEach(function(d,i){var li=document.createElement('li'),b=document.createElement('button');b.textContent=d.n;var m=document.createElement('small');m.textContent=d.w;b.appendChild(m);b.onclick=function(){j=i;s=0;draw()};li.appendChild(b);$('list').appendChild(li)});
$('next').onclick=go;$('back').onclick=back;addEventListener('keydown',function(e){if(e.key==='ArrowRight')go();if(e.key==='ArrowLeft')back()});
var q=+new URLSearchParams(location.search).get('j');if(q>=0&&q<J.length)j=q;draw();
</script></body></html>'''


# ── Showcase page ────────────────────────────────────────────────────
def ph(i, cap='', cls=''):
    t = BY[need(i)]['title']
    return '<figure class="sh %s"><img src="%s" alt="%s" loading="lazy" width="393" height="852">%s</figure>' % (cls, shot(i), esc(t), '<figcaption>%s</figcaption>' % esc(cap) if cap else '')


DECISIONS = [
    ('Put the risk before the switch', ['fo_turn_on'], 'F&O off by default. Turning it on starts with the loss figure, not the benefits.',
     'One toggle in settings, or a tick box inside a long agreement.',
     'The biggest loss in this category sits behind this single action, so this is the one place where added friction helps the user.',
     'Share of people who turn on F&O and then trade in their first week, compared with how many read the risk screen in full.'),
    ('A full-screen pad, not a swipe', ['buy_pad', 'buy_large_order_check'], 'Keypad docked, charges and cash in view. Swipe stays only for one-tap repeat orders.',
     'Swipe-to-buy on every order.',
     'Quantity and price are typed, so the keyboard should be the layout. A gesture is quick to learn but does not help someone check an order.',
     'Time to place a first order, and how often people edit an order straight after placing it.'),
    ('Placed is not filled', ['order_placed', 'buy_partly_filled', 'buy_filled'], 'A limit order gets its own waiting screen, with the gap to the last price.',
     'One "Order successful" screen for every outcome.',
     '"Success" suggests the shares are already yours. Waiting, part-filled and filled are different states with different money.',
     'Support contacts asking "where are my shares", and repeat orders placed by mistake.'),
    ('Profit after charges', ['sell_filled', 'charges_breakdown'], 'Booked profit is net of brokerage, STT and fees, so it matches the contract note.',
     'The gross figure, with charges on a separate statement.',
     'A number that differs from the contract note reads as a mistake, even when the arithmetic is right.',
     'Tickets about a profit figure that does not match the statement.'),
    ('One number leads the portfolio', ['portfolio'], 'Value first. Each holding takes two lines.',
     'A dense table for people watching sixteen holdings hourly, and a mixed view for funds and ETFs.',
     'I expect most visits to ask one question: how am I doing? The dense view stays in the design for traders; the mixed view returns when funds and ETFs ship.',
     'Time to answer "how much am I up today" in a moderated test.'),
    ('Mobile number first', ['sign_in'], 'OTP sign-in leads. Client ID is a secondary link.',
     'Client ID and password first, the older broker pattern.',
     'People coming from Groww and Kite already expect this, and a client ID is easy to forget.',
     'Sign-in success on the first try, and use of the Client ID link.'),
    ('Green means Buy, whatever the brand does', ['stock_overview'], 'Buy is green, Sell is red, always with the word. Navy is the brand.',
     'Buy in the brand colour, which is what an earlier version did.',
     'A trade button should not change meaning when the brand changes, and colour alone fails people who cannot tell the two apart.',
     'Wrong-side orders corrected within a minute.'),
]

STATES = [('funds_zero', 'Empty'), ('stock_fundamentals_loading', 'Loading'), ('buy_rejected', 'Rejected'), ('bank_declined', 'Bank declined'),
          ('buy_partly_filled', 'Part-filled'), ('add_funds_pending', 'Waiting on the bank'), ('report_delayed', 'Running late'), ('sip_mandate_expired', 'Expired'),
          ('basket_leg_rejected', 'One leg failed'), ('kill_switch', 'Stop everything')]

INSIGHTS = [
    ('F&O losses', 'Leverage is one toggle away, and the possible loss is rarely on screen at that moment.', 'A gate before F&O, and the most you can lose shown on the order.', 'option_buy_pad'),
    ('Confusing order types', 'Limit, GTT, SL-M and AMO are exchange words, not choices a new investor can weigh.', 'Plain names with one line each, and terms explained the first time they matter.', 'order_types'),
    ('Slow KYC', 'A long form hides how much is left, and failures rarely say what to do next.', 'Short steps with a clear next action, and every failure has its own screen.', 'kyc_account_ready'),
    ('Hidden charges', 'The price on the button is rarely what leaves the account.', 'Total shown before the order, and a full breakdown one tap away.', 'charges_breakdown'),
]

PERSONAS = [
    ('Aarav', '27, first-time investor', 'Wants to understand before acting, and fears the wrong tap.'),
    ('Meera', '41, long-term SIP investor', 'Checks weekly and needs tax clarity at filing time.'),
    ('Rahul', '33, active F&O trader', 'Opens the app many times a day and wants margin and depth at a glance.'),
    ('Savitri', '62, careful and low in confidence', 'Needs readable text, and signals that are not colour alone.'),
]

TOKENS = [('Navy', '#0F2942', 'Brand, primary action'), ('Ink', '#0A1120', 'Text'), ('Slate', '#475569', 'Secondary text'), ('Mist', '#F1F5F9', 'Surfaces'),
          ('Gain', '#057A55', 'Buy, profit'), ('Loss', '#C81E1E', 'Sell, loss'), ('Signal', '#C2410C', 'Attention, orange text'), ('Night', '#070B14', 'Dark background')]

CONTRAST = [('Body text on white', '#0A1120', '#FFFFFF', '18.85'), ('Secondary on surface', '#475569', '#F1F5F9', '6.92'), ('White on navy button', '#FFFFFF', '#0F2942', '14.83'),
            ('White on Buy', '#FFFFFF', '#057A55', '5.36'), ('White on Sell', '#FFFFFF', '#C81E1E', '5.74'), ('Orange text on white', '#C2410C', '#FFFFFF', '5.18'),
            ('Dark theme text', '#E8EEF7', '#070B14', '16.87'), ('Dark theme accent', '#38BDF8', '#070B14', '9.19')]

SPEC = [(2, 'Trader home, denser mode'), (6, 'Order reconciling'), (10, 'Kill switch limits'), (11, 'Physical delivery warning'), (13, 'FIFO tax lots'), (17, 'UPI trading block')]


def page():
    secs, order = {}, []
    for m in MAN:
        s = m['section'] or 'Other'
        if s not in secs:
            secs[s] = {'n': 0, 'sec': m['sec']}
            order.append(s)
        secs[s]['n'] += 1
    full = sum(1 for m in MAN if '_full' in m['id'])
    low = sum(1 for m in MAN if m['low'])
    over = sum(1 for m in MAN if m['over'])
    data = [{'i': m['id'], 't': m['title'], 's': m['section'] or 'Other', 'f': int('_full' in m['id'])} for m in MAN]
    dec = ''
    for n, (t, ids, chose, rej, why, measure) in enumerate(DECISIONS):
        vis = ('<div class="seq">%s</div>' % ''.join('<img src="%s" alt="%s" loading="lazy">' % (shot(i), esc(BY[i]['title'])) for i in ids)) if len(ids) == 3 else ''.join(ph(i) for i in ids)
        dec += ('<article class="dec"><div class="dv c%d">%s</div><div><span class="n">%02d</span><h3>%s</h3><p class="big">%s</p><dl>'
                '<dt>Instead of</dt><dd>%s</dd><dt>Because</dt><dd>%s</dd><dt>I would measure</dt><dd>%s</dd></dl></div></article>') % (min(len(ids), 2), vis, n + 1, esc(t), esc(chose), esc(rej), esc(why), esc(measure))
    wire_ids = ['home', 'stock_overview', 'buy_pad', 'portfolio', 'option_chain']
    tabs = ''.join('<button class="chip" data-w="%s"%s>%s</button>' % (i, ' aria-pressed="true"' if n == 0 else ' aria-pressed="false"', esc(BY[i]['title'])) for n, i in enumerate(wire_ids))
    rep = {
        '__COUNT__': str(len(MAN)), '__PHONE__': str(len(MAN) - full), '__FULL__': str(full), '__SECS__': str(len(order)),
        '__DECISIONS__': dec, '__WTABS__': tabs,
        '__INSIGHTS__': ''.join('<article class="ins"><div class="iv">%s</div><div><h3>%s</h3><p>%s</p><p class="to">%s</p></div></article>' % (ph(i), esc(a), esc(b), esc(c)) for a, b, c, i in INSIGHTS),
        '__PERSONAS__': ''.join('<div class="pers"><b>%s</b><span>%s</span><p>%s</p></div>' % (esc(a), esc(b), esc(c)) for a, b, c in PERSONAS),
        '__STATES__': ''.join(ph(i, cap) for i, cap in STATES),
        '__BIG__': ''.join(ph(i, cap) for i, cap in (('portfolio_200pct', 'Portfolio at 200% text'), ('sell_pad_200pct', 'Sell pad at 200% text'), ('option_buy_pad_200pct', 'Option pad at 200% text'))),
        '__TOKENS__': ''.join('<div class="sw"><i style="background:%s"></i><b>%s</b><code>%s</code><span>%s</span></div>' % (h, n, h, u) for n, h, u in TOKENS),
        '__CONTRAST__': ''.join('<tr><td><span class="aa" style="background:%s;color:%s">Aa</span></td><td>%s</td><td class="num">%s:1</td></tr>' % (bg, fg, esc(t), r) for t, fg, bg, r in CONTRAST),
        '__DARK__': ''.join('<div class="dl">%s<figure class="sh"><img src="%s" alt="%s, dark theme" loading="lazy"></figure></div>' % (ph(i), shot(i, 'v5/dark'), esc(BY[i]['title'])) for i in ('stock_overview', 'portfolio')),
        '__MAP__': ''.join('<li><button class="row" data-sec="%s"><span>%s</span><b>%s</b><em>%d</em></button></li>' % (esc(s), esc(secs[s]['sec']), esc(s), secs[s]['n']) for s in order),
        '__CHIPS__': '<button class="chip" data-f="" aria-pressed="false">All %d</button>' % len(MAN) + ''.join('<button class="chip" data-f="%s" aria-pressed="%s">%s</button>' % (esc(s), 'true' if n == 0 else 'false', esc(s)) for n, s in enumerate(order)),
        '__SPEC__': ''.join('<figure class="sh"><img src="v4/shots/n%02d.png" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>' % (n, esc(c), esc(c)) for n, c in SPEC),
        '__LOW__': str(low), '__OVER__': str(over),
        '__DATA__': json.dumps(data, ensure_ascii=False).replace('</', '<\\/'),
    }
    out = PAGE
    for k, v in rep.items():
        out = out.replace(k, v)
    (ROOT / 'showcase.html').write_text(out)
    print('page', len(out) // 1024, 'KB; audit: low', low, 'over', over, [m['id'] for m in MAN if m['low']][:8], [m['id'] for m in MAN if m['over']][:12])


PAGE = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Crestline, a concept broking app · Vikas Banjare</title>
<meta name="description" content="A self-initiated concept: an Indian investing and trading app designed around the moments where people lose money or get stuck.">
<meta property="og:title" content="Crestline, a concept broking app"><meta property="og:image" content="https://vikasbanjare.github.io/vikas-portfolio/case-studies/crestline/v5/mockups/hero.jpg">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--ink:#0A1120;--ink2:#475569;--navy:#0F2942;--deep:#0A1E33;--paper:#FFFFFF;--mist:#F1F5F9;--mist2:#E2E8F0;--signal:#C2410C;--ease:cubic-bezier(.2,.7,.3,1)}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth;scroll-padding-top:72px}
body{font:17px/1.6 Inter,system-ui,sans-serif;color:var(--ink);background:var(--paper);-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{display:block;max-width:100%;height:auto}a{color:inherit}button{font:inherit;color:inherit}
h1,h2,h3{font-family:Manrope,sans-serif;letter-spacing:-.025em;line-height:1.12}
.w{max-width:1200px;margin:0 auto;padding:0 clamp(16px,4vw,40px)}
section{padding:clamp(64px,9vw,120px) 0}.tint{background:var(--mist)}.dark{background:var(--navy);color:#fff}
.eb{display:block;font:500 12.5px 'JetBrains Mono',monospace;letter-spacing:.04em;color:var(--signal);margin-bottom:14px}.dark .eb{color:#FDBA74}
h2{font-size:clamp(30px,4.2vw,50px);font-weight:800;max-width:17em}.sub{margin-top:16px;max-width:38em;color:var(--ink2);font-size:18px}.dark .sub{color:#CBD5E1}
nav.top{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.94);backdrop-filter:blur(10px)}
nav.top .w{display:flex;align-items:center;gap:22px;height:58px;font-size:14.5px;font-weight:500}nav.top a{text-decoration:none;color:var(--ink2);white-space:nowrap}nav.top a:hover{color:var(--ink)}
nav.top .home{color:var(--ink);font-weight:600;margin-right:auto}nav.top .links{display:flex;gap:20px;overflow-x:auto;scrollbar-width:none}
:focus-visible{outline:3px solid var(--signal);outline-offset:3px;border-radius:6px}
.hero{padding:clamp(40px,6vw,76px) 0 0;background:var(--navy);color:#fff}.tagc{font:500 13px 'JetBrains Mono',monospace;color:#FDBA74}
.hero h1{font-size:clamp(52px,10vw,124px);font-weight:800;letter-spacing:-.045em;line-height:.98;margin-top:16px}
.hero .lede{font-size:clamp(20px,2.5vw,30px);line-height:1.3;max-width:24em;margin-top:18px;font-family:Manrope,sans-serif;font-weight:500;color:#E2E8F0}
.hero img{margin:clamp(24px,4vw,44px) auto 0;width:100%;max-width:1320px}
.cta{display:inline-flex;align-items:center;min-height:48px;padding:0 22px;border-radius:999px;background:#fff;color:var(--navy);font-weight:600;text-decoration:none;margin:26px 10px 0 0}.cta.alt{background:rgba(255,255,255,.13);color:#fff}
.cta.solid{background:var(--navy);color:#fff}.cta.soft{background:var(--mist2);color:var(--ink)}
.tldr{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:26px;padding:clamp(30px,4vw,46px) 0}.tldr b{display:block;font:500 12.5px 'JetBrains Mono',monospace;color:var(--signal);margin-bottom:8px}.tldr p{font-size:15px;line-height:1.5}
.stat{font:800 clamp(72px,14vw,176px)/.95 Manrope,sans-serif;letter-spacing:-.05em}
.two{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(30px,6vw,88px);align-items:start;margin-top:40px}
.src{font-size:13.5px;color:#CBD5E1;margin-top:14px}.src a{color:#fff}
.gaps{display:grid;gap:18px;list-style:none}.gaps b{display:block;font:700 19px Manrope,sans-serif}.gaps span{color:#CBD5E1;font-size:15.5px}
.roles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:40px}.card{background:var(--mist);border-radius:18px;padding:24px}.tint .card{background:#fff}.card h3{font-size:19px;margin-bottom:10px}.card li{margin:6px 0 0 18px;font-size:15.5px;color:var(--ink2)}.card p{font-size:15.5px;color:var(--ink2)}
.sh{margin:0}.sh img{width:100%;filter:drop-shadow(0 18px 26px rgba(10,17,32,.16))}.sh figcaption{margin-top:12px;font-size:14px;color:var(--ink2);text-align:center}
.inss{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:40px}.ins{display:grid;grid-template-columns:150px minmax(0,1fr);gap:22px;background:#fff;border-radius:20px;padding:22px;align-items:center}
.ins h3{font-size:21px}.ins p{font-size:15.5px;color:var(--ink2);margin-top:8px}.ins .to{color:var(--ink);font-weight:500}
.perss{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;margin-top:30px}.pers b{font:700 19px Manrope,sans-serif;display:block}.pers span{font-size:14px;color:var(--ink2)}.pers p{font-size:15px;margin-top:6px}
.note{font-size:14.5px;color:var(--ink2);margin-top:20px;max-width:46em}
.dec{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,6vw,90px);align-items:center;padding:clamp(40px,6vw,76px) 0}.dec+.dec{box-shadow:0 -1px 0 var(--mist2)}
.dv{display:flex;gap:16px;justify-content:center}.dv .sh{width:min(100%,300px)}.dv.c2 .sh{width:min(48%,260px)}
.dec .n{font:500 13px 'JetBrains Mono',monospace;color:var(--signal)}.dec h3{font-size:clamp(26px,3vw,36px);font-weight:800;margin-top:6px}.big{font-size:19px;margin-top:12px}
dl{margin-top:20px;display:grid;grid-template-columns:130px minmax(0,1fr);gap:10px 18px;font-size:15.5px}dt{font-weight:600}dd{color:var(--ink2)}
.seq{position:relative;width:min(100%,300px);aspect-ratio:393/852;filter:drop-shadow(0 18px 26px rgba(10,17,32,.16))}.seq img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top;opacity:0;animation:seq 9s infinite}.seq img:nth-child(2){animation-delay:3s}.seq img:nth-child(3){animation-delay:6s}
@keyframes seq{0%,3%{opacity:0}6%,33%{opacity:1}37%,100%{opacity:0}}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px}.chip{border:0;background:var(--mist2);border-radius:999px;padding:0 15px;min-height:40px;font-size:14px;font-weight:500;cursor:pointer}.chip:hover{background:#CBD5E1}.chip[aria-pressed=true]{background:var(--navy);color:#fff}
.cmp-wrap{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:clamp(30px,6vw,80px);align-items:center;margin-top:30px}
.cmp{position:relative;aspect-ratio:393/852;border-radius:44px;overflow:hidden;box-shadow:0 24px 48px -18px rgba(10,17,32,.28);background:#fff}.cmp img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top}.cmp .hi{clip-path:inset(0 0 0 50%)}
.cmp i{position:absolute;top:0;bottom:0;left:50%;width:2px;background:var(--navy);pointer-events:none}.cmp i::after{content:"↔";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:38px;height:38px;border-radius:50%;background:var(--navy);color:#fff;display:grid;place-items:center;font-style:normal;font-size:15px}
.cmp input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.map{list-style:none;columns:2;column-gap:34px;margin-top:0}.map li{break-inside:avoid}.row{width:100%;display:grid;grid-template-columns:38px minmax(0,1fr) auto;gap:8px;border:0;background:none;text-align:left;padding:10px 8px;border-radius:10px;cursor:pointer;min-height:44px;font-size:15px;align-items:center}.row:hover{background:var(--mist2)}.row span{font:500 12.5px 'JetBrains Mono',monospace;color:var(--ink2)}.row b{font-weight:500}.row em{font-style:normal;font:500 13px 'JetBrains Mono',monospace;color:var(--ink2)}
.frame{width:100%;height:min(960px,88vh);min-height:760px;border:0;border-radius:24px;background:var(--mist);margin-top:34px;display:block}
.grid5{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:26px 22px;margin-top:40px}.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,240px));gap:26px;margin-top:40px;justify-content:start}
.swatches{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}.sw i{display:block;height:84px;border-radius:14px;margin-bottom:10px}.sw b{display:block;font-size:15px}.sw code{font:400 12.5px 'JetBrains Mono',monospace;color:var(--ink2)}.sw span{display:block;font-size:13.5px;color:var(--ink2);margin-top:2px}
.type>div{padding:14px 0}.type small{display:block;font:500 12.5px 'JetBrains Mono',monospace;color:var(--ink2);margin-bottom:4px}
table{width:100%;border-collapse:collapse;font-size:15px}td{padding:9px 8px 9px 0;box-shadow:0 1px 0 var(--mist2)}.tint td{box-shadow:0 1px 0 #D5DDE8}.num{text-align:right;font:500 14px 'JetBrains Mono',monospace}.aa{display:inline-grid;place-items:center;width:44px;height:30px;border-radius:7px;font-weight:600;font-size:14px;box-shadow:0 0 0 1px var(--mist2)}
.comp{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.btn{display:inline-flex;align-items:center;min-height:46px;padding:0 22px;border-radius:999px;font-weight:600;font-size:15px;color:#fff}.notice{border-radius:14px;padding:14px 16px;font-size:14.5px;line-height:1.45;flex:1 1 240px}.notice b{display:block}
.dls{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px;margin-top:40px}.dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.scene{border-radius:24px;width:100%;margin-top:22px}.scenes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px;margin-top:18px}.scenes .scene{margin:0}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:24px 18px;margin-top:30px}.gal button{border:0;background:none;cursor:pointer;text-align:left;display:block;min-width:0}.gal .th{display:block;aspect-ratio:393/852;overflow:hidden;border-radius:20px;background:var(--mist)}.gal img{width:100%;height:100%;object-fit:cover;object-position:top;transition:transform .5s var(--ease)}.gal button:hover img{transform:translateY(-4px)}.gal span.c{display:block;font-size:13px;margin-top:8px;color:var(--ink2);line-height:1.3}
dialog{margin:auto;border:0;background:transparent;max-width:min(94vw,560px);max-height:96vh;overflow:visible;padding:0}dialog::backdrop{background:rgba(7,11,20,.88)}
.lb{display:grid;grid-template-columns:48px minmax(0,1fr) 48px;align-items:center;gap:10px}.lb .pic{max-height:88vh;overflow:auto;border-radius:30px;background:#fff}.lb img{width:100%}.lb button{width:48px;height:48px;border-radius:50%;border:0;background:rgba(255,255,255,.14);color:#fff;font-size:20px;cursor:pointer}
.lbcap{color:#fff;text-align:center;margin-top:8px;font-size:14.5px;display:flex;justify-content:center;gap:14px;align-items:center}.lbcap button{background:rgba(255,255,255,.14);border:0;color:#fff;border-radius:999px;min-height:40px;padding:0 16px;cursor:pointer}
.val{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:40px}.val .card{padding:28px}.tagv{font:500 12.5px 'JetBrains Mono',monospace;color:var(--signal);display:block;margin-bottom:10px}.val .fig{font:800 44px/1 Manrope,sans-serif;letter-spacing:-.03em;margin-bottom:10px}
.bugfix{display:grid;grid-template-columns:minmax(0,1fr) 220px;gap:30px;margin-top:20px;align-items:center;background:#fff;border-radius:20px;padding:28px}.bugfix code{font:400 14px 'JetBrains Mono',monospace;background:var(--mist);padding:1px 5px;border-radius:5px}
.reflect{font:600 clamp(24px,3vw,36px)/1.25 Manrope,sans-serif;letter-spacing:-.02em;max-width:26em}
.strip{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:18px;margin-top:30px}
footer{padding:48px 0 64px;font-size:14.5px;color:var(--ink2)}footer p{max-width:50em;margin-top:10px}
@media (max-width:980px){.tldr{grid-template-columns:repeat(2,minmax(0,1fr))}.two,.dec,.cmp-wrap,.roles,.inss,.val,.dls,.bugfix{grid-template-columns:1fr}.grid5{grid-template-columns:repeat(3,minmax(0,1fr))}.perss{grid-template-columns:repeat(2,minmax(0,1fr))}.strip{grid-template-columns:repeat(3,minmax(0,1fr))}.scenes{grid-template-columns:1fr}.map{columns:1}.cmp{max-width:340px;margin:0 auto}.dec .dv{order:2}}
@media (max-width:620px){body{font-size:16px}nav.top .links{display:none}.tldr{grid-template-columns:1fr}.ins{grid-template-columns:96px minmax(0,1fr);gap:14px;padding:16px}.grid5,.grid3,.strip{grid-template-columns:repeat(2,minmax(0,1fr))}.swatches{grid-template-columns:repeat(2,minmax(0,1fr))}dl{grid-template-columns:1fr;gap:2px}dd{margin-bottom:10px}.dl{gap:10px}.frame{border-radius:16px;height:1040px;min-height:0}.lb{grid-template-columns:1fr}.lb>button{display:none}.gal{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.seq img{animation:none}.seq img:nth-child(3){opacity:1}.gal img{transition:none}}
</style></head><body>
<nav class="top" aria-label="Page"><div class="w"><a class="home" href="../">← All UI/UX work</a><div class="links"><a href="#problem">Problem</a><a href="#decisions">Decisions</a><a href="#prototype">Prototype</a><a href="#app">Working app</a><a href="#system">System</a><a href="#screens">All screens</a><a href="#proof">What is proven</a></div></div></nav>
<header class="hero"><div class="w">
<span class="tagc">Self-initiated concept · fictional broker · not a live product</span>
<h1>Crestline</h1>
<p class="lede">An Indian investing and trading app designed around the moments where people lose money or get stuck.</p>
<a class="cta" href="#prototype">Try the prototype</a><a class="cta alt" href="#screens">See all __COUNT__ frames</a>
<img src="v5/mockups/hero.jpg" alt="Three phones showing the Crestline stock page, home screen and buy pad" width="1600" height="1040">
</div></header>
<div class="w"><div class="tldr">
<div><b>Problem</b><p>Broking apps make the tap easy. Losses and confusion come from what the tap hides.</p></div>
<div><b>My role</b><p>Sole designer: research framing, product decisions, flows, design system and every screen.</p></div>
<div><b>Constraints</b><p>Indian exchange and SEBI rules, no engineers, no backend, no real users to test with.</p></div>
<div><b>What I made</b><p>__PHONE__ phone frames across __SECS__ areas, __FULL__ full-scroll views, light and dark, a clickable prototype.</p></div>
<div><b>Not proven yet</b><p>No real person has used it. Testing so far is audits and a simulated study, stated below.</p></div>
</div></div>

<section class="dark" id="problem"><div class="w">
<span class="eb">The problem</span>
<p class="stat">91%</p>
<h2 style="margin-top:12px">of individual F&amp;O traders made a net loss in FY25.</h2>
<div class="two"><div><p class="sub" style="margin-top:0">Together they lost ₹1,05,603 crore, up about 41% in a year. The apps they used are fast and polished. I wanted to know what a broking app looks like if it keeps that speed and stops hiding the consequences.</p>
<p class="src">SEBI study, July 2025, reported by <a href="https://www.business-standard.com/markets/news/net-losses-of-traders-in-fo-widens-in-fy25-sebi-study-125070701221_1.html" rel="noopener">Business Standard</a> and <a href="https://moneylife.in/article/91-percentage-of-retail-traders-lost-money-in-derivatives-losses-in-fo-surged-41-percentage-to-rs105-lakh-crore-in-fy25-sebi-study/77613.html" rel="noopener">Moneylife</a>.</p></div>
<ul class="gaps"><li><b>Order types</b><span>Exchange terms stand in for choices.</span></li><li><b>Hidden charges</b><span>What leaves the account is not the number on the button.</span></li><li><b>Slow KYC</b><span>Long forms, and failures with no next step.</span></li><li><b>"Success"</b><span>A placed order reads as a bought share.</span></li></ul></div>
</div></section>

<section id="role"><div class="w">
<span class="eb">Role and limits</span><h2>A concept is only as credible as its constraints.</h2>
<div class="roles">
<div class="card"><h3>What I did</h3><ul><li>Framed the research and set the direction</li><li>Made the product decisions below</li><li>Designed flows, system and screens</li><li>Audited and revised across rounds</li></ul></div>
<div class="card"><h3>Rules I held to</h3><ul><li>Real Indian products: delivery, intraday, MTF, GTT, IPO, SIP, F&amp;O</li><li>SEBI risk wording on order screens</li><li>WCAG 2.1 AA as the baseline</li><li>Sample data that adds up across screens</li></ul></div>
<div class="card"><h3>What I did not have</h3><ul><li>Real users or analytics</li><li>Engineers or a backend</li><li>A compliance review</li><li>A client or a brief. I set my own</li></ul></div>
</div></div></section>

<section class="tint" id="research"><div class="w">
<span class="eb">Research</span><h2>Four complaints became four design briefs.</h2>
<p class="sub">Desk research: competitor apps from screenshots and recordings, what investors and traders say on X, Quora and Reddit, and 2026 data from NSE, SEBI and AMFI.</p>
<div class="inss">__INSIGHTS__</div>
<h3 style="font-size:24px;margin-top:56px">Who I designed for</h3><div class="perss">__PERSONAS__</div>
<p class="note">These four are proto-personas written from desk research, not from interviews. A study kit is ready to replace them with evidence.</p>
</div></section>

<section id="decisions" style="padding-bottom:30px"><div class="w">
<span class="eb">Decisions</span><h2>Seven calls, what I passed on, and how I would test each.</h2>
__DECISIONS__
</div></section>

<section class="tint" id="structure"><div class="w">
<span class="eb">Structure to screen</span><h2>Wireframes settled the order before any colour.</h2>
<div class="chips" id="wtabs">__WTABS__</div>
<div class="cmp-wrap"><div class="cmp" id="cmp"><img class="lo" alt="Wireframe"><img class="hi" alt="Final screen"><i></i><input type="range" min="0" max="100" value="50" aria-label="Compare wireframe and final screen"></div>
<div><p class="sub" style="margin:0 0 20px">Drag across the phone. Left is structure, right is the final screen. These wireframes are derived from the finished layouts to show the skeleton; the working rounds were separate.</p><ul class="map" style="columns:1">__MAP__</ul></div></div>
</div></section>

<section id="prototype"><div class="w">
<span class="eb">Prototype</span><h2>Nine journeys. Tap through them.</h2>
<p class="sub">Press the glowing control on the phone. Click-through of the final screens with sample data.</p>
<iframe class="frame" src="v5/prototype.html" title="Crestline click-through prototype" loading="lazy"></iframe>
<a class="cta soft" href="v5/prototype.html">Open it full screen</a>
</div></section>

<section id="app"><div class="w">
<span class="eb">Working app</span><h2>Every journey, in one app you can use.</h2>
<p class="sub">387 screens across 18 areas, in light and dark. It covers the checks and documents each product needs, turning on F&amp;O, commodities and currency, NRI and family accounts, stock SIPs, deposits, pension and insurance. Prices and orders are simulated, and nothing you type leaves the page.</p>
<a class="cta solid" href="app/">Open the working app</a>
<div class="grid3">
<figure class="sh"><img src="v5/native/kyc-hub.jpg" alt="KYC and documents screen listing what each product asks for" loading="lazy" width="660" height="1434"><figcaption>Each product asks for its own checks</figcaption></figure>
<figure class="sh"><img src="v5/native/fo-proof.jpg" alt="F&amp;O income proof screen with eight accepted documents" loading="lazy" width="660" height="1434"><figcaption>F&amp;O income proof, step by step</figcaption></figure>
<figure class="sh"><img src="v5/native/offline.jpg" alt="Home screen as skeleton shapes with a no internet card" loading="lazy" width="660" height="1434"><figcaption>No internet: skeleton shapes, then saved numbers</figcaption></figure>
</div>
<p class="sub" style="margin-top:34px">These pictures are from a native SwiftUI build of the same design, which I run on my own iPhone. It is a private build and is not on the App Store.</p>
</div></section>

<section class="tint" id="states"><div class="w">
<span class="eb">States</span><h2>Concepts usually stop at the happy path. Money apps cannot.</h2>
<p class="sub">Most trust is won or lost when something goes wrong, so each failure says what happened, where the money is and what to do next.</p>
<div class="grid5">__STATES__</div>
<h3 style="font-size:24px;margin-top:60px">Still works at 200% text</h3><p class="sub" style="font-size:16px;margin-top:8px">For people like Savitri. Screens reflow, and the numbers never shrink.</p><div class="grid3">__BIG__</div>
</div></section>

<section id="system"><div class="w">
<span class="eb">Design system</span><h2>Calm navy, three typefaces, and colour that always means something.</h2>
<div class="two"><div class="swatches">__TOKENS__</div>
<div class="type"><div><small>Manrope, headings</small><span style="font:800 34px/1.1 Manrope,sans-serif;letter-spacing:-.02em">Sell three losers</span></div><div><small>Inter, reading</small><span style="font-size:17px">Your bank may take up to 30 minutes to confirm.</span></div><div><small>JetBrains Mono, every figure</small><span style="font:500 28px 'JetBrains Mono',monospace">₹1,24,500.75</span></div></div></div>
<div class="two"><div><h3 style="font-size:22px;margin-bottom:14px">Measured contrast</h3><table>__CONTRAST__</table><p class="note">Signal orange #EA580C measures 3.56:1 on white, which fails for small text. Orange words use #C2410C instead.</p></div>
<div><h3 style="font-size:22px;margin-bottom:14px">Core parts</h3><div class="comp"><span class="btn" style="background:#057A55">Buy 10</span><span class="btn" style="background:#C81E1E">Sell 10</span><span class="btn" style="background:#0F2942">Add funds</span></div>
<div class="comp" style="margin-top:14px"><div class="notice" style="background:rgba(200,30,30,.09)"><b>Not placed</b>The limit is above today's price band.</div><div class="notice" style="background:rgba(180,83,9,.1)"><b>Approve by 3 pm</b>Your UPI request expires today.</div></div>
<p class="note">Warnings are tinted surfaces, never outlines. The kit covers every state of each component, two icon sets and content rules, in light and dark.</p></div></div>
<img class="scene" style="margin-top:50px" src="v5/mockups/pair.jpg" alt="The Crestline home screen in light and dark themes" loading="lazy" width="1600" height="900">
<div class="dls">__DARK__</div>
</div></section>

<section class="tint" id="mockups"><div class="w">
<span class="eb">In the round</span><h2>One product, end to end.</h2>
<img class="scene" src="v5/mockups/wall.jpg" alt="A wall of Crestline screens from sign-in to tax reports" loading="lazy" width="1600" height="900">
<div class="scenes" style="margin-top:22px"><img class="scene" src="v5/mockups/iso.jpg" alt="Error and waiting states arranged at an angle" loading="lazy" width="1600" height="900"><img class="scene" src="v5/mockups/cover.jpg" alt="Stock page, home and portfolio screens" loading="lazy" width="1200" height="750"></div>
</div></section>

<section id="screens"><div class="w">
<span class="eb">Everything</span><h2>All __COUNT__ frames.</h2>
<p class="sub">__PHONE__ phone frames and __FULL__ full-scroll views, by area. Open any one to read it at full size.</p>
<div class="chips" id="chips">__CHIPS__</div><div class="gal" id="gal"></div>
</div></section>

<section class="tint" id="proof"><div class="w">
<span class="eb">What is proven, and what is not</span><h2>Nothing here has met a real user yet.</h2>
<div class="val">
<div class="card"><span class="tagv">Expert review</span><p class="fig">8 rounds</p><p>UX audits as new and experienced users, then a multi-persona and WCAG 2.1 AA audit of about 230 frames, plus light-theme and 200% text checks.</p></div>
<div class="card"><span class="tagv">Simulated, not people</span><p class="fig">26 of 32 tasks</p><p>A simulated test with 8 personas completed these without help and surfaced 12 issues, which I fixed. It finds friction cheaply. It does not stand in for real behaviour.</p></div>
<div class="card"><span class="tagv">Automated check on this set</span><p class="fig">__COUNT__ frames</p><p>Each frame was measured for text contrast and overflow after the final pass: __LOW__ with contrast warnings and __OVER__ overflow flags. Five are hidden arrow labels in sideways-scrolling rows. The other is real and still open: at 200% text the option chain runs wider than the screen.</p></div>
<div class="card"><span class="tagv">Not done</span><p class="fig">Real people</p><p>Still to do: a study with real investors, a built demo, compliance review, real stock logos and final legal text. The study kit, with recruitment, 9 tasks and pass targets, is ready.</p></div>
</div>
<div class="bugfix"><div><h3 style="font-size:24px">A final pass still found a real bug.</h3><p style="margin-top:10px;color:var(--ink2);font-size:16px">The lump-sum calculator showed <code>₹Infinity Cr in 100000 years</code>. The code looked for a field with "time" in its name and matched "One-<b>time</b> amount". Rounds of screen review had missed it, because a calculator is easy to skim. Fixed, along with coloured card outlines, a clipped Buy button and a period chip with unreadable text.</p></div>
<figure class="sh" style="max-width:200px;margin:auto">__CALC__</figure></div>
</div></section>

<section id="outcome"><div class="w">
<span class="eb">If it shipped</span><h2>What I expect to change, and how I would know.</h2>
<table style="margin-top:30px"><tr><td><b>Wrong-assumption tickets</b></td><td style="color:var(--ink2)">"Where are my shares", "why does my profit differ". Fewer, per 1,000 orders.</td></tr><tr><td><b>First order</b></td><td style="color:var(--ink2)">Share of funded accounts placing an order, and how often it is edited at once.</td></tr><tr><td><b>F&amp;O activation</b></td><td style="color:var(--ink2)">Deliberately lower is fine. Watch early losses per new F&amp;O user instead.</td></tr><tr><td><b>KYC completion</b></td><td style="color:var(--ink2)">Drop-off at each step, and recovery after a failure.</td></tr></table>
<p class="note">No baselines exist, so I have set no targets. These are the measures, not results.</p>
<p class="reflect" style="margin-top:60px">I set out to design a broker. The real work was writing what happens after the tap, and the next step is to watch real people use it before I add a single screen.</p>
<h3 style="font-size:24px;margin-top:60px">Still in the spec</h3><p class="sub" style="font-size:16px;margin-top:8px">A later review listed blind spots the hi-fi set does not cover yet. These are rougher explorations, kept separate from the main set.</p>
<div class="strip">__SPEC__</div>
<a class="cta soft" href="v4/case-study.html">Read the full specification</a>
</div></section>

<footer><div class="w"><b style="color:var(--ink)">Credits and how this was made</b>
<p>Concept, research framing and design direction by Vikas Banjare. I set the brief, the research framing and the design direction. Screens, specifications and documentation were produced with AI assistance and directed and reviewed by me.</p>
<p>Crestline is fictional. Figures are sample data. Company names appear only to make the examples realistic, with no affiliation implied. This is not investment advice.</p>
<a class="cta soft" href="../">Back to all work</a></div></footer>
<dialog id="lb" aria-label="Screen viewer"><div class="lb"><button id="lbp" aria-label="Previous">←</button><div class="pic"><img id="lbi" alt=""></div><button id="lbn" aria-label="Next">→</button></div><div class="lbcap"><span id="lbc"></span><button id="lbx">Close</button></div></dialog>
<script>
var D=__DATA__,$=function(i){return document.getElementById(i)},cur=[],at=0;
function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML}
function src(i){return 'v5/screens/'+i+'.webp'}
function show(f){cur=D.filter(function(x){return !f||x.s===f});$('gal').innerHTML=cur.map(function(x,n){return '<button data-n="'+n+'"><span class="th"><img src="'+src(x.i)+'" alt="" loading="lazy"></span><span class="c">'+esc(x.t)+(x.f?' · full scroll':'')+'</span></button>'}).join('');[].forEach.call($('chips').children,function(c){c.setAttribute('aria-pressed',c.getAttribute('data-f')===f)})}
function open_(n){at=(n+cur.length)%cur.length;$('lbi').src=src(cur[at].i);$('lbi').alt=cur[at].t;$('lbc').textContent=cur[at].t+' · '+(at+1)+' of '+cur.length;$('lb').querySelector('.pic').scrollTop=0;if(!$('lb').open)$('lb').showModal()}
$('chips').addEventListener('click',function(e){var b=e.target.closest('.chip');if(b)show(b.getAttribute('data-f'))});
$('gal').addEventListener('click',function(e){var b=e.target.closest('button');if(b)open_(+b.getAttribute('data-n'))});
$('lbp').onclick=function(){open_(at-1)};$('lbn').onclick=function(){open_(at+1)};$('lbx').onclick=function(){$('lb').close()};
$('lb').addEventListener('click',function(e){if(e.target===$('lb'))$('lb').close()});
$('lb').addEventListener('keydown',function(e){if(e.key==='ArrowRight')open_(at+1);if(e.key==='ArrowLeft')open_(at-1)});
document.querySelectorAll('.row').forEach(function(r){r.onclick=function(){show(r.getAttribute('data-sec'));location.hash='screens'}});
show($('chips').children[1].getAttribute('data-f'));
var cmp=$('cmp'),lo=cmp.querySelector('.lo'),hi=cmp.querySelector('.hi'),rng=cmp.querySelector('input'),bar=cmp.querySelector('i');
function pick(i){lo.src='v5/wire/'+i+'.webp';hi.src=src(i)}
rng.addEventListener('input',function(){hi.style.clipPath='inset(0 0 0 '+rng.value+'%)';bar.style.left=rng.value+'%'});
$('wtabs').addEventListener('click',function(e){var b=e.target.closest('.chip');if(!b)return;[].forEach.call(this.children,function(c){c.setAttribute('aria-pressed',c===b)});pick(b.getAttribute('data-w'))});
pick($('wtabs').children[0].getAttribute('data-w'));
</script></body></html>'''
PAGE = PAGE.replace('__CALC__', '<img src="v5/screens/calc_lump_sum.webp" alt="Lump-sum calculator, fixed, showing 2.6 lakh in 10 years" loading="lazy">')

if __name__ == '__main__':
    todo = sys.argv[1:] or ['mock', 'proto', 'page']
    if 'mock' in todo: mockups()
    if 'proto' in todo: prototype()
    if 'page' in todo: page()
