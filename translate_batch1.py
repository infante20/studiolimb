import os
import re

base_dir = './'
tools_to_translate = [
    'index.html', 
    'gradient-generator.html', 
    'css-triangle-generator.html', 
    'glassmorphism-generator.html', 
    'box-shadow-generator.html', 
    'border-radius-visualizer.html'
]

translations = {
    'es': {
        'lang': 'es',
        'btn_flag': '<span class="lang-flag">🇪🇸</span> ES',
        'lang_meta': 'es-ES',
        
        'index.html': {
            'title': 'StudioLimb | Herramientas Esenciales de Diseño y Desarrollo Web',
            'desc': 'Descubre StudioLimb: Una suite premium y gratuita de más de 30 micro-herramientas web modernas. Generadores CSS, flexbox, grid, compresión de imágenes y optimización SVG.',
            'hero_pill': '30+ Herramientas Gratuitas',
            'hero_title': 'El Kit Definitivo para <br />\n            <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-fuchsia-500">Creadores Web Modernos</span>',
            'hero_desc': 'Eleva tu flujo de trabajo con nuestra suite premium de micro-herramientas. Genera propiedades CSS, optimiza recursos y diseña layouts más rápido que nunca. 100% gratis, siempre rápido.',
            'start_btn': 'Comenzar a Crear',
            'bookmark_btn': 'Guardar en Favoritos (Ctrl+D)',
            'dir_title': 'Directorio de Herramientas',
            'dir_desc': 'Todo lo que necesitas, directamente en tu navegador.',
            'cat_css': 'Generadores CSS',
            'cat_typo': 'Tipografía y Layout',
            'cat_img': 'Imágenes y Recursos',
            'cat_dev': 'Utilidades para Devs',
            'cat_color': 'Color y Utilidades',
            't_grad': 'Gen. de Degradados', 'd_grad': 'Crea hermosos degradados CSS lineales y radiales para fondos.',
            't_tri': 'Triángulo CSS', 'd_tri': 'Genera triángulos puros en CSS para tooltips y flechas instantáneamente.',
            't_glass': 'Glassmorphism', 'd_glass': 'Genera componentes perfectos de vidrio esmerilado para tus interfaces.',
            't_box': 'Sombra de Caja', 'd_box': 'Diseña visualmente sombras en capas para dar profundidad y elevación.',
            't_border': 'Borde Redondeado', 'd_border': 'Visualiza y genera valores complejos de border-radius de 8 puntos en CSS.',
            't_snow': 'Efecto Nieve', 'd_snow': 'Generador interactivo de efecto de nieve de partículas CSS.',
            't_flex': 'Playground Flexbox', 'd_flex': 'Domina CSS Flexbox visualmente con controles interactivos.',
            't_grid': 'Gen. de CSS Grid', 'd_grid': 'Construye layouts complejos de CSS Grid en segundos, arrastra cuadrículas visualmente.',
            't_font': 'Combinar Fuentes', 'd_font': 'Descubre y previsualiza combinaciones armoniosas de Google Fonts.',
            't_type': 'Escala Tipográfica', 'd_type': 'Genera escalas tipográficas modulares perfectas usando ratios matemáticos.',
            't_lorem': 'Lorem Ipsum', 'd_lorem': 'Genera texto simulado instantáneamente con controles de párrafos y palabras.',
            't_comp': 'Compresor de Imágenes', 'd_comp': 'Reduce el tamaño de las imágenes al instante completamente en tu navegador.',
            't_place': 'Placeholder de Imagen', 'd_place': 'Crea imágenes falsas personalizadas para wireframes y exporta a SVG o PNG.',
            't_form': 'Convertidor de Formato', 'd_form': 'Convierte entre WebP, PNG y JPG preservando la transparencia.',
            't_res': 'Redimensionar Imagen', 'd_res': 'Redimensiona imágenes con precisión manteniendo la relación de aspecto.',
            't_bg': 'Quitar Fondo', 'd_bg': 'Elimina fondos de imágenes al instante y de forma privada usando IA en el dispositivo.',
            't_crop': 'Recortar Imagen', 'd_crop': 'Recorta imágenes a relaciones de aspecto específicas o dimensiones personalizadas.',
            't_filter': 'Filtros de Fotos', 'd_filter': 'Aplica filtros estilo Instagram y ajusta los parámetros de la imagen.',
            't_water': 'Creador de Marca de Agua', 'd_water': 'Protege tus imágenes superponiendo texto o logos como marca de agua.',
            't_col': 'Creador de Collages', 'd_col': 'Combina múltiples fotos en hermosos layouts de cuadrícula personalizables.',
            't_opt': 'Optimizador SVG', 'd_opt': 'Limpia y reduce el código SVG para entornos de producción.',
            't_wave': 'Generador de Ondas SVG', 'd_wave': 'Genera hermosos divisores de sección curvos y ondas vectoriales escalables.',
            't_qr': 'Generador Código QR', 'd_qr': 'Crea códigos QR personalizados de alta resolución con incrustación de logo.',
            't_reg': 'Tester de Regex', 'd_reg': 'Prueba, depura y entiende Expresiones Regulares con resaltado en tiempo real.',
            't_json': 'Formateador JSON', 'd_json': 'Embellece, valida y minifica datos JSON de forma segura en tu navegador.',
            't_base': 'Codificador Base64', 'd_base': 'Codifica y decodifica texto o archivos al formato Base64 al instante.',
            't_url': 'Codificador URL', 'd_url': 'Codifica tus URLs con seguridad o decodifica parámetros de consulta.',
            't_pal': 'Paleta de Colores', 'd_pal': 'Extrae y genera combinaciones de colores automáticamente.',
            't_con': 'Comprobador Contraste', 'd_con': 'Garantiza la accesibilidad comprobando los ratios de contraste de color WCAG.',
            't_px': 'PX a REM', 'd_px': 'Convierte rápidamente valores de píxeles a rem para CSS escalable.',
            't_soc': 'Tamaños Redes Sociales', 'd_soc': 'Hoja de referencia actualizada para las dimensiones de imágenes en todas las plataformas.'
        },
        'gradient-generator.html': {
            'title': 'Generador de Degradados CSS | StudioLimb',
            'desc': 'Crea hermosos degradados CSS lineales y radiales con nuestra herramienta visual interactiva.',
            'h2': 'Herramienta de Degradado CSS visual',
            'p': 'Diseña hermosos degradados ajustando colores, ángulos y opciones de mezcla para fondos fluidos.',
            'direction': 'Dirección', 'type': 'Tipo', 'linear': 'Lineal', 'radial': 'Radial', 'colors': 'Colores',
            'add_color': 'Añadir Color', 'output': 'Código CSS', 'copy': 'Copiar'
        },
        'css-triangle-generator.html': {
            'title': 'Generador de Triángulos CSS | StudioLimb',
            'desc': 'Genera formas de triángulos CSS puros instantáneamente para tus web tooltips e iconos.',
            'h2': 'Creador de Triángulos CSS puros',
            'p': 'Construye triángulos precisos y sin imágenes para tus interfaces ajustando dimensiones y colores.',
            'direction': 'Dirección', 'size': 'Tamaño', 'width': 'Cerrar Ancho', 'height': 'Cerrar Alto', 'color': 'Color',
            'output': 'Snippets de HTML y CSS', 'copy': 'Copiar Código'
        },
        'glassmorphism-generator.html': {
            'title': 'Generador Glassmorphism CSS | StudioLimb',
            'desc': 'Crea efectos modernos de vidrio esmerilado con propiedades CSS backdrop-filter.',
            'h2': 'Generador de Efecto Vidrio Esmerilado',
            'p': 'Crea interfaces translúcidas premium ajustando desenfoque, opacidad y brillo del borde lateral.',
            'blur': 'Desenfoque (Blur)', 'transparency': 'Transparencia', 'outline': 'Borde Luminoso',
            'bg_color': 'Color', 'output': 'Código CSS', 'copy': 'Copiar'
        },
        'box-shadow-generator.html': {
            'title': 'Generador Sombra de Caja CSS | StudioLimb',
            'desc': 'Diseña de forma interactiva sombras complejas en capas para diseños modernos y profundidad.',
            'h2': 'Diseñador Visual Box-Shadow',
            'p': 'Apila varias sombras para conseguir una profundidad suave y realista en tus componentes UI.',
            'layer': 'Capa de Sombra', 'inset': 'Sombra Interior (Inset)', 'x_offset': 'Posición X', 'y_offset': 'Posición Y',
            'blur': 'Desenfoque', 'spread': 'Propagación', 'color': 'Color', 'add_layer': 'Añadir Capa Sombra',
            'output': 'Código CSS', 'copy': 'Copiar CSS'
        },
        'border-radius-visualizer.html': {
            'title': 'Generador Border Radius CSS | StudioLimb',
            'desc': 'Genera de forma visual formas orgánicas usando valores de border-radius de 8 puntos.',
            'h2': 'Creador Formas Border Radius',
            'p': 'Manipula esquinas individuales para generar bordes creativos y asimétricos para botones o tarjetas.',
            'tl': 'Superior Izquierda', 'tr': 'Superior Derecha', 'br': 'Inferior Derecha', 'bl': 'Inferior Izquierda',
            'output': 'Regla de CSS', 'copy': 'Copiar'
        }
    },
    'fr': {
        'lang': 'fr',
        'btn_flag': '<span class="lang-flag">🇫🇷</span> FR',
        'lang_meta': 'fr-FR',
        
        'index.html': {
            'title': 'StudioLimb | Outils Essentiels de Design et Développement Web',
            'desc': 'Découvrez StudioLimb : Une suite premium et gratuite de plus de 30 micro-outils web modernes. Générateurs CSS, flexbox, grille, compression d\'images et optimisation SVG.',
            'hero_pill': '30+ Outils Gratuits',
            'hero_title': 'Le Kit Ultime pour <br />\n            <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-fuchsia-500">les Créateurs Web Modernes</span>',
            'hero_desc': 'Améliorez votre flux de travail avec notre suite premium de micro-outils. Générez des propriétés CSS, optimisez les ressources et concevez des mises en page plus rapidement que jamais. 100% gratuit, toujours rapide.',
            'start_btn': 'Commencer la Création',
            'bookmark_btn': 'Ajouter aux Favoris (Ctrl+D)',
            'dir_title': 'Annuaire des Outils',
            'dir_desc': 'Tout ce dont vous avez besoin, directement dans votre navigateur.',
            'cat_css': 'Générateurs CSS',
            'cat_typo': 'Typographie et Mise en Page',
            'cat_img': 'Images et Ressources',
            'cat_dev': 'Utilitaires pour Dévs',
            'cat_color': 'Couleur et Utilitaires',
            't_grad': 'Gén. de Dégradés', 'd_grad': 'Créez de superbes dégradés CSS linéaires et radiaux pour les arrière-plans.',
            't_tri': 'Triangle CSS', 'd_tri': 'Générez instantanément des triangles purs en CSS pour les info-bulles et les flèches.',
            't_glass': 'Glassmorphism', 'd_glass': 'Générez des composants parfaits en verre dépoli pour vos interfaces.',
            't_box': 'Ombre de Boîte', 'd_box': 'Concevez visuellement des ombres superposées pour donner de la profondeur et de l\'élévation.',
            't_border': 'Rayon de Bordure', 'd_border': 'Visualisez et générez des valeurs complexes de border-radius à 8 points en CSS.',
            't_snow': 'Effet Neige', 'd_snow': 'Générateur interactif d\'effets de neige de particules CSS.',
            't_flex': 'Playground Flexbox', 'd_flex': 'Maîtrisez visuellement CSS Flexbox avec des contrôles interactifs.',
            't_grid': 'Gén. de Grille CSS', 'd_grid': 'Construisez des mises en page complexes CSS Grid en quelques secondes, faites glisser les grilles visuellement.',
            't_font': 'Associer Polices', 'd_font': 'Découvrez et prévisualisez des combinaisons harmonieuses de Google Fonts.',
            't_type': 'Échelle Typographique', 'd_type': 'Générez des échelles typographiques modulaires parfaites en utilisant des ratios mathématiques.',
            't_lorem': 'Lorem Ipsum', 'd_lorem': 'Générez instantanément du faux texte avec des contrôles de paragraphes et de mots.',
            't_comp': 'Compresseur d\'Images', 'd_comp': 'Réduisez la taille des images instantanément et entièrement dans votre navigateur.',
            't_place': 'Espace Rempl. d\'Image', 'd_place': 'Créez des fausses images personnalisées pour les maquettes et exportez-les en SVG ou PNG.',
            't_form': 'Convertisseur de Format', 'd_form': 'Convertissez entre WebP, PNG et JPG tout en préservant la transparence.',
            't_res': 'Redimensionner Image', 'd_res': 'Redimensionnez les images avec précision tout en conservant les proportions.',
            't_bg': 'Suppresseur de Fond', 'd_bg': 'Supprimez les fonds d\'images instantanément et en privé en utilisant l\'IA sur l\'appareil.',
            't_crop': 'Recadrer Image', 'd_crop': 'Recadrez les images selon des proportions spécifiques ou des dimensions personnalisées.',
            't_filter': 'Filtres Photos', 'd_filter': 'Appliquez des filtres de style Instagram et ajustez les paramètres de l\'image.',
            't_water': 'Créateur de Filigrane', 'd_water': 'Protégez vos images en superposant du texte ou des logos en filigrane.',
            't_col': 'Créateur de Collages', 'd_col': 'Combinez plusieurs photos en de superbes grilles personnalisables.',
            't_opt': 'Optimiseur SVG', 'd_opt': 'Nettoyez et réduisez le code SVG pour les environnements de production.',
            't_wave': 'Gén. de Vagues SVG', 'd_wave': 'Générez de magnifiques séparateurs de sections courbes et des vagues vectorielles.',
            't_qr': 'Générateur Code QR', 'd_qr': 'Créez des codes QR haute résolution personnalisés avec incorporation de logo.',
            't_reg': 'Testeur Regex', 'd_reg': 'Testez, déboguez et comprenez les expressions régulières avec mise en surbrillance en temps réel.',
            't_json': 'Formateur JSON', 'd_json': 'Embellissez, validez et minifiez les données JSON en toute sécurité dans votre navigateur.',
            't_base': 'Encodeur Base64', 'd_base': 'Encodez et décodez instantanément du texte ou des fichiers au format Base64.',
            't_url': 'Encodeur URL', 'd_url': 'Encodez vos URL en toute sécurité ou décodez les paramètres de requête.',
            't_pal': 'Palette de Couleurs', 'd_pal': 'Extrayez et générez automatiquement des combinaisons de couleurs.',
            't_con': 'Vérificateur. Contraste', 'd_con': 'Assurez l\'accessibilité en vérifiant les ratios de contraste de couleurs WCAG.',
            't_px': 'PX en REM', 'd_px': 'Convertissez rapidement les valeurs de pixels en rem pour des CSS évolutives.',
            't_soc': 'Tailles Réf. Sociaux', 'd_soc': 'Fiche de référence à jour pour les dimensions des images sur toutes les plateformes.'
        },
        'gradient-generator.html': {
            'title': 'Générateur de Dégradés CSS | StudioLimb',
            'desc': 'Créez de superbes dégradés CSS linéaires et radiaux avec notre outil interactif.',
            'h2': 'Outil Dégradé CSS',
            'p': 'Concevez de beaux dégradés en ajustant les couleurs, les angles et les mélanges.',
            'direction': 'Direction', 'type': 'Type', 'linear': 'Linéaire', 'radial': 'Radial', 'colors': 'Couleurs',
            'add_color': 'Ajouter Couleur', 'output': 'Code CSS', 'copy': 'Copier'
        },
        'css-triangle-generator.html': {
            'title': 'Générateur de Triangles CSS | StudioLimb',
            'desc': 'Générez instantanément des triangles CSS purs pour vos info-bulles et icônes.',
            'h2': 'Créateur Triangles CSS',
            'p': 'Créez des triangles précis sans image pour vos interfaces en ajustant taille et couleur.',
            'direction': 'Direction', 'size': 'Taille', 'width': 'Largeur', 'height': 'Hauteur', 'color': 'Couleur',
            'output': 'Extraits HTML & CSS', 'copy': 'Copier le Code'
        },
        'glassmorphism-generator.html': {
            'title': 'Générateur Glassmorphism CSS | StudioLimb',
            'desc': 'Créez des effets modernes de verre dépoli avec les propriétés CSS.',
            'h2': 'Générateur Verre Dépoli',
            'p': 'Créez des interfaces premium translucides en ajustant le flou et la bordure.',
            'blur': 'Flou (Blur)', 'transparency': 'Transparence', 'outline': 'Contour Lumineux',
            'bg_color': 'Couleur', 'output': 'Code CSS', 'copy': 'Copier'
        },
        'box-shadow-generator.html': {
            'title': 'Générateur Ombre de Boîte CSS | StudioLimb',
            'desc': 'Concevez de manière interactive des ombres complexes en couches.',
            'h2': 'Ombres Visuelles CSS',
            'p': 'Empilez des ombres pour obtenir une profondeur fluide et réaliste.',
            'layer': 'Couche d\'Ombre', 'inset': 'Ombre Interne', 'x_offset': 'Décalage X', 'y_offset': 'Décalage Y',
            'blur': 'Flou', 'spread': 'Étalement', 'color': 'Couleur', 'add_layer': 'Ajouter Couche',
            'output': 'Code CSS', 'copy': 'Copier CSS'
        },
        'border-radius-visualizer.html': {
            'title': 'Générateur Border Radius CSS | StudioLimb',
            'desc': 'Générez visuellement des formes organiques à l\'aide de border-radius CSS.',
            'h2': 'Créateur Formes CSS',
            'p': 'Manipulez des coins individuels pour générer des bordures asymétriques.',
            'tl': 'Haut Gauche', 'tr': 'Haut Droit', 'br': 'Bas Droit', 'bl': 'Bas Gauche',
            'output': 'Règle CSS', 'copy': 'Copier'
        }
    },
    'hi': {
        'lang': 'hi',
        'btn_flag': '<span class="lang-flag">🇮🇳</span> HI',
        'lang_meta': 'hi-IN',
        'index.html': {
            'title': 'StudioLimb | आवश्यक वेब डिज़ाइन और विकास उपकरण',
            'desc': 'StudioLimb की खोज करें: 30 से अधिक आधुनिक वेब माइक्रो-टूल्स का एक मुफ्त, प्रीमियम सूट। सीएसएस ग्रेडिएंट्स, फ्लेक्सबॉक्स, ग्रिड, छवि संपीड़न और एसवीजी अनुकूलन के लिए जनरेटर।',
            'hero_pill': '30+ मुफ्त उपकरण',
            'hero_title': '<span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-fuchsia-500">आधुनिक वेब निर्माताओं</span><br />के लिए अंतिम टूलकिट',
            'hero_desc': 'माइक्रो-टूल्स के हमारे प्रीमियम सूट के साथ अपने वर्कफ़्लो को बढ़ाएं। सीएसएस गुण उत्पन्न करें, संपत्तियों को अनुकूलित करें और लेआउट को पहले से कहीं अधिक तेज़ी से डिज़ाइ करें। 100% मुफ्त, हमेशा तेज।',
            'start_btn': 'बनाना शुरू करें',
            'bookmark_btn': 'बुकमार्क करें (Ctrl+D)',
            'dir_title': 'टूल निर्देशिका',
            'dir_desc': 'वह सब कुछ जो आपको चाहिए, सीधे आपके ब्राउज़र में।',
            'cat_css': 'सीएसएस जेनरेटर',
            'cat_typo': 'टाइपोग्राफी और लेआउट',
            'cat_img': 'चित्र और संपत्तियां',
            'cat_dev': 'डेवलपर उपयोगिताएँ',
            'cat_color': 'रंग और उपयोगिताएँ',
            't_grad': 'ग्रेडिएंट जेनरेटर', 'd_grad': 'पृष्ठभूमि के लिए सुंदर रैखिक और रेडियल सीएसएस ग्रेडिएंट बनाएं।',
            't_tri': 'सीएसएस त्रिकोण', 'd_tri': 'टूलटिप्स और तीर के लिए तुरंत शुद्ध सीएसएस त्रिकोण बनाएं।',
            't_glass': 'ग्लासमॉर्फिज्म', 'd_glass': 'अपने इंटरफेस के लिए सही पाले सेओढ़े कांच घटक उत्पन्न करें।',
            't_box': 'बॉक्स शैडो', 'd_box': 'गहराई और ऊंचाई के लिए स्तरित ड्रॉप छाया को नेत्रहीन रूप से डिजाइन करें।',
            't_border': 'बॉर्डर रेडियस', 'd_border': 'विज़ुअलाइज़ करें और जटिल 8-पॉइंट सीएसएस बॉर्डर त्रिज्या मान उत्पन्न करें।',
            't_snow': 'बर्फबारी प्रभाव', 'd_snow': 'इंटरएक्टिव सीएसएस पार्टिकल स्नो इफेक्ट जनरेटर।',
            't_flex': 'फ्लेक्सबॉक्स खेल का मैदान', 'd_flex': 'इंटरैक्टिव नियंत्रणों के साथ नेत्रहीन सीएसएस फ्लेक्सबॉक्स में महारत हासिल करें।',
            't_grid': 'सीएसएस ग्रिड जेनरेटर', 'd_grid': 'सेकंड में जटिल सीएसएस ग्रिड लेआउट बनाएं, लेआउट ग्रिड को नेत्रहीन खींचें।',
            't_font': 'फ़ॉन्ट पेयरिंग', 'd_font': 'सुरीले Google फ़ॉन्ट संयोजनों की खोज और पूर्वावलोकन करें।',
            't_type': 'टाइप स्केल', 'd_type': 'गणितीय अनुपात का उपयोग करके मॉड्यूलर सही टाइपोग्राफी स्केल उत्पन्न करें।',
            't_lorem': 'लोरेम इप्सम', 'd_lorem': 'अनुच्छेद और शब्द नियंत्रण के साथ तुरंत प्लेसहोल्डर पाठ उत्पन्न करें।',
            't_comp': 'छवि कंप्रेसर', 'd_comp': 'पूरी तरह से अपने ब्राउज़र के भीतर छवि फ़ाइल आकार तुरंत कम करें।',
            't_place': 'छवि प्लेसहोल्डर', 'd_place': 'वायरफ्रेम के लिए कस्टम डमी चित्र बनाएं और एसवीजी या पीएनजी में निर्यात करें।',
            't_form': 'प्रारूप कनवर्टर', 'd_form': 'पारदर्शिता को संरक्षित करते हुए वेबपी, पीएनजी और जेपीजी के बीच कनव्ट करें।',
            't_res': 'छवि रिसाइज़र', 'd_res': 'पहलू अनुपात की बाधाओं के साथ छवियों का सटीक रूप से आकार बदलें।',
            't_bg': 'बीजी रिमूवर', 'd_bg': 'ऑन-डिवाइस एआई का उपयोग करके तुरंत और निजी तौर पर छवि पृष्ठभूमि हटा दें।',
            't_crop': 'छवि क्रॉपर', 'd_crop': 'छवियों को विशिष्ट पहलू अनुपात या कस्टम आयामों में मूल रूप से क्रॉप करें।',
            't_filter': 'फोटो फिल्टर', 'd_filter': 'इंस्टाग्राम-शैली के फिल्टर लागू करें और छवि समायोजन को ठीक करें।',
            't_water': 'वॉटरमार्क निर्माता', 'd_water': 'कस्टम टेक्स्ट या लोगो वॉटरमार्क को ओवरले करके अपनी छवियों को सुरक्षित रखें।',
            't_col': 'कोलाज निर्माता', 'd_col': 'कई तस्वीरों को सुंदर, अनुकूलन योग्य ग्रिड लेआउट में संयोजित करें।',
            't_opt': 'एसवीजी ऑप्टिमाइज़र', 'd_opt': 'उत्पादन वातावरण के लिए एसवीजी मार्कअप को साफ और सिकोड़ें।',
            't_wave': 'एसवीजी वेव जेनरेटर', 'd_wave': 'सुंदर स्केलेबल अनुभाग विभक्त और लहर आकार उत्पन्न करें।',
            't_qr': 'क्यूआर कोड जेनरेटर', 'd_qr': 'लोगो एम्बेडिंग के साथ कस्टम, उच्च-रिज़ॉल्यूशन क्यूआर कोड बनाएं।',
            't_reg': 'रेगेक्स परीक्षक', 'd_reg': 'रीयल-टाइम हाइलाइटिंग के साथ रेगुलर एक्सप्रेशन का परीक्षण, डीबग और समझें।',
            't_json': 'JSON फ़ॉर्मेटर', 'd_json': 'अपने ब्राउज़र में JSON डेटा को सुरक्षित रूप से सुशोभित, मान्य और छोटा करें।',
            't_base': 'Base64 एनकोडर', 'd_base': 'टेक्स्ट या फाइलों को तुरंत Base64 फॉर्मेट में एन्कोड और डिकोड करें।',
            't_url': 'URL एनकोडर', 'd_url': 'अपने URL को सुरक्षित रूप से एन्कोड करें या क्वेरी पैरामीटर डिकोड करें।',
            't_pal': 'रंग पैलेट', 'd_pal': 'स्वचालित रूप से रंग संयोजनों को निकालें और उत्पन्न करें।',
            't_con': 'कंट्रास्ट चेकर', 'd_con': 'WCAG रंग विपरीत अनुपातों की जाँच करके पहुँच सुनिश्चित करें।',
            't_px': 'PX से REM', 'd_px': 'स्केलेबल सीएसएस के लिए पिक्सेल मानों को रेम ें तेज़ी से बदलें।',
            't_soc': 'सामाजिक आकार सूची', 'd_soc': 'सभी प्लेटफॉर्म छवि आयामों के लिए अप-टू-डेट संदर्भ पत्रक।'
        },
        'gradient-generator.html': {
            'title': 'CSS ग्रेडिएंट जनरेटर | StudioLimb',
            'desc': 'हमारे संवादात्मक दृश्य टूल के साथ सुंदर रैखिक और रेडियल CSS ग्रेडिएंट बनाएं।',
            'h2': 'CSS ग्रेडिएंट टूल',
            'p': 'सहज पृष्ठभूमि के लिए रंग, कोण और सम्मिश्रण विकल्पों को समायोजित करके सुंदर ग्रेडिएंट डिज़ाइन करें।',
            'direction': 'दिशा', 'type': 'प्रकार', 'linear': 'रैखिक', 'radial': 'रेडियल', 'colors': 'रंग',
            'add_color': 'रंग जोड़ें', 'output': 'CSS कोड', 'copy': 'कॉपी करें'
        },
        'css-triangle-generator.html': {
            'title': 'CSS त्रिकोण जनरेटर | StudioLimb',
            'desc': 'अपने टूलटिप्स और आइकन के लिए तुरंत शुद्ध CSS त्रिकोण आकार बनाएं।',
            'h2': 'शुद्ध CSS त्रिकोण',
            'p': 'आयामों और रंगों को समायोजित करके अपने इंटरफेस के लिए सटीक त्रिोण बनाएं।',
            'direction': 'दिशा', 'size': 'आकार', 'width': 'चौड़ाई', 'height': 'ऊंचाई', 'color': 'रंग',
            'output': 'HTML और CSS कोड', 'copy': 'कोड कॉपी करें'
        },
        'glassmorphism-generator.html': {
            'title': 'ग्लासमॉर्फिज्म जनरेटर | StudioLimb',
            'desc': 'CSS बैकड्रॉप-फ़िल्टर गुणों के साथ आधुनिक पाले सेओढ़े कांच के प्रभाव बनाएँ।',
            'h2': 'पाले सेओढ़े कांच जनरेटर',
            'p': 'धुंधलापन, अपारदर्शिता और किनारे की चमक को समायोजित करके प्रीमियम पारभासी इंटरफेस बनाएं।',
            'blur': 'धुंधलापन', 'transparency': 'पारदर्शिता', 'outline': 'चमकदार आउटलाइन',
            'bg_color': 'रंग', 'output': 'CSS कोड', 'copy': 'कॉपी करें'
        },
        'box-shadow-generator.html': {
            'title': 'बॉक्स शैडो जनरेटर | StudioLimb',
            'desc': 'आधुनिक और गहराई वाले डिज़ाइनों के लिए अंतःक्रियात्मक रूप से जटिल छाया परतें डिज़ाइन करें।',
            'h2': 'दृश्य छाया डिज़ाइनर',
            'p': 'यथार्थवादी गहराई के लिए अपने UI घटकों में कई छायाओं को स्टैक करें।',
            'layer': 'छाया परत', 'inset': 'आंतरिक छाया', 'x_offset': 'X ऑफसेट', 'y_offset': 'Y ऑफसेट',
            'blur': 'धुंधला', 'spread': 'फैलाव', 'color': 'रंग', 'add_layer': 'छाया परत जोड़ें',
            'output': 'CSS कोड', 'copy': 'CSS कॉपी करें'
        },
        'border-radius-visualizer.html': {
            'title': 'बॉर्डर रेडियस जनरेटर | StudioLimb',
            'desc': '8-बिंदु वाले CSS बॉर्डर-रेडियस मानों का उपयोग करके दृष्टिगत रूप से जैविक आकार उत्पन्न करें।',
            'h2': 'बॉर्डर रेडियस आकार',
            'p': 'बटन या कार्ड के लिए रचनात्मक और असममित बॉर्डर उत्पन्न करने के लिए कोनों में हेरफेर करें।',
            'tl': 'शीर्ष बायां', 'tr': 'शीर्ष दायां', 'br': 'नीचे दायां', 'bl': 'नीचे बायां',
            'output': 'CSS नियम', 'copy': 'कॉपी करें'
        }
    },
    'pt': {
        'lang': 'pt',
        'btn_flag': '<span class="lang-flag">🇧🇷</span> PT',
        'lang_meta': 'pt-BR',
        
        'index.html': {
            'title': 'StudioLimb | Ferramentas Essenciais de Design e Desenvolvimento Web',
            'desc': 'Descubra a StudioLimb: Um conjunto premium e gratuito de mais de 30 micro-ferramentas da web modernas. Geradores CSS, flexbox, grade, compressão de imagens e otimização de SVG.',
            'hero_pill': '30+ Ferramentas Gratuitas',
            'hero_title': 'O Kit Definitivo para <br />\n            <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-fuchsia-500">Criadores Web Modernos</span>',
            'hero_desc': 'Aumente o seu fluxo de trabalho com nosso conjunto premium de micro-ferramentas. Gere propriedades CSS, otimize recursos e crie layouts mais rápido do que nunca. 100% gratuito, sempre rápido.',
            'start_btn': 'Começar a Criar',
            'bookmark_btn': 'Salvar nos Favoritos (Ctrl+D)',
            'dir_title': 'Diretório de Ferramentas',
            'dir_desc': 'Tudo o que você precisa, diretamente no seu navegador.',
            'cat_css': 'Geradores CSS',
            'cat_typo': 'Tipografia e Layout',
            'cat_img': 'Imagens e Recursos',
            'cat_dev': 'Utilitários para Devs',
            'cat_color': 'Cores e Utilitários',
            't_grad': 'Gen. de Gradientes', 'd_grad': 'Crie belos gradientes CSS lineares e radiais para planos de fundo.',
            't_tri': 'Triângulo CSS', 'd_tri': 'Gere instantaneamente triângulos puros em CSS para balões de dicas e setas.',
            't_glass': 'Glassmorfismo', 'd_glass': 'Gere componentes perfeitos de vidro fosco para suas interfaces.',
            't_box': 'Sombra de Caixa', 'd_box': 'Crie visualmente sombras em camadas para dar profundidade e elevação.',
            't_border': 'Raio da Borda', 'd_border': 'Visualize e gere valores complexos de border-radius de 8 pontos no CSS.',
            't_snow': 'Efeito de Neve', 'd_snow': 'Gerador interativo de efeito de neve com partículas de CSS.',
            't_flex': 'Playground Flexbox', 'd_flex': 'Domine visualmente o CSS Flexbox com controles interativos.',
            't_grid': 'Gen. de Grade CSS', 'd_grid': 'Construa layouts complexos em CSS Grid em segundos, arraste as grades visualmente.',
            't_font': 'Combinação de Fontes', 'd_font': 'Descubra e visualize combinações harmoniosas do Google Fonts.',
            't_type': 'Escala Tipográfica', 'd_type': 'Gere escalas tipográficas modulares perfeitas usando proporções matemáticas.',
            't_lorem': 'Lorem Ipsum', 'd_lorem': 'Gere texto fictício instantaneamente com controles de parágrafo e palavras.',
            't_comp': 'Compressor de Imagem', 'd_comp': 'Reduza instantaneamente o tamanho dos arquivos de imagem inteiramente no seu navegador.',
            't_place': 'Espaço Res. Imagens', 'd_place': 'Crie imagens falsas personalizadas para esboços e exporte para SVG ou PNG.',
            't_form': 'Conversor de Formato', 'd_form': 'Converta entre WebP, PNG e JPG preservando a transparência.',
            't_res': 'Redimensionar Imagem', 'd_res': 'Redimensione as imagens com precisão mantendo a proporção da tela.',
            't_bg': 'Remover Fundo', 'd_bg': 'Remova fundos de imagens de maneira instantânea e privada usando IA no dispositivo.',
            't_crop': 'Recortar Imagem', 'd_crop': 'Corte imagens em proporções específicas ou dimensões personalizadas de forma contínua.',
            't_filter': 'Filtros de Fotos', 'd_filter': 'Aplique filtros no estilo do Instagram e ajuste as opções de imagem.',
            't_water': 'Criador Marca d\'Água', 'd_water': 'Proteja suas imagens sobrepondo texto ou logotipos com marcas d\'água.',
            't_col': 'Fazedor de Colagens', 'd_col': 'Combine várias fotos em belos layouts de grade personalizáveis.',
            't_opt': 'Otimizador de SVG', 'd_opt': 'Limpe e reduza a marcação de SVG para ambientes de produção.',
            't_wave': 'Gen. de Ondas SVG', 'd_wave': 'Gere belos divisores de seção flexíveis e de formatos curvos em vetor.',
            't_qr': 'Gerador de QR Code', 'd_qr': 'Crie QR codes de alta resolução com logotipos incorporados.',
            't_reg': 'Testador Regex', 'd_reg': 'Teste, depure e entenda Expressões Regulares com destaque em tempo real.',
            't_json': 'Formatador JSON', 'd_json': 'Embeleze, valide e minimize os dados JSON de forma mais segura em seu navegador.',
            't_base': 'Codificador Base64', 'd_base': 'Codifique e decodifique texto ou arquivos para o formato Base64 instantaneamente.',
            't_url': 'Codificador de URL', 'd_url': 'Codifique suas URLs com mais segurança ou decodifique parâmetros de pesquisa.',
            't_pal': 'Paleta de Cores', 'd_pal': 'Extraia e gere combinações de cores mais atraentes automaticamente.',
            't_con': 'Verificar Contraste', 'd_con': 'Garante a acessibilidade com os diferentes níveis de proporções de contraste de cores WCAG.',
            't_px': 'PX para REM', 'd_px': 'Converta rapidamente os valores de pixel em milésimos para seu dimensionamento.',
            't_soc': 'Tamanhos para Redes', 'd_soc': 'Informações para referência mais recentes no quesito dimensões para todas as suas plataformas.'
        },
        'gradient-generator.html': {
            'title': 'Gerador de Gradientes CSS | StudioLimb',
            'desc': 'Crie belos gradientes CSS lineares e radiais com nossa ferramenta visual e interativa.',
            'h2': 'Criador Gradientes CSS',
            'p': 'Crie gradientes agradáveis definindo a cor, angulação e também o mix de mesclagem ideal de cores.',
            'direction': 'Direção', 'type': 'Tipo', 'linear': 'Linear', 'radial': 'Radial', 'colors': 'Cores',
            'add_color': 'Adicionar Cor', 'output': 'Código CSS', 'copy': 'Copiar'
        },
        'css-triangle-generator.html': {
            'title': 'Gerador de Triângulos CSS | StudioLimb',
            'desc': 'Gere instantaneamente marcações em formatos CSS para criar balões informativos de dicas entre outras melhorias.',
            'h2': 'Triângulo CSS Puro',
            'p': 'Gere triângulos precisos para deixar as interfaces aprimoradas, adequando a largura ideal.',
            'direction': 'Direção', 'size': 'Tamanho', 'width': 'Largura', 'height': 'Altura', 'color': 'Cor',
            'output': 'Snippets HTML e CSS', 'copy': 'Copiar Código'
        },
        'glassmorphism-generator.html': {
            'title': 'Gerador de Glassmorfismo | StudioLimb',
            'desc': 'Crie efeitos modernos contendo uma pegada transparente em cima de itens que dão efeitos vitrificados.',
            'h2': 'Gen. Vidro Fosco',
            'p': 'Produza a variação visual premium aplicando algumas definições na intensidade da opacidade com reflexos.',
            'blur': 'Borrão (Blur)', 'transparency': 'Transparência', 'outline': 'Brilhar Borda',
            'bg_color': 'Cor', 'output': 'Código CSS', 'copy': 'Copiar'
        },
        'box-shadow-generator.html': {
            'title': 'Gerador de Sombra CSS | StudioLimb',
            'desc': 'Crie projetos complexos utilizando design visual dinâmico focado em camadas complexas de sombras baseadas na profundidade.',
            'h2': 'Designer de Box-Shadow',
            'p': 'Inclua variações criativas sobre as intensidades na geração realista de sombras contínuas aplicadas nos atributos e botões principais.',
            'layer': 'Camada da Sombra', 'inset': 'Sombra Interna (Inset)', 'x_offset': 'Posição X', 'y_offset': 'Posição Y',
            'blur': 'Desfoque', 'spread': 'Propagação', 'color': 'Cor', 'add_layer': 'Adicionar Sombras',
            'output': 'Código CSS', 'copy': 'Copiar CSS'
        },
        'border-radius-visualizer.html': {
            'title': 'Gerador de Border Radius | StudioLimb',
            'desc': 'Gere marcações únicas de componentes através dos limites ajustáveis de curvas estéticas complexas para aplicações mais robustas que demandam variações dinâmicas visualmente orgânicas.',
            'h2': 'Construtor de Bordas CSS',
            'p': 'Experimente configurações focadas nas quatro quinas ajustáveis até elaborar visuais inovadores e desproporcionais visivelmente originais.',
            'tl': 'Superior Esquerda', 'tr': 'Superior Direita', 'br': 'Inferior Direita', 'bl': 'Inferior Esquerda',
            'output': 'Regra CSS', 'copy': 'Copiar'
        }
    }
}


