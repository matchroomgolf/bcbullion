# -*- coding: utf-8 -*-
# Generates the standalone pages (about/faq/contact/privacy) from one shared
# chrome (CSS + header nav + footer). Edit here + re-run; do not hand-edit the HTML.
import os
OUT = os.path.expanduser('~/bc-deploy/bcbullion')
LOGO = '/assets/logo.png'

CSS = """
  :root{--cream:#F6F2E9;--navy:#0E1B2C;--navy2:#0A1422;--navy3:#08111E;--gold:#C6A04A;--gold-soft:#F0D89B;--gold-deep:#A8842F;--crimson:#A11D22;--ink:#2A2A24;--muted:#6E6A5C;--line:#ECE4D2;--d-text:#C7D2DF;--d-muted:#9FB0C3;--d-faint:#7E90A6;}
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{background:var(--cream);color:var(--ink);font-family:'Inter',system-ui,-apple-system,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
  a{color:inherit}
  .util{background:var(--navy2);color:var(--d-muted);font-size:12.5px;letter-spacing:.2px;border-bottom:1px solid rgba(198,160,74,.16)}
  .util-in{max-width:1060px;margin:0 auto;padding:8px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
  .util .star{color:var(--gold)}
  .util a{color:#E8DFC9;text-decoration:none;font-weight:600;letter-spacing:.3px}
  header{position:sticky;top:0;z-index:60;background:rgba(14,27,44,.97);backdrop-filter:blur(10px);border-bottom:1px solid rgba(198,160,74,.22);box-shadow:0 8px 30px rgba(8,16,28,.28)}
  .hdr-in{max-width:1060px;margin:0 auto;padding:13px 24px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}
  .brand{display:flex;align-items:center;gap:13px;text-decoration:none}
  .brand .logo{height:46px;width:auto;display:block}
  .brand .tag{display:flex;align-items:center;height:30px;padding-left:13px;border-left:1px solid rgba(198,160,74,.3);font-size:9px;color:var(--gold);letter-spacing:2.5px;text-transform:uppercase;max-width:110px;line-height:1.5}
  nav.main{display:flex;align-items:center;gap:22px}
  nav.main a{color:var(--d-text);text-decoration:none;font-size:13.5px;font-weight:500;letter-spacing:.2px;padding:6px 0;border-bottom:1.5px solid transparent;transition:color .2s,border-color .2s}
  nav.main a:hover{color:#fff;border-bottom-color:rgba(198,160,74,.5)}
  nav.main a.active{color:var(--gold);border-bottom-color:var(--gold)}
  .cta{background:linear-gradient(135deg,var(--gold-soft),var(--gold) 55%,#9C7A2E);color:var(--navy);font-weight:700;font-size:13px;padding:10px 20px;border-radius:8px;text-decoration:none;letter-spacing:.3px}
  .band{background:radial-gradient(120% 120% at 80% 0%,#173050 0%,var(--navy) 55%,var(--navy2) 100%);color:var(--cream);border-bottom:1px solid rgba(198,160,74,.22)}
  .band-in{max-width:1060px;margin:0 auto;padding:60px 24px 52px}
  .eyebrow{font-size:12px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:600;margin-bottom:14px}
  .band h1{font-family:'Cinzel',serif;font-weight:800;font-size:clamp(34px,5vw,52px);line-height:1.05;letter-spacing:.5px;margin-bottom:16px}
  .band p{font-size:16px;color:#BFCBDA;max-width:640px}
  .wrap{max-width:1060px;margin:0 auto;padding:54px 24px 30px}
  .card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:clamp(26px,4vw,48px);box-shadow:0 10px 30px rgba(14,27,44,.06)}
  .card+.card{margin-top:26px}
  .card section+section{margin-top:32px;padding-top:32px;border-top:1px solid var(--line)}
  .card h2{font-family:'Cinzel',serif;font-weight:700;font-size:22px;color:var(--navy);margin-bottom:14px;display:flex;align-items:center;gap:11px}
  .card h2 .dot{color:var(--gold);font-size:13px}
  .card p{color:#54503F;font-size:15.5px;margin-bottom:13px}
  .card p:last-child{margin-bottom:0}
  .lead{font-size:17px;color:#3C3930}
  .card a.inline{color:#8A6D24;text-decoration:underline;font-weight:600}
  .vals{display:grid;grid-template-columns:repeat(2,1fr);gap:26px 30px;margin-top:8px}
  .val{display:flex;gap:15px;align-items:flex-start}
  .val .vi{flex-shrink:0;width:46px;height:46px;border-radius:50%;border:1px solid rgba(198,160,74,.5);background:rgba(198,160,74,.10);display:flex;align-items:center;justify-content:center;color:var(--gold-deep)}
  .val h3{font-size:15.5px;font-weight:600;color:var(--navy);margin-bottom:4px}
  .val p{font-size:13.5px;color:#6E6A5C;margin:0;line-height:1.55}
  details.faq{border:1px solid var(--line);border-radius:13px;padding:0;margin-bottom:12px;background:#fff;overflow:hidden}
  details.faq summary{list-style:none;cursor:pointer;padding:20px 22px;font-weight:600;font-size:15.5px;color:var(--navy);display:flex;align-items:center;justify-content:space-between;gap:14px}
  details.faq summary::-webkit-details-marker{display:none}
  details.faq summary .pm{color:var(--gold);font-size:22px;font-weight:400;line-height:1;transition:transform .2s}
  details.faq[open] summary .pm{transform:rotate(45deg)}
  details.faq .ans{padding:0 22px 20px;color:#54503F;font-size:14.5px;line-height:1.6}
  .ct-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-bottom:8px}
  .ct{display:block;background:#fff;border:1px solid var(--line);border-radius:14px;padding:26px;text-decoration:none;transition:border-color .2s,box-shadow .2s}
  .ct:hover{border-color:var(--gold);box-shadow:0 10px 26px rgba(14,27,44,.08)}
  .ct .k{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);font-weight:600;margin-bottom:9px}
  .ct .v{font-family:'Cinzel',serif;font-size:24px;font-weight:700;color:var(--navy)}
  .ct .s{font-size:13px;color:#6E6A5C;margin-top:6px}
  .frm{display:grid;gap:14px;margin-top:6px}
  .frm label{font-size:12px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:5px;display:block}
  .frm input,.frm textarea{width:100%;border:1px solid var(--line);border-radius:10px;padding:13px 15px;font:inherit;font-size:15px;color:var(--ink);background:#FCFAF5}
  .frm input:focus,.frm textarea:focus{outline:none;border-color:var(--gold);box-shadow:0 0 0 3px rgba(198,160,74,.15)}
  .frm .row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .frm button{justify-self:start;background:var(--navy);color:var(--cream);border:none;font:inherit;font-weight:600;font-size:15px;padding:14px 30px;border-radius:9px;cursor:pointer;letter-spacing:.3px}
  .frm button:hover{background:#16263C}
  .note{margin:22px auto 0;max-width:1060px;padding:0 24px;font-size:12.5px;color:var(--muted);line-height:1.55;text-align:center}
  .verse{text-align:center;margin:40px auto 0;max-width:1060px;padding:0 24px}
  .verse p{font-family:'Cinzel',serif;font-style:italic;font-size:18px;color:#8A6D24;line-height:1.5}
  .verse .ref{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-top:12px}
  footer.foot{background:var(--navy3);color:var(--d-muted);margin-top:48px}
  .foot-in{max-width:1060px;margin:0 auto;padding:54px 24px 0}
  .foot-grid{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:40px}
  .foot .logo{height:54px;width:auto;display:block;margin-bottom:6px}
  .foot .ftag{font-size:9px;color:var(--gold);letter-spacing:2.5px;text-transform:uppercase}
  .foot p.blurb{font-size:13px;line-height:1.6;color:var(--d-faint);margin:16px 0 18px;max-width:320px}
  .foot .ci{font-size:13px;line-height:1.95;color:var(--d-muted)}
  .foot .ci a{color:#E8DFC9;text-decoration:none;font-weight:600}
  .foot .ci .dim{color:#6E8097}
  .foot h4{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin-bottom:16px;font-weight:600}
  .foot .links{display:flex;flex-direction:column;gap:11px;align-items:flex-start}
  .foot .links a{color:var(--d-muted);text-decoration:none;font-size:13.5px}
  .foot .links a:hover{color:#fff}
  .legal{display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-top:44px;padding:18px 0 30px;border-top:1px solid rgba(255,255,255,.06)}
  .legal span{font-size:11.5px;color:#5E7088}
  .legal a{color:var(--d-muted);text-decoration:underline}
  .shopnote{background:linear-gradient(180deg,#16263C,#0E1B2C);border:1px solid rgba(198,160,74,.3);border-radius:14px;padding:18px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:28px}
  .shopnote .t{color:var(--cream);font-size:14.5px}.shopnote .t b{color:var(--gold-soft)}
  .shopnote a{background:linear-gradient(135deg,var(--gold-soft),var(--gold) 55%,#9C7A2E);color:var(--navy);font-weight:700;font-size:14px;padding:11px 22px;border-radius:8px;text-decoration:none;white-space:nowrap}
  .chips{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px}
  .chips a{font-size:13px;font-weight:600;letter-spacing:.2px;color:#6E6A5C;text-decoration:none;padding:8px 16px;border:1px solid var(--line);border-radius:30px;background:#fff;transition:border-color .15s,color .15s}
  .chips a:hover{border-color:var(--gold);color:var(--navy)}
  .chips a.active{background:var(--navy);color:var(--cream);border-color:var(--navy)}
  .pcount{font-size:13px;color:var(--muted);margin-bottom:18px}
  .pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(228px,1fr));gap:22px}
  .pcard{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;text-decoration:none;transition:border-color .2s,box-shadow .2s,transform .2s}
  .pcard:hover{border-color:var(--gold);box-shadow:0 14px 30px rgba(14,27,44,.10);transform:translateY(-2px)}
  .pimg{aspect-ratio:1/1;background:radial-gradient(circle at 50% 38%,#fff,#F1EBDD);display:flex;align-items:center;justify-content:center;padding:20px;border-bottom:1px solid var(--line)}
  .pimg img{max-width:100%;max-height:100%;object-fit:contain}
  .pinfo{padding:15px 16px 17px;display:flex;flex-direction:column;gap:7px;flex:1}
  .pinfo h3{font-size:14px;font-weight:600;color:var(--navy);line-height:1.32;margin:0}
  .pprice{font-size:12.5px;color:#6E6A5C;margin-top:auto}.pprice b{font-family:'Cinzel',serif;font-size:16px;color:var(--gold-deep);font-weight:700}
  .porder{font-size:12.5px;font-weight:600;color:var(--gold-deep);letter-spacing:.3px}
  .video{position:relative;width:100%;padding-bottom:56.25%;height:0;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#000;margin:8px 0 2px}
  .video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
  .steps{display:flex;flex-direction:column;gap:14px;margin-top:4px}
  .step{display:flex;gap:16px;align-items:flex-start;background:#FBF8F1;border:1px solid var(--line);border-radius:12px;padding:18px 20px}
  .step .n{flex-shrink:0;width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--gold-soft),var(--gold) 60%,#9C7A2E);color:var(--navy);font-family:'Cinzel',serif;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:15px}
  .step h3{font-size:15px;font-weight:600;color:var(--navy);margin-bottom:3px}
  .step p{font-size:13.5px;color:#6E6A5C;margin:0;line-height:1.5}
  @media(max-width:760px){.vals,.ct-grid,.foot-grid{grid-template-columns:1fr}.frm .row{grid-template-columns:1fr}.brand .tag{display:none}nav.main{gap:16px;font-size:13px}.pgrid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px}.shopnote{flex-direction:column;align-items:flex-start}}
"""

