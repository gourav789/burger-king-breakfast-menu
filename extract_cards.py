import re
import json

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

categories = ['breakfast', 'burgers', 'chicken', 'sides', 'meals', 'desserts', 'drinks']
all_cards_data = []

for cat in categories:
    pattern = rf'<section class="category-section[^>]*id="{cat}"[^>]*>(.*?)</section>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        cat_html = match.group(1)
        cards = re.findall(r'<article class="menu-card"(.*?)</article>', cat_html, re.DOTALL)
        for card_html in cards:
            data_name_m = re.search(r'data-name="([^"]+)"', card_html)
            img_m = re.search(r'src="([^"]+)"', card_html)
            badge_m = re.search(r'<span class="menu-card-badge">([^<]+)</span>', card_html)
            name_m = re.search(r'<div class="menu-card-name">([^<]+)</div>', card_html)
            desc_m = re.search(r'<div class="menu-card-desc">([^<]+)</div>', card_html)
            
            all_cards_data.append({
                'category': cat,
                'data_name': data_name_m.group(1) if data_name_m else '',
                'img': img_m.group(1).replace('images/', '') if img_m else '',
                'badge': badge_m.group(1) if badge_m else '',
                'name': name_m.group(1) if name_m else '',
                'desc': desc_m.group(1).strip() if desc_m else '',
            })

with open('cards_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_cards_data, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(all_cards_data)} cards into cards_data.json")
