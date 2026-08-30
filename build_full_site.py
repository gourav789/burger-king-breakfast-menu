#!/usr/bin/env python3
"""
Complete Multilingual Site Builder & Google SEO Optimizer
Generates all 35 localized HTML files, sitemap.xml, and robots.txt.
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
from build_all_multilingual import (
    LANGS, LANG_META, get_page_url, get_asset_prefix,
    build_head, build_sidebar, build_topbar, build_footer, build_page_wrapper,
    generate_index, generate_about, generate_contact, generate_privacy, generate_disclaimer
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://burgerkingbreakfastmenu.co.uk"
PAGES = ['index', 'menu', 'calories', 'about', 'contact', 'privacy-policy', 'disclaimer']

def parse_menu_cards():
    """Extracts category sections and cards from original menu.html"""
    with open(os.path.join(BASE_DIR, 'menu.html'), 'r', encoding='utf-8') as f:
        html_content = f.read()

    categories = ['breakfast', 'burgers', 'chicken', 'sides', 'meals', 'desserts', 'drinks']
    parsed = {}
    
    for cat in categories:
        pattern = rf'<section class="category-section[^>]*id="{cat}"[^>]*>(.*?)</section>'
        match = re.search(pattern, html_content, re.DOTALL)
        if match:
            cat_html = match.group(1)
            # extract all articles
            cards = re.findall(r'<article class="menu-card".*?</article>', cat_html, re.DOTALL)
            parsed[cat] = cards
        else:
            parsed[cat] = []
    
    return parsed

def parse_calories_body():
    """Extracts tables and sections from original calories.html"""
    with open(os.path.join(BASE_DIR, 'calories.html'), 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Extract inside <div class="prose fade-in">...</div>
    match = re.search(r'<div class="prose fade-in">(.*?)</div>\s*</div>\s*</main>', html_content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def generate_menu_page(lang, parsed_cards):
    t = COMMON_I18N[lang]
    asset_p = get_asset_prefix(lang)
    meta = PAGE_META['menu'][lang]
    
    categories = ['breakfast', 'burgers', 'chicken', 'sides', 'meals', 'desserts', 'drinks']
    
    sections_html = []
    for cat_id in categories:
        cat_info = MENU_CATEGORIES[cat_id]
        cat_t = cat_info[lang]
        cat_cards = parsed_cards.get(cat_id, [])
        
        # Adjust image paths for cards
        adjusted_cards = []
        for card in cat_cards:
            c_html = card
            # Fix any HTML entities in image src filenames
            c_html = re.sub(r'src="([^"]+)"', lambda m: f'src="{m.group(1).replace("&amp;", "&")}"', c_html)
            if asset_p:
                c_html = re.sub(r'src="images/', f'src="{asset_p}images/', c_html)
            adjusted_cards.append(c_html)

        grid_cls = "menu-grid large" if cat_id in ['breakfast', 'burgers'] else "menu-grid"
        
        sections_html.append(f'''      <!-- =================== {cat_id.upper()} =================== -->
      <section class="category-section fade-in" id="{cat_id}" aria-labelledby="{cat_id}-heading">
        <div class="category-header">
          <div class="cat-icon-wrap">{cat_info['icon']}</div>
          <div class="cat-info">
            <h2 id="{cat_id}-heading">{cat_t['title']}</h2>
            <p>{cat_t['hours']}</p>
          </div>
          <div class="cat-count">{len(cat_cards)} {t['items_count']}</div>
        </div>
        <div class="cat-intro">
          <p>{cat_t['desc']}</p>
        </div>
        <div class="{grid_cls}">
{chr(10).join(adjusted_cards)}
        </div>
      </section>''')

    body = f'''      <!-- Page Hero -->
      <div class="page-hero fade-in">
        <h1>{meta['title']}</h1>
        <p>{meta['desc']}</p>
      </div>

      <!-- Search bar -->
      <div class="menu-search-bar fade-in">
        <span class="menu-search-icon">🔍</span>
        <input type="search" id="menuSearchInput" placeholder="{t['search_placeholder']}" aria-label="Search menu items" />
        <span class="menu-search-count" id="menuCount">113 {t['items_count']}</span>
      </div>
      <div class="no-results" id="noResults" role="status"><div class="emoji">🍔</div><p>{COMMON_I18N[lang]['search_placeholder']}</p></div>

{chr(10).join(sections_html)}'''

    return build_page_wrapper(lang, 'menu', body)

def generate_calories_page(lang, base_prose):
    t = COMMON_I18N[lang]
    meta = PAGE_META['calories'][lang]
    
    # Adjust table headers and text according to language
    prose = base_prose
    if lang != 'en':
        # Translate table headers
        prose = re.sub(r'<strong>Gender</strong>', f'<strong>{t["item"]}</strong>', prose)
        prose = re.sub(r'<strong>Recommended Daily Intake</strong>', f'<strong>{t["calories"]} ({t["kcal"]})</strong>', prose)
        prose = re.sub(r'<strong>Menu Item</strong>', f'<strong>{t["item"]}</strong>', prose)
        prose = re.sub(r'<strong>Calories</strong>', f'<strong>{t["calories"]}</strong>', prose)
        prose = re.sub(r'<strong>Fat \(g\)</strong>', f'<strong>{t["fat"]} (g)</strong>', prose)
        prose = re.sub(r'<strong>Protein \(g\)</strong>', f'<strong>{t["protein"]} (g)</strong>', prose)
        prose = re.sub(r'<strong>Carbs \(g\)</strong>', f'<strong>{t["carbs"]} (g)</strong>', prose)
        prose = re.sub(r'<strong>Serving Size</strong>', f'<strong>{t["serving"]}</strong>', prose)

    body = f'''      <div class="prose-page">
        <div class="page-hero fade-in">
          <h1>{meta['title']}</h1>
          <p>{meta['desc']}</p>
        </div>

        <div class="prose fade-in">
{prose}
        </div>
      </div>'''

    return build_page_wrapper(lang, 'calories', body)

def build_sitemap():
    """Builds a comprehensive multilingual sitemap with xhtml:link hreflangs"""
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">'
    ]
    
    # Define priorities
    priorities = {
        'index': '1.0',
        'menu': '0.95',
        'calories': '0.90',
        'about': '0.70',
        'contact': '0.60',
        'privacy-policy': '0.40',
        'disclaimer': '0.40'
    }

    for slug in PAGES:
        for lang in LANGS:
            loc = get_page_url(lang, slug)
            prio = priorities.get(slug, '0.50')
            if lang != 'en':
                prio = str(round(float(prio) * 0.95, 2))
                
            xml_lines.append('  <url>')
            xml_lines.append(f'    <loc>{loc}</loc>')
            xml_lines.append('    <changefreq>weekly</changefreq>')
            xml_lines.append(f'    <priority>{prio}</priority>')
            
            # x-default
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{get_page_url("en", slug)}" />')
            # all languages
            for l in LANGS:
                xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{get_page_url(l, slug)}" />')
                
            xml_lines.append('  </url>')

    xml_lines.append('</urlset>')
    return "\n".join(xml_lines)

def build_robots_txt():
    return f"""User-agent: *
