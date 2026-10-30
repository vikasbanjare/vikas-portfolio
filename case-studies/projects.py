"""Per-project content for showcase_gen.py. Copy comes from the source material only."""
import showcase_gen as g

SANS_LATO = '"Lato",system-ui,sans-serif'
FONT_PLAYFAIR_LATO = 'https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&family=Playfair+Display:ital,wght@1,400;1,500&display=swap'
MOHIT_WEB = 'https://mohitmehra.framer.website/website-ui-design'
MOHIT_APP = 'https://mohitmehra.framer.website/wealthy-mobile-ui'
SW = lambda *a: [(n, c, t) for n, c, t in a]


# ------------------------------------------------------------------ Wealthy website UI
def wealthy_web():
    S = []
    S.append(g.intro('The brief', 'Structured UI for <span class="serif">trust and demos.</span>',
        'A website UI for Wealthy, a fintech platform built for distributors. The goal: move the site from a long feature list to a clear platform story that earns trust and drives demo bookings.',
        [('From listing to positioning', 'The product list becomes a platform story with a clear hierarchy.'),
         ('Modular product clarity', 'Products are grouped into scannable modules instead of one dense list.'),
         ('Tech-first positioning', 'Technology and API credibility sit next to the sales message.')]))
    S.append(g.section(
        g.heading('The page', 'The whole site, <span class="serif">top to bottom.</span>', 'Scroll the frame to move through the full page design.')
        + '<div class="rv" style="margin-top:46px;max-width:760px;margin-left:auto;margin-right:auto">' + g.browser_frame('img/fullpage.png') + '</div>', band=True))
    S.append(g.section(
        g.heading('Positioning gap', 'From feature listing to <span class="serif">platform positioning.</span>')
        + g.beforeafter(['Dense product listing', 'Weak hierarchy', 'Limited tech emphasis'],
                        ['Modular product clarity', 'Strong section structure', 'Tech-first positioning'])))
    S.append(g.section(
        g.heading('Execution framework', 'Outcome-focused, <span class="serif">in three phases.</span>',
                  'Each phase prioritised clarity, hierarchy and conversion, so the experience reflects the scale and technology behind Wealthy.')
        + g.lists3([('Research & positioning', ['Distributor persona', 'Market audit', 'Competitor analysis', 'Business goals']),
                    ('Architecture & systems', ['Content hierarchy', 'Platform flow', 'Feature grouping', 'CTA mapping']),
                    ('Interface & refinement', ['UI system', 'Component consistency', 'Hierarchy & spacing', 'Handoff & polish'])]), band=True))
    S.append(g.section(
        g.heading('Information architecture', 'Authority before capability, <span class="serif">trust before conversion.</span>',
                  'Each section builds on the previous one.')
        + g.steps([('01', 'Authority', 'Establish scale and credibility first.'), ('02', 'Products', 'Modular product ecosystem.'),
                   ('03', 'Onboarding', 'A clear, step-by-step path in.'), ('04', 'Conversion', 'CTAs near high-intent sections.'),
                   ('05', 'Capability', 'What the platform can do.'), ('06', 'Tech', 'Technology and API credibility.'),
                   ('07', 'Support', 'Help when it is needed.')], cols=4)))
    S.append(g.section(
        g.spread('01', 'Product ecosystem', [('Modular grouping', 'improves scan speed.'), ('Feature clusters', 'reduce cognitive load.'),
                                          ('CTA anchored', 'near high-intent sections.')], ['Products', 'Hierarchy', 'CTA'],
                 g.flat_vis('img/home.jpg'))
        + '<div class="gap"></div>'
        + g.spread('02', 'Onboarding & tech', [('Step-by-step flow', 'reduces drop-off.'), ('Tech credibility', 'reinforces trust.'),
                                              ('API documentation', 'signals capability.')], ['Onboarding', 'Platform', 'Trust'],
                   g.flat_vis('img/hero.jpg'), flip=True), band=True))
    S.append(g.section(
        g.heading('Live today', 'The site, <span class="serif">as it ships.</span>', 'Captured from wealthy.in with permission. Scroll inside each frame.')
        + '<div class="duo rv"><div>' + g.browser_frame('img/live-home.jpg', 'Home page · scroll inside the frame') + '</div><div>' + g.mobile_frame('img/live-mobile.jpg', 'Home on mobile') + '</div></div>'
        + '<div class="cols2 rv" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;margin-top:40px"><div>' + g.browser_frame('img/live-calculators.jpg', 'Calculators') + '</div><div>' + g.browser_frame('img/live-insights.jpg', 'Insights') + '</div></div>', band=True))
    S.append(g.section(
        g.heading('Visual system', 'Typography <span class="serif">and colour.</span>',
                  'Brand purple is used strategically to signal trust and drive action, paired with bold, confident typography that establishes strong hierarchy and clarity.')
        + g.system(SW(('Brand purple', '#5F29EB', '#fff'), ('White', '#FFFFFF', '#1a1030'), ('Soft purple', '#927EC7', '#fff'),
                     ('Black', '#000000', '#fff'), ('Lavender tint', '#F9F6FE', '#1a1030'), ('Cream', '#FCF5E7', '#1a1030')),
                   'Aa Playfair', 'font-family:\'Playfair Display\',serif;font-style:italic',
                   [('Headlines', 'Playfair · Bold'), ('Body', 'Lato · Regular'), ('Labels', 'Lato · Medium / Semibold')],
                   'Components', '<div style="display:grid;gap:14px;margin-top:20px"><div style="background:#5F29EB;color:#fff;border-radius:99px;padding:14px 22px;font-weight:700;text-align:center">Book a demo</div><div style="background:#F9F6FE;color:#1a1030;border-radius:18px;padding:18px;font-weight:700">Products<br><span style="font-weight:400;font-size:14px;color:#6a5f8f">Modular, scannable, calm.</span></div><div style="background:#FCF5E7;color:#1a1030;border-radius:18px;padding:18px;font-weight:700">Trust strip<br><span style="font-weight:400;font-size:14px;color:#7a6a45">Authority first.</span></div></div>'))
        )
    S.append(g.section(
        g.heading('Conversion & clarity', 'Design outcomes, <span class="serif">in four lines.</span>')
        + g.steps([('1', 'Stronger feature comprehension', 'Modular layouts enable faster scanning and understanding.'),
                   ('2', 'Clearer tech positioning', 'API-first messaging reinforces platform credibility.'),
                   ('3', 'Higher CTA visibility', 'Strategic placement at high-intent decision points.'),
                   ('4', 'Reduced cognitive friction', 'Progressive disclosure over information overload.')], cols=4), band=True))
    S.append(g.section(
        g.heading('Execution', 'Four days. <span class="serif">One system.</span>', 'Focused and outcome driven.')
        + g.steps([('Day 1', 'Research', 'Understanding how distributors actually work and where they face friction.'),
                   ('Day 2', 'Architecture', 'Simplifying the structure so everything is easier to find.'),
                   ('Day 3', 'Wireframes', 'Exploring layouts to make the experience more intuitive.'),
                   ('Day 4', 'Visual refinement', 'Improving clarity and consistency across screens.'),
                   ('Day 5', 'Final refinement', 'Polishing and aligning everything before delivery.')])
        + '<div style="text-align:center">' + g.credit('MM', 'Designed by <b>Mohit Mehra</b> &middot; view the original case study', MOHIT_WEB) + '</div>'))
    return dict(title='Wealthy Website UI Showcase', desc='Structured UI for trust and demo conversions: Wealthy fintech website, 2025.',
                bg='#0E0A22', bg2='#140F2E', surface='#1B1540', mut='#B3ABD2', mut2='#9890BC', accent='#8B63FF', accent_ink='#fff',
                sans=SANS_LATO, serif='"Playfair Display",serif', fonts=FONT_PLAYFAIR_LATO,
                herobg='radial-gradient(900px 520px at 50% 12%,#3A1D9B 0%,rgba(14,10,34,0) 70%),#0E0A22',
                kicker='Fintech · Website UI · 2025', h1='Wealthy <span class="serif">website</span>',
                lede='Structured UI focused on trust and demo conversions.', hero_vis=g.hero_fig('img/laptop.jpg', 'Wealthy website on a laptop'),
                meta=[('Design', 'Mohit Mehra'), ('Company', 'Wealthy'), ('Service', 'Website UI'), ('Year', '2025')],
                sections=S, stepcols=4, swn=6, outro_h2='More work, <span class="serif">same care.</span>',
                footer='Wealthy website UI &middot; design by <a href="' + MOHIT_WEB + '" target="_blank" rel="noopener">Mohit Mehra</a> &middot; showcased by Vikas Banjare',
                nav_label='Original case study', nav_link=MOHIT_WEB)


