#!/usr/bin/env python3
"""
Full Multilingual Website Generator for Burger King Breakfast Menu UK
Generates localized pages for English (en), Spanish (es), French (fr), German (de), and Hindi (hi).
Complies 100% with Google International SEO guidelines.
"""

import os
import re
import html
from i18n_data import COMMON_I18N
from i18n_pages import PAGE_META
from i18n_content import INDEX_CONTENT
from i18n_prose import ABOUT_CONTENT, CONTACT_CONTENT
from i18n_legal import LEGAL_CONTENT

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
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
    asset_p = get_asset_prefix(lang)
    topbar_sw, sidebar_sw = build_switchers(lang, active_slug)
    
    home_act = ' active' if active_slug == 'index' else ''
    menu_act = ' active' if active_slug == 'menu' else ''
    cal_act  = ' active' if active_slug == 'calories' else ''
    abt_act  = ' active' if active_slug == 'about' else ''
    cnt_act  = ' active' if active_slug == 'contact' else ''
    prv_act  = ' active' if active_slug == 'privacy-policy' else ''
    dsc_act  = ' active' if active_slug == 'disclaimer' else ''
    
    home_link = 'index' if active_slug != 'index' else 'index'
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
        <div class="footer-inner">
          <div class="footer-col">
            <div class="footer-logo">🍔 {t['site_title']}</div>
            <p>{t['footer_rights']}</p>
            <p style="font-size:0.75rem;margin-top:6px;color:var(--bk-muted);">{t['footer_trademark']}</p>
          </div>
          <div class="footer-links">
            <a href="index">{t['nav_home']}</a>
            <a href="menu">{t['nav_menu']}</a>
            <a href="calories">{t['nav_calories']}</a>
            <a href="about">{t['nav_about']}</a>
            <a href="contact">{t['nav_contact']}</a>
            <a href="privacy-policy">{t['nav_privacy']}</a>
            <a href="disclaimer">{t['nav_disclaimer']}</a>
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

print("Page wrapper and layout builders ready.")