Allow: /
Allow: /es/
Allow: /fr/
Allow: /de/
Allow: /hi/

Sitemap: {SITE_URL}/sitemap.xml
"""

def main():
    print("=" * 60)
    print("Burger King Breakfast Menu UK – Multilingual SEO Builder")
    print("=" * 60)

    # 1. Parse cards & calorie data
    print("Parsing menu cards from menu.html...")
    parsed_cards = parse_menu_cards()
    print(f"Loaded {sum(len(v) for v in parsed_cards.values())} total menu cards across {len(parsed_cards)} categories.")
    
    print("Parsing calorie tables from calories.html...")
    calories_prose = parse_calories_body()
    print("Calories data loaded.")

    # 2. Ensure directories exist
    for lang in LANGS:
        sub = LANG_META[lang]['sub']
        if sub:
            dir_path = os.path.join(BASE_DIR, sub.rstrip('/'))
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory confirmed: {dir_path}")

    # 3. Generate all pages for all languages
    total_files = 0
    for lang in LANGS:
        sub = LANG_META[lang]['sub']
        target_dir = os.path.join(BASE_DIR, sub.rstrip('/')) if sub else BASE_DIR

        # Index
        index_html = generate_index(lang)
        with open(os.path.join(target_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(index_html)
        total_files += 1

        # Menu
        menu_html = generate_menu_page(lang, parsed_cards)
        with open(os.path.join(target_dir, 'menu.html'), 'w', encoding='utf-8') as f:
            f.write(menu_html)
        total_files += 1

        # Calories
        calories_html = generate_calories_page(lang, calories_prose)
        with open(os.path.join(target_dir, 'calories.html'), 'w', encoding='utf-8') as f:
            f.write(calories_html)
        total_files += 1

        # About
        about_html = generate_about(lang)
        with open(os.path.join(target_dir, 'about.html'), 'w', encoding='utf-8') as f:
            f.write(about_html)
        total_files += 1

        # Contact
        contact_html = generate_contact(lang)
        with open(os.path.join(target_dir, 'contact.html'), 'w', encoding='utf-8') as f:
            f.write(contact_html)
        total_files += 1

        # Privacy Policy
        privacy_html = generate_privacy(lang)
        with open(os.path.join(target_dir, 'privacy-policy.html'), 'w', encoding='utf-8') as f:
            f.write(privacy_html)
        total_files += 1

        # Disclaimer
        disclaimer_html = generate_disclaimer(lang)
        with open(os.path.join(target_dir, 'disclaimer.html'), 'w', encoding='utf-8') as f:
            f.write(disclaimer_html)
        total_files += 1

        print(f"Generated 7 pages for language: {lang} ({LANG_META[lang]['name']})")

    # 4. Generate sitemap.xml
    sitemap_xml = build_sitemap()
    with open(os.path.join(BASE_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    print("Generated multilingual sitemap.xml (35 URLs + hreflangs)")

    # 5. Generate robots.txt
    robots_txt = build_robots_txt()
    with open(os.path.join(BASE_DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots_txt)
    print("Generated robots.txt")

    print("=" * 60)
    print(f"SUCCESS: Generated {total_files} HTML files + sitemap.xml + robots.txt!")
    print("=" * 60)

if __name__ == "__main__":
    main()