# ------------------------------------------------------------------ Wealthy Partner App
def wealthy_app():
    S = []
    S.append(g.intro('Overview', 'Faster decisions, <span class="serif">less effort.</span>',
        'Built for distributors managing multiple clients and portfolios, the Wealthy Partner App supports fast, everyday decision-making. As the product evolved, growing complexity began to slow users down. The redesign simplifies the experience and brings clarity to key information.',
        [('Visual direction', 'Shaping the overall visual language, tone and interaction patterns.'),
         ('Design system', 'UI guidelines and a consistent, scalable system across the app.'),
         ('Cross-functional work', 'Close work with product and engineering to keep the interface clean and scalable.')]))
    S.append(g.section(
        g.heading('The screens', 'Core screens, <span class="serif">one language.</span>')
        + g.strip(['img/s0%d.png' % i if i < 10 else 'img/s%d.png' % i for i in range(1, 7)],
                  ['Home', 'Client profile', 'Tax saver', 'Wealth view', 'Mutual funds', 'Home, expanded']), band=True))
    S.append(g.section(
        g.spread('01', 'Structural re-architecture', [('Clearer modules.', 'The app was reorganised into clear functional modules.'),
                 ('Faster navigation.', 'Distributors can quickly find clients, portfolios and transactions.'),
                 ('Less load.', 'Each module reduces cognitive load and surfaces key actions first.')], ['Modules', 'Navigation', 'IA'], g.phone_vis('img/s05.png'))
        + '<div class="gap"></div>'
        + g.spread('02', 'Stronger visual hierarchy', [('Key metrics up front.', 'Important financial data is easy to scan instantly.'),
                 ('Quick actions surfaced.', 'The actions that matter stay visible to support faster decisions.')], ['Hierarchy', 'Data', 'Actions'],
                   g.phone_vis('img/s02.png'), flip=True)))
    S.append(g.section(
        g.heading('Problem & solution', 'Dense interface, <span class="serif">clearer paths.</span>',
                  'As the app expanded with more features, the interface started to feel dense and harder to navigate. Distributors struggled to quickly scan financial data and access important actions.')
        + g.beforeafter(['Dense, feature-heavy screens', 'Hard to scan financial data', 'Important actions buried'],
                        ['Clear functional modules', 'Strong visual hierarchy', 'Key metrics and quick actions surfaced']), band=True))
    S.append(g.section(
        g.heading('Design objective', 'Three principles <span class="serif">guided the redesign.</span>')
        + g.steps([('1', 'Visual clarity over complexity', 'Financial information should be easy to scan instantly.'),
                   ('2', 'Speed over friction', 'Users should complete tasks quickly.'),
                   ('3', 'Action over browsing', 'Important actions must remain visible.')], cols=3)
        + '<p class="quote rv" style="margin-top:70px">&ldquo;Can a distributor act faster here?&rdquo;</p><p class="p rv" style="margin:18px auto 0;text-align:center">This question guided many design decisions.</p>'))
    S.append(g.section(
        g.heading('More screens', 'Across the <span class="serif">whole app.</span>')
        + g.strip(['img/s%02d.png' % i for i in range(7, 14)][:7], ['Screen 07', 'Screen 08', 'Screen 09', 'Screen 10', 'Screen 11', 'Screen 12', 'Screen 13']), band=True))
    S.append(g.section(
        g.heading('Information architecture', 'Five modules, <span class="serif">one clear map.</span>', 'Get started leads to log in or sign up. From there the app splits into Home (quick actions and portfolio), Proposals (insights, choose a client), Store (all products), Clients (dashboard) and Resources (sales kit, poster gallery).')
        + '<div class="rv" style="margin-top:46px;background:#fff;border-radius:28px;padding:28px"><img src="img/ia-map.svg" alt="Information architecture map" style="width:100%"></div>'))
    S.append(g.section(
        g.heading('System', 'One purple, <span class="serif">used with care.</span>')
        + g.system(SW(('Partner purple', '#6725F4', '#fff'), ('Lavender', '#F8F4FF', '#1c1c1c'), ('Gain green', '#4FC16F', '#0b2a14'),
                     ('Alert red', '#FF4E4E', '#fff'), ('Ink', '#1C1C1C', '#fff'), ('Grey', '#7E7E7E', '#fff')),
                   'Aa Lato', 'font-family:Lato,sans-serif;font-weight:900',
                   [('Typeface', 'Lato'), ('Scale', 'Defined type scale'), ('Colour', 'Purple for action, green and red for gain and loss')],
                   'Components', '<div style="display:grid;gap:14px;margin-top:20px"><div style="background:#6725F4;color:#fff;border-radius:14px;padding:14px;font-weight:700;text-align:center">Complete Now</div><div style="background:#F8F4FF;color:#1c1c1c;border-radius:16px;padding:16px;display:flex;justify-content:space-between"><b>Portfolio</b><b style="color:#4FC16F">+12.5%</b></div><div style="background:#F8F4FF;color:#1c1c1c;border-radius:16px;padding:16px;display:flex;justify-content:space-between"><b>Pending</b><b style="color:#FF4E4E">Action needed</b></div></div>'), band=True))
    S.append(g.section(
        g.heading('Where partners start', 'The partner website, <span class="serif">live.</span>', 'The app sits behind this page on wealthy.in, captured with permission.')
        + '<div class="rv" style="margin-top:40px;max-width:820px;margin-left:auto;margin-right:auto">' + g.browser_frame('img/live-partner.jpg', 'wealthy.in/partner · scroll inside the frame') + '</div>', band=True))
    S.append('<section><div class="wrap" style="text-align:center">' + g.credit('MM', 'Designed by <b>Mohit Mehra</b>, Creative Lead &middot; view the original case study', MOHIT_APP) + '</div></section>')
    return dict(title='Wealthy Partner App Showcase', desc='UI redesign of the Wealthy Partner App for distributors, 2025.',
                bg='#0E0A22', bg2='#140F2E', surface='#1B1540', mut='#B3ABD2', mut2='#9890BC', accent='#8B63FF', accent_ink='#fff',
                sans=SANS_LATO, serif='"Playfair Display",serif', fonts=FONT_PLAYFAIR_LATO,
                herobg='radial-gradient(900px 520px at 50% 12%,#3A1D9B 0%,rgba(14,10,34,0) 70%),#0E0A22',
                kicker='Fintech · Mobile app UI · 2025', h1='Wealthy <span class="serif">Partner</span> App',
                lede='Built for distributors managing multiple clients and portfolios.',
                hero_vis=g.hero_phones(['img/s02.png', 'img/s01.png', 'img/s03.png']),
                meta=[('Design', 'Mohit Mehra'), ('Company', 'Wealthy'), ('Platform', 'Mobile app'), ('Year', '2025')],
                sections=S, cols=6, stepcols=3, swn=6, outro_h2='More work, <span class="serif">same care.</span>',
                footer='Wealthy Partner App &middot; design by <a href="' + MOHIT_APP + '" target="_blank" rel="noopener">Mohit Mehra</a> &middot; showcased by Vikas Banjare',
                nav_label='Original case study', nav_link=MOHIT_APP)


