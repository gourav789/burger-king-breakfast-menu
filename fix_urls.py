#!/usr/bin/env python3
"""
Fix GitHub Pages Redirect Error
Removes .html extensions from internal links and canonical URLs
"""

import re
import os

# Files to fix
files_to_fix = [
    'index.html',
    'menu.html',
    'about.html',
    'contact.html',
    'privacy-policy.html',
    'disclaimer.html',
    'calories.html',
]

def fix_html_file(filename):
    """Fix a single HTML file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 1. Fix internal links: href="page.html" → href="page"
        # But don't change: href="css/style.css", href="js/main.js", etc.
        content = re.sub(
            r'href="([a-z-]+)\.html"',
            r'href="\1"',
            content
        )
        
        # 2. Fix canonical URLs: remove .html
        content = re.sub(
            r'href="https://burgerkingbreakfastmenu\.co\.uk/([a-z-]+)\.html"',
            r'href="https://burgerkingbreakfastmenu.co.uk/\1"',
            content
        )
        
        # 3. Fix anchor links in navigation (like menu.html#breakfast → menu#breakfast)
        content = re.sub(
            r'href="([a-z-]+)\.html(#[a-z-]+)"',
            r'href="\1\2"',
            content
        )
        
        if content != original:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {filename}")
            return True
        else:
            print(f"⚠️  No changes needed: {filename}")
            return False
            
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return False
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("GitHub Pages URL Fix Script")
    print("=" * 60)
    
    fixed_count = 0
    for filename in files_to_fix:
        if fix_html_file(filename):
            fixed_count += 1
    
    print("=" * 60)
    print(f"Fixed {fixed_count} file(s)")
    print("\nNext steps:")
    print("1. Run this script in your project directory")
    print("2. Commit changes: git add . && git commit -m 'Fix GitHub Pages redirect errors'")
    print("3. Push to GitHub: git push")
    print("4. Wait 5-10 minutes for deployment")
    print("5. Check Google Search Console for crawl success")
    print("=" * 60)
