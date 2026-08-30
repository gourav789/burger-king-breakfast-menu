"""
Menu Items and Descriptions for Menu & Calorie pages across 5 languages.
"""

MENU_CATEGORIES = {
    'breakfast': {
        'icon': '🥐',
        'badge': '9',
        'en': {
            'title': 'Burger King Breakfast Menu',
            'hours': 'Served daily from 6:00 AM until 10:30 AM (weekdays) / 11:00 AM (weekends)',
            'desc': 'The <strong>Burger King breakfast menu</strong> is built around the iconic Croissan\'wich range — warm, flaky croissant buns filled with fresh egg, melted cheese, and a choice of flame-grilled or crispy proteins. Alongside the sandwiches, enjoy hearty Breakfast Kings, crispy Potato Bites, and premium hot coffee drinks.'
        },
        'es': {
            'title': 'Menú de Desayuno Burger King',
            'hours': 'Servido diariamente de 6:00 AM a 10:30 AM (lunes a viernes) / 11:00 AM (fines de semana)',
            'desc': 'El <strong>menú de desayuno de Burger King</strong> se centra en la gama Croissan\'wich: cruasanes calientes y mantecosos rellenos de huevo, queso fundido y carne a la parrilla o pollo crujiente. Incluye también la hamburguesa Breakfast King, deliciosos Potato Bites y cafés recién preparados.'
        },
        'fr': {
            'title': 'Menu Petit-déjeuner Burger King',
            'hours': 'Servi tous les jours de 6h00 à 10h30 (semaine) / 11h00 (week-end)',
            'desc': 'Le <strong>petit-déjeuner Burger King</strong> met à l\'honneur la gamme Croissan\'wich : de délicieux croissants dorés garnis d\'œufs, de fromage fondu et de viandes savoureuses grillées à la flamme. Retrouvez également le Breakfast King, les Potato Bites et un large choix de cafés.'
        },
        'de': {
            'title': 'Burger King Frühstückskarte',
            'hours': 'Täglich serviert von 6:00 bis 10:30 Uhr (werktags) / 11:00 Uhr (Wochenende)',
            'desc': 'Die <strong>Burger King Frühstückskarte</strong> basiert auf der beliebten Croissan\'wich-Reihe: buttrige Croissant-Brötchen mit Ei, zart schmelzendem Käse und flammengegrilltem Beef oder knusprigem Chicken. Dazu gibt es den Breakfast King, krosse Potato Bites und feinste Kaffeespezialitäten.'
        },
        'hi': {
            'title': 'बर्गर किंग ब्रेकफास्ट मेनू',
            'hours': 'प्रतिदिन सुबह 6:00 AM से 10:30 AM (सोम-शुक्र) / 11:00 AM (शनि-रवि) तक उपलब्ध',
            'desc': '<strong>बर्गर किंग ब्रेकफास्ट मेनू</strong> की खासियत इसके प्रसिद्ध क्रॉसों\'विच सैंडविच हैं – गर्म मक्खन क्रॉसों में अंडा, पिघला हुआ चीज़ और फ्लेम-ग्रिल्ड पैटी। इसके साथ ही ब्रेकफास्ट किंग, कुरकुरी पोटैटो बाइट्स और प्रीमियम हॉट कॉफी उपलब्ध है।'
        }
    },
    'burgers': {
        'icon': '🍔',
        'badge': '22',
        'en': {
            'title': 'Flame-Grilled Burgers',
            'hours': 'Available from 10:30 AM daily',
            'desc': 'Burger King\'s legendary flame-grilled beef burgers, including the iconic WHOPPER®, Big King, Angus range, and plant-based alternatives.'
        },
        'es': {
            'title': 'Hamburguesas a la Parrilla',
            'hours': 'Disponible a partir de las 10:30 AM diariamente',
            'desc': 'Las legendarias hamburguesas de ternera 100% a la parrilla de Burger King, como el emblemático WHOPPER®, Big King, gama Angus y opciones 100% vegetales.'
        },
        'fr': {
            'title': 'Burgers Grillés à la Flamme',
            'hours': 'Disponible à partir de 10h30 tous les jours',
            'desc': 'Les célèbres burgers au bœuf grillé à la flamme de Burger King, dont le mythique WHOPPER®, le Big King, la gamme Angus et les options végétales.'
        },
        'de': {
            'title': 'Flammengegrillte Burger',
            'hours': 'Täglich ab 10:30 Uhr erhältlich',
            'desc': 'Die legendären flammengegrillten Rindfleischburger von Burger King, darunter der ikonische WHOPPER®, Big King, die Angus-Linie und pflanzliche Alternativen.'
        },
        'hi': {
            'title': 'फ्लेम-ग्रिल्ड बर्गर',
            'hours': 'प्रतिदिन सुबह 10:30 AM के बाद उपलब्ध',
            'desc': 'बर्गर किंग के प्रसिद्ध खुली आग पर ग्रिल्ड बीफ और वेज बर्गर, जिनमें क्लासिक WHOPPER®, बिग किंग और प्रीमियम रेंज शामिल हैं।'
        }
    },
    'chicken': {
        'icon': '🍗',
        'badge': '8',
        'en': {
            'title': 'Chicken & Snacks',
            'hours': 'Available from 10:30 AM daily',
            'desc': 'Crispy chicken nuggets, Chicken Fries, Burger Buddies, and tasty snacks cooked to golden perfection.'
        },
        'es': {
            'title': 'Pollo y Snacks',
            'hours': 'Disponible a partir de las 10:30 AM diariamente',
            'desc': 'Crujientes nuggets de pollo, Chicken Fries, Burger Buddies y deliciosos aperitivos cocinados a la perfección.'
        },
        'fr': {
            'title': 'Poulet & Snacks',
            'hours': 'Disponible à partir de 10h30 tous les jours',
            'desc': 'Nuggets croustillants, Chicken Fries, Burger Buddies et savoureux snacks dorés à point.'
        },
        'de': {
            'title': 'Hähnchen & Snacks',
            'hours': 'Täglich ab 10:30 Uhr erhältlich',
            'desc': 'Knusprige Chicken Nuggets, Chicken Fries, Burger Buddies und leckere Snacks, goldbraun zubereitet.'
        },
        'hi': {
            'title': 'चिकन और स्नैक्स',
            'hours': 'प्रतिदिन सुबह 10:30 AM के बाद उपलब्ध',
            'desc': 'कुरकुरे चिकन नगेट्स, चिकन फ्राइज़, बर्गर बडीज़ और स्वादिष्ट स्नैक्स।'
        }
    },
    'sides': {
        'icon': '🍟',
        'badge': '10',
        'en': {
            'title': 'Sides & Dips',
            'hours': 'Available all day',
            'desc': 'Golden French fries, loaded King fries with bacon or cheese, Halloumi fries, onion rings, and signature dip pots.'
        },
        'es': {
            'title': 'Acompañamientos y Salsas',
            'hours': 'Disponible todo el día',
            'desc': 'Patatas fritas clásicas, Loaded King Fries con beicon o queso, palitos de halloumi, aros de cebolla y deliciosas salsas.'
        },
        'fr': {
            'title': 'Accompagnements & Sauces',
            'hours': 'Disponible toute la journée',
            'desc': 'Frites croustillantes, frites King gourmandes au bacon et fromage, frites de halloumi, rondelles d\'oignon et sauces savoureuses.'
        },
        'de': {
            'title': 'Beilagen & Dips',
            'hours': 'Den ganzen Tag erhältlich',
            'desc': 'Goldene Pommes Frites, Loaded King Fries mit Bacon oder Käse, Halloumi Fries, Zwiebelringe und Saucen-Dips.'
        },
        'hi': {
            'title': 'साइड्स और डिप्स',
            'hours': 'दिनभर उपलब्ध',
            'desc': 'सुनहरी फ्रेंच फ्राइज़, बेकन और चीज़ वाली लोडेड किंग फ्राइज़, हलोमी फ्राइज़, अनियन रिंग्स और टेस्टी डिप सॉस।'
        }
    },
    'meals': {
        'icon': '🎁',
        'badge': '14',
        'en': {
            'title': 'King Boxes & Meals',
            'hours': 'Available from 10:30 AM daily',
            'desc': 'Complete meal deals, King Boxes packed with sides and mains, and fun kids meals with drinks and treats.'
        },
        'es': {
            'title': 'Combos y Menús King',
            'hours': 'Disponible a partir de las 10:30 AM diariamente',
            'desc': 'Menús completos con hamburguesa, patatas y bebida, cajas King Box y menús infantiles para los más pequeños.'
        },
        'fr': {
            'title': 'Menus King & Box',
            'hours': 'Disponible à partir de 10h30 tous les jours',
            'desc': 'Menus complets avec boisson et frites, King Boxes généreuses et menus enfants équilibrés.'
        },
        'de': {
            'title': 'King Boxen & Menüs',
            'hours': 'Täglich ab 10:30 Uhr erhältlich',
            'desc': 'Komplette Menüs mit Burger, Pommes und Getränk, King Boxen sowie Kindermenüs für die Kleinen.'
        },
        'hi': {
            'title': 'किंग बॉक्स और मील्स',
            'hours': 'प्रतिदिन सुबह 10:30 AM के बाद उपलब्ध',
            'desc': 'बर्गर, फ्राइज़ और ड्रिंक के साथ पूरे मील कॉम्बो, किंग बॉक्स और बच्चों के लिए स्पेशल किड्स मील।'
        }
    },
    'desserts': {
        'icon': '🍦',
        'badge': '22',
        'en': {
            'title': 'Desserts & Sweets',
            'hours': 'Available all day',
            'desc': 'Creamy soft-serve sundaes, thick milkshakes, King Fusion with Smarties & Twix, Ben & Jerry\'s ice creams, and cheesecake bars.'
        },
        'es': {
            'title': 'Postres y Dulces',
            'hours': 'Disponible todo el día',
            'desc': 'Cremosos helados sundae, batidos espesos, King Fusion con Smarties y Twix, tarrinas Ben & Jerry\'s y barritas de cheesecake.'
        },
        'fr': {
            'title': 'Desserts & Douceurs',
            'hours': 'Disponible toute la journée',
            'desc': 'Sundaes onctueux, milkshakes gourmands, King Fusion aux Smarties & Twix, glaces Ben & Jerry\'s et barres cheesecake.'
        },
        'de': {
            'title': 'Desserts & Süßes',
            'hours': 'Den ganzen Tag erhältlich',
            'desc': 'Cremige Softeis-Sundaes, dicke Milkshakes, King Fusion mit Smarties & Twix, Ben & Jerry\'s Eisbecher und Cheesecake-Riegel.'
        },
        'hi': {
            'title': 'डेसर्ट और मीठा',
            'hours': 'दिनभर उपलब्ध',
            'desc': 'क्रीमी संडे आइसक्रीम, गाढ़े मिल्कशेक, स्मार्टीज़ और ट्विक्स वाले किंग फ्यूजन, बेन एंड जेरीज़ और चीज़केक बार।'
        }
    },
    'drinks': {
        'icon': '🥤',
        'badge': '20',
        'en': {
            'title': 'Drinks & Beverages',
            'hours': 'Available all day',
            'desc': 'Refreshing soft drinks, Frozen Fanta, Monster Energy, mineral water, and premium hot coffees and teas.'
        },
        'es': {
            'title': 'Bebidas y Cafés',
            'hours': 'Disponible todo el día',
            'desc': 'Refrescos helados, Frozen Fanta, Monster Energy, agua mineral y cafés calientes recién molidos.'
        },
        'fr': {
            'title': 'Boissons Fraîches & Chaudes',
            'hours': 'Disponible toute la journée',
            'desc': 'Sodas rafraîchissants, Frozen Fanta, boissons énergisantes Monster, eau minérale et cafés chauds de qualité.'
        },
        'de': {
            'title': 'Getränke & Kaffeespezialitäten',
            'hours': 'Den ganzen Tag erhältlich',
            'desc': 'Erfrischende Softdrinks, Frozen Fanta, Monster Energy, Mineralwasser sowie frisch gebrühter Kaffee und Tee.'
        },
        'hi': {
            'title': 'ड्रिंक्स और पेय पदार्थ',
            'hours': 'दिनभर उपलब्ध',
            'desc': 'ठंडे सॉफ्ट ड्रिंक्स, फ्रोजन फैंटा, मॉन्स्टर एनर्जी ड्रिंक, मिनरल वाटर, और ताज़ा गर्म कॉफी और चाय।'
        }
    }
}