# ------------------------------------------------------------------ LeadSquared
def leadsquared():
    S = []
    S.append(g.intro('The brief', 'One page, <span class="serif">three personas.</span>',
        "Design a high-converting homepage for LeadSquared's Healthcare CRM product, aimed at hospital executives, heads of patient experience and marketing directors. Healthcare decision-makers are skeptical, data-driven and risk-averse, so the page had to speak to ROI, compliance and workflow fit at once.",
        [('Financial impact', 'ROI-first messaging for finance stakeholders.'), ('Compliance assurance', 'HIPAA-forward messaging for legal and IT.'),
         ('EHR connectivity', 'Workflow fit for operations teams.')]))
    S.append(g.section(
        g.heading('Process', 'Five stages, <span class="serif">brief to build.</span>')
        + g.steps([('01', 'Audience research', 'Three decision-maker personas: financial executives, IT and compliance, and operations. Each needed a different hook.'),
                   ('02', 'Message hierarchy', 'Three pillars: Financial Impact, Compliance Assurance and EHR Connectivity, ordered by when each objection surfaces.'),
                   ('03', 'Wireframing', 'A psychological funnel: Promise, Credibility, Solution, Proof, Differentiation, Action.'),
                   ('04', 'Visual design', 'A clean, light background, chosen over dark mode to signal clarity and precision.'),
                   ('05', 'A/B test proposal', 'Control versus Variant B, with distinct CTA copy to isolate which trust signal drives demo bookings.')]), band=True))
    S.append(g.section(
        g.heading('Final designs', 'Desktop <span class="serif">and mobile.</span>', 'The complete landing page across both breakpoints, from hero to footer. Scroll inside each frame.')
        + '<div class="duo rv"><div>' + g.browser_frame('img/desktop.jpg', 'Desktop, 1440px · scroll inside the frame') + '</div><div>' + g.mobile_frame('img/mobile.jpg', 'Mobile · scroll inside the phone') + '</div></div>'))
    S.append(g.section(
        g.spread('01', 'Persuasion funnel', [('Hero.', 'An immediate hook and audience identification.'), ('Features.', 'Answer the "how?" raised by the hero.'),
                 ('Core solution.', 'A radial layout makes the differentiator visible.'), ('Proof, then CTA.', 'Named outcomes first, one clear command last.')],
                 ['Strategy', 'Hierarchy', 'Funnel'], '<div class="shot wide" style="background:#EEF4FF"><div style="max-height:520px;overflow:hidden;border-radius:14px"><img class="flat" src="img/desktop.jpg" alt="" loading="lazy" style="border-radius:0"></div></div>'), band=True))
    S.append(g.section(
        g.heading('Visual identity', 'Colour <span class="serif">and typography.</span>',
                  'The palette communicates clarity, clinical precision and digital confidence. A white background was chosen over dark: in healthcare, bright and clean maps to trust and competence.')
        + g.system(SW(('Primary blue', '#0D63F3', '#fff'), ('Deep navy', '#0B1536', '#fff'), ('Body text', '#666666', '#fff'),
                     ('Page background', '#F6FAFF', '#0B1536'), ('Border', '#E0E0E0', '#333')),
                   '5X Growth', 'font-family:"DM Serif Display",serif',
                   [('Hero H1', 'Display Bold · 80px'), ('Section H2', 'Semibold · 36px'), ('Feature H3', 'Medium · 18px'), ('Body', 'Regular · 15px')],
                   'Components', '<div style="display:grid;gap:14px;margin-top:20px"><div style="background:#0D63F3;color:#fff;border-radius:10px;padding:14px;font-weight:600;text-align:center">Book a Demo &rarr;</div><div style="background:#F6FAFF;color:#0B1536;border-radius:16px;padding:18px;font-weight:600">Patient Intake Automation<br><span style="font-weight:400;font-size:14px;color:#666">Never miss an inquiry.</span></div><div style="display:flex;gap:8px"><i style="flex:1;height:38px;border-radius:10px;background:#D7EEFF"></i><i style="flex:1;height:38px;border-radius:10px;background:#FFE9C2"></i><i style="flex:1;height:38px;border-radius:10px;background:#D3F5E1"></i><i style="flex:1;height:38px;border-radius:10px;background:#E5DBFF"></i></div></div>')))
    S.append(g.section(
        g.heading('Testing strategy', 'An A/B test proposal <span class="serif">for post-launch.</span>',
                  'Two variants isolate which trust signal drives the highest demo booking rate.')
        + g.lists3([('Control A', ['Headline: 5X Conversions with the Healthcare CRM Built for Growth.', 'CTA: Book a Demo', 'ROI-driven messaging for executive buyers.']),
                    ('Variant B', ['Headline: The HIPAA-Compliant CRM for Seamless Patient Experience.', 'CTA: Schedule Your Consultation', 'Safety and trust messaging for compliance-first buyers.']),
                    ('What was rejected', ['A lead form in the hero: too much friction before self-qualification.', 'A dark, heavy blue theme: light reads as trustworthy in healthcare.'])]), band=True))
    S.append(g.section(
        '<p class="quote rv">&ldquo;The biggest purchase objection in enterprise healthcare software isn\'t cost. It\'s &lsquo;will this break our existing stack?&rsquo;&rdquo;</p>'
        '<div style="text-align:center">' + g.credit('VB', 'Concept by <b>Vikas Banjare</b> &middot; an interview task for LeadSquared, shown as a concept') + '</div>'))
    return dict(title='LeadSquared Healthcare CRM Showcase', desc='A conversion-first homepage concept for LeadSquared Healthcare CRM, 2025.',
                bg='#080A12', bg2='#0D1120', surface='#141A2E', mut='#A9B3CF', mut2='#8E99B8', accent='#4C86FF', accent_ink='#fff',
                sans='"DM Sans",system-ui,sans-serif', serif='"DM Serif Display",serif',
                fonts='https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@400;500;600;700&display=swap',
                herobg='radial-gradient(900px 520px at 50% 10%,#10337F 0%,rgba(8,10,18,0) 70%),#080A12',
                kicker='UX / Landing page design · 2025', h1='LeadSquared <span class="serif">Healthcare</span> CRM',
                lede='A conversion-first landing page for the healthcare enterprise.', hero_vis=g.hero_fig('img/desktop.jpg', 'Landing page hero'),
                meta=[('My role', 'Strategy, UI and copy'), ('Brief', 'Interview task'), ('Deliverable', 'Homepage landing page'), ('Responsive', 'Desktop + mobile')],
                sections=S, stepcols=5, swn=5, outro_h2='More work, <span class="serif">same care.</span>',
                footer='LeadSquared Healthcare CRM concept &middot; designed by Vikas Banjare &middot; not an official LeadSquared page')


