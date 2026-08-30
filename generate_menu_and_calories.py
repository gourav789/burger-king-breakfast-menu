#!/usr/bin/env python3
"""
Menu & Calories Page Localization Generator for Burger King Breakfast Menu UK
Generates translated and SEO-optimized menu.html and calories.html for en, es, fr, de, hi.
"""

import os
import re

from i18n_data import COMMON_I18N
from i18n_pages import PAGE_META
from i18n_menu_cards import MENU_CATEGORIES
from build_all_multilingual import (
    LANGS, LANG_META, get_page_url, get_asset_prefix,
    build_head, build_sidebar, build_topbar, build_footer, build_page_wrapper
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MENU_INTROS = {
    'en': {
        'hero_h1': 'Burger King Full Menu UK – Complete Guide with Photos 2026',
        'hero_p': 'Your definitive reference for every item on the Burger King UK menu, organised by category with photos and full descriptions. From the flame-grilled Croissan\'wich breakfast range that starts each morning, to iconic WHOPPER® burgers, crispy chicken, loaded fries, indulgent desserts, and refreshing drinks — everything Burger King has to offer is right here. Use the search bar below to find any specific item instantly, or scroll through each category to discover the full breadth of the BK menu.',
        'search_placeholder': 'Search any menu item — e.g. Croissan\'wich, WHOPPER, fries…',
        'items_count': '113 items',
        'no_results': 'No items match your search. Try a different term!'
    },
    'es': {
        'hero_h1': 'Menú Completo de Burger King UK – Guía con Fotos 2026',
        'hero_p': 'Tu referencia definitiva de cada producto del menú de Burger King en el Reino Unido, organizado por categorías con fotografías y descripciones completas. Desde los sándwiches Croissan\'wich a la parrilla de la mañana, hasta las legendarias hamburguesas WHOPPER®, pollo crujiente, patatas cargadas, postres y bebidas refrescantes. Utiliza la barra de búsqueda para encontrar cualquier producto o navega por las categorías.',
        'search_placeholder': 'Buscar cualquier producto — ej. Croissan\'wich, WHOPPER, patatas…',
        'items_count': '113 productos',
        'no_results': 'No se encontraron productos para tu búsqueda. ¡Prueba otro término!'
    },
    'fr': {
        'hero_h1': 'Menu Complet Burger King UK – Guide avec Photos 2026',
        'hero_p': 'Votre guide complet pour chaque produit du menu Burger King au Royaume-Uni, classé par catégorie avec photos et descriptions détaillées. Des Croissan\'wiches matinaux aux célèbres burgers WHOPPER®, en passant par le poulet croustillant, les frites gourmandes, les desserts et les boissons fraîches.',
        'search_placeholder': 'Rechercher un produit — ex. Croissan\'wich, WHOPPER, frites…',
        'items_count': '113 articles',
        'no_results': 'Aucun produit ne correspond à votre recherche. Essayez un autre mot !'
    },
    'de': {
        'hero_h1': 'Burger King Speisekarte UK – Alle Produkte mit Fotos 2026',
        'hero_p': 'Ihr umfassender Überblick über das gesamte Burger King Angebot in Großbritannien, übersichtlich nach Kategorien sortiert mit Fotos und Produktbeschreibungen. Von den morgendlichen Croissan\'wiches über den kultigen WHOPPER® bis hin zu knusprigem Chicken, Loaded Fries, Desserts und Erfrischungsgetränken.',
        'search_placeholder': 'Menü durchsuchen — z.B. Croissan\'wich, WHOPPER, Pommes…',
        'items_count': '113 Artikel',
        'no_results': 'Keine Produkte gefunden. Bitte versuchen Sie einen anderen Begriff!'
    },
    'hi': {
        'hero_h1': 'बर्गर किंग पूरा मेनू यूके – फोटो और विवरण सहित 2026',
        'hero_p': 'यूके में बर्गर किंग के हर मेनू आइटम की संपूर्ण और स्पष्ट जानकारी, फोटो और विस्तृत विवरण के साथ। सुबह के फ्लेम-ग्रिल्ड क्रॉसों\'विच ब्रेकफास्ट से लेकर प्रसिद्ध व्हॉपर® बर्गर, क्रिस्पी चिकन, लोडेड फ्राइज़, डेसर्ट और ड्रिंक्स तक सब कुछ यहाँ देखें।',
        'search_placeholder': 'कोई भी मेनू आइटम खोजें — जैसे Croissan\'wich, WHOPPER, Fries…',
        'items_count': '113 आइटम',
        'no_results': 'आपकी खोज से मेल खाता कोई आइटम नहीं मिला। कृपया दूसरा शब्द खोजें!'
    }
}

CALORIES_INTROS = {
    'en': {
        'hero_h1': 'Burger King Calories UK – Complete Nutritional Guide 2026',
        'hero_p': 'Your comprehensive guide to understanding calories at Burger King UK, including detailed nutritional information for every menu item, healthiest choices, and how to fit BK into your daily diet plan.',
        'sec1_h2': 'Understanding Calories at Burger King UK',
        'sec1_p1': 'Whether you\'re planning a quick breakfast, lunch, or dinner at Burger King, understanding the calorie content of menu items is essential for making informed dietary choices. This comprehensive guide provides detailed nutritional information for all Burger King UK menu items, helping you understand how different meals fit into your daily calorie allowance.',
        'sec1_p2': 'In the UK, food labelling regulations require all major fast-food chains to display calorie information on their menus. This transparency empowers customers to make healthier choices while still enjoying the foods they love.',
        'sec2_h2': 'Daily Calorie Intake Guidelines in the UK',
        'sec2_p': 'According to the NHS and UK dietary guidelines, the recommended daily calorie intake varies based on age, sex, and activity level. For adults, standard recommendations are 2,000 kcal for women and 2,500 kcal for men.',
    },
    'es': {
        'hero_h1': 'Calorías Burger King UK – Tabla Nutricional Completa 2026',
        'hero_p': 'Guía completa sobre calorías y valores nutricionales en Burger King UK, con información detallada de cada producto, opciones saludables y consejos para equilibrar tu dieta.',
        'sec1_h2': 'Cómo Entender las Calorías en Burger King UK',
        'sec1_p1': 'Ya sea para un desayuno rápido, almuerzo o cena, conocer las calorías de cada producto es fundamental para mantener una dieta equilibrada. Esta guía detalla las calorías, proteínas, grasas y carbohidratos de todo el menú de Burger King UK.',
        'sec1_p2': 'La normativa del Reino Unido exige mostrar el aporte calórico en los menús, facilitando a los clientes la elección de opciones más saludables sin renunciar a sus favoritos.',
        'sec2_h2': 'Guía de Ingesta Calórica Diaria en el Reino Unido',
        'sec2_p': 'Según las directrices sanitarias del NHS británico, la ingesta media recomendada es de 2.000 kcal al día para mujeres y 2.500 kcal para hombres.',
    },
    'fr': {
        'hero_h1': 'Calories Burger King UK – Guide Nutritionnel Complet 2026',
        'hero_p': 'Guide complet des calories et valeurs nutritionnelles chez Burger King au Royaume-Uni : apports énergétiques, options les plus saines et conseils diététiques.',
        'sec1_h2': 'Comprendre les Calories chez Burger King UK',
        'sec1_p1': 'Que ce soit pour le petit-déjeuner, le midi ou le soir, connaître l\'apport calorique des produits permet de mieux gérer son alimentation au quotidien. Retrouvez ici les données complètes pour chaque produit.',
        'sec1_p2': 'Au Royaume-Uni, l\'affichage des calories est obligatoire dans les chaînes de restauration rapide, permettant à chacun de faire des choix équilibrés.',
        'sec2_h2': 'Recommandations d\'Apports Journaliers au Royaume-Uni',
        'sec2_p': 'Selon les recommandations du NHS britannique, les apports moyens conseillés sont d\'environ 2 000 kcal par jour pour les femmes et 2 500 kcal pour les hommes.',
    },
    'de': {
        'hero_h1': 'Burger King Kalorien UK – Komplette Nährwerttabelle 2026',
        'hero_p': 'Ihr umfassender Leitfaden zu Kalorien und Nährwerten bei Burger King UK. Detaillierte Nährwertangaben für alle Produkte, kalorienarme Optionen und Ernährungstipps.',
        'sec1_h2': 'Kalorienangaben bei Burger King UK verstehen',
        'sec1_p1': 'Ob Frühstück, Mittag- oder Abendessen: Das Wissen um die Kalorienwerte hilft bei einer bewussten und ausgewogenen Ernährung. Dieser Ratgeber liefert genaue Daten zu Kalorien, Fett, Eiweiß und Kohlenhydraten.',
        'sec1_p2': 'In Großbritannien sind Kalorienangaben auf den Speisekarten gesetzlich vorgeschrieben, um Gästen eine transparente Auswahl zu ermöglichen.',
        'sec2_h2': 'Richtwerte für den täglichen Kalorienbedarf (UK)',
        'sec2_p': 'Gemäß den Richtlinien des britischen Gesundheitsdienstes NHS liegt der durchschnittliche Richtwert bei 2.000 kcal für Frauen und 2.500 kcal für Männer.',
    },
    'hi': {
        'hero_h1': 'बर्गर किंग कैलोरी यूके – पूरा पोषण और न्यूट्रिशन गाइड 2026',
        'hero_p': 'बर्गर किंग यूके के कैलोरी और न्यूट्रिशन को समझने के लिए विस्तृत गाइड। हर मेनू आइटम के लिए कैलोरी काउंट, प्रोटीन, कार्ब्स, फैट और स्वस्थ विकल्पों की जानकारी।',
        'sec1_h2': 'बर्गर किंग यूके में कैलोरी को समझें',
        'sec1_p1': 'चाहे आप सुबह का नाश्ता कर रहे हों या लंच/डिनर, मेनू आइटम्स की कैलोरी जानना सेहतमंद खान-पान के लिए बेहद जरूरी है। यह गाइड आपको हर आइटम के न्यूट्रिशन वैल्यू की सटीक जानकारी देती है।',
        'sec1_p2': 'यूके के नियमों के अनुसार फास्ट-फूड चेन को मेनू पर कैलोरी प्रदर्शित करना अनिवार्य है, जिससे ग्राहक सोच-समझकर सही भोजन चुन सकें।',
        'sec2_h2': 'दैनिक कैलोरी आवश्यकता (यूके दिशानिर्देश)',
        'sec2_p': 'यूके एनएचएस (NHS) के अनुसार वयस्कों के लिए दैनिक औसत आवश्यकता महिलाओं के लिए 2,000 कैलोरी और पुरुषों के लिए 2,500 कैलोरी है।',
    }
}

print("Menu and Calories helper dicts ready.")