def build_dropdown(current_lang, filename):
    def link_for(target_lang):
        if target_lang == 'en': 
            return f'../{filename}' if current_lang != 'en' else filename
        else: 
            return f'{target_lang}/{filename}' if current_lang == 'en' else (filename if current_lang == target_lang else f'../{target_lang}/{filename}')

    return f'''        <div class="lang-selector">
            <button class="lang-btn">
                {translations[current_lang]['btn_flag'] if current_lang != 'en' else '<span class="lang-flag">🇺🇸</span> EN'}
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="lang-dropdown">
                <a href="{link_for('en')}" class="lang-option {'active' if current_lang == 'en' else ''}"><span class="lang-flag">🇺🇸</span> English</a>
                <a href="{link_for('es')}" class="lang-option {'active' if current_lang == 'es' else ''}"><span class="lang-flag">🇪🇸</span> Español</a>
                <a href="{link_for('fr')}" class="lang-option {'active' if current_lang == 'fr' else ''}"><span class="lang-flag">🇫🇷</span> Français</a>
                <a href="{link_for('hi')}" class="lang-option {'active' if current_lang == 'hi' else ''}"><span class="lang-flag">🇮🇳</span> हिन्दी</a>
                <a href="{link_for('pt')}" class="lang-option {'active' if current_lang == 'pt' else ''}"><span class="lang-flag">🇧🇷</span> Português</a>
            </div>
        </div>'''