# ------------------------------------------------------------------ PullLogic
def pulllogic():
    S = []
    S.append(g.intro('The brief', 'A webinar page <span class="serif">built to fill seats.</span>',
        'A landing page for a live webinar on AI-driven availability optimization. One goal: get supply chain leaders to register. Dark, high-contrast and gold-accented, with the form in view from the first screen.',
        [('Register in view', 'The sign-up form sits beside the headline, above the fold.'), ('Numbers up front', 'Three big figures frame the problem before the detail.'),
         ('Two ideas, two cards', 'The new KPIs, PAR and RAP, each get a clear card.')]))
    S.append(g.section(
        g.heading('The page', 'Top to bottom, <span class="serif">desktop and mobile.</span>', 'Scroll inside each frame.')
        + '<div class="duo rv"><div>' + g.browser_frame('img/desktop.jpg', 'Desktop · scroll inside the frame') + '</div><div>' + g.mobile_frame('img/mobile.jpg', 'Mobile · scroll inside the phone') + '</div></div>', band=True))
    S.append(g.section(
        g.heading('Structure', 'One section, <span class="serif">one job.</span>')
        + g.steps([('01', 'Hero + form', 'Headline, date chips and the registration form in one view.'), ('02', 'Key figures', 'Three large numbers that frame the problem.'),
                   ('03', 'Challenge and learning', 'Two columns: what holds growth back, and what attendees will learn.'),
                   ('04', 'Two KPIs', 'PAR and RAP, introduced with one card each.'), ('05', 'Outcomes, speakers, final CTA', 'Four outcome cards, three speakers and a closing call to register.')])))
    S.append(g.section(
        g.heading('Visual system', 'Black, white <span class="serif">and one gold.</span>', 'Gold marks the single thing to act on: the register button, the key words and the data points.')
        + g.system(SW(('Gold', '#FFAE33', '#1a1000'), ('Black', '#000000', '#fff'), ('Surface', '#111111', '#fff'), ('Border', '#262626', '#fff'), ('Text', '#F5F5F5', '#111')),
                   'Competitive edge.', 'font-family:Inter,sans-serif;font-weight:800;color:#FFAE33',
                   [('Headline', 'Inter · Bold'), ('Body', 'Inter · Regular'), ('Labels', 'Inter · Semibold, small caps')],
                   'Components', '<div style="display:grid;gap:14px;margin-top:20px"><div style="background:#FFAE33;color:#1a1000;border-radius:8px;padding:14px;font-weight:700;text-align:center">Reserve my spot &rarr;</div><div style="background:#111;border:1px solid #262626;border-radius:14px;padding:16px"><b style="color:#FFAE33">PAR</b><br><span style="font-size:14px;color:#aaa">Product Availability Readiness</span></div><div style="display:flex;gap:8px"><span style="border:1px solid #333;border-radius:99px;padding:6px 12px;font-size:12px">Sep 29, 2025</span><span style="border:1px solid #333;border-radius:99px;padding:6px 12px;font-size:12px">Online · Free</span></div></div>'), band=True))
    S.append('<section><div class="wrap" style="text-align:center">' + g.credit('VB', 'Designed and built by <b>Vikas Banjare</b>') + '</div></section>')
    return dict(title='PullLogic Webinar Landing Showcase', desc='A webinar landing page for Pull Logic, 2025.',
                bg='#050505', bg2='#0E0E0E', surface='#161616', line='rgba(255,255,255,.1)', mut='#B4B4B4', mut2='#8F8F8F', accent='#FFAE33', accent_ink='#1a1000',
                sans='"Inter",system-ui,sans-serif', serif='"Instrument Serif",serif',
                fonts='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@1&display=swap',
                herobg='radial-gradient(900px 520px at 50% 10%,#4A3205 0%,rgba(5,5,5,0) 70%),#050505',
                kicker='Landing page · Webinar · 2025', h1='Pull <span class="serif">Logic</span> webinar',
                lede='Intelligent inventory. Competitive edge.', hero_vis=g.hero_fig('img/desktop.jpg', 'Landing page hero'),
                meta=[('My role', 'Design and build'), ('Type', 'Webinar landing page'), ('Goal', 'Registrations'), ('Formats', 'Desktop + mobile')],
                sections=S, stepcols=5, swn=5, outro_h2='More work, <span class="serif">same care.</span>',
                footer='Pull Logic webinar page &middot; designed by Vikas Banjare')


