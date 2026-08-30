"""
Full Multi-language translation database for all 107 Burger King Menu Cards.
Languages: English (en), Spanish (es), French (fr), German (de), Hindi (hi)
"""

import json

# Badges translation map
BADGE_MAP = {
    '⭐ Best Seller': {
        'en': '⭐ Best Seller',
        'es': '⭐ Más Vendido',
        'fr': '⭐ Meilleure Vente',
        'de': '⭐ Bestseller',
        'hi': '⭐ बेस्ट सेलर'
    },
    '🔥 Popular': {
        'en': '🔥 Popular',
        'es': '🔥 Popular',
        'fr': '🔥 Populaire',
        'de': '🔥 Beliebt',
        'hi': '🔥 लोकप्रिय'
    },
    '👑 Iconic': {
        'en': '👑 Iconic',
        'es': '👑 Icónico',
        'fr': '👑 Mythique',
        'de': '👑 Kult',
        'hi': '👑 आइकॉनिक'
    },
    '👑 The King': {
        'en': '👑 The King',
        'es': '👑 El Rey',
        'fr': '👑 Le Roi',
        'de': '👑 Der King',
        'hi': '👑 द किंग'
    },
    '🌱 100% Plant-Based': {
        'en': '🌱 100% Plant-Based',
        'es': '🌱 100% Vegetal',
        'fr': '🌱 100% Végétal',
        'de': '🌱 100% Pflanzlich',
        'hi': '🌱 100% प्लांट-बेस्ड'
    },
    '🌱 Vegan Certified': {
        'en': '🌱 Vegan Certified',
        'es': '🌱 Certificado Vegano',
        'fr': '🌱 Certifié Végan',
        'de': '🌱 Vegan Zertifiziert',
        'hi': '🌱 वीगन प्रमाणित'
    },
    '🥩 Premium Wagyu': {
        'en': '🥩 Premium Wagyu',
        'es': '🥩 Wagyu Prémium',
        'fr': '🥩 Wagyu Premium',
        'de': '🥩 Premium Wagyu',
        'hi': '🥩 प्रीमियम वाग्यू'
    },
    '👶 Kids': {
        'en': '👶 Kids',
        'es': '👶 Infantil',
        'fr': '👶 Enfants',
        'de': '👶 Kids',
        'hi': '👶 किड्स'
    }
}

