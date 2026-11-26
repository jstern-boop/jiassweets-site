#!/usr/bin/env python3
"""Build Jia's Sweets static site into ../site. Re-run after any content change.
Island Pixel Studios. Keep this file with the site repo (gen.py was lost once)."""
import os, html

OUT = os.path.join(os.path.dirname(__file__), '..', 'site')
VER = '1'          # bump after CSS/JS changes so phones reload
NOINDEX = True     # True until launch

PHONE1, PHONE2 = '631-278-1700', '631-839-0948'
EMAIL = 'jiassweets@gmail.com'

PRODUCTS = [
    # slug, name, price, image
    ('custom-connections', 'Custom Connections', '25.00', 'prod-custom-connections.webp'),
    ('events-favor', 'Events Favor', '50.00', 'prod-events-favor.webp'),
    ('fudge', 'Fudge', '15.00', 'prod-fudge.webp'),
    ('gift-boxes', 'Gift Boxes', '50.00', 'prod-gift-boxes.webp'),
    ('seasonal-treats', 'Seasonal Treats', '40.00', 'prod-seasonal-treats.webp'),
]
MENU = [
    ('Classic Chocolate Fudge', '14.99'),
    ('Salted Caramel Fudge', '15.99'),
    ('Peanut Butter Chocolate Fudge', '18.99'),
    ('Custom Party Favor Box', '24.99'),
    ('Gourmet Fudge Gift Box (12 Pieces)', '29.99'),
]
LEFT = [('index.html', 'Home'), ('about.html', 'About'), ('products.html', 'Products'), ('services.html', 'Services')]
RIGHT = [('blog.html', 'Blog'), ('contact.html', 'Contact'), ('menu.html', 'Menu'), ('pictures.html', 'Pictures')]

ICON = {
 'phone': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>',
}
e = html.escape

def tel(p): return 'tel:+1' + p.replace('-', '')

def todo(what):
    return f'<div class="todo"><strong>Jia\'s words go here</strong>{e(what)}</div>'

def page(fname, title, desc, body, current=None):
    nav = lambda items: ''.join(
        f'<li><a class="link" href="{h}"{" aria-current=page" if h == current else ""}>{t}</a></li>' for h, t in items)
    mob = ''.join(f'<a href="{h}"{" aria-current=page" if h == current else ""}>{t}</a>' for h, t in LEFT + RIGHT)
    robots = '<meta name="robots" content="noindex, nofollow">\n' if NOINDEX else ''
    year = '2026'
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots}<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="images/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Satisfy&display=swap">
<link rel="stylesheet" href="css/site.css?v={VER}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span class="phones">
    <a href="{tel(PHONE1)}">{ICON['phone']}{PHONE1}</a>
    <a href="{tel(PHONE2)}">{ICON['phone']}{PHONE2}</a>
  </span>
  <span class="extra">
    <a href="mailto:{EMAIL}">{ICON['mail']}{EMAIL}</a>
    <a href="contact.html">{ICON['pin']}Servicing Long Island</a>
  </span>
</div></div>
<header class="site-header">
  <nav class="nav" aria-label="Main">
    <ul>{nav(LEFT)}</ul>
    <a class="logo" href="index.html" aria-label="Jia's Sweets home"><img src="images/logo.png" alt="Jia's Sweets – Fudge &amp; Confections" width="120" height="110"></a>
    <ul class="right">{nav(RIGHT)}</ul>
    <button class="menu-btn" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu"><span></span></button>
    <div class="mobile-menu" id="mobile-menu">{mob}</div>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap cols">
    <div>
      <a class="logo" href="index.html"><img src="images/logo.png" alt="Jia's Sweets" width="130" height="119"></a>
      <p>Handcrafted fudge, sweet favors and custom confections, made by hand on Long Island.</p>
    </div>
    <div><h2>Quick links</h2><ul>
      <li><a href="about.html">About</a></li><li><a href="products.html">Products</a></li>
      <li><a href="services.html">Services</a></li><li><a href="menu.html">Menu</a></li>
      <li><a href="pictures.html">Pictures</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul></div>
    <div><h2>Contact us</h2><ul>
      <li><a class="nowrap" href="{tel(PHONE1)}">{PHONE1}</a></li>
      <li><a class="nowrap" href="{tel(PHONE2)}">{PHONE2}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>Servicing Long Island</li></ul></div>
    <div><h2>Order &amp; pay</h2>
      <p>We accept orders and payments with Square.</p>
      <img class="square" src="images/square.png" alt="Square" width="120" height="34">
    </div>
  </div>
  <div class="copy">© {year} Jia's Sweets · Website by <a href="https://islandpixelstudios.com">Island Pixel Studios</a></div>
