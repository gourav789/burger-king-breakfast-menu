#!/usr/bin/env python3
"""
Master Multilingual Site Generator for Burger King Breakfast Menu UK
Generates all 5 languages (English, Spanish, French, German, Hindi) for all 7 pages.
Ensures full Google SEO compatibility, hreflangs, canonicals, sitemap, and robots.txt.
"""

import os
import re
import json

from i18n_data import COMMON_I18N
from i18n_pages import PAGE_META
from i18n_content import INDEX_CONTENT
from i18n_prose import ABOUT_CONTENT, CONTACT_CONTENT
from i18n_legal import LEGAL_CONTENT
from i18n_menu_cards import MENU_CATEGORIES

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://burgerkingbreakfastmenu.co.uk"

LANGS = ['en', 'es', 'fr', 'de', 'hi']

LANG_META = {
    'en': {'code': 'en', 'locale': 'en_GB', 'name': 'English', 'flag': '🇬🇧', 'native': 'English (UK)', 'sub': ''},
    'es': {'code': 'es', 'locale': 'es_ES', 'name': 'Spanish', 'flag': '🇪🇸', 'native': 'Español', 'sub': 'es/'},
    'fr': {'code': 'fr', 'locale': 'fr_FR', 'name': 'French', 'flag': '🇫🇷', 'native': 'Français', 'sub': 'fr/'},
    'de': {'code': 'de', 'locale': 'de_DE', 'name': 'German', 'flag': '🇩🇪', 'native': 'Deutsch', 'sub': 'de/'},
    'hi': {'code': 'hi', 'locale': 'hi_IN', 'name': 'Hindi', 'flag': '🇮🇳', 'native': 'हिन्दी', 'sub': 'hi/'},
}

PAGES = ['index', 'menu', 'calories', 'about', 'contact', 'privacy-policy', 'disclaimer']

def get_page_url(lang, slug):
    sub = LANG_META[lang]['sub']
    if slug == 'index':
        return f"{SITE_URL}/{sub}" if sub else f"{SITE_URL}/"
    else:
        return f"{SITE_URL}/{sub}{slug}"

def get_rel_url(curr_lang, target_lang, slug):
    is_sub = bool(LANG_META[curr_lang]['sub'])
    prefix = "../" if is_sub else ""
    target_sub = LANG_META[target_lang]['sub']
    if slug == 'index':
        if not target_sub:
            return "../" if is_sub else "index"
        else:
            return "index" if curr_lang == target_lang else f"{prefix}{target_sub}"
    else:
        if curr_lang == target_lang:
            return slug
        else:
            return f"{prefix}{target_sub}{slug}"

def get_asset_prefix(lang):
    return "../" if LANG_META[lang]['sub'] else ""

def generate_hreflangs(slug):
    lines = [f'  <link rel="alternate" hreflang="x-default" href="{get_page_url("en", slug)}" />']
    for l in LANGS:
        lines.append(f'  <link rel="alternate" hreflang="{l}" href="{get_page_url(l, slug)}" />')
    return "\n".join(lines)

def build_switchers(curr_lang, slug):
    meta = LANG_META[curr_lang]
    
    # Topbar dropdown
    opts = []
    for l in LANGS:
        l_meta = LANG_META[l]
        active = " active" if l == curr_lang else ""
        link = get_rel_url(curr_lang, l, slug)
        opts.append(f'        <a href="{link}" class="lang-option{active}" role="menuitem"><span class="lang-opt-flag">{l_meta["flag"]}</span> {l_meta["native"]}</a>')
    
    topbar = f'''      <div class="lang-selector-wrap" id="langSelector">
        <button class="lang-btn" id="langToggleBtn" aria-label="Select Language" aria-expanded="false">
          <span class="lang-flag">{meta['flag']}</span>
          <span class="lang-text">{meta['code'].upper()}</span>
          <span class="lang-arrow">▼</span>
        </button>
        <div class="lang-dropdown" id="langDropdown" role="menu">
{chr(10).join(opts)}
        </div>
      </div>'''

    # Sidebar chips
    chips = []
    for l in LANGS:
        l_meta = LANG_META[l]
        active = " active" if l == curr_lang else ""
        link = get_rel_url(curr_lang, l, slug)
        chips.append(f'        <a href="{link}" class="sidebar-lang-chip{active}">{l_meta["flag"]} {l_meta["code"].upper()}</a>')

    sidebar = f'''    <div class="sidebar-lang-container">
      <div class="sidebar-lang-label"><span>🌐</span> Language</div>
      <div class="sidebar-lang-grid">
{chr(10).join(chips)}
      </div>
    </div>'''
    
    return topbar, sidebar

