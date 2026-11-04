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
def build():
    return {'wealthy-web': wealthy_web(), }