</footer>
<script src="js/site.js?v={VER}"></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f:
        f.write(doc)

def heading(kicker_pink, kicker_rest, title_html, center=True):
    c = ' center' if center else ''
    return (f'<div class="{c.strip()}"><p class="kicker">{kicker_pink} <b>{kicker_rest}</b></p>'
            f'<h2 class="title">{title_html}</h2>'
            f'<img class="divider" src="images/heart-divider.png" alt="" width="105" height="19"></div>')

def cards(items=PRODUCTS):
    out = []
    for slug, name, price, img in items:
        out.append(f'''<article class="card">
  <a class="pic" href="product-{slug}.html"><img src="images/{img}" alt="{e(name)}" loading="lazy" width="450" height="450"></a>
  <div class="body"><h3><a href="product-{slug}.html">{e(name)}</a></h3><span class="price">${price}</span>
  <a class="btn" href="product-{slug}.html">View &amp; order</a></div>
</article>''')
    return '<div class="grid">' + ''.join(out) + '</div>'

def banner(title, crumb=None):
    c = f'<p class="crumbs"><a href="index.html">Home</a> / {crumb or e(title)}</p>'
    return f'<section class="banner"><div class="wrap"><h1>{e(title)}</h1>{c}</div></section>'

CALLOUT = '''<section class="callout band"><div class="wrap"><div class="box">
  <h2>Need custom fudge or party favors?</h2>
  <p>We create handcrafted fudge, sweet favors and custom confections tailored to your special event.</p>
  <a class="btn" href="contact.html">Design your own favor</a>
</div></div></section>'''

WHERE = f'''<section class="split band bg-cream"><div class="wrap">
  <div class="media"><img src="images/prod-gift-boxes.webp" alt="Gift box with fudge" loading="lazy" width="900" height="773"></div>
  <div>{heading("Where's the", "fudge", "Find us", center=False)}
    {todo("Where people can buy Jia's fudge: markets, shops, pop-ups or events, with days and times.")}
    <p style="margin-top:20px"><a class="btn brown" href="contact.html">Ask where we'll be next</a></p></div>
</div></section>'''

MENU_TEASER = f'''<section class="split reverse band bg-teal"><div class="wrap">
  <div class="media"><img src="images/prod-seasonal-treats.webp" alt="Seasonal chocolate treats" loading="lazy" width="900" height="900"></div>
  <div>{heading("What's on the", "menu today?", "Fresh this week", center=False)}
    <p>Classic chocolate, salted caramel, peanut butter chocolate and more, plus favor boxes and gift boxes.</p>
    <a class="btn brown" href="menu.html">See our menu</a></div>
</div></section>'''

