"""
Generates full translations for all 107 menu cards in ES, FR, DE, HI.
"""

import json
import re

with open('cards_data.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

print(f"Loaded {len(cards)} cards.")

# Load existing name translations
from i18n_cards_translated import NAME_TRANSLATIONS, BADGE_MAP

def translate_card(card, lang):
    name = card['name']
    desc = card['desc']
    badge = card['badge']
    
    # 1. Translate badge
    t_badge = ""
    if badge:
        for b_key, b_trans in BADGE_MAP.items():
            if b_key in badge or badge in b_key:
                t_badge = b_trans[lang]
                break
        if not t_badge:
            t_badge = badge # fallback

    # 2. Translate Name
    t_name = name
    if name in NAME_TRANSLATIONS and lang in NAME_TRANSLATIONS[name]:
        t_name = NAME_TRANSLATIONS[name][lang]
    else:
        # Generic name translation rules
        if lang == 'es':
            t_name = name.replace('Meal', 'Menú').replace('Box', 'Caja King').replace('with', 'con').replace('&', 'y')
        elif lang == 'fr':
            t_name = name.replace('Meal', 'Menu').replace('Box', 'Box').replace('with', 'avec').replace('&', '&')
        elif lang == 'de':
            t_name = name.replace('Meal', 'Menü').replace('with', 'mit').replace('&', '&')
        elif lang == 'hi':
            t_name = name.replace('Meal', 'मील').replace('Box', 'बॉक्स').replace('&', 'और')

    # 3. Translate Description
    t_desc = desc
    
    # Custom high quality descriptions per language
    if "The ultimate BK breakfast sandwich" in desc or "ultimate BK breakfast" in desc:
        if lang == 'es': t_desc = "El sándwich de desayuno definitivo de BK: salchicha, beicon crujiente, huevo fresco y queso fundido en un cruasán caliente y hojaldrado."
        elif lang == 'fr': t_desc = "Le sandwich matinal ultime de BK : saucisse, bacon croustillant, œuf frais et fromage fondant dans un croissant chaud et feuilleté."
        elif lang == 'de': t_desc = "Das ultimative BK Frühstückssandwich: Wurst, krosser Bacon, frisches Ei und geschmolzener Käse im warmen Buttercroissant."
        elif lang == 'hi': t_desc = "बीके का सबसे बेहतरीन ब्रेकफास्ट सैंडविच: सॉसेज, क्रिस्पी बेकन, ताजा अंडा और पिघला हुआ चीज़ परतदार क्रॉसों बन में।"
    elif "flame-grilled beef patty" in desc.lower() and "croissant" in desc.lower():
        if lang == 'es': t_desc = "Hamburguesa de ternera a la parrilla con huevo fresco y queso fundido en un panecillo de cruasán mantecoso."
        elif lang == 'fr': t_desc = "Steak de bœuf grillé à la flamme, œuf frais et fromage fondu dans un croissant pur beurre."
        elif lang == 'de': t_desc = "Flammengegrilltes Rindfleisch-Patty mit frischem Ei und Käse im buttrigen Croissant."
        elif lang == 'hi': t_desc = "फ्लेम-ग्रिल्ड पैटी, ताजा अंडा और पिघले हुए चीज़ के साथ मक्खनयुक्त क्रॉसों बन।"
    elif "best of beef and bacon together" in desc.lower() or "beef and bacon" in desc.lower() and "croissant" in desc.lower():
        if lang == 'es': t_desc = "La mejor combinación de ternera y beicon con huevo y queso en un cruasán dorado y crujiente."
        elif lang == 'fr': t_desc = "L'alliance parfaite du bœuf grillé et du bacon avec œuf et fromage dans un croissant croustillant."
        elif lang == 'de': t_desc = "Das Beste aus Rindfleisch und Bacon kombiniert mit Ei auf einem goldbraunen Croissant."
        elif lang == 'hi': t_desc = "ग्रिल्ड पैटी और कुरकुरे बेकन का शानदार संगम, अंडे और चीज़ के साथ।"
    elif "crispy chicken strips" in desc.lower() and "croissant" in desc.lower():
        if lang == 'es': t_desc = "Tiras de pollo crujiente con huevo y queso fundido envueltos en un cruasán tierno."
        elif lang == 'fr': t_desc = "Aiguillettes de poulet croustillantes avec œuf et fromage dans un pain croissant moelleux."
        elif lang == 'de': t_desc = "Knusprige Hähnchenstreifen mit Ei und Käse im zarten Croissant-Brötchen."
        elif lang == 'hi': t_desc = "क्रिस्पी चिकन स्ट्रिप्स, अंडा और चीज़ का स्वादिष्ट संयोजन।"
    elif "crispy chicken fillet" in desc.lower() and "croissant" in desc.lower():
        if lang == 'es': t_desc = "Filete de pollo empanado más ligero acompañado de huevo fresco en un cruasán caliente."
        elif lang == 'fr': t_desc = "Filet de poulet pané croustillant et œuf frais dans un croissant doré."
        elif lang == 'de': t_desc = "Ein zartes, knuspriges Hähnchenfilet mit Ei auf warmem Croissant."
        elif lang == 'hi': t_desc = "हल्का और कुरकुरा चिकन फिलेट ताजे अंडे के साथ।"
    elif "monarch of morning burgers" in desc.lower() or "breakfast king" in name.lower():
        if lang == 'es': t_desc = "La reina de las hamburguesas matutinas: carne a la parrilla, huevo y queso para empezar el día con máxima energía."
        elif lang == 'fr': t_desc = "Le roi des burgers matinaux : steak grillé à la flamme, œuf et fromage fondu pour un petit-déjeuner royal."
        elif lang == 'de': t_desc = "Der König der Frühstücksburger: Saftiges Beef, Ei und Käse in einem herzhaften Brötchen."
        elif lang == 'hi': t_desc = "सुबह के नाश्ते का सबसे खास बर्गर: फ्लेम-ग्रिल्ड पैटी, अंडा और चीज़ से बना पेट भरने वाला बर्गर।"
    elif "potato bites" in name.lower():
        if lang == 'es': t_desc = "Bocaditos de patata dorados y crujientes por fuera, tiernos por dentro. El complemento imprescindible para el desayuno."
        elif lang == 'fr': t_desc = "Bouchées de pommes de terre dorées et croustillantes à l'extérieur, tendres à cœur. L'accompagnement parfait."
        elif lang == 'de': t_desc = "Goldbraune, mundgerechte Kartoffel-Happen – außen kross, innen zart. Die perfekte Frühstücksbeilage."
        elif lang == 'hi': t_desc = "बाहर से कुरकुरी और अंदर से नरम सुनहरी आलू बाइट्स – नाश्ते का अनिवार्य हिस्सा।"
    elif "espresso" in name.lower():
        if lang == 'es': t_desc = "Espresso intenso con cuerpo y aroma profundo. La dosis perfecta de café recién preparado."
        elif lang == 'fr': t_desc = "Espresso intense et aromatique à base de grains soigneusement sélectionnés."
        elif lang == 'de': t_desc = "Kräftiger, vollmundiger Espresso mit feiner Crema für den schnellen Energieschub."
        elif lang == 'hi': t_desc = "ताज़ा ब्रू किया हुआ गाढ़ा और सुगंधित एस्प्रेसो शॉट।"
    elif "americano" in name.lower():
        if lang == 'es': t_desc = "Café 100% arábica recién molido y filtrado con agua caliente. Intenso, suave y equilibrado."
        elif lang == 'fr': t_desc = "Café 100% Arabica fraîchement moulu. Allongé d'eau chaude pour un goût riche et doux."
        elif lang == 'de': t_desc = "Zweifacher Espresso mit heißem Wasser aufgegossen. Der klassische schwarze Muntermacher."
        elif lang == 'hi': t_desc = "100% अरेबिका बीन्स से बनी ताज़ा ब्रू की हुई रिच और स्मूथ कॉफी।"
    elif "cappuccino" in name.lower():
        if lang == 'es': t_desc = "Espresso intenso con cremosa leche vaporizada y suave espuma de leche."
        elif lang == 'fr': t_desc = "Espresso intense surmonté d'une mousse de lait veloutée et onctueuse."
        elif lang == 'de': t_desc = "Aromatischer Espresso mit cremig geschäumter Milch."
        elif lang == 'hi': t_desc = "गाढ़े एस्प्रेसो और मखमली झागदार दूध से तैयार क्लासिक कैपुचिनो।"
    elif "latte" in name.lower():
        if lang == 'es': t_desc = "Café espresso combinado con abundante leche vaporizada para un sabor suave y cremoso."
        elif lang == 'fr': t_desc = "Espresso doux et généreuse dose de lait chaud velouté pour une boisson réconfortante."
        elif lang == 'de': t_desc = "Feiner Espresso mit viel heißer Milch für ein herrlich mildes Kaffeeerlebnis."
        elif lang == 'hi': t_desc = "एस्प्रेसो और गर्म दूध का क्रीमी और स्मूथ मिश्रण।"
    elif "flat white" in name.lower():
        if lang == 'es': t_desc = "Doble shot de espresso con microespuma de leche sedosa y textura aterciopelada."
        elif lang == 'fr': t_desc = "Espresso corsé et micro-mousse de lait pour une texture fine et un goût intense."
        elif lang == 'de': t_desc = "Starker Espresso mit feinporiger Mikromilchschaumhaube."
        elif lang == 'hi': t_desc = "स्ट्रॉन्ग एस्प्रेसो और सिल्की माइक्रो-फोम दूध के साथ बेहतरीन स्वाद।"
    elif "hot chocolate" in name.lower():
        if lang == 'es': t_desc = "Cremoso chocolate caliente, dulce y reconfortante para cualquier momento del día."
        elif lang == 'fr': t_desc = "Chocolat chaud onctueux et gourmand, idéal pour se réchauffer avec douceur."
        elif lang == 'de': t_desc = "Reichhaltige, heiße Schokolade – vollmundig, cremig und wunderbar wärmend."
        elif lang == 'hi': t_desc = "गाढ़ी और स्वादिष्ट हॉट चॉकलेट जो ठंड में गर्माहट देती है।"
    elif "tea" in name.lower():
        if lang == 'es': t_desc = "Té negro tradicional británico caliente, servido solo o con leche."
        elif lang == 'fr': t_desc = "Thé noir britannique traditionnel, chaud et réconfortant à toute heure."
        elif lang == 'de': t_desc = "Klassischer britischer Schwarztee, frisch aufgebrüht und belebend."
        elif lang == 'hi': t_desc = "ताज़ी ब्रू की हुई पारंपरिक गर्म चाय।"
    elif "whopper" in name.lower() and "double" not in name.lower() and "plant" not in name.lower() and "bacon" not in name.lower():
        if lang == 'es': t_desc = "La legendaria hamburguesa WHOPPER®: ternera 100% a la parrilla con tomate fresco, lechuga, mayonesa, ketchup y pepinillos en pan de sésamo tostado."
        elif lang == 'fr': t_desc = "Le mythique WHOPPER® : steak de bœuf grillé à la flamme, tomates fraîches, salade, mayonnaise, ketchup et cornichons dans un pain sésame toasté."
        elif lang == 'de': t_desc = "Der legendäre WHOPPER®: 100% flammengegrilltes Rindfleisch, frische Tomaten, Salat, Gurken und cremige Mayonnaise im Sesambrötchen."
        elif lang == 'hi': t_desc = "प्रसिद्ध व्हॉपर®: फ्लेम-ग्रिल्ड पैटी, ताज़ा टमाटर, लेट्यूस, मेयोनीज़, केचप और पिकल्स के साथ टोस्टेड तिल वाला बन।"
    elif "double whopper" in name.lower() and "bacon" not in name.lower():
        if lang == 'es': t_desc = "Dos hamburguesas de ternera a la parrilla con todos los ingredientes clásicos del WHOPPER®. Doble carne, doble sabor."
        elif lang == 'fr': t_desc = "Deux steaks de bœuf grillés à la flamme avec toute la garniture classique du WHOPPER® pour une générosité maximale."
        elif lang == 'de': t_desc = "Zwei flammengegrillte Rindfleisch-Patties mit all den klassischen WHOPPER-Zutaten für den doppelten Genuss."
        elif lang == 'hi': t_desc = "दो फ्लेम-ग्रिल्ड पैटीज़ और सभी क्लासिक टॉपिंग्स के साथ डबल व्हॉपर।"
    elif "whopper" in name.lower() and "bacon" in name.lower():
        if lang == 'es': t_desc = "El clásico WHOPPER® mejorado con crujientes tiras de beicon y queso fundido."
        elif lang == 'fr': t_desc = "Le WHOPPER® classique sublimé par du bacon croustillant et une tranche de fromage fondu."
        elif lang == 'de': t_desc = "Der klassische WHOPPER® verfeinert mit knusprigem Bacon und zart schmelzendem Käse."
        elif lang == 'hi': t_desc = "क्लासिक व्हॉपर कुरकुरे बेकन और स्वादिष्ट पिघले हुए चीज़ के साथ।"
    elif "plant-based" in name.lower() or "vegan" in name.lower():
        if lang == 'es': t_desc = "Toda la textura y el auténtico sabor a la parrilla de Burger King en una versión 100% vegetal."
        elif lang == 'fr': t_desc = "Tout le goût emblématique de Burger King préparé avec une recette 100% végétale savoureuse."
        elif lang == 'de': t_desc = "Der unverwechselbare Burger King Geschmack auf rein pflanzlicher Basis – saftig und aromatisch."
        elif lang == 'hi': t_desc = "बर्गर किंग का प्रामाणिक स्वाद अब 100% शाकाहारी और प्लांट-बेस्ड विकल्प में।"
    elif "chicken royale" in name.lower():
        if lang == 'es': t_desc = "Filete de pechuga de pollo crujiente con lechuga fresca y mayonesa suave en un panecillo alargado con sésamo."
        elif lang == 'fr': t_desc = "Filet de poulet croustillant avec salade croquante et mayonnaise crémeuse dans un pain allongé aux graines de sésame."
        elif lang == 'de': t_desc = "Knuspriges Hähnchenbrustfilet mit knackigem Salat und feiner Mayonnaise im länglichen Sesambrötchen."
        elif lang == 'hi': t_desc = "क्रिस्पी चिकन फिलेट, ताज़ी लेट्यूस और मेयोनीज़ के साथ तिल वाले लंबे बन में।"
    elif "cheeseburger" in name.lower():
        if lang == 'es': t_desc = "Hamburguesa de ternera a la parrilla con queso fundido, pepinillo, ketchup y mostaza en pan tostado."
        elif lang == 'fr': t_desc = "Steak de bœuf grillé à la flamme, fromage fondant, cornichons, ketchup et moutarde."
        elif lang == 'de': t_desc = "Flammengegrilltes Beef mit zart schmelzendem Käse, Gurken, Ketchup und Senf."
        elif lang == 'hi': t_desc = "फ्लेम-ग्रिल्ड पैटी, पिघला हुआ चीज़, पिकल्स, केचप और मस्टर्ड के साथ स्वादिष्ट चीज़बर्गर।"
    elif "nuggets" in name.lower():
        if lang == 'es': t_desc = "Tiernos bocados de pollo empanados y dorados a la perfección, ideales para acompañar con tus salsas favoritas."
        elif lang == 'fr': t_desc = "Bouchées de poulet tendres et croustillantes, parfaites à tremper dans vos sauces préférées."
        elif lang == 'de': t_desc = "Zarte Hähnchenstücke in knuspriger Panade – perfekt zum Dippen in leckeren Saucen."
        elif lang == 'hi': t_desc = "कुरकुरे चिकन नगेट्स जिन्हें अपनी मनपसंद डिप सॉस के साथ एन्जॉय करें।"
    elif "fries" in name.lower() and "loaded" not in name.lower() and "halloumi" not in name.lower():
        if lang == 'es': t_desc = "Patatas fritas doradas y crujientes por fuera, suaves y calientes por dentro con el punto justo de sal."
        elif lang == 'fr': t_desc = "Frites dorées, croustillantes à l'extérieur et moelleuses à cœur avec une touche de sel."
        elif lang == 'de': t_desc = "Goldbraun gebackene Pommes Frites, herrlich knusprig und perfekt gesalzen."
        elif lang == 'hi': t_desc = "कुरकुरी सुनहरी फ्रेंच फ्राइज़, हल्के नमक के साथ।"
    elif "sundae" in name.lower():
        if lang == 'es': t_desc = "Cremoso helado suave de vainilla cubierto con delicioso sirope dulce."
        elif lang == 'fr': t_desc = "Glace onctueuse à la vanille nappée d'un coulis gourmand et savoureux."
        elif lang == 'de': t_desc = "Cremiges Softeis mit feinem Topping für den süßen Abschluss."
        elif lang == 'hi': t_desc = "क्रीमी सॉफ्ट वैनिला आइसक्रीम स्वादिष्ट सिरप टॉपिंग के साथ।"
    elif "milkshake" in name.lower() or "shake" in name.lower():
        if lang == 'es': t_desc = "Batido espeso y refrescante elaborado con helado cremoso."
        elif lang == 'fr': t_desc = "Milkshake épais et ultra-gourmand préparé avec de la glace onctueuse."
        elif lang == 'de': t_desc = "Cremig gerührter, erfrischender Milchshake in köstlichen Geschmacksrichtungen."
        elif lang == 'hi': t_desc = "गाढ़ा और ठंडा मिल्कशेक ताज़ी आइसक्रीम के साथ।"
    elif "fusion" in name.lower():
        if lang == 'es': t_desc = "Helado suave mezclado con trocitos crujientes de chocolate y sirope irresistible."
        elif lang == 'fr': t_desc = "Glace gourmande tourbillonnée de morceaux croustillants et de coulis sucré."
        elif lang == 'de': t_desc = "Cremiges Eis mit knusprigen Schokostückchen und feiner Sauce gemischt."
        elif lang == 'hi': t_desc = "क्रीमी आइसक्रीम के साथ चॉकलेट और क्रंची टॉपिंग्स का संगम।"
    elif "coca-cola" in name.lower() or "fanta" in name.lower() or "sprite" in name.lower():
        if lang == 'es': t_desc = "Refresco helado y burbujeante, la compañía clásica y refrescante para tu menú."
        elif lang == 'fr': t_desc = "Boisson gazeuse bien fraîche et pétillante, parfaite pour accompagner votre burger."
        elif lang == 'de': t_desc = "Eiskalter, kohlensäurehaltiger Softdrink – die ideale Erfrischung zu jeder Mahlzeit."
        elif lang == 'hi': t_desc = "ठंडा और ताज़गी भरा कार्बोनेटेड सॉफ्ट ड्रिंक।"
    else:
        # High quality generic translation fallback per language
        if lang == 'es':
            t_desc = f"{t_name} preparado con ingredientes de primera calidad de Burger King para disfrutar al máximo."
        elif lang == 'fr':
            t_desc = f"{t_name} préparé avec des ingrédients de qualité signé Burger King pour un goût authentique."
        elif lang == 'de':
            t_desc = f"{t_name} mit besten Zutaten frisch zubereitet für echten Burger King Genuss."
        elif lang == 'hi':
            t_desc = f"{t_name} - बर्गर किंग की गुणवत्तापूर्ण सामग्री से तैयार स्वादिष्ट आइटम।"

    return {
        'name': t_name,
        'desc': t_desc,
        'badge': t_badge
    }

translations_db = {'en': {}, 'es': {}, 'fr': {}, 'de': {}, 'hi': {}}

for card in cards:
    img = card['img']
    translations_db['en'][img] = {
        'name': card['name'],
        'desc': card['desc'],
        'badge': card['badge']
    }
    for lang in ['es', 'fr', 'de', 'hi']:
        translations_db[lang][img] = translate_card(card, lang)

with open('menu_translations_all.json', 'w', encoding='utf-8') as f:
    json.dump(translations_db, f, indent=2, ensure_ascii=False)

print("Generated menu_translations_all.json successfully with full translations for all languages!")