# ------------------------------------------------------------------ Crestline
def crestline():
    sh = lambda k, n: 'v4/shots/%s%02d.png' % (k, n)
    sflat = lambda srcs, caps: g.strip(srcs, caps, flat=True)
    one = lambda src: '<div class="shot"><img src="%s" alt="" style="width:min(100%%,320px)"></div>' % src
    CS = 'v4/case-study.html'
    S = []
    S.append(g.intro('The brief', 'A broking app that <span class="serif">never lies about money.</span>',
        'Crestline is a fictional Indian broker. Version 4 follows a master specification: fifteen real-world blind spots where investors lose money or get stuck, an institutional navy and signal-orange system, three typefaces with one job each, Wealth and Trader modes, and live states in place of promises.',
        [('Honest states', 'Orders, pledges, withdrawals and account activation show what is actually happening.'), ('Two modes', 'Wealth mode is calm and roomy. Trader mode packs 14 rows above the fold.'),
         ('Self-contained case study', 'Every screen and wireframe is embedded, so the page works when shared on its own.')])
        + '<div style="text-align:center;margin-top:-30px;padding-bottom:20px"><a class="cta" href="' + CS + '">Read the v4 case study</a></div>')
    S.append(g.section(
        g.spread('01', 'Command home', [('Investor notice', 'shown up front, as the regulator asks.'), ('Net worth and UPI block', 'in one navy card.'), ('Actions and deadlines', 'such as a pledge due by 7 PM or expiry-day margin.')],
                 ['Home', 'Deadlines', 'Wealth mode'], one(sh('n', 1)))
        + '<div class="gap"></div>'
        + g.spread('02', 'Trader mode', [('42-pixel rows', 'with exchange, settlement and surveillance badges.'), ('Margin meter', 'warns at 85% before a peak-margin penalty.'), ('Open positions strip', 'with an Exit all button.')],
                   ['Density', 'Badges', 'Margin'], one(sh('n', 2)), flip=True)
        + '<div class="gap"></div>'
        + g.spread('03', 'An order pad that shows the maths', [('MTF 4x drawer', 'splits your cash, the funded amount and daily interest.'), ('Protected market orders', 'cap slippage on thin strikes.'), ('Pledge reminder', 'for the 4 PM to 7 PM window.')],
                   ['MTF', 'Order pad', 'Charges'], one(sh('n', 4)))
        + '<div class="gap"></div>'
        + g.spread('04', 'Nothing double-fires', [('Network drop', 'locks Buy and reconciles with the exchange.'), ('Rejections', 'come with a plain reason and one-tap fixes.'), ('Feed failover', 'switches to BSE when NSE stalls.')],
                   ['Reliability', 'Errors', 'Failover'], one(sh('n', 6)), flip=True)
        + '<div class="gap"></div>'
        + g.spread('05', 'Risk you can see', [('Option chain', 'with lot 65, future-equivalent OI and expiry-day margin.'), ('Physical delivery warning', 'for stock options in expiry week.'), ('Kill switch', 'pauses F&O after a daily loss limit, exits still allowed.')],
                   ['F&O', 'Expiry', 'Limits'], one(sh('n', 9))), band=True))
    S.append(g.section(
        g.heading('New in version 4', 'Twenty-three screens <span class="serif">from the specification.</span>')
        + sflat([sh('n', i) for i in (5, 7, 8, 10, 11, 12)], ['Surveillance lock', 'Rejection fixes', 'CDSL pledge', 'Kill switch', 'Physical delivery', 'Diagnostics'])
        + sflat([sh('n', i) for i in (13, 14, 15, 16, 17, 18)], ['FIFO tax lots', 'Fix buy average', 'Fund cut-off', 'Bond checkout', 'UPI block', 'Withdrawable'])
        + sflat([sh('n', i) for i in (19, 20, 21, 22, 23, 3)], ['Activation pipeline', 'KYC fast-track', 'Nominees', 'Trader watchlist', 'Service status', 'Feed failover'])))
    S.append(g.section(
        g.heading('Every flow, re-themed', 'Account, orders, <span class="serif">portfolio and more.</span>', 'All earlier flows use the v4 system and copy rules.')
        + sflat([sh('a', i) for i in range(1, 12)], ['Welcome', 'Mobile', 'OTP', 'Email', 'PAN', 'Aadhaar', 'Bank', 'Selfie', 'Nominee', 'PIN', 'Activation'])
        + sflat([sh('c', i) for i in range(1, 8)], ['Open', 'Executed', 'GTT', 'Detail', 'Modify', 'Rejected', 'Sell'])
        + sflat([sh('f', i) for i in (1, 3, 5, 8, 10, 11)], ['Top movers', 'Screener', 'Depth', 'News', 'Calendar', 'Compare'])
        + sflat([sh('h', i) for i in (2, 3, 4, 7, 8, 10)], ['First trade', 'Practice', 'Tax', 'Security', 'Privacy', 'Display']), band=True))
    S.append(g.section(
        g.heading('Design system', 'Navy, signal orange <span class="serif">and three typefaces.</span>', 'Manrope for wealth figures, Inter for the interface, JetBrains Mono for live data. Orange text uses a darker shade because the specified orange is only 3.5:1 on white.')
        + g.system(SW(('Navy', '#0F2942', '#fff'), ('Canvas', '#F8FAFC', '#0A1120'), ('Signal', '#EA580C', '#0A1120'), ('Buy', '#057A55', '#fff'), ('Sell', '#C81E1E', '#fff')),
                   '\u20b914,82,450', 'font-family:Manrope,sans-serif;font-weight:800',
                   [('Wealth and titles', 'Manrope'), ('Interface', 'Inter'), ('Live data', 'JetBrains Mono')],
                   'Badges', '<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:20px;font:700 12px JetBrains Mono,monospace">' + ''.join('<span style="background:%s;color:%s;border-radius:4px;padding:5px 8px">%s</span>' % (b, c, t) for t, b, c in [('NSE', '#E2E8F0', '#334155'), ('T+0', '#FFEDD5', '#C2410C'), ('MTF 4x', '#E0F2FE', '#0C4A6E'), ('ASM-I', '#FEF3C7', '#B45309'), ('ILLIQUID', '#FDE8E8', '#C81E1E'), ('STALE 4s', '#FEF3C7', '#B45309')]) + '</div>')))
    S.append('<section><div class="wrap" style="text-align:center"><p class="p rv" style="margin:0 auto 14px;text-align:center">How this was made: I set the brief, the research framing and the design direction. Screens, specifications and documentation were produced with AI assistance and directed and reviewed by me. Regulatory details follow the v4 specification and must be checked with compliance before real use.</p><a class="cta" href="' + CS + '">Read the v4 case study</a> <a class="cta ghost" href="v2/case-study.html">Version 2 case study</a><div style="margin-top:20px">'
             + g.credit('VB', 'Concept by <b>Vikas Banjare</b> &middot; Crestline is a fictional broker') + '</div></div></section>')
    return dict(title='Crestline Trading App Showcase', desc='Crestline v4: an Indian broking app concept with fifteen blind spots designed, honest state machines and 115 screens.',
                bg='#0A1626', bg2='#0F1E33', surface='#16263F', mut='#B4C0D3', mut2='#97A6BD', accent='#FB923C', accent_ink='#0A1120',
                sans='"Inter",system-ui,sans-serif', serif='"Instrument Serif",serif',
                fonts='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Manrope:wght@700;800&family=Instrument+Serif:ital@1&display=swap',
                herobg='radial-gradient(900px 520px at 50% 12%,#1E3A5F 0%,rgba(10,22,38,0) 70%),#0A1626',
                kicker='Fintech · Mobile app · Concept · v4', h1='Crest<span class="serif">line</span>',
                lede='An Indian broking app that never lies about money. 115 screens, a 128-screen map and a self-contained case study.',
                hero_vis='<div class="wrap"><div class="stage phones">' + ''.join('<div class="phone flatp p%d"><img src="%s" alt=""></div>' % (i + 1, s) for i, s in enumerate([sh('n', 1), sh('n', 4), sh('n', 9)])) + '</div></div>',
                meta=[('My role', 'Product design, research, system'), ('Screens', '115 designed · 128 mapped'), ('Modes', 'Wealth and Trader'), ('Type', 'Mobile app, concept')],
                sections=S, cols=6, swn=5, outro_h2='More work, <span class="serif">same care.</span>',
                footer='Crestline concept &middot; designed by Vikas Banjare &middot; fictional broker, no real brand implied',
                nav_label='Case study', nav_link=CS,
                extra_css='.phone.flatp{background:none;padding:0;box-shadow:none;aspect-ratio:880/1780;border-radius:0;filter:drop-shadow(0 30px 40px rgba(0,0,0,.5))}.phone.flatp img{border-radius:0;object-fit:contain}.shot img{filter:drop-shadow(0 24px 40px rgba(0,0,0,.35))}')