def header(active):
    def a(href,label,key):
        cls=' class="active"' if key==active else ''
        return f'<a href="{href}"{cls}>{label}</a>'
    nav=''.join([a('/#category','Shop','shop'),a('/ira.html','IRA','ira'),a('/about.html','About','about'),a('/faq.html','FAQ','faq'),a('/contact.html','Contact','contact')])
    return f"""  <div class="util">
    <div class="util-in">
      <span><span class="star">&#9733;</span> Family-owned &middot; 20+ years in precious metals</span>
      <a href="tel:8505851115">(850) 585-1115</a>
    </div>
  </div>
  <header>
    <div class="hdr-in">
      <a class="brand" href="/"><img class="logo" src="{LOGO}" alt="B.C. Bullion"><span class="tag">Your Wealth Starts Here</span></a>
      <nav class="main">{nav}</nav>
      <a class="cta" href="/#category">Shop Metals</a>
    </div>
  </header>"""

def band(eyebrow,h1,sub):
    return f"""  <div class="band"><div class="band-in">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p>{sub}</p>
  </div></div>"""

FOOTER = f"""  <footer class="foot"><div class="foot-in">
    <div class="foot-grid">
      <div>
        <img class="logo" src="{LOGO}" alt="B.C. Bullion">
        <div class="ftag">Your Wealth Starts Here</div>
        <p class="blurb">Family-owned precious-metals dealer in Northwest Florida. Honest pricing, insured delivery, real people &mdash; for 20+ years.</p>
        <div class="ci">
          <div><a href="tel:8505851115">(850) 585-1115</a></div>
          <div><a href="mailto:hello@bcbullion.com" style="color:#9FB0C3;font-weight:400">hello@bcbullion.com</a></div>
          <div>Northwest Florida &middot; Online only</div>
          <div class="dim">Mon&ndash;Fri, 9am&ndash;5pm CT</div>
        </div>
      </div>
      <div><h4>Shop</h4><div class="links">
        <a href="/gold.html">Gold</a><a href="/silver.html">Silver</a><a href="/graded-coins.html">Graded Coins</a>
        <a href="/patriot-stackers.html">Patriot Stackers</a><a href="/biblical-coins.html">Biblical Coins</a><a href="/ira.html">Precious-Metals IRA</a>
      </div></div>
      <div><h4>Company</h4><div class="links">
        <a href="/about.html">About B.C.</a><a href="/faq.html">FAQ</a><a href="/contact.html">Contact</a>
      </div></div>
    </div>
    <div class="legal">
      <span>&copy; 2026 B.C. Bullion. All rights reserved. &middot; <a href="/privacy.html">Privacy Policy</a></span>
      <span><a href="/">Return to homepage</a></span>
    </div>
  </div></footer>"""

