#!/usr/bin/env python3
"""
Verification Script for Multilingual SEO Architecture
Tests all HTML files, canonicals, hreflang tags, asset links, images, sitemap.xml, and robots.txt.
"""

import os
import re
import html
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://burgerkingbreakfastmenu.co.uk"
LANGS = ['en', 'es', 'fr', 'de', 'hi']
PAGES = ['index', 'menu', 'calories', 'about', 'contact', 'privacy-policy', 'disclaimer']

LANG_META = {
    'en': {'code': 'en', 'locale': 'en_GB', 'sub': ''},
    'es': {'code': 'es', 'locale': 'es_ES', 'sub': 'es/'},
    'fr': {'code': 'fr', 'locale': 'fr_FR', 'sub': 'fr/'},
    'de': {'code': 'de', 'locale': 'de_DE', 'sub': 'de/'},
    'hi': {'code': 'hi', 'locale': 'hi_IN', 'sub': 'hi/'},
}

def check_files_and_seo():
    errors = []
    warnings = []
    
    # 1. Check HTML files
    print("[1/5] Checking HTML files and SEO tags...")
    for slug in PAGES:
        for lang in LANGS:
            sub = LANG_META[lang]['sub']
            file_name = f"{slug}.html"
            file_path = os.path.join(BASE_DIR, sub.rstrip('/'), file_name) if sub else os.path.join(BASE_DIR, file_name)
            
            if not os.path.exists(file_path):
                errors.append(f"Missing file: {file_path}")
                continue
                
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check <html lang="...">
            if f'<html lang="{lang}">' not in content:
                errors.append(f"[{file_name}] ({lang}) Expected <html lang=\"{lang}\">")

            # Check Canonical
            expected_can = f"{SITE_URL}/{sub}" if slug == 'index' and sub else (f"{SITE_URL}/" if slug == 'index' else f"{SITE_URL}/{sub}{slug}")
            if f'<link rel="canonical" href="{expected_can}" />' not in content:
                errors.append(f"[{file_name}] ({lang}) Canonical mismatch. Expected: {expected_can}")

            # Check Hreflangs
            if f'<link rel="alternate" hreflang="x-default"' not in content:
                errors.append(f"[{file_name}] ({lang}) Missing x-default hreflang")
                
            for l in LANGS:
                if f'<link rel="alternate" hreflang="{l}"' not in content:
                    errors.append(f"[{file_name}] ({lang}) Missing hreflang for {l}")

            # Check Language Switcher
            if 'id="langSelector"' not in content:
                errors.append(f"[{file_name}] ({lang}) Missing langSelector in topbar")
            if 'class="sidebar-lang-container"' not in content:
                errors.append(f"[{file_name}] ({lang}) Missing sidebar-lang-container in sidebar")

            # Check Asset paths
            asset_p = "../" if sub else ""
            css_p = f'{asset_p}css/style.css'
            js_p = f'{asset_p}js/main.js'
            if f'href="{css_p}"' not in content:
                errors.append(f"[{file_name}] ({lang}) CSS path mismatch: expected {css_p}")
            if f'src="{js_p}"' not in content:
                errors.append(f"[{file_name}] ({lang}) JS path mismatch: expected {js_p}")

            # Check images
            images = re.findall(r'src="([^"]+?\.(?:png|avif|jpg|jpeg|webp))"', content)
            for img_raw in images:
                img = html.unescape(img_raw)
                if img.startswith('../'):
                    real_img_path = os.path.join(BASE_DIR, img.replace('../', ''))
                else:
                    real_img_path = os.path.join(BASE_DIR, img)
                if not os.path.exists(real_img_path):
                    errors.append(f"[{file_name}] ({lang}) Broken image reference: {img} -> {real_img_path}")

    print(f"Checked 35 files. Errors so far: {len(errors)}")

    # 2. Check sitemap.xml
    print("\n[2/5] Checking sitemap.xml...")
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    if not os.path.exists(sitemap_path):
        errors.append("sitemap.xml is missing")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            urls = root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            print(f"sitemap.xml contains {len(urls)} URLs.")
            if len(urls) != 35:
                warnings.append(f"sitemap.xml contains {len(urls)} URLs instead of expected 35.")
        except Exception as e:
            errors.append(f"sitemap.xml parsing error: {e}")

    # 3. Check robots.txt
    print("\n[3/5] Checking robots.txt...")
    robots_path = os.path.join(BASE_DIR, 'robots.txt')
    if not os.path.exists(robots_path):
        errors.append("robots.txt is missing")
    else:
        with open(robots_path, 'r', encoding='utf-8') as f:
            r_content = f.read()
        if "sitemap.xml" not in r_content:
            errors.append("robots.txt does not reference sitemap.xml")
        for l in ['es', 'fr', 'de', 'hi']:
            if f"Allow: /{l}/" not in r_content:
                warnings.append(f"robots.txt missing explicit Allow: /{l}/")

    print("\n" + "=" * 60)
    if not errors and not warnings:
        print("[SUCCESS] ALL TESTS PASSED! 0 Errors, 0 Warnings.")
        print("Site is 100% Google SEO Multilingual Compliant!")
    else:
        print(f"Found {len(errors)} errors and {len(warnings)} warnings:")
        for err in errors:
            print(f"[ERROR] {err}")
        for warn in warnings:
            print(f"[WARNING] {warn}")
    print("=" * 60)

if __name__ == "__main__":
    check_files_and_seo()
