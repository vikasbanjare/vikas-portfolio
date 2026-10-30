#!/usr/bin/env python3
"""Builds case-studies/index.html: one shareable page listing every UI/UX showcase.
Reuses the cards + CSS from components/uiux-section.html. Run: python3 case-studies/hub_gen.py"""
import re, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
ux = (R / "components" / "uiux-section.html").read_text()
css = re.search(r"<style>(.*?)</style>", ux, re.S).group(1)
grid = re.search(r'(<ul class="vux-grid">.*?</ul>)', ux, re.S).group(1)
grid = grid.replace('href="case-studies/', 'href="').replace('src="assets/', 'src="../assets/')
EMAIL, LINKEDIN, BEHANCE = "vikas.banjare@gmail.com", "https://www.linkedin.com/in/vikasbanjare/", "https://www.behance.net/vikas-banjare"
SITE = "https://vikasbanjare.github.io/vikas-portfolio/case-studies/"
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>UI/UX &amp; Websites — Vikas Banjare</title>
<meta name="description" content="Apps, websites and the thinking behind them: seven UI/UX showcases by Vikas Banjare.">
<link rel="canonical" href="{SITE}"><meta property="og:title" content="UI/UX &amp; Websites — Vikas Banjare"><meta property="og:description" content="Apps, websites and the thinking behind them. Seven showcases."><meta property="og:image" content="{SITE}../assets/uiux/crestline.jpg"><meta property="og:type" content="website">
<link rel="icon" href="../assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Onest:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>*{{margin:0}}body{{background:#04060d}}{css}
[data-vbux]{{min-height:100vh;padding-top:clamp(70px,10vh,120px)}}
.hub-nav{{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:clamp(44px,7vw,90px);font-size:14px;font-weight:600}}
.hub-nav a{{color:#8da0c4;text-decoration:none;min-height:44px;display:inline-flex;align-items:center}}.hub-nav a:hover{{color:#f6f9ff}}
.hub-nav b{{font-family:'Space Grotesk',sans-serif;color:#f6f9ff;font-size:17px;letter-spacing:-.02em}}
.hub-foot{{margin-top:clamp(60px,9vw,110px);padding-top:28px;border-top:1px solid rgba(255,255,255,.1);display:flex;flex-wrap:wrap;gap:12px 28px;justify-content:space-between;align-items:center}}
.hub-foot p{{font-size:15px;color:#8da0c4}}.hub-foot nav{{display:flex;flex-wrap:wrap;gap:10px 22px}}
.hub-foot a{{color:#b6f500;text-decoration:none;font-weight:600;font-size:15px;min-height:44px;display:inline-flex;align-items:center}}.hub-foot a:hover{{text-decoration:underline}}
</style></head><body>
<main data-vbux>
<div class="vux-wrap">
<div class="hub-nav"><b>Vikas Banjare</b><a href="../index.html">&larr; Back to portfolio</a></div>
<header class="vux-head"><div><span class="vux-eyebrow">UI/UX &amp; websites</span>
<h1 class="vux-h2" style="font-size:clamp(38px,6vw,84px)">Interfaces,<br>told as <span class="vux-accent">stories.</span></h1></div>
<p class="vux-sub">Apps, websites and the thinking behind them. Open any one for the full showcase.</p></header>
{grid}
<footer class="hub-foot"><p>Let&rsquo;s talk about your product.</p><nav><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a><a href="{BEHANCE}" target="_blank" rel="noopener">Behance</a></nav></footer>
</div></main></body></html>'''
(R / "case-studies" / "index.html").write_text(page)
print("wrote case-studies/index.html", len(page) // 1024, "KB")
