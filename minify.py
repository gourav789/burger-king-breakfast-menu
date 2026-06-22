import os
import re

def minify_css(css):
    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Collapse whitespace
    css = re.sub(r'\s+', ' ', css)
    # Remove spaces around tokens
    css = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css)
    return css.strip()

def minify_js(js):
    # Remove multiline comments
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    # Remove single line comments (rough approx)
    js = re.sub(r'(?<!:)\/\/.*', '', js)
    # Collapse whitespace
    js = re.sub(r'\s+', ' ', js)
    return js.strip()

def minify_html(html):
    # Remove HTML comments
    html = re.sub(r'<!--(.*?)-->', '', html, flags=re.DOTALL)
    # Remove spaces between tags
    html = re.sub(r'>\s+<', '><', html)
    # Collapse whitespace
    html = re.sub(r'\s{2,}', ' ', html)
    return html.strip()

files_to_minify = {
    'css/style.css': minify_css,
    'js/main.js': minify_js,
    'index.html': minify_html,
    'menu.html': minify_html,
    'about.html': minify_html,
    'contact.html': minify_html,
    'privacy-policy.html': minify_html,
    'disclaimer.html': minify_html,
}

base_dir = r"c:\Users\goura\Desktop\bk-breakfast-menu-site"

for file_path, minifier in files_to_minify.items():
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Save a backup
        with open(full_path + '.bak', 'w', encoding='utf-8') as f:
            f.write(content)
            
        minified = minifier(content)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(minified)
        print(f"Minified {file_path}")
    else:
        print(f"File not found: {file_path}")