# ------------------------------------------------------------------ Purple Finance
def purple():
    S = []
    S.append(g.intro('The project', 'Lending for small business, <span class="serif">made approachable.</span>',
        'Purple Finance lends to micro, small and medium businesses. I designed the whole website. It has to do two jobs at once: reassure a shop owner that a loan is within reach, and give investors and regulators the disclosures they expect.',
        [('One promise up front', 'Levelling the playing field, with real borrowers in the hero.'), ('Proof in numbers', 'Growth figures and branch reach sit right under the hero.'),
         ('Two audiences, clear paths', 'Borrowers get eligibility and benefits. Investors get disclosures in one place.')]))
    S.append(g.section(
        g.heading('The pages', 'Home, about, loans <span class="serif">and investors.</span>', 'Captured from purplefinance.in with permission. Scroll inside each frame.')
        + '<div class="duo rv"><div>' + g.browser_frame('img/home.jpg', 'Home · scroll inside the frame') + '</div><div>' + g.mobile_frame('img/home-mobile.jpg', 'Home on mobile') + '</div></div>'
        + '<div class="rv" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;margin-top:40px"><div>' + g.browser_frame('img/msme.jpg', 'MSME loans') + '</div><div>' + g.browser_frame('img/about.jpg', 'About') + '</div><div>' + g.browser_frame('img/investors.jpg', 'Investors') + '</div></div>', band=True))
    S.append(g.section(
        g.heading('Structure', 'Each page, <span class="serif">one job.</span>')
        + g.steps([('01', 'Home', 'A clear promise, growth in numbers, why choose us, and borrower stories.'), ('02', 'MSME loans', 'Benefits, eligibility and documents, then a loan eligibility calculator.'),
                   ('03', 'About', 'History, vision and the people behind the company.'), ('04', 'Investors', 'Disclosures grouped so they are easy to find.')], cols=4)))
    S.append(g.section(
        g.heading('Visual system', 'Purple, paper <span class="serif">and plain type.</span>', 'Colours sampled from the live site.')
        + g.swatches(SW(('Purple', '#772682', '#fff'), ('Paper', '#F4F5EF', '#1a1a1a'), ('Ink', '#000000', '#fff'), ('Soft purple', '#BF8CC7', '#2a0f30'))), band=True))
    S.append('<section><div class="wrap" style="text-align:center"><a class="cta" href="https://www.purplefinance.in/" target="_blank" rel="noopener">Visit purplefinance.in</a><div style="margin-top:20px">' + g.credit('VB', 'Designed by <b>Vikas Banjare</b> &middot; every page, end to end') + '</div></div></section>')
    return dict(title='Purple Finance Website Showcase', desc='The Purple Finance website: MSME lending, borrower stories and investor disclosures.',
                bg='#140A17', bg2='#1B0F1F', surface='#24142A', mut='#C7B3CC', mut2='#A893AE', accent='#D9A6E2', accent_ink='#1B0F1F',
                sans='"Plus Jakarta Sans",system-ui,sans-serif', serif='"Instrument Serif",serif', fonts=g.FONT_PJS,
                herobg='radial-gradient(900px 520px at 50% 10%,#5A1C66 0%,rgba(20,10,23,0) 70%),#140A17',
                kicker='Fintech · Website · Lending', h1='Purple <span class="serif">Finance</span>',
                lede='A website for small-business lending: approachable for borrowers, complete for investors.', hero_vis=g.hero_fig('img/home.jpg', 'Purple Finance home page'),
                meta=[('My role', 'Website design, end to end'), ('Company', 'Purple Finance'), ('Audience', 'MSME borrowers, investors'), ('Pages shown', 'Home, loans, about, investors')],
                sections=S, stepcols=4, swn=4, outro_h2='More work, <span class="serif">same care.</span>',
                footer='Purple Finance website &middot; designed by Vikas Banjare &middot; shown with permission', nav_label='Visit site', nav_link='https://www.purplefinance.in/')


def build():
    return {'wealthy-web': wealthy_web(), 'wealthy-app': wealthy_app(), 'leadsquared': leadsquared(), 'pulllogic': pulllogic(), 'crestline': crestline(), 'purple-finance': purple()}