# Generic patterns and terms dictionary for automated authentic translation
NAME_TRANSLATIONS = {
    "Fully Loaded Croissanwich® with Egg": {
        "es": "Fully Loaded Croissanwich® con Huevo",
        "fr": "Fully Loaded Croissanwich® avec Œuf",
        "de": "Fully Loaded Croissanwich® mit Ei",
        "hi": "फुल्ली लोडेड क्रॉसों'विच® अंडे के साथ"
    },
    "Beef Croissan'wich® with Egg": {
        "es": "Beef Croissan'wich® con Huevo",
        "fr": "Beef Croissan'wich® avec Œuf",
        "de": "Beef Croissan'wich® mit Ei",
        "hi": "बीफ क्रॉसों'विच® अंडे के साथ"
    },
    "Beefacon Croissan'wich® with Egg": {
        "es": "Beefacon Croissan'wich® con Huevo",
        "fr": "Beefacon Croissan'wich® avec Œuf",
        "de": "Beefacon Croissan'wich® mit Ei",
        "hi": "बीफैकन क्रॉसों'विच® अंडे के साथ"
    },
    "Chicken Strips Croissan'wich® with Egg": {
        "es": "Chicken Strips Croissan'wich® con Huevo",
        "fr": "Chicken Strips Croissan'wich® avec Œuf",
        "de": "Chicken Strips Croissan'wich® mit Ei",
        "hi": "चिकन स्ट्रिप्स क्रॉसों'विच® अंडे के साथ"
    },
    "Chick'N Crisp Croissan'wich® with Egg": {
        "es": "Chick'N Crisp Croissan'wich® con Huevo",
        "fr": "Chick'N Crisp Croissan'wich® avec Œuf",
        "de": "Chick'N Crisp Croissan'wich® mit Ei",
        "hi": "चिक'एन क्रिस्प क्रॉसों'विच® अंडे के साथ"
    },
    "Breakfast King": {
        "es": "Breakfast King",
        "fr": "Breakfast King",
        "de": "Breakfast King",
        "hi": "ब्रेकफास्ट किंग"
    },
    "Potato Bites": {
        "es": "Potato Bites (Bocaditos de Patata)",
        "fr": "Potato Bites (Bouchées de Pommes de Terre)",
        "de": "Potato Bites (Kartoffel-Happen)",
        "hi": "पोटैटो बाइट्स"
    },
    "Espresso": {
        "es": "Café Espresso",
        "fr": "Café Espresso",
        "de": "Espresso",
        "hi": "एस्प्रेंसो कॉफी"
    },
    "Americano": {
        "es": "Café Americano",
        "fr": "Café Americano",
        "de": "Americano Kaffee",
        "hi": "अमेरिकानो कॉफी"
    },
    "WHOPPER®": {
        "es": "WHOPPER®",
        "fr": "WHOPPER®",
        "de": "WHOPPER®",
        "hi": "व्हॉपर® (WHOPPER®)"
    },
    "Double WHOPPER®": {
        "es": "Doble WHOPPER®",
        "fr": "Double WHOPPER®",
        "de": "Double WHOPPER®",
        "hi": "डबल व्हॉपर®"
    },
    "WHOPPER® with Bacon & Cheese": {
        "es": "WHOPPER® con Beicon y Queso",
        "fr": "WHOPPER® avec Bacon & Fromage",
        "de": "WHOPPER® mit Bacon & Käse",
        "hi": "व्हॉपर® बेकन और चीज़ के साथ"
    },
    "Double WHOPPER® with Bacon & Cheese": {
        "es": "Doble WHOPPER® con Beicon y Queso",
        "fr": "Double WHOPPER® avec Bacon & Fromage",
        "de": "Double WHOPPER® mit Bacon & Käse",
        "hi": "डबल व्हॉपर® बेकन और चीज़ के साथ"
    },
    "Big King": {
        "es": "Big King",
        "fr": "Big King",
        "de": "Big King",
        "hi": "बिग किंग"
    },
    "Big King Little King": {
        "es": "Big King Little King",
        "fr": "Big King Little King",
        "de": "Big King Little King",
        "hi": "बिग किंग लिटिल किंग"
    },
    "Big King Royale": {
        "es": "Big King Royale",
        "fr": "Big King Royale",
        "de": "Big King Royale",
        "hi": "बिग किंग रॉयल"
    },
    "Big King Double Royale": {
        "es": "Big King Double Royale",
        "fr": "Big King Double Royale",
        "de": "Big King Double Royale",
        "hi": "बिग किंग डबल रॉयल"
    },
    "Chicken Royale": {
        "es": "Chicken Royale",
        "fr": "Chicken Royale",
        "de": "Chicken Royale",
        "hi": "चिकन रॉयल"
    },
    "Chicken Royale Bacon & Cheese": {
        "es": "Chicken Royale con Beicon y Queso",
        "fr": "Chicken Royale Bacon & Fromage",
        "de": "Chicken Royale mit Bacon & Käse",
        "hi": "चिकन रॉयल बेकन और चीज़ के साथ"
    },
    "Double Chicken Royale": {
        "es": "Doble Chicken Royale",
        "fr": "Double Chicken Royale",
        "de": "Double Chicken Royale",
        "hi": "डबल चिकन रॉयल"
    },
    "Double Chicken Royale Bacon & Cheese": {
        "es": "Doble Chicken Royale con Beicon y Queso",
        "fr": "Double Chicken Royale Bacon & Fromage",
        "de": "Double Chicken Royale mit Bacon & Käse",
        "hi": "डबल चिकन रॉयल बेकन और चीज़ के साथ"
    },
    "Bacon Double Cheeseburger": {
        "es": "Doble Cheeseburger con Beicon",
        "fr": "Double Cheeseburger au Bacon",
        "de": "Bacon Double Cheeseburger",
        "hi": "बेकन डबल चीज़बर्गर"
    },
    "Bacon Double Cheese XL": {
        "es": "Bacon Double Cheese XL",
        "fr": "Bacon Double Cheese XL",
        "de": "Bacon Double Cheese XL",
        "hi": "बेकन डबल चीज़ XL"
    },
    "Double Cheeseburger": {
        "es": "Doble Cheeseburger",
        "fr": "Double Cheeseburger",
        "de": "Double Cheeseburger",
        "hi": "डबल चीज़बर्गर"
    },
    "Cheeseburger": {
        "es": "Cheeseburger (Hamburguesa con Queso)",
        "fr": "Cheeseburger",
        "de": "Cheeseburger",
        "hi": "चीज़बर्गर"
    },
    "Hamburger": {
        "es": "Hamburguesa Clásica",
        "fr": "Hamburger Classique",
        "de": "Hamburger",
        "hi": "हैमबर्गर"
    },
    "Plant-Based WHOPPER®": {
        "es": "Plant-Based WHOPPER® (100% Vegetal)",
        "fr": "Plant-Based WHOPPER® (100% Végétal)",
        "de": "Plant-Based WHOPPER® (Pflanzlich)",
        "hi": "प्लांट-बेस्ड व्हॉपर®"
    },
    "Vegan Royale": {
        "es": "Vegan Royale (Certificado Vegano)",
        "fr": "Vegan Royale (Certifié Végan)",
        "de": "Vegan Royale (Vegan)",
        "hi": "वीगन रॉयल"
    },
    "BBQ Steakhouse Angus": {
        "es": "BBQ Steakhouse Angus",
        "fr": "BBQ Steakhouse Angus",
        "de": "BBQ Steakhouse Angus",
        "hi": "BBQ स्टेकहाउस एंगस"
    },
    "BBQ Steakhouse Crispy Chicken": {
        "es": "BBQ Steakhouse Crispy Chicken",
        "fr": "BBQ Steakhouse Crispy Chicken",
        "de": "BBQ Steakhouse Crispy Chicken",
        "hi": "BBQ स्टेकहाउस क्रिस्पी चिकन"
    },
    "The Wagyu": {
        "es": "The Wagyu",
        "fr": "The Wagyu",
        "de": "The Wagyu",
        "hi": "द वाग्यू"
    },
    "Wagyu Wellington": {
        "es": "Wagyu Wellington",
        "fr": "Wagyu Wellington",
        "de": "Wagyu Wellington",
        "hi": "वाग्यू वेलिंगटन"
    },
    "Chicken Nuggets": {
        "es": "Nuggets de Pollo",
        "fr": "Nuggets de Poulet",
        "de": "Chicken Nuggets",
        "hi": "चिकन नगेट्स"
    },
    "Burger Buddies (3pc)": {
        "es": "Burger Buddies (3 uds)",
        "fr": "Burger Buddies (3 pièces)",
        "de": "Burger Buddies (3 Stück)",
        "hi": "बर्गर बडीज़ (3 पीस)"
    },
    "Burger Buddies (9pc)": {
        "es": "Burger Buddies (9 uds)",
        "fr": "Burger Buddies (9 pièces)",
        "de": "Burger Buddies (9 Stück)",
        "hi": "बर्गर बडीज़ (9 पीस)"
    },
    "Garlic & Jalapeno Chicken Fries": {
        "es": "Chicken Fries de Ajo y Jalapeño",
        "fr": "Chicken Fries Ail & Piment Jalapeno",
        "de": "Knoblauch & Jalapeno Chicken Fries",
        "hi": "गार्लिक और जलापेनो चिकन फ्राइज़"
    },
    "9pc Pringles Sour Cream & Onion Chicken Fries": {
        "es": "Chicken Fries Pringles Crema Agria y Cebolla (9 uds)",
        "fr": "Chicken Fries Pringles Crème & Oignon (9 pièces)",
        "de": "9er Pringles Sour Cream & Onion Chicken Fries",
        "hi": "प्रिंगल्स सोर क्रीम और अनियन चिकन फ्राइज़ (9 पीस)"
    },
    "Chilli Cheese Bites": {
        "es": "Chilli Cheese Bites (Bocaditos de Queso y Chile)",
        "fr": "Chilli Cheese Bites (Bouchées Fromage Piment)",
        "de": "Chilli Cheese Bites",
        "hi": "चिली चीज़ बाइट्स"
    },
    "Halloumi Fries": {
        "es": "Halloumi Fries (Palitos de Queso Halloumi)",
        "fr": "Frites de Halloumi",
        "de": "Halloumi Fries",
        "hi": "हलोमी फ्राइज़"
    },
    "Onion Rings": {
        "es": "Aros de Cebolla Crujientes",
        "fr": "Rondelles d'Oignon Croustillantes",
        "de": "Knusprige Zwiebelringe",
        "hi": "क्रिस्पी अनियन रिंग्स"
    },
    "Fries": {
        "es": "Patatas Fritas Clásicas",
        "fr": "Frites Croustillantes",
        "de": "Pommes Frites",
        "hi": "फ्रेंच फ्राइज़"
    },
    "Loaded King Fries": {
        "es": "Loaded King Fries",
        "fr": "Loaded King Fries",
        "de": "Loaded King Fries",
        "hi": "लोडेड किंग फ्राइज़"
    },
    "Loaded King Fries With Bacon": {
        "es": "Loaded King Fries con Beicon",
        "fr": "Loaded King Fries au Bacon",
        "de": "Loaded King Fries mit Bacon",
        "hi": "बेकन के साथ लोडेड किंग फ्राइज़"
    },
    "Truffle Loaded King Fries": {
        "es": "Loaded King Fries con Trufa",
        "fr": "Loaded King Fries à la Truffe",
        "de": "Trüffel Loaded King Fries",
        "hi": "ट्रफल लोडेड किंग फ्राइज़"
    },
    "Loaded Force Fries": {
        "es": "Loaded Force Fries",
        "fr": "Loaded Force Fries",
        "de": "Loaded Force Fries",
        "hi": "लोडेड फोर्स फ्राइज़"
    },
    "Cheddar Cheese Sauce XL": {
        "es": "Salsa de Queso Cheddar XL",
        "fr": "Sauce Cheddar Fondant XL",
        "de": "Cheddar Cheese Sauce XL",
        "hi": "चेडर चीज़ सॉस XL"
    },
    "BBQ Dip Pot": {
        "es": "Salsa Barbacoa (BBQ Dip)",
        "fr": "Sauce Barbecue (BBQ Dip)",
        "de": "BBQ Dip Sauce",
        "hi": "BBQ डिप पॉट"
    },
    "Sweet Chilli Dip Pot": {
        "es": "Salsa Sweet Chilli Dip",
        "fr": "Sauce Sweet Chilli Dip",
        "de": "Sweet Chilli Dip",
        "hi": "स्वीट चिली डिप"
    },
    "Vanilla Sundae": {
        "es": "Sundae de Vainilla",
        "fr": "Sundae Vanille",
        "de": "Vanille Sundae",
        "hi": "वैनिला संडे"
    },
    "Chocolate Sundae": {
        "es": "Sundae de Chocolate",
        "fr": "Sundae Chocolat",
        "de": "Schoko Sundae",
        "hi": "चॉकलेट संडे"
    },
    "Strawberry Sundae": {
        "es": "Sundae de Fresa",
        "fr": "Sundae Fraise",
        "de": "Erdbeer Sundae",
        "hi": "स्ट्रॉबेरी संडे"
    },
    "Salted Caramel Sundae": {
        "es": "Sundae de Caramelo Salado",
        "fr": "Sundae Caramel Salé",
        "de": "Salted Caramel Sundae",
        "hi": "सॉल्टेड कारमेल संडे"
    },
    "Vanilla Milkshake": {
        "es": "Batido de Vainilla",
        "fr": "Milkshake Vanille",
        "de": "Vanille Milkshake",
        "hi": "वैनिला मिल्कशेक"
    },
    "Chocolate Milkshake": {
        "es": "Batido de Chocolate",
        "fr": "Milkshake Chocolat",
        "de": "Schoko Milkshake",
        "hi": "चॉकलेट मिल्कशेक"
    },
    "Strawberry Milkshake": {
        "es": "Batido de Fresa",
        "fr": "Milkshake Fraise",
        "de": "Erdbeer Milkshake",
        "hi": "स्ट्रॉबेरी मिल्कशेक"
    },
    "Salted Caramel Milkshake": {
        "es": "Batido de Caramelo Salado",
        "fr": "Milkshake Caramel Salé",
        "de": "Salted Caramel Milkshake",
        "hi": "सॉल्टेड कारमेल मिल्कशेक"
    },
    "Smarties Fusion": {
        "es": "King Fusion con Smarties",
        "fr": "King Fusion Smarties",
        "de": "Smarties King Fusion",
        "hi": "स्मार्टीज़ किंग फ्यूजन"
    },
    "Twix Fusion": {
        "es": "King Fusion con Twix",
        "fr": "King Fusion Twix",
        "de": "Twix King Fusion",
        "hi": "ट्विक्स किंग फ्यूजन"
    },
    "Coca-Cola®": {
        "es": "Coca-Cola® Clásica",
        "fr": "Coca-Cola® Original",
        "de": "Coca-Cola® Original",
        "hi": "कोका-कोला®"
    },
    "Diet Coca-Cola®": {
        "es": "Coca-Cola Light (Diet)",
        "fr": "Coca-Cola Light (Diet)",
        "de": "Coca-Cola Light",
        "hi": "डाइट कोका-कोला®"
    },
    "Coca-Cola Zero Sugar": {
        "es": "Coca-Cola Zero Azúcar",
        "fr": "Coca-Cola Sans Sucres",
        "de": "Coca-Cola Zero Zucker",
        "hi": "कोका-कोला ज़ीरो शुगर"
    },
    "Fanta Zero": {
        "es": "Fanta Naranja Zero",
        "fr": "Fanta Orange Sans Sucres",
        "de": "Fanta Zero",
        "hi": "फैंटा ज़ीरो"
    },
    "Sprite Zero": {
        "es": "Sprite Zero",
        "fr": "Sprite Sans Sucres",
        "de": "Sprite Zero",
        "hi": "स्प्राइट ज़ीरो"
    },
    "Cappuccino": {
        "es": "Café Cappuccino",
        "fr": "Café Cappuccino",
        "de": "Cappuccino",
        "hi": "कैपुचिनो"
    },
    "Latte": {
        "es": "Café Latte con Leche",
        "fr": "Café Latte Onctueux",
        "de": "Caffè Latte",
        "hi": "लाते कॉफी"
    },
    "Flat White": {
        "es": "Café Flat White",
        "fr": "Café Flat White",
        "de": "Flat White",
        "hi": "फ्लैट व्हाइट कॉफी"
    },
    "Hot Chocolate": {
        "es": "Chocolate Caliente",
        "fr": "Chocolat Chaud Gourmand",
        "de": "Heiße Schokolade",
        "hi": "हॉट चॉकलेट"
    },
    "Tea": {
        "es": "Té Caliente Tradicional",
        "fr": "Thé Chaud Traditionnel",
        "de": "Feiner Tee",
        "hi": "गर्म चाय"
    },
    "Bottled Water": {
        "es": "Agua Mineral Embotellada",
        "fr": "Eau Minérale en Bouteille",
        "de": "Mineralwasser Flasche",
        "hi": "मिनरल वाटर की बोतल"
    }
}