def build_sidebar(lang, active_slug):
    t = COMMON_I18N[lang]
    topbar_sw, sidebar_sw = build_switchers(lang, active_slug)
    
    home_act = ' active' if active_slug == 'index' else ''
    menu_act = ' active' if active_slug == 'menu' else ''
    cal_act  = ' active' if active_slug == 'calories' else ''
    abt_act  = ' active' if active_slug == 'about' else ''
    cnt_act  = ' active' if active_slug == 'contact' else ''
    prv_act  = ' active' if active_slug == 'privacy-policy' else ''
    dsc_act  = ' active' if active_slug == 'disclaimer' else ''
    
    home_link = 'index'
    menu_link = 'menu'
    cal_link = 'calories'
    abt_link = 'about'
    cnt_link = 'contact'
    prv_link = 'privacy-policy'
    dsc_link = 'disclaimer'

    return f'''  <!-- ===== SIDEBAR ===== -->
  <aside class="sidebar" id="sidebar" aria-label="Site navigation">
    <div class="sidebar-logo">
      <div class="sidebar-logo-icon">🍔</div>
      <div class="sidebar-logo-text">
        <strong>{t['site_title']}</strong>
        <span>{t['site_domain']}</span>
      </div>
    </div>
    <div class="sidebar-search">
      <div class="search-wrap">
        <span class="search-icon">🔍</span>
        <input type="search" id="sidebarSearch" placeholder="{t['search_placeholder']}" aria-label="Search menu" />
      </div>
    </div>
{sidebar_sw}
    <nav class="sidebar-nav" aria-label="Main menu">
      <a href="{home_link}" class="nav-top-link{home_act}"><span class="nav-icon">🏠</span> {t['nav_home']}</a>
      <a href="{menu_link}" class="nav-top-link{menu_act}"><span class="nav-icon">📋</span> {t['nav_menu']}</a>
      <a href="{cal_link}" class="nav-top-link{cal_act}"><span class="nav-icon">🔥</span> {t['nav_calories']}</a>
      <div class="sidebar-divider"></div>
      <div class="nav-section">
        <div class="nav-section-header" tabindex="0" role="button" aria-expanded="false">
          <div class="nav-section-left"><span class="nav-section-icon">🥐</span><span>{t['nav_breakfast']}</span><span class="nav-section-badge">9</span></div>
          <span class="nav-section-arrow">▶</span>
        </div>
        <ul class="nav-children">
          <li><a href="{menu_link}#breakfast" class="nav-link">Croissan'wiches</a></li>
          <li><a href="{menu_link}#breakfast" class="nav-link">Breakfast King</a></li>
          <li><a href="{menu_link}#breakfast" class="nav-link">Potato Bites</a></li>
          <li><a href="{menu_link}#breakfast" class="nav-link">Hot Drinks</a></li>
        </ul>
      </div>
      <div class="nav-section">
        <div class="nav-section-header" tabindex="0" role="button" aria-expanded="false">
          <div class="nav-section-left"><span class="nav-section-icon">🍔</span><span>{t['nav_burgers']}</span><span class="nav-section-badge">22</span></div>
          <span class="nav-section-arrow">▶</span>
        </div>
        <ul class="nav-children">
          <li><a href="{menu_link}#burgers" class="nav-link">WHOPPER®</a></li>
          <li><a href="{menu_link}#burgers" class="nav-link">Big King</a></li>
          <li><a href="{menu_link}#burgers" class="nav-link">Chicken Royale</a></li>
          <li><a href="{menu_link}#burgers" class="nav-link">Plant-Based</a></li>
          <li><a href="{menu_link}#burgers" class="nav-link">Wagyu Range</a></li>
        </ul>
      </div>
      <div class="nav-section">
        <div class="nav-section-header" tabindex="0" role="button" aria-expanded="false">
          <div class="nav-section-left"><span class="nav-section-icon">🍗</span><span>{t['nav_chicken']}</span><span class="nav-section-badge">8</span></div>
          <span class="nav-section-arrow">▶</span>
        </div>
        <ul class="nav-children">
          <li><a href="{menu_link}#chicken" class="nav-link">Chicken Nuggets</a></li>
          <li><a href="{menu_link}#chicken" class="nav-link">Chicken Fries</a></li>
          <li><a href="{menu_link}#chicken" class="nav-link">Burger Buddies</a></li>
        </ul>
      </div>
      <div class="nav-section">
        <div class="nav-section-header" tabindex="0" role="button" aria-expanded="false">
          <div class="nav-section-left"><span class="nav-section-icon">🍟</span><span>{t['nav_sides']}</span><span class="nav-section-badge">10</span></div>
          <span class="nav-section-arrow">▶</span>
        </div>
        <ul class="nav-children">
          <li><a href="{menu_link}#sides" class="nav-link">Fries</a></li>
          <li><a href="{menu_link}#sides" class="nav-link">Loaded King Fries</a></li>
          <li><a href="{menu_link}#sides" class="nav-link">Halloumi Fries</a></li>
          <li><a href="{menu_link}#sides" class="nav-link">Dip Pots</a></li>
        </ul>
      </div>
      <div class="nav-section">
        <div class="nav-section-header" tabindex="0" role="button" aria-expanded="false">
          <div class="nav-section-left"><span class="nav-section-icon">🎁</span><span>{t['nav_meals']}</span><span class="nav-section-badge">14</span></div>
          <span class="nav-section-arrow">▶</span>
        </div>
        <ul class="nav-children">
          <li><a href="{menu_link}#meals" class="nav-link">King Boxes</a></li>
          <li><a href="{menu_link}#meals" class="nav-link">Kids Meals</a></li>
          <li><a href="{menu_link}#meals" class="nav-link">Galactic Mandalorian</a></li>
        </ul>
      </div>
      <div class="nav-section">
        <div class="nav-section-header" tabindex="0" role="button" aria-expanded="false">
          <div class="nav-section-left"><span class="nav-section-icon">🍦</span><span>{t['nav_desserts']}</span><span class="nav-section-badge">22</span></div>
          <span class="nav-section-arrow">▶</span>
        </div>
        <ul class="nav-children">
          <li><a href="{menu_link}#desserts" class="nav-link">Sundaes</a></li>
          <li><a href="{menu_link}#desserts" class="nav-link">Milkshakes</a></li>
          <li><a href="{menu_link}#desserts" class="nav-link">King Fusion</a></li>
          <li><a href="{menu_link}#desserts" class="nav-link">Ben &amp; Jerry's</a></li>
        </ul>
      </div>
      <div class="nav-section">
        <div class="nav-section-header" tabindex="0" role="button" aria-expanded="false">
          <div class="nav-section-left"><span class="nav-section-icon">🥤</span><span>{t['nav_drinks']}</span><span class="nav-section-badge">20</span></div>
          <span class="nav-section-arrow">▶</span>
        </div>
        <ul class="nav-children">
          <li><a href="{menu_link}#drinks" class="nav-link">Soft Drinks</a></li>
          <li><a href="{menu_link}#drinks" class="nav-link">Frozen Fanta</a></li>
          <li><a href="{menu_link}#drinks" class="nav-link">Energy Drinks</a></li>
          <li><a href="{menu_link}#drinks" class="nav-link">Hot Beverages</a></li>
        </ul>
      </div>
      <div class="sidebar-divider"></div>
      <a href="{abt_link}" class="nav-top-link{abt_act}"><span class="nav-icon">ℹ️</span> {t['nav_about']}</a>
      <a href="{cnt_link}" class="nav-top-link{cnt_act}"><span class="nav-icon">✉️</span> {t['nav_contact']}</a>
      <a href="{prv_link}" class="nav-top-link{prv_act}"><span class="nav-icon">🔒</span> {t['nav_privacy']}</a>
      <a href="{dsc_link}" class="nav-top-link{dsc_act}"><span class="nav-icon">⚠️</span> {t['nav_disclaimer']}</a>
    </nav>
    <div class="sidebar-footer">{t['sidebar_footer']}</div>
  </aside>'''