def page(title,desc,active,band_html,body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | B.C. Bullion</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/favicon-16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header(active)}
{band_html}
{body_html}
{FOOTER}
</body>
</html>"""

def icon(path):
    return f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"></path></svg>'

def val(path,t,d):
    return f'<div class="val"><div class="vi">{icon(path)}</div><div><h3>{t}</h3><p>{d}</p></div></div>'

# homepage whyItems icons (verbatim) + a 6th star for American sound money
I_PRICE='M20.6 12.4l-8.2 8.2a1.8 1.8 0 0 1-2.5 0l-6.5-6.5a1.8 1.8 0 0 1-.5-1.3V4.6A1.6 1.6 0 0 1 4.6 3h8.2c.5 0 .9.2 1.3.5l6.5 6.5a1.8 1.8 0 0 1 0 2.4Z M6.5 8a1.5 1.5 0 1 0 3 0a1.5 1.5 0 1 0-3 0'
I_SHIP='M12 3l7 2.4v5.3c0 4.3-3 7.6-7 9-4-1.4-7-4.7-7-9V5.4L12 3Z M8.8 12.2l2.1 2.1 4.3-4.5'
I_BUYBACK='M20 12a8 8 0 1 1-2.4-5.7 M20 4.2v3.4h-3.4'
I_PHONE='M15.6 13.9l-1.9 1.9a13 13 0 0 1-5.4-5.4l1.9-1.9L8.1 4H4.3A1.3 1.3 0 0 0 3 5.4 16.6 16.6 0 0 0 18.7 21 1.3 1.3 0 0 0 20 19.7v-3.8Z'
I_SCALES='M12 4.5v14.5 M6 8h12 M9 19h6 M6 8l-3 4.8 M6 8l3 4.8 M3 12.8a3 3 0 0 0 6 0 M18 8l-3 4.8 M18 8l3 4.8 M15 12.8a3 3 0 0 0 6 0'
I_STAR='M12 3.2l2.47 5.01 5.53.8-4 3.9.94 5.5L12 16.8l-4.94 2.6.94-5.5-4-3.9 5.53-.8z'

about_body = f"""  <div class="wrap">
    <div class="card">
      <section>
        <p class="lead">B.C. Bullion is a growing, family-owned precious-metals company in Northwest Florida &mdash; online only, with honest pricing and a real person on the other end of the phone.</p>
      </section>
      <section>
        <h2><span class="dot">&#9670;</span>Two decades in the trade</h2>
        <p>Our co-founders and staff have been in the precious metals industry for over 20 years. What was originally planned as a smaller, one-on-one business has grown tremendously &mdash; led down that path by a single focus: making sure each individual client gets exactly what suits them, in a timely manner, at the best price.</p>
        <p>We can&rsquo;t out-shout the big warehouses, so we do the opposite. We answer the phone, we quote you straight, and we ship fast and quietly.</p>
      </section>
      <section>
        <h2><span class="dot">&#9670;</span>Why families buy from us</h2>
        <p>We strongly believe that in this rapidly changing world, every family should have the financial security that owning precious metals can provide. We offer a focused handful of options that appeal to the seasoned stacker and the first-time buyer alike &mdash; from American Gold &amp; Silver Eagles to USA-made Patriot Stackers, graded coins, and our Biblical Coins collection.</p>
        <div class="vals">
          {val(I_PRICE,'Transparent spot-based pricing','Every price ties to the live market &mdash; no hidden markups, no games. You always see how your price is built.')}
          {val(I_SHIP,'Fully insured &amp; discreet shipping','Plain, unmarked packaging, signature required, insured door to door from the moment it leaves us.')}
          {val(I_BUYBACK,'Buyback guarantee','We buy back what we sell at fair, live-market pricing &mdash; a standing offer, whenever you are ready.')}
          {val(I_PHONE,'Personal one-on-one service','Talk to a real person who knows your name and your goals. No call centers, no scripts.')}
          {val(I_SCALES,'Faith-informed integrity','Honest weights and honest dealings &mdash; a family business run the way business ought to be done.')}
          {val(I_STAR,'American sound money','Physical gold and silver you hold in your own hands, in your own name.')}
        </div>
      </section>
    </div>
  </div>
  <div class="verse"><p>&ldquo;Dishonest money dwindles away, but whoever gathers money little by little makes it grow.&rdquo;</p><div class="ref">&mdash; Proverbs 13:11 &mdash;</div></div>"""

faqs = [
 ("Is my information secure?","Yes. Checkout runs over encrypted, PCI-compliant connections, and we never sell or share your information. Every order ships in plain, unmarked packaging with no indication of the contents."),
 ("How fast do you ship &mdash; and is it insured?","Most in-stock orders leave within 1&ndash;2 business days, fully insured door to door with signature required on delivery. Insured shipping is free on orders over $199."),
 ("What payment methods do you accept &mdash; and what is the discount?","We accept major cards, bank wire, and personal check. Wire and check orders receive a lower price than card, because we pass the processing savings straight back to you."),
 ("Do you buy back what you sell?","Always. We offer a standing buyback at fair, live-market pricing. Call us and a real person will walk you through it &mdash; no runaround, no pressure."),
 ("What metals are IRA-eligible?","IRS-approved gold, silver, platinum and palladium that meet minimum fineness requirements. We help you choose eligible products and coordinate directly with your custodian."),
 ("How do I place an order?","Shop online and check out securely, or simply call us at (850) 585-1115 and we&rsquo;ll take care of you over the phone &mdash; whichever you prefer."),
 ("Where are you located?","We&rsquo;re a family-owned dealer based in Northwest Florida, operating online only so we can serve customers across the country."),
]
faq_items=''.join([f'<details class="faq"><summary>{q}<span class="pm">+</span></summary><div class="ans">{a}</div></details>' for q,a in faqs])
faq_body = f"""  <div class="wrap">
    {faq_items}
    <div class="card" style="margin-top:26px;text-align:center">
      <p style="margin-bottom:14px">Still have a question? A real person is glad to help.</p>
      <a class="cta" href="/contact.html" style="display:inline-block">Contact us</a>
    </div>
  </div>"""

contact_body = """  <div class="wrap">
    <div class="ct-grid">
      <a class="ct" href="tel:8505851115"><div class="k">Call us</div><div class="v">(850) 585-1115</div><div class="s">Mon&ndash;Fri, 9am&ndash;5pm CT</div></a>
      <a class="ct" href="mailto:hello@bcbullion.com"><div class="k">Email us</div><div class="v">hello@bcbullion.com</div><div class="s">We reply within one business day</div></a>
    </div>
    <div class="card">
      <section>
        <h2><span class="dot">&#9670;</span>Send us a message</h2>
        <p>Tell us what you&rsquo;re looking for &mdash; a specific coin or bar, a buyback quote, or help getting started. We&rsquo;ll get right back to you.</p>
        <form class="frm" onsubmit="event.preventDefault();var f=this;var subj=encodeURIComponent('Website inquiry from '+f.nm.value);var body=encodeURIComponent(f.msg.value+'\\n\\nName: '+f.nm.value+'\\nReply to: '+f.em.value);window.location.href='mailto:hello@bcbullion.com?subject='+subj+'&body='+body;">
          <div class="row">
            <div><label>Your name</label><input name="nm" required placeholder="Jane Smith"></div>
            <div><label>Email</label><input name="em" type="email" required placeholder="you@example.com"></div>
          </div>
          <div><label>Message</label><textarea name="msg" rows="5" required placeholder="I'm interested in&hellip;"></textarea></div>
          <button type="submit">Send message</button>
        </form>
        <p style="margin-top:16px;font-size:13px;color:#6E6A5C">Prefer the phone? Call <a class="inline" href="tel:8505851115">(850)&nbsp;585-1115</a> &mdash; a real person, every time.</p>
      </section>
      <section>
        <h2><span class="dot">&#9670;</span>Hours &amp; location</h2>
        <p><b>Northwest Florida &middot; Online only.</b><br>Monday&ndash;Friday, 9am&ndash;5pm Central. We ship nationwide, fully insured and discreet.</p>
      </section>
    </div>
  </div>"""

privacy_body = """  <div class="wrap">
    <div class="card">
      <section><p class="lead">B.C. Bullion is a family-owned precious-metals dealer in Northwest Florida. We keep our privacy practices as straightforward as our pricing: we collect only what we need to serve you, we protect it, and we never sell it. <span style="color:#8A6D24">Last updated: June 16, 2026.</span></p></section>
      <section><h2><span class="dot">&#9670;</span>Information we collect</h2>
        <p><b>Order &amp; contact details</b> &mdash; your name, shipping address, phone number, and email when you place an order or reach out.<br>
        <b>Price-alert sign-ups</b> &mdash; the email address you give us to receive spot-price alerts and new-arrival notices.<br>
        <b>Payment information</b> &mdash; processed securely by our payment and bank-wire providers; we do not store full card numbers.<br>
        <b>Basic site data</b> &mdash; standard, non-identifying analytics that help us keep the site fast and useful.</p></section>
      <section><h2><span class="dot">&#9670;</span>How we use it</h2>
        <p>To process, insure, and discreetly ship your order; to send the price alerts you asked for; to provide real, one-on-one customer service; and to meet our legal, tax, and recordkeeping obligations.</p></section>
      <section><h2><span class="dot">&#9670;</span>What we never do</h2>
        <p>We never sell, rent, or trade your personal information. We share it only with the partners required to complete what you asked us to do &mdash; an insured carrier to deliver your order, or a payment processor to handle a transaction &mdash; and only the minimum they need.</p></section>
      <section><h2><span class="dot">&#9670;</span>How we protect it</h2>
        <p>Our site runs over encrypted (SSL) connections, and checkout is handled through PCI-compliant providers. Every order ships in plain, unmarked packaging with signature required on delivery.</p></section>
      <section><h2><span class="dot">&#9670;</span>Your choices</h2>
        <p>Unsubscribe from price alerts anytime via the link in any email. To review, update, or delete the information we hold, call <a class="inline" href="tel:8505851115">(850)&nbsp;585-1115</a> or email <a class="inline" href="mailto:hello@bcbullion.com">hello@bcbullion.com</a> and a real person will take care of it.</p></section>
    </div>
  </div>
  <p class="note">Precious metals carry market risk and can lose value; nothing here is investment, tax, or legal advice.</p>"""

# ---------------- CATEGORY (SHOP) PAGES — real catalog from bcbullion.com ----------------
import json as _json
CATALOG = _json.load(open(os.path.join(OUT,'scripts','catalog.json'), encoding='utf-8'))
CAT_ORDER = [('gold','Gold'),('silver','Silver'),('graded-coins','Graded Coins'),
             ('patriot-stackers','Patriot Stackers'),('biblical-coins','Biblical Coins')]
CAT_SUB = {'gold':'.9999 fine gold bars &amp; coins','silver':'.999 fine rounds, bars &amp; coins',
           'graded-coins':'PCGS &amp; NGC certified sets','patriot-stackers':'USA-made .999 fine silver',
           'biblical-coins':'.999 fine silver Biblical Series'}
esc = lambda s: (s or '').replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def catnav(active):
    out=[]
    for s,n in CAT_ORDER:
        cls=' class="active"' if s==active else ''
        out.append(f'<a href="/{s}.html"{cls}>{n}</a>')
    return '<div class="chips">'+''.join(out)+'</div>'

def pcard(p):
    img=p.get('local') or p.get('img') or ''
    title=esc(p['title'].replace('*',''))
    price=p.get('price') or ''
    if '$' in price:
        pre,amt=price.split('$',1); pr=f'<div class="pprice">{esc(pre.strip())} <b>${esc(amt.strip())}</b></div>'
    else:
        pr=f'<div class="pprice">{esc(price)}</div>' if price else ''
    return (f'<a class="pcard" href="tel:8505851115" title="Call to order">'
            f'<div class="pimg"><img src="{img}" alt="{title}" loading="lazy"></div>'
            f'<div class="pinfo"><h3>{title}</h3>{pr}<div class="porder">Call to order &rarr;</div></div></a>')

def category_page(slug,name):
    prods=CATALOG[slug]['products']
    note=('<div class="shopnote"><div class="t">Live, <b>spot-based pricing</b> &mdash; updated continuously. '
          'Wire &amp; check orders save vs. card; insured, discreet shipping.</div>'
          '<a href="tel:8505851115">Call (850) 585-1115 to order</a></div>')
    grid='<div class="pgrid">'+''.join(pcard(p) for p in prods)+'</div>'
    cnt=f'{len(prods)} {"item" if len(prods)==1 else "items"}'
    body=f'  <div class="wrap">{catnav(slug)}{note}<div class="pcount">{cnt} in {name}</div>{grid}</div>'
    sub=CAT_SUB.get(slug,'')
    return page(name, f'Shop {name} at B.C. Bullion — {name} bullion with live spot-based pricing, insured discreet shipping.',
                'shop', band('Shop', name, f'{sub}. Live spot-based pricing, insured &amp; discreet shipping, real one-on-one service.'), body)

ira_body = """  <div class="wrap">
    <div class="card">
      <section>
        <p class="lead">Hold IRS-approved gold and silver inside a tax-advantaged retirement account &mdash; physical metal, in your name, stored in an insured, IRS-approved depository. We make the setup simple and stay with you through every step.</p>
      </section>
      <section>
        <h2><span class="dot">&#9670;</span>Watch: how a precious-metals IRA works</h2>
        <p>Want to diversify your IRA? This short video walks through how it works &mdash; from account setup to secure storage.</p>
        <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/K9UWz3RQpOY" title="Precious Metals IRAs explained" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
      </section>
      <section>
        <h2><span class="dot">&#9670;</span>How it works</h2>
        <div class="steps">
          <div class="step"><div class="n">1</div><div><h3>Open a self-directed IRA</h3><p>We connect you with a trusted custodian and keep the paperwork simple.</p></div></div>
          <div class="step"><div class="n">2</div><div><h3>Fund &amp; choose metals</h3><p>Transfer or roll over existing funds, then select IRA-eligible gold &amp; silver.</p></div></div>
          <div class="step"><div class="n">3</div><div><h3>Securely vaulted</h3><p>Your metals are held in an insured, IRS-approved depository in your name.</p></div></div>
        </div>
      </section>
      <section>
        <h2><span class="dot">&#9670;</span>What&rsquo;s IRA-eligible?</h2>
        <p>IRS-approved gold, silver, platinum and palladium that meet minimum fineness requirements. We help you choose eligible products and coordinate directly with your custodian.</p>
      </section>
      <section style="text-align:center;border-top:1px solid var(--line);padding-top:32px">
        <a class="cta" href="tel:8505851115" style="display:inline-block">Call (850) 585-1115 to get started</a>
        <p style="margin-top:14px;font-size:12.5px;color:#6E6A5C">We coordinate directly with your custodian. Nothing here is investment, tax, or legal advice.</p>
      </section>
    </div>
  </div>"""

pages = {
 'ira.html': page('Gold &amp; Silver IRA','Diversify your retirement with IRS-approved physical gold and silver. B.C. Bullion makes a precious-metals IRA simple.','ira',
    band('Precious-metals IRA','Gold &amp; Silver IRAs','Diversify your retirement with physical metals &mdash; held in your name, in an insured, IRS-approved depository.'), ira_body),
 'about.html': page('About','Family-owned precious-metals dealer in Northwest Florida with over 20 years in the industry.','about',
    band('Our Story','About B.C. Bullion','A growing, family-owned precious-metals company built on honest pricing, insured delivery, and real one-on-one service.'), about_body),
 'faq.html': page('FAQ','Answers on shipping, insurance, payment, buyback, and IRA-eligible metals from B.C. Bullion.','faq',
    band('Questions, answered','Frequently Asked','Straight answers on shipping, payment, buyback, and getting started &mdash; and a real person if you need one.'), faq_body),
 'contact.html': page('Contact','Call (850) 585-1115 or email hello@bcbullion.com. Family-owned precious-metals dealer, Northwest Florida.','contact',
    band('Get in touch','Contact B.C. Bullion','A real person, every time. Call, email, or send us a note and we&rsquo;ll get right back to you.'), contact_body),
 'privacy.html': page('Privacy Policy','How B.C. Bullion collects, uses, and protects your information.','',
    band('Legal','Privacy Policy','Your trust matters as much as your metal. Here is what we collect, how we use it, and our simple promise &mdash; we never sell or share your information.'), privacy_body),
}
for slug,name in CAT_ORDER:
    pages[f'{slug}.html']=category_page(slug,name)
for fn,html in pages.items():
    open(os.path.join(OUT,fn),'w',encoding='utf-8').write(html)
    print(f"wrote {fn} ({len(html)} bytes)")