def process_translation():
    for f in tools_to_translate:
        print(f"Translating {f}")
        file_path = os.path.join(base_dir, f)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as src:
                html = src.read()
            original_html = html
        except FileNotFoundError:
             print(f"Skipping {f} - File not found")
             continue

        for code, data in translations.items():
            t_data = data.get(f)
            if not t_data:
                 print(f"No translation data for {code} - {f}")
                 continue
                 
            html = original_html.replace('lang="en"', f'lang="{code}"')
            
            # 1. Update Dropdown logic using a Regex
            # Find the lang-selector div and replace it, we need to locate it first.
            dropdown_pattern = re.compile(r'<div class="lang-selector">.*?</div>\s*</div>', re.DOTALL)
            html = dropdown_pattern.sub(build_dropdown(code, f), html)

            
            # --- INDEX TRANSLATIONS ---
            if f == 'index.html':
                html = html.replace('<title>StudioLimb | Essential Web Design & Development Tools</title>', f'<title>{t_data["title"]}</title>')
                html = html.replace('content="A free, premium suite of modern web micro-tools for designers and developers."', f'content="{t_data["desc"]}"')
                html = html.replace('content="Discover StudioLimb: A free, premium suite of over 20+ modern web micro-tools. Generators for CSS gradients, glassmorphism, flexbox, grid, image compression, and SVG optimization."', f'content="{t_data["desc"]}"')
                html = html.replace('30+ Free Tools Available', t_data["hero_pill"])
                html = html.replace('The Ultimate Toolkit for <br />\n            <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-fuchsia-500">Modern Web\n                Creators</span>', t_data["hero_title"])
                html = html.replace('Elevate your workflow with our premium suite of micro-tools. Generate CSS properties, optimize assets, and\n            design layouts faster than ever. 100% free, always fast.', t_data["hero_desc"])
                html = html.replace('Start Creating', t_data["start_btn"])
                html = html.replace('Bookmark (Ctrl+D)', t_data["bookmark_btn"])
                html = html.replace('Tool Directory', t_data["dir_title"])
                html = html.replace('Everything you need, directly in your browser.', t_data["dir_desc"])
                html = html.replace('CSS Generators', t_data["cat_css"])
                html = html.replace('Typography & Layout', t_data["cat_typo"])
                html = html.replace('Image & Assets', t_data["cat_img"])
                html = html.replace('Developer Utilities', t_data["cat_dev"])
                html = html.replace('Color & Utilities', t_data["cat_color"])
                
                # Grid Items
                html = html.replace('Gradient Gen', t_data["t_grad"]).replace('Create beautiful linear and radial CSS background\n                    gradients.', t_data["d_grad"]).replace('Create beautiful linear and radial CSS background gradients.', t_data["d_grad"])
                html = html.replace('CSS Triangle', t_data["t_tri"]).replace('Generate pure CSS triangles instantly for tooltips and\n                    arrows.', t_data["d_tri"]).replace('Generate pure CSS triangles instantly for tooltips and arrows.', t_data["d_tri"])
                html = html.replace('Glassmorphism', t_data["t_glass"]).replace('Generate perfect frosted glass UI components for your\n                    interfaces.', t_data["d_glass"]).replace('Generate perfect frosted glass UI components for your interfaces.', t_data["d_glass"])
                html = html.replace('Box Shadow', t_data["t_box"]).replace('Visually design layered drop shadows for depth and\n                    elevation.', t_data["d_box"]).replace('Visually design layered drop shadows for depth and elevation.', t_data["d_box"])
                html = html.replace('Border Radius', t_data["t_border"]).replace('Visualize and generate complex 8-point CSS border radius\n                    values.', t_data["d_border"]).replace('Visualize and generate complex 8-point CSS border radius values.', t_data["d_border"])
                html = html.replace('Snowfall Effect', t_data["t_snow"]).replace('Interactive CSS particle snow effect generator.', t_data["d_snow"])
                html = html.replace('Flexbox Playground', t_data["t_flex"]).replace('Master CSS Flexbox visually with interactive controls.', t_data["d_flex"])
                html = html.replace('CSS Grid Gen', t_data["t_grid"]).replace('Build complex CSS Grid layouts in seconds, drag layout\n                    grids visually.', t_data["d_grid"]).replace('Build complex CSS Grid layouts in seconds, drag layout grids visually.', t_data["d_grid"])
                html = html.replace('Font Pairing', t_data["t_font"]).replace('Discover and preview harmonious Google Font combinations.', t_data["d_font"])
                html = html.replace('Type Scale', t_data["t_type"]).replace('Generate modular perfect typography scales using\n                    mathematical ratios.', t_data["d_type"]).replace('Generate modular perfect typography scales using mathematical ratios.', t_data["d_type"])
                html = html.replace('Lorem Ipsum', t_data["t_lorem"]).replace('Generate placeholder text instantly with paragraph and\n                    word controls.', t_data["d_lorem"]).replace('Generate placeholder text instantly with paragraph and word controls.', t_data["d_lorem"])
                html = html.replace('Image Compressor', t_data["t_comp"]).replace('Reduce image file sizes instantly entirely within your\n                    browser.', t_data["d_comp"]).replace('Reduce image file sizes instantly entirely within your browser.', t_data["d_comp"])
                html = html.replace('Image Placeholder', t_data["t_place"]).replace('Create custom dummy images for wireframes and export to\n                    SVG or PNG.', t_data["d_place"]).replace('Create custom dummy images for wireframes and export to SVG or PNG.', t_data["d_place"])
                html = html.replace('Format Converter', t_data["t_form"]).replace('Convert between WebP, PNG, and JPG preserving\n                    transparency.', t_data["d_form"]).replace('Convert between WebP, PNG, and JPG preserving transparency.', t_data["d_form"])
                html = html.replace('Image Resizer', t_data["t_res"]).replace('Resize images accurately with aspect ratio constraints.', t_data["d_res"])
                html = html.replace('BG Remover', t_data["t_bg"]).replace('Remove image backgrounds instantly and privately using\n                    on-device AI.', t_data["d_bg"]).replace('Remove image backgrounds instantly and privately using on-device AI.', t_data["d_bg"])
                html = html.replace('Image Cropper', t_data["t_crop"]).replace('Crop images to specific aspect ratios or custom\n                    dimensions seamlessly.', t_data["d_crop"]).replace('Crop images to specific aspect ratios or custom dimensions seamlessly.', t_data["d_crop"])
                html = html.replace('Photo Filters', t_data["t_filter"]).replace('Apply Instagram-style filters and fine-tune image\n                    adjustments.', t_data["d_filter"]).replace('Apply Instagram-style filters and fine-tune image adjustments.', t_data["d_filter"])
                html = html.replace('Watermark Creator', t_data["t_water"]).replace('Protect your images by overlaying custom text or logo\n                    watermarks.', t_data["d_water"]).replace('Protect your images by overlaying custom text or logo watermarks.', t_data["d_water"])
                html = html.replace('Collage Maker', t_data["t_col"]).replace('Combine multiple photos into beautiful, customizable grid\n                    layouts.', t_data["d_col"]).replace('Combine multiple photos into beautiful, customizable grid layouts.', t_data["d_col"])
                html = html.replace('SVG Optimizer', t_data["t_opt"]).replace('Clean and shrink SVG markup for production environments.', t_data["d_opt"])
                html = html.replace('SVG Waves', t_data["t_wave"]).replace('Generate beautiful scalable section dividers and wave\n                    shapes.', t_data["d_wave"]).replace('Generate beautiful scalable section dividers and wave shapes.', t_data["d_wave"])
                html = html.replace('QR Code Gen', t_data["t_qr"]).replace('Create custom, high-resolution QR codes with logo\n                    embedding.', t_data["d_qr"]).replace('Create custom, high-resolution QR codes with logo embedding.', t_data["d_qr"])
                html = html.replace('Regex Tester', t_data["t_reg"]).replace('Test, debug, and understand Regular Expressions with\n                    real-time highlighting.', t_data["d_reg"]).replace('Test, debug, and understand Regular Expressions with real-time highlighting.', t_data["d_reg"])
                html = html.replace('JSON Formatter', t_data["t_json"]).replace('Beautify, validate, and minify JSON data securely in your\n                    browser.', t_data["d_json"]).replace('Beautify, validate, and minify JSON data securely in your browser.', t_data["d_json"])
                html = html.replace('Base64 Encoder', t_data["t_base"]).replace('Encode and decode text or files to Base64 format\n                    instantly.', t_data["d_base"]).replace('Encode and decode text or files to Base64 format instantly.', t_data["d_base"])
                html = html.replace('URL Encoder', t_data["t_url"]).replace('Safely encode your URLs or decode query parameters.', t_data["d_url"])
                html = html.replace('Color Palette', t_data["t_pal"]).replace('Extract and generate color combinations automatically.', t_data["d_pal"])
                html = html.replace('Contrast Checker', t_data["t_con"]).replace('Ensure accessibility by checking WCAG color contrast\n                    ratios.', t_data["d_con"]).replace('Ensure accessibility by checking WCAG color contrast ratios.', t_data["d_con"])
                html = html.replace('PX to REM', t_data["t_px"]).replace('Quickly convert pixel values to rem for scalable CSS.', t_data["d_px"])
                html = html.replace('Social Sizes List', t_data["t_soc"]).replace('Up-to-date reference sheet for all platform image\n                    dimensions.', t_data["d_soc"]).replace('Up-to-date reference sheet for all platform image dimensions.', t_data["d_soc"])

            # --- TOOLS TRANSLATIONS ---
            else:
                html = html.replace(f'<title>CSS Gradient Generator | StudioLimb</title>', f'<title>{t_data.get("title", "")}</title>')
                html = html.replace(f'<title>CSS Triangle Generator | StudioLimb</title>', f'<title>{t_data.get("title", "")}</title>')
                html = html.replace(f'<title>Glassmorphism CSS Generator | StudioLimb</title>', f'<title>{t_data.get("title", "")}</title>')
                html = html.replace(f'<title>CSS Box Shadow Generator | StudioLimb</title>', f'<title>{t_data.get("title", "")}</title>')
                html = html.replace(f'<title>CSS Border Radius Generator | StudioLimb</title>', f'<title>{t_data.get("title", "")}</title>')
                
                # Update meta descriptions
                html = re.sub(r'<meta name="description"\s+content="[^"]+">', f'<meta name="description" content="{t_data.get("desc", "")}">', html)

                # Find the main hero <h2> inside <header>
                html = re.sub(r'<h2[^>]*>.*?</h2>', f'<h2 class="text-4xl md:text-5xl font-bold tracking-tight mb-4 text-transparent bg-clip-text bg-gradient-to-r from-white to-slate-400">{t_data.get("h2", "")}</h2>', html, count=1, flags=re.DOTALL)
                
                # Find the main <p> right after <h2>
                html = re.sub(r'<p class="text-lg md:text-xl text-slate-400 max-w-2xl font-medium mx-auto">(.*?)</p>', f'<p class="text-lg md:text-xl text-slate-400 max-w-2xl font-medium mx-auto">{t_data.get("p", "")}</p>', html, count=1, flags=re.DOTALL)
                
                # Tool specific tags replace
                for eng_key, lang_key in [('Direction', 'direction'), ('Type', 'type'), ('Linear', 'linear'), ('Radial', 'radial'), 
                                        ('Colors', 'colors'), ('Add Color', 'add_color'), ('Output', 'output'), ('Copy', 'copy'),
                                        ('Size', 'size'), ('Close Width', 'width'), ('Close Height', 'height'), ('Color', 'color'),
                                        ('Blur', 'blur'), ('Transparency', 'transparency'), ('Light Outline', 'outline'), ('Background', 'bg_color'),
                                        ('Layer', 'layer'), ('Inset', 'inset'), ('X-Offset', 'x_offset'), ('Y-Offset', 'y_offset'), 
                                        ('Spread', 'spread'), ('Add Shadow Layer', 'add_layer'), ('Top Left', 'tl'), ('Top Right', 'tr'), ('Bottom Right', 'br'), ('Bottom Left', 'bl')]:
                    if lang_key in t_data:
                        # Make sure to not replace generic text incorrectly. Do exact tag content replacements if possible.
                         html = html.replace(f'>{eng_key}<', f'>{t_data[lang_key]}<')
                         html = html.replace(f'="{eng_key}"', f'="{t_data[lang_key]}"')
                         html = html.replace(f' {eng_key} ', f' {t_data[lang_key]} ')
                         html = html.replace(f'>{eng_key}:', f'>{t_data[lang_key]}:')


            # Fix relative links inside the subfolder explicitly for logos and sw.js
            html = html.replace('href="index.html" class="flex items-center gap-3', 'href="index.html" class="flex items-center gap-3')
            html = html.replace("navigator.serviceWorker.register('/sw.js')", "navigator.serviceWorker.register('../sw.js')")
            html = html.replace('href="/manifest.json"', 'href="../manifest.json"')
            html = html.replace('href="/icons/icon-192x192.png"', 'href="../icons/icon-192x192.png"')

            # Path fixes specific to tools linking back to CSS/JS if any (not present here mostly tailwind CDN is used)
            # The logo link specifically needs to step out if inside a subfolder tool, BUT for our implementation we want localization to keep users in the same lang folder.
            # So <a href="index.html"> is PERFECT because in `/es/tool.html` it will go to `/es/index.html`.

            os.makedirs(os.path.join(base_dir, code), exist_ok=True)
            with open(os.path.join(base_dir, code, f), 'w', encoding='utf-8') as out:
                out.write(html)

if __name__ == '__main__':
    process_translation()
    print("Batch 1 Translation Complete!")