def build_topbar(lang, slug):
    meta = PAGE_META[slug][lang]
    t = COMMON_I18N[lang]
    topbar_sw, _ = build_switchers(lang, slug)
    
    if slug == 'index':
        breadcrumb_html = f'<span>{meta["breadcrumb"]}</span>'
    else:
        breadcrumb_html = f'<a href="index">{t["nav_home"]}</a> / <span>{meta["breadcrumb"]}</span>'

    return f'''    <header class="topbar">
      <div class="topbar-left">
        <button class="hamburger-btn" id="hamburgerBtn" aria-label="Open navigation menu"><span></span><span></span><span></span></button>
        <h2>{t['site_title']}</h2>
      </div>
      <div class="topbar-right">
        <div class="topbar-breadcrumb">{breadcrumb_html}</div>
{topbar_sw}
      </div>
    </header>'''

def build_footer(lang):
    t = COMMON_I18N[lang]
    return f'''      <!-- ===== FOOTER ===== -->
      <footer class="site-footer fade-in">
        <div class="footer-container">
          <div class="footer-top">
            <div class="footer-brand">
              <div class="footer-logo">🍔 {t['site_title']}</div>
              <p>{t['footer_rights']}</p>
            </div>
            <nav class="footer-nav" aria-label="Footer navigation">
              <a href="index">{t['nav_home']}</a>
              <a href="menu">{t['nav_menu']}</a>
              <a href="calories">{t['nav_calories']}</a>
              <a href="about">{t['nav_about']}</a>
              <a href="contact">{t['nav_contact']}</a>
              <a href="privacy-policy">{t['nav_privacy']}</a>
              <a href="disclaimer">{t['nav_disclaimer']}</a>
            </nav>
          </div>
          <div class="footer-bottom">
            <div class="footer-copy">© 2024–2026 {t['site_title']} • {t['site_domain']}</div>
            <div class="footer-disclaimer">{t['footer_trademark']}</div>
          </div>
        </div>
      </footer>'''

def build_head(lang, slug):
    meta = PAGE_META[slug][lang]
    hreflangs = generate_hreflangs(slug)
    canonical = get_page_url(lang, slug)
    asset_p = get_asset_prefix(lang)
    locale = LANG_META[lang]['locale']
    
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta name="msvalidate.01" content="BDA14BCC33E0B333F058CFB01996A9B6" />
  
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-V96KCK1QB4"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'G-V96KCK1QB4');
  </script>
  
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{meta['title']}</title>
  <meta name="description" content="{meta['desc']}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />
{hreflangs}
  <meta property="og:title" content="{meta['og_title']}" />
  <meta property="og:description" content="{meta['og_desc']}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="{locale}" />
  <link rel="stylesheet" href="{asset_p}css/style.css" />
</head>
<body>
<div class="overlay" id="overlay"></div>
<div class="layout">'''

def build_page_wrapper(lang, slug, main_html):
    head = build_head(lang, slug)
    sidebar = build_sidebar(lang, slug)
    topbar = build_topbar(lang, slug)
    footer = build_footer(lang)
    asset_p = get_asset_prefix(lang)
    
    return f'''{head}