def build():
    os.makedirs(OUT, exist_ok=True)
    # Home
    feats = ''.join(f'<div class="feature"><img src="images/{i}" alt="" width="58" height="58"><span>{t}</span></div>' for i, t in
                    [('icon-love.png', 'Made<br>with love'), ('icon-ingredients.png', 'Premium<br>ingredients'),
                     ('icon-occasion.png', 'Perfect for<br>any occasion'), ('icon-location.png', 'Servicing<br>Long Island')])
    home = f'''<section class="hero"><div class="wrap">
  <div>
    <p class="kicker">Handcrafted <b>with love</b></p>
    <h1>Sweet moments</h1>
    <p class="script">made by hand</p>
    {todo("One or two sentences in Jia's voice: what she makes and who it's for.")}
    <div class="actions"><a class="btn" href="products.html">Shop our products</a><a class="btn ghost" href="contact.html">Design your own favor</a></div>
  </div>
  <div class="hero-img"><img src="images/prod-fudge.webp" alt="Assorted handmade fudge" width="900" height="900"></div>
</div></section>
<section class="features"><div class="wrap">{feats}</div></section>
<section class="band"><div class="wrap">
  {heading("Explore our", "favorites", "Handcrafted <em>creations</em>")}
  {cards()}
  <p class="center" style="margin-top:30px"><a class="btn" href="products.html">View all products</a></p>
</div></section>
<section class="split band bg-blush"><div class="wrap">
  <div class="media"><img src="images/prod-events-favor.webp" alt="Event favor bags" loading="lazy" width="900" height="788"></div>
  <div>{heading("What we", "do", "Custom sweets for every occasion and celebration.", center=False)}
    {todo("A short paragraph about Jia's services: custom favors, event orders, gift boxes, how far ahead to order.")}
    <p style="margin-top:20px"><a class="btn brown" href="services.html">Learn more about our services</a></p></div>
</div></section>
{CALLOUT}
{WHERE}
{MENU_TEASER}
<section class="band bg-brown"><div class="wrap center" style="max-width:760px">
  <h2 class="title">Kind words</h2>
  {todo("Real reviews from Jia's customers, in their own words, with first name and town. Leave this section out until she has some.")}
</div></section>'''
    page('index.html', "Jia's Sweets | Handcrafted Fudge & Party Favors on Long Island",
         "Handcrafted fudge, custom party favors, gift boxes and seasonal treats made by hand on Long Island.", home, 'index.html')

    # About
    about = f'''{banner("About")}
<section class="split band"><div class="wrap">
  <div>{heading("About", "us", "Crafting delicious moments every day", center=False)}
    {todo("Jia's story: who she is, how Jia's Sweets started, what makes her fudge different. Her words, a few short paragraphs.")}</div>
  <div class="media"><img src="images/about.webp" alt="Jia's Sweets treats" width="1264" height="844"></div>
</div></section>
{CALLOUT}
{WHERE}
{MENU_TEASER}'''
    page('about.html', "About | Jia's Sweets", "The story behind Jia's Sweets, handcrafted fudge and confections on Long Island.", about, 'about.html')

    # Products
    prods = f'''{banner("Products")}
<section class="band"><div class="wrap">
  {heading("Explore our", "favorites", "Handcrafted <em>creations</em>")}
  {cards()}
</div></section>
{CALLOUT}'''
    page('products.html', "Products | Jia's Sweets", "Fudge, custom favors, event favors, gift boxes and seasonal treats from Jia's Sweets.", prods, 'products.html')

    # Services
    serv = f'''{banner("Services")}
<section class="split band"><div class="wrap">
  <div class="media"><img src="images/prod-custom-connections.webp" alt="Custom favor bag with Jia's Sweets label" width="900" height="793"></div>
  <div>{heading("What we", "do", "Custom sweets for every occasion and celebration.", center=False)}
    {todo("Each service Jia offers (for example: wedding and shower favors, corporate gifts, holiday boxes), with minimum order and lead time.")}
    <p style="margin-top:20px"><a class="btn" href="contact.html">Request a quote</a></p></div>
</div></section>
<section class="band bg-cream"><div class="wrap">
  {heading("Explore our", "favorites", "Handcrafted <em>creations</em>")}
  {cards()}
</div></section>'''
    page('services.html', "Services | Jia's Sweets", "Custom fudge, party favors and gift boxes for weddings, showers, holidays and events on Long Island.", serv, 'services.html')

    # Menu
    items = ''.join(f'<li><span>{e(n)}</span><span class="p">${p}</span></li>' for n, p in MENU)
    menu = f'''{banner("Our Menu")}
<section class="band"><div class="wrap">
  {heading("Our", "menu", "Taste the magic in every slice")}
  <ul class="menu-list">{items}</ul>
</div></section>
<section class="band bg-cream"><div class="wrap">
  {heading("Explore our", "favorites", "Handcrafted <em>creations</em>")}
  {cards()}
</div></section>'''
    page('menu.html', "Menu | Jia's Sweets", "Jia's Sweets menu: chocolate, salted caramel and peanut butter fudge, favor boxes and gift boxes.", menu, 'menu.html')

    # Pictures
    gal = '<img src="images/about.webp" alt="Jia\'s Sweets treats" loading="lazy" width="1264" height="844"><img src="images/blog-fudge.webp" alt="Handcrafted fudge" loading="lazy" width="1296" height="725">'
    pics = f'''{banner("Pictures")}
<section class="band"><div class="wrap">
  {heading("Most popular", "creations", "From our kitchen")}
  {todo("More of Jia's own photos: finished orders, events, her kitchen. Her real photos will make this page.")}
  <div class="gallery" style="margin-top:20px">{''.join(f'<img src="images/{p[3]}" alt="{e(p[1])}" loading="lazy" width="450" height="450">' for p in PRODUCTS)}{gal}</div>
</div></section>
{CALLOUT}'''
    page('pictures.html', "Pictures | Jia's Sweets", "Photos of handcrafted fudge, favors and gift boxes by Jia's Sweets.", pics, 'pictures.html')

    # Blog
    blog = f'''{banner("Blog")}
<section class="band"><div class="wrap">
  {heading("Explore our", "blog", "What's new at Jia's Sweets")}
  <article class="post-card">
    <a href="blog-handcrafted-fudge.html"><img src="images/blog-fudge.webp" alt="Handcrafted fudge" loading="lazy" width="1296" height="725"></a>
    <div class="body"><p class="meta">June 12, 2026</p>
      <h2><a href="blog-handcrafted-fudge.html">Handcrafted Fudge – Made Fresh with Love</a></h2>
      <a class="btn ghost" href="blog-handcrafted-fudge.html">Read more</a></div>
  </article>
</div></section>'''
    page('blog.html', "Blog | Jia's Sweets", "News and stories from Jia's Sweets.", blog, 'blog.html')
    post = f'''{banner("Handcrafted Fudge – Made Fresh with Love", '<a href="blog.html">Blog</a>')}
<section class="band"><div class="wrap"><article class="post">
  <p class="meta">June 12, 2026</p>
  <img src="images/blog-fudge.webp" alt="Handcrafted fudge" width="1296" height="725">
  {todo("The blog post itself, written by Jia.")}
</article></div></section>'''
    page('blog-handcrafted-fudge.html', "Handcrafted Fudge – Made Fresh with Love | Jia's Sweets", "How Jia's Sweets makes its fudge by hand.", post, 'blog.html')

    # Contact
    contact = f'''{banner("Contact")}
<section class="band split"><div class="wrap" style="align-items:start">
  <div>
    <p class="kicker">Did not find your <b>answer?</b></p>
    <h2 class="title">Get in touch</h2>
    <img class="divider" style="margin-left:0" src="images/heart-divider.png" alt="" width="105" height="19">
    <form class="contact" id="contact-form" action="https://api.web3forms.com/submit" method="POST">
      <input type="hidden" name="access_key" value="WEB3FORMS_KEY_AT_LAUNCH">
      <input type="hidden" name="subject" value="New message from jiassweets.com">
      <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
      <div class="row"><label>Name<input name="name" autocomplete="name" required></label>
        <label>Email<input type="email" name="email" autocomplete="email" required></label></div>
      <div class="row"><label>Phone (optional)<input type="tel" name="phone" autocomplete="tel"></label>
        <label>What's it for?<select name="topic"><option>General question</option><option>Custom favors</option><option>Event order</option><option>Gift boxes</option><option>Other</option></select></label></div>
      <label>Message<textarea name="message" required></textarea></label>
      <div><button class="btn" type="submit">Send message</button></div>
      <p class="form-msg" role="status" aria-live="polite"></p>
    </form>
  </div>
  <div class="contact-cards">
    <a href="{tel(PHONE1)}">{ICON['phone']}{PHONE1}</a>
    <a href="{tel(PHONE2)}">{ICON['phone']}{PHONE2}</a>
    <a href="mailto:{EMAIL}">{ICON['mail']}{EMAIL}</a>
    <div>{ICON['pin']}Servicing Long Island</div>
  </div>
</div></section>'''
    page('contact.html', "Contact | Jia's Sweets", "Contact Jia's Sweets for custom fudge, party favors, event orders and gift boxes on Long Island.", contact, 'contact.html')

    # Product pages
    for slug, name, price, img in PRODUCTS:
        others = [p for p in PRODUCTS if p[0] != slug][:4]
        body = f'''<section class="banner" style="padding:28px 0"><div class="wrap"><p class="crumbs" style="margin:0"><a href="index.html">Home</a> / <a href="products.html">Products</a> / {e(name)}</p></div></section>
<section class="product band"><div class="wrap">
  <img src="images/{img}" alt="{e(name)}" width="900" height="900">
  <div>
    <h1>{e(name)}</h1>
    <span class="price">${price}</span>
    {todo(f"A short description of {name}: what's in it, sizes or flavors, how far ahead to order.")}
    <p style="margin-top:22px"><a class="btn" href="contact.html">Order this</a></p>
    <p class="order-note">Online payment with Square will be added here.</p>
  </div>
</div></section>
<section class="band bg-cream"><div class="wrap">
  {heading("You may", "also like", "More <em>creations</em>")}
  {cards(others)}
</div></section>'''
        page(f'product-{slug}.html', f"{name} | Jia's Sweets", f"{name} from Jia's Sweets, ${price}. Handcrafted on Long Island.", body, 'products.html')

    with open(os.path.join(OUT, 'robots.txt'), 'w') as f:
        f.write('User-agent: *\nDisallow: /\n' if NOINDEX else 'User-agent: *\nAllow: /\n')

if __name__ == '__main__':
    build()
    print('built', sorted(os.listdir(OUT)))