{sidebar}

  <!-- ===== MAIN CONTENT ===== -->
  <div class="main-content">

{topbar}

    <main class="page-content" id="main">
{main_html}
    </main>

{footer}

  </div>
</div>

<script src="{asset_p}js/main.js"></script>
</body>
</html>
'''

# ----------------- PAGE GENERATORS -----------------

FEATURED_CARDS = {
    'en': [
        {'img': 'Fully Loaded Croissanwich with Egg.gmsr.png', 'name': 'Fully Loaded Croissanwich® with Egg', 'badge': '⭐ Best Seller', 'desc': 'The ultimate BK breakfast. Flaky croissant loaded with egg, cheese, sausage, and bacon – everything in one perfect bite.'},
        {'img': 'Beef Croissan’wich with Egg.gmsr.png', 'name': 'Beef Croissan\'wich® with Egg', 'badge': '🔥 Popular', 'desc': 'Flame-grilled beef patty with a fresh egg and melted cheese on a warm, buttery croissant bun.'},
        {'img': 'Beefacon Croissan’wich with Egg.gmsr.png', 'name': 'Beefacon Croissan\'wich® with Egg', 'badge': '', 'desc': 'The best of beef AND bacon combined with egg on a golden croissant for a truly indulgent breakfast.'},
        {'img': 'Chicken Strips Croissan’wich with Egg.gmsr.png', 'name': 'Chicken Strips Croissan\'wich® with Egg', 'badge': '', 'desc': 'Crispy chicken strips with egg and melted cheese wrapped in a flaky croissant – a fan favourite.'},
        {'img': 'Chick’N Crisp Croissan’wich with Egg.gmsr.png', 'name': 'Chick\'N Crisp Croissan\'wich® with Egg', 'badge': '', 'desc': 'A lighter crispy chicken fillet paired with a fresh egg on a warm croissant. Light yet satisfying.'},
        {'img': 'Breakfast King.gmsr.avif', 'name': 'Breakfast King®', 'badge': '👑 Signature', 'desc': 'A flame-grilled beef burger layered with egg and cheese. Hearty, filling, and built for serious morning hunger.'},
        {'img': 'Potato Bites.gmsr.png', 'name': 'Potato Bites', 'badge': '🍟 Essential Side', 'desc': 'Golden, bite-sized hash brown potato pieces. Crispy on the outside, fluffy inside – the essential breakfast side.'},
        {'img': 'Americano.gmsr.avif', 'name': 'Americano Coffee', 'badge': '☕ 100% Arabica', 'desc': 'Freshly ground and brewed 100% Arabica coffee. Rich, smooth, and the perfect morning energy boost.'},
        {'img': 'Cappuccino.gmsr.avif', 'name': 'Cappuccino', 'badge': '', 'desc': 'Rich espresso topped with velvety steamed and foamed milk. A classic morning coffee made with quality Arabica beans.'},
    ],
    'es': [
        {'img': 'Fully Loaded Croissanwich with Egg.gmsr.png', 'name': 'Fully Loaded Croissanwich® con Huevo', 'badge': '⭐ Más Vendido', 'desc': 'El desayuno definitivo de BK: salchicha, beicon crujiente, huevo fresco y queso fundido en un cruasán caliente y hojaldrado.'},
        {'img': 'Beef Croissan’wich with Egg.gmsr.png', 'name': 'Beef Croissan\'wich® con Huevo', 'badge': '🔥 Popular', 'desc': 'Hamburguesa de ternera a la parrilla con huevo fresco y queso fundido en un panecillo de cruasán mantecoso.'},
        {'img': 'Beefacon Croissan’wich with Egg.gmsr.png', 'name': 'Beefacon Croissan\'wich® con Huevo', 'badge': '', 'desc': 'La mejor combinación de ternera y beicon con huevo y queso en un cruasán dorado y crujiente.'},
        {'img': 'Chicken Strips Croissan’wich with Egg.gmsr.png', 'name': 'Chicken Strips Croissan\'wich® con Huevo', 'badge': '', 'desc': 'Tiras de pollo crujiente con huevo y queso fundido envueltos en un cruasán tierno.'},
        {'img': 'Chick’N Crisp Croissan’wich with Egg.gmsr.png', 'name': 'Chick\'N Crisp Croissan\'wich® con Huevo', 'badge': '', 'desc': 'Filete de pollo empanado más ligero acompañado de huevo fresco en un cruasán caliente.'},
        {'img': 'Breakfast King.gmsr.avif', 'name': 'Breakfast King®', 'badge': '👑 Especialidad', 'desc': 'Hamburguesa completa con carne a la parrilla, huevo y queso para los desayunos más contundentes.'},
        {'img': 'Potato Bites.gmsr.png', 'name': 'Potato Bites', 'badge': '🍟 Crujiente', 'desc': 'Pequeños bocaditos de patata dorados y crujientes por fuera, tiernos por dentro. El complemento imprescindible.'},
        {'img': 'Americano.gmsr.avif', 'name': 'Café Americano', 'badge': '☕ 100% Arábica', 'desc': 'Café 100% arábica recién molido y filtrado. Intenso, aromático y con toda la energía que necesitas.'},
        {'img': 'Cappuccino.gmsr.avif', 'name': 'Cappuccino', 'badge': '', 'desc': 'Espresso intenso cubierto de cremosa espuma de leche emulsionada. Elaborado con granos arábica seleccionados.'},
    ],
    'fr': [
        {'img': 'Fully Loaded Croissanwich with Egg.gmsr.png', 'name': 'Fully Loaded Croissanwich® avec Œuf', 'badge': '⭐ Meilleure Vente', 'desc': 'Le sandwich matinal ultime de BK : saucisse, bacon croustillant, œuf frais et fromage fondant dans un croissant chaud et feuilleté.'},
        {'img': 'Beef Croissan’wich with Egg.gmsr.png', 'name': 'Beef Croissan\'wich® avec Œuf', 'badge': '🔥 Populaire', 'desc': 'Steak de bœuf grillé à la flamme, œuf frais et fromage fondu dans un croissant pur beurre.'},
        {'img': 'Beefacon Croissan’wich with Egg.gmsr.png', 'name': 'Beefacon Croissan\'wich® avec Œuf', 'badge': '', 'desc': 'L\'alliance parfaite du bœuf grillé et du bacon avec œuf et fromage dans un croissant croustillant.'},
        {'img': 'Chicken Strips Croissan’wich with Egg.gmsr.png', 'name': 'Chicken Strips Croissan\'wich® avec Œuf', 'badge': '', 'desc': 'Aiguillettes de poulet croustillantes avec œuf et fromage dans un pain croissant moelleux.'},
        {'img': 'Chick’N Crisp Croissan’wich with Egg.gmsr.png', 'name': 'Chick\'N Crisp Croissan\'wich® avec Œuf', 'badge': '', 'desc': 'Filet de poulet pané croustillant et œuf frais dans un croissant doré.'},
        {'img': 'Breakfast King.gmsr.avif', 'name': 'Breakfast King®', 'badge': '👑 Signature', 'desc': 'Un burger complet au bœuf grillé à la flamme garni d\'œuf et de fromage pour les grands appétits du matin.'},
        {'img': 'Potato Bites.gmsr.png', 'name': 'Potato Bites', 'badge': '🍟 Incontournable', 'desc': 'Bouchées de pommes de terre dorées et croustillantes à l\'extérieur, tendres à cœur.'},
        {'img': 'Americano.gmsr.avif', 'name': 'Café Americano', 'badge': '☕ 100% Arabica', 'desc': 'Café 100% Arabica fraîchement moulu. Arôme riche et corsé pour un réveil énergique.'},
        {'img': 'Cappuccino.gmsr.avif', 'name': 'Cappuccino', 'badge': '', 'desc': 'Espresso intense surmonté d\'une mousse de lait veloutée et onctueuse.'},
    ],
    'de': [
        {'img': 'Fully Loaded Croissanwich with Egg.gmsr.png', 'name': 'Fully Loaded Croissanwich® mit Ei', 'badge': '⭐ Bestseller', 'desc': 'Das ultimative BK Frühstückssandwich: Wurst, krosser Bacon, frisches Ei und geschmolzener Käse im warmen Buttercroissant.'},
        {'img': 'Beef Croissan’wich with Egg.gmsr.png', 'name': 'Beef Croissan\'wich® mit Ei', 'badge': '🔥 Beliebt', 'desc': 'Flammengegrilltes Rindfleisch-Patty mit frischem Ei und Käse im buttrigen Croissant.'},
        {'img': 'Beefacon Croissan’wich with Egg.gmsr.png', 'name': 'Beefacon Croissan\'wich® mit Ei', 'badge': '', 'desc': 'Das Beste aus Rindfleisch und Bacon kombiniert mit Ei auf einem goldbraunen Croissant.'},
        {'img': 'Chicken Strips Croissan’wich with Egg.gmsr.png', 'name': 'Chicken Strips Croissan\'wich® mit Ei', 'badge': '', 'desc': 'Knusprige Hähnchenstreifen mit Ei und Käse im zarten Croissant-Brötchen.'},
        {'img': 'Chick’N Crisp Croissan’wich with Egg.gmsr.png', 'name': 'Chick\'N Crisp Croissan\'wich® mit Ei', 'badge': '', 'desc': 'Ein zartes, knuspriges Hähnchenfilet mit Ei auf warmem Croissant.'},
        {'img': 'Breakfast King.gmsr.avif', 'name': 'Breakfast King®', 'badge': '👑 Spezialität', 'desc': 'Deftiger Frühstücksburger mit flammengegrilltem Beef, Ei und Käse für den großen Morgenhunger.'},
        {'img': 'Potato Bites.gmsr.png', 'name': 'Potato Bites', 'badge': '🍟 Highlight', 'desc': 'Goldbraune, mundgerechte Kartoffel-Happen – außen kross, innen zart.'},
        {'img': 'Americano.gmsr.avif', 'name': 'Americano Kaffee', 'badge': '☕ 100% Arabica', 'desc': 'Frisch gemahlener 100% Arabica-Kaffee. Vollmundig, aromatisch und belebend.'},
        {'img': 'Cappuccino.gmsr.avif', 'name': 'Cappuccino', 'badge': '', 'desc': 'Intensiver Espresso mit samtig cremigem Milchschaum aus hochwertigen Arabica-Bohnen.'},
    ],
    'hi': [
        {'img': 'Fully Loaded Croissanwich with Egg.gmsr.png', 'name': 'फुल्ली लोडेड क्रॉसों\'विच® अंडे के साथ', 'badge': '⭐ सबसे ज्यादा बिकने वाला', 'desc': 'बीके का सबसे बेहतरीन ब्रेकफास्ट सैंडविच: सॉसेज, क्रिस्पी बेकन, ताजा अंडा और पिघला हुआ चीज़ परतदार क्रॉसों बन में।'},
        {'img': 'Beef Croissan’wich with Egg.gmsr.png', 'name': 'बीफ क्रॉसों\'विच® अंडे के साथ', 'badge': '🔥 लोकप्रिय', 'desc': 'फ्लेम-ग्रिल्ड पैटी, ताजा अंडा और पिघले हुए चीज़ के साथ मक्खनयुक्त क्रॉसों बन।'},
        {'img': 'Beefacon Croissan’wich with Egg.gmsr.png', 'name': 'बीफैकन क्रॉसों\'विच® अंडे के साथ', 'badge': '', 'desc': 'ग्रिल्ड पैटी और कुरकुरे बेकन का शानदार संगम, अंडे और चीज़ के साथ।'},
        {'img': 'Chicken Strips Croissan’wich with Egg.gmsr.png', 'name': 'चिकन स्ट्रिप्स क्रॉसों\'विच® अंडे के साथ', 'badge': '', 'desc': 'क्रिस्पी चिकन स्ट्रिप्स, अंडा और चीज़ का स्वादिष्ट संयोजन।'},
        {'img': 'Chick’N Crisp Croissan’wich with Egg.gmsr.png', 'name': 'चिक\'एन क्रिस्प क्रॉसों\'विच® अंडे के साथ', 'badge': '', 'desc': 'हल्का और कुरकुरा चिकन फिलेट ताजे अंडे के साथ।'},
        {'img': 'Breakfast King.gmsr.avif', 'name': 'ब्रेकफास्ट किंग®', 'badge': '👑 सिग्नेचर', 'desc': 'फ्लेम-ग्रिल्ड पैटी, अंडा और चीज़ से बना पेट भरने वाला शानदार बर्गर।'},
        {'img': 'Potato Bites.gmsr.png', 'name': 'पोटैटो बाइट्स', 'badge': '🍟 क्रिस्पी साइड', 'desc': 'बाहर से कुरकुरी और अंदर से नरम सुनहरी आलू बाइट्स – नाश्ते का अनिवार्य हिस्सा।'},
        {'img': 'Americano.gmsr.avif', 'name': 'अमेरिकानो कॉफी', 'badge': '☕ 100% अरेबिका', 'desc': '100% अरेबिका बीन्स से बनी ताज़ा ब्रू की हुई रिच और स्मूथ कॉफी।'},
        {'img': 'Cappuccino.gmsr.avif', 'name': 'कैपुचिनो', 'badge': '', 'desc': 'गाढ़े एस्प्रेसो और मखमली झागदार दूध से तैयार क्लासिक कैपुचिनो।'},
    ]
}

def generate_index(lang):
    c = INDEX_CONTENT[lang]
    t = COMMON_I18N[lang]
    asset_p = get_asset_prefix(lang)
    
    # Cards
    cards_html = []
    for card in FEATURED_CARDS[lang]:
        badge_html = f'<span class="menu-card-badge">{card["badge"]}</span>' if card['badge'] else ''
        cards_html.append(f'''          <article class="menu-card" data-name="{card['name']}">
            <div class="menu-card-img">
              <img src="{asset_p}images/{card['img']}" alt="{card['name']} – {t['site_title']}" loading="lazy" />
              {badge_html}
            </div>
            <div class="menu-card-body">
              <div class="menu-card-name">{card['name']}</div>
              <div class="menu-card-desc">{card['desc']}</div>
            </div>
          </article>''')

    # FAQs
    faqs_html = []
    for faq in c['faqs']:
        faqs_html.append(f'''        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            <span>{faq['q']}</span>
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>{faq['a']}</p>
          </div>
        </div>''')

    body = f'''      <!-- HERO -->
      <section class="hero fade-in" aria-label="Welcome banner">
        <div class="hero-content">
          <div class="hero-badge">{c['hero_badge']}</div>
          <h1>{c['hero_h1']}</h1>
          <p>{c['hero_p']}</p>
          <div class="hero-cta">
            <a href="menu" class="btn-primary" id="cta-view-menu">{c['btn_view_menu']}</a>
            <a href="#breakfast-items" class="btn-secondary" id="cta-breakfast">{c['btn_breakfast']}</a>
          </div>
        </div>
        <div class="hero-image">
          <div class="hero-img-wrap">
            <img src="{asset_p}images/Fully Loaded Croissanwich with Egg.gmsr.png" alt="Fully Loaded Croissanwich with Egg – {t['site_title']}" loading="eager" />
          </div>
        </div>
      </section>

      <!-- STATS -->
      <section class="stats-row fade-in" aria-label="Menu statistics">
        <div class="stat-card"><span class="stat-number">113+</span><div class="stat-label">{c['stat_items']}</div></div>
        <div class="stat-card"><span class="stat-number">9</span><div class="stat-label">{c['stat_breakfast']}</div></div>
        <div class="stat-card"><span class="stat-number">7</span><div class="stat-label">{c['stat_categories']}</div></div>
        <div class="stat-card"><span class="stat-number">6am</span><div class="stat-label">{c['stat_starts']}</div></div>
      </section>

      <!-- INTRODUCTION -->
      <section class="content-section fade-in" id="introduction" aria-labelledby="intro-heading">
        <h2 id="intro-heading">{c['intro_h2']}</h2>
        <p>{c['intro_p1']}</p>
        <p>{c['intro_p2']}</p>
        <p>{c['intro_p3']}</p>
        <p>{c['intro_p4']}</p>
        <div class="info-box">
          <p>{c['intro_tip']}</p>
        </div>
        <p>{c['intro_p5']}</p>
        <p>{c['intro_p6']}</p>
      </section>

      <!-- FEATURED BREAKFAST ITEMS -->
      <section id="breakfast-items" aria-labelledby="featured-heading">
        <div class="section-header fade-in">
          <div class="section-title">{c['featured_title']}</div>
          <a href="menu#breakfast" class="view-all-link" id="breakfast-view-all">{t['view_all']}</a>
        </div>
        <div class="menu-grid fade-in">
{chr(10).join(cards_html)}
        </div>
      </section>

      <!-- SPECIAL FEATURES -->
      <section class="content-section fade-in" id="special-features" style="margin-top:40px;">
        <h2>{c['special_h2']}</h2>
        <p>{c['special_p1']}</p>
        <div class="features-grid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:20px;margin-top:20px;">
          <div class="feature-box" style="background:var(--bk-card2);padding:20px;border-radius:12px;border:1px solid var(--bk-border);">
            <h3 style="color:var(--bk-orange);margin-bottom:8px;">🥐 {c['special_point1_t']}</h3>
            <p style="font-size:0.9rem;color:var(--bk-text);">{c['special_point1_d']}</p>
          </div>
          <div class="feature-box" style="background:var(--bk-card2);padding:20px;border-radius:12px;border:1px solid var(--bk-border);">
            <h3 style="color:var(--bk-orange);margin-bottom:8px;">🔥 {c['special_point2_t']}</h3>
            <p style="font-size:0.9rem;color:var(--bk-text);">{c['special_point2_d']}</p>
          </div>
          <div class="feature-box" style="background:var(--bk-card2);padding:20px;border-radius:12px;border:1px solid var(--bk-border);">
            <h3 style="color:var(--bk-orange);margin-bottom:8px;">🥩 {c['special_point3_t']}</h3>
            <p style="font-size:0.9rem;color:var(--bk-text);">{c['special_point3_d']}</p>
          </div>
          <div class="feature-box" style="background:var(--bk-card2);padding:20px;border-radius:12px;border:1px solid var(--bk-border);">
            <h3 style="color:var(--bk-orange);margin-bottom:8px;">🍟 {c['special_point4_t']}</h3>
            <p style="font-size:0.9rem;color:var(--bk-text);">{c['special_point4_d']}</p>
          </div>
        </div>
      </section>

      <!-- HOURS -->
      <section class="content-section fade-in" id="hours" style="margin-top:30px;">
        <h2>{c['hours_h2']}</h2>
        <p>{c['hours_p1']}</p>
        <ul style="margin:16px 0 16px 20px;line-height:1.8;color:var(--bk-text);">
          <li>{c['hours_li1']}</li>
          <li>{c['hours_li2']}</li>
          <li>{c['hours_li3']}</li>
          <li>{c['hours_li4']}</li>
        </ul>
        <div class="info-box">
          <p>{c['hours_box']}</p>
        </div>
      </section>

      <!-- FAQ -->
      <section class="content-section fade-in" id="faq" style="margin-top:30px;">
        <h2>❓ {t['frequently_asked']}</h2>
        <div class="faq-list">
{chr(10).join(faqs_html)}
        </div>
      </section>'''

    return build_page_wrapper(lang, 'index', body)

def generate_about(lang):
    c = ABOUT_CONTENT[lang]
    t = COMMON_I18N[lang]
    
    body = f'''      <div class="prose-page">
        <div class="page-hero fade-in">
          <h1>{c['h1']}</h1>
          <p>{c['p_lead']}</p>
        </div>

        <div class="prose fade-in">
          <h2>{c['sec1_h2']}</h2>
          <p>{c['sec1_p']}</p>

          <h2>{c['sec2_h2']}</h2>
          <p>{c['sec2_p1']}</p>
          <p>{c['sec2_p2']}</p>

          <h2>{c['sec3_h2']}</h2>
          <ul style="margin: 16px 0 16px 20px; line-height: 1.8;">
            <li>{c['offer_li1']}</li>
            <li>{c['offer_li2']}</li>
            <li>{c['offer_li3']}</li>
            <li>{c['offer_li4']}</li>
            <li>{c['offer_li5']}</li>
          </ul>

          <h2>{c['sec4_h2']}</h2>
          <p>{c['author_p']}</p>
        </div>
      </div>'''

    return build_page_wrapper(lang, 'about', body)

def generate_contact(lang):
    c = CONTACT_CONTENT[lang]
    t = COMMON_I18N[lang]
    
    body = f'''      <div class="prose-page" style="max-width:900px;">
        <div class="page-hero fade-in">
          <h1>{c['h1']}</h1>
          <p>{c['p_lead']}</p>
        </div>

        <!-- Contact Info Cards -->
        <div class="contact-grid fade-in">
          <div class="contact-card">
            <div class="contact-card-icon">📧</div>
            <h3>{c['card1_h3']}</h3>
            <p>{c['card1_p']}</p>
            <p><a href="mailto:bgfastmenu@gmail.com">bgfastmenu@gmail.com</a></p>
          </div>

          <div class="contact-card">
            <div class="contact-card-icon">⏱️</div>
            <h3>{c['card2_h3']}</h3>
            <p>{c['card2_p']}</p>
          </div>

          <div class="contact-card">
            <div class="contact-card-icon">💬</div>
            <h3>{c['card3_h3']}</h3>
            <p>{c['card3_p']}</p>
          </div>

          <div class="contact-card">
            <div class="contact-card-icon">🌐</div>
            <h3>{c['card4_h3']}</h3>
            <p>{c['card4_p']}</p>
          </div>
        </div>

        <!-- Form -->
        <div class="contact-form-card fade-in" style="background:var(--bk-card);border:1px solid var(--bk-border);border-radius:14px;padding:32px;margin-top:32px;">
          <h2 style="font-family:'Outfit',sans-serif;margin-bottom:20px;font-size:1.4rem;">{c['form_h2']}</h2>
          <form id="contactForm" style="display:flex;flex-direction:column;gap:18px;">
            <div class="form-row" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
              <div>
                <label style="display:block;font-size:0.85rem;color:var(--bk-muted);margin-bottom:6px;">{c['form_name']}</label>
                <input type="text" required style="width:100%;padding:10px 14px;background:var(--bk-card2);border:1px solid var(--bk-border);border-radius:8px;color:var(--bk-text);font-family:inherit;" />
              </div>
              <div>
                <label style="display:block;font-size:0.85rem;color:var(--bk-muted);margin-bottom:6px;">{c['form_email']}</label>
                <input type="email" required style="width:100%;padding:10px 14px;background:var(--bk-card2);border:1px solid var(--bk-border);border-radius:8px;color:var(--bk-text);font-family:inherit;" />
              </div>
            </div>
            <div>
              <label style="display:block;font-size:0.85rem;color:var(--bk-muted);margin-bottom:6px;">{c['form_subject']}</label>
              <input type="text" required style="width:100%;padding:10px 14px;background:var(--bk-card2);border:1px solid var(--bk-border);border-radius:8px;color:var(--bk-text);font-family:inherit;" />
            </div>
            <div>
              <label style="display:block;font-size:0.85rem;color:var(--bk-muted);margin-bottom:6px;">{c['form_msg']}</label>
              <textarea rows="5" required style="width:100%;padding:10px 14px;background:var(--bk-card2);border:1px solid var(--bk-border);border-radius:8px;color:var(--bk-text);font-family:inherit;resize:vertical;"></textarea>
            </div>
            <button type="submit" class="btn-primary" style="align-self:flex-start;padding:12px 28px;border-radius:8px;background:linear-gradient(135deg, var(--bk-orange), var(--bk-red));color:white;font-weight:600;font-size:0.95rem;">{c['form_submit']}</button>
          </form>
        </div>
      </div>'''

    return build_page_wrapper(lang, 'contact', body)

def generate_privacy(lang):
    c = LEGAL_CONTENT['privacy'][lang]
    t = COMMON_I18N[lang]
    
    body = f'''      <div class="prose-page">
        <div class="page-hero fade-in">
          <h1>{c['h1']}</h1>
          <p>{c['lead']}</p>
        </div>

        <div class="prose fade-in">
          <h2>{c['sec1_h2']}</h2>
          <p>{c['sec1_p1']}</p>
          <p>{c['sec1_p2']}</p>

          <h2>{c['sec2_h2']}</h2>
          <p>{c['sec2_p']}</p>

          <h2>{c['sec3_h2']}</h2>
          <p>{c['sec3_p']}</p>

          <h2>{c['sec4_h2']}</h2>
          <p>{c['sec4_p']}</p>
        </div>
      </div>'''

    return build_page_wrapper(lang, 'privacy-policy', body)

def generate_disclaimer(lang):
    c = LEGAL_CONTENT['disclaimer'][lang]
    t = COMMON_I18N[lang]
    
    body = f'''      <div class="prose-page">
        <div class="page-hero fade-in">
          <h1>{c['h1']}</h1>
          <p>{c['lead']}</p>
        </div>

        <div class="prose fade-in">
          <h2>{c['sec1_h2']}</h2>
          <p>{c['sec1_p']}</p>

          <h2>{c['sec2_h2']}</h2>
          <p>{c['sec2_p']}</p>

          <h2>{c['sec3_h2']}</h2>
          <p>{c['sec3_p']}</p>

          <h2>{c['sec4_h2']}</h2>
          <p>{c['sec4_p']}</p>
        </div>
      </div>'''

    return build_page_wrapper(lang, 'disclaimer', body)

print("Standard pages generators ready.")
