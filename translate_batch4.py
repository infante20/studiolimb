import os
import re

base_dir = './'
tools_to_translate = [
    'collage-maker.html', 
    'color-palette-generator.html', 
    'contrast-checker.html', 
    'font-pairing.html', 
    'px-rem-converter.html'
]

translations = {
    'es': {
        'lang': 'es',
        'btn_flag': '<span class="lang-flag">🇪🇸</span> ES',
        'collage-maker.html': {
            'title': 'StudioLimb | Creador de Collages de Fotos',
            'desc': 'Combina múltiples fotos en hermosos layouts de cuadrículas configurables.',
            'h1': 'Photo Collage', 'p': 'Herramienta Creadora', 'Export Image': 'Exportar Imagen',
            'Grid': 'Cuadrícula', 'Overall': 'General', 'Border': 'Bordes', 'Thickness (Spacing)': 'Grosor (Espaciado)',
            'Corner Radius': 'Radio de Borde', 'Border Color': 'Color del Borde'
        },
        'color-palette-generator.html': {
            'title': 'StudioLimb | Palette Gen Premier',
            'desc': 'Generador de paletas de colores profesionales. Encuentra tu esquema perfecto.',
            'h1': 'Color Palette Gen', 'p': 'Diseñador Visual', 'Generate': 'Generar Paleta',
            'Randomized': 'Aleatorio', 'Analogous': 'Análogo', 'Monochromatic': 'Monocromático',
            'Triadic': 'Triádico', 'Complementary': 'Complementario', 'Shades': 'Sombras',
            'Modern UI Preview': 'Previsualización de UI', 'Action Button': 'Botón de Acción', 'Color copied!': '¡Color Copiado!'
        },
        'contrast-checker.html': {
            'title': 'StudioLimb | Comprobador de Contraste',
            'desc': 'Asegura la accesibilidad con analizador de contraste WCAG en tiempo real.',
            'h1': 'Contrast Checker', 'p': 'Accesibilidad Web', 'Text': 'Texto', 'Background': 'Fondo',
            'Fail': 'No Pasa', 'Pass': 'Pasa', 'Great': 'Excelente'
        },
        'font-pairing.html': {
            'title': 'StudioLimb | Combinaciones de Fuentes',
            'desc': 'Descubre combinaciones de Google Fonts listas para usar.',
            'h1': 'Font Pairing', 'p': 'Tipografías Modernas', 'Generate Pairing': 'Generar Combinación',
            'Heading Font': 'Fuente de Título', 'Body Font': 'Fuente de Texto'
        },
        'px-rem-converter.html': {
            'title': 'StudioLimb | Conversor PX a REM',
            'desc': 'Convierte valores px a rem al instante para hojas de estilo responsivas.',
            'h1': 'PX &harr; REM Converter', 'p': 'Conversión Instantánea',
            'Pixels (px)': 'Píxeles (px)', 'Root font-size': 'Tamaño Base (HTML)', 'Swap Directions': 'Invertir',
            'Copy Value': 'Copiar Valor', 'Copied!': '¡Copiado!'
        }
    },
    'fr': {
        'lang': 'fr',
        'btn_flag': '<span class="lang-flag">🇫🇷</span> FR',
        'collage-maker.html': {
            'title': 'Créateur de Collages | StudioLimb',
            'desc': 'Combinez plusieurs photos en de superbes grilles personnalisables.',
            'h1': 'Photo Collage', 'p': 'Outil de Création', 'Export Image': 'Exporter l\'Image',
            'Grid': 'Grille', 'Overall': 'Global', 'Border': 'Bordure', 'Thickness (Spacing)': 'Épaisseur',
            'Corner Radius': 'Rayon de Bordure', 'Border Color': 'Couleur Bordure'
        },
        'color-palette-generator.html': {
            'title': 'Générateur de Palette | StudioLimb',
            'desc': 'Générateur professionnel de palettes de couleurs web.',
            'h1': 'Color Palette Gen', 'p': 'Designer Visuel', 'Generate': 'Générer Palette',
            'Randomized': 'Aléatoire', 'Analogous': 'Analogue', 'Monochromatic': 'Monochromatique',
            'Triadic': 'Triadique', 'Complementary': 'Complémentaire', 'Shades': 'Nuances',
            'Modern UI Preview': 'Aperçu UI Moderne', 'Action Button': 'Bouton d\'Action', 'Color copied!': 'Couleur Copiée !'
        },
        'contrast-checker.html': {
            'title': 'Vérificateur. Contraste | StudioLimb',
            'desc': 'Assurez l\'accessibilité avec l\'analyseur de contraste WCAG en temps réel.',
            'h1': 'Contrast Checker', 'p': 'Outil d\'Accessibilité', 'Text': 'Texte', 'Background': 'Fond',
            'Fail': 'Échec', 'Pass': 'Passable', 'Great': 'Excellent'
        },
        'font-pairing.html': {
            'title': 'Combinaisons de Polices | StudioLimb',
            'desc': 'Découvrez des combinaisons de polices Google prêtes à l\'emploi.',
            'h1': 'Font Pairing', 'p': 'Typographie Moderne', 'Generate Pairing': 'Générer Combinaison',
            'Heading Font': 'Police de Titre', 'Body Font': 'Police de Corps'
        },
        'px-rem-converter.html': {
            'title': 'Convertisseur PX ↔ REM | StudioLimb',
            'desc': 'Convertissez instantanément des pixels en rem pour des CSS évolutives.',
            'h1': 'PX &harr; REM Converter', 'p': 'Conversion Instantanée',
            'Pixels (px)': 'Pixels (px)', 'Root font-size': 'Taille Base (HTML)', 'Swap Directions': 'Inverser',
            'Copy Value': 'Copier la Valeur', 'Copied!': 'Copié !'
        }
    },
    'hi': {
        'lang': 'hi',
        'btn_flag': '<span class="lang-flag">🇮🇳</span> HI',
        'collage-maker.html': {
            'title': 'कोलाज निर्माता | StudioLimb',
            'desc': 'सैकड़ों तस्वीरों को सुंदर ग्रिड लेआउट में संयोजित करें।',
            'h1': 'Photo Collage', 'p': 'सृजन उपकरण', 'Export Image': 'छवि निर्यात करें',
            'Grid': 'ग्रिड', 'Overall': 'समग्र', 'Border': 'सीमा', 'Thickness (Spacing)': 'मोटाई (अंतराल)',
            'Corner Radius': 'कोने की त्रिज्या', 'Border Color': 'सीमा का रंग'
        },
        'color-palette-generator.html': {
            'title': 'रंग पैलेट जनरेटर | StudioLimb',
            'desc': 'वेब और डिजाइन के लिए पेशेवर रंग पैलेट जनरेटर।',
            'h1': 'Color Palette Gen', 'p': 'विजुअल डिजाइनर', 'Generate': 'उत्पन्न करें',
            'Randomized': 'यादृच्छिक', 'Analogous': 'अनुरूप', 'Monochromatic': 'मोनोक्रोमैटिक',
            'Triadic': 'त्रिकोणीय', 'Complementary': 'पूरक', 'Shades': 'शेड्स',
            'Modern UI Preview': 'आधुनिक UI पूर्वावलोकन', 'Action Button': 'कार्य बटन', 'Color copied!': 'रंग कॉपी किया गया!'
        },
        'contrast-checker.html': {
            'title': 'कंट्रास्ट चेकर | StudioLimb',
            'desc': 'WCAG रंग विपरीत अनुपातों की जाँच करके पहुँच सुनिश्चित करें।',
            'h1': 'Contrast Checker', 'p': 'पहुँच उपकरण', 'Text': 'पाठ', 'Background': 'पृष्ठभूमि',
            'Fail': 'विफल', 'Pass': 'उत्तीर्ण', 'Great': 'महान'
        },
        'font-pairing.html': {
            'title': 'फ़ॉन्ट पेयरिंग | StudioLimb',
            'desc': 'Google फ़ॉन्ट संयोजनों की खोज और पूर्वावलोकन करें।',
            'h1': 'Font Pairing', 'p': 'आधुनिक टाइपोग्राफी', 'Generate Pairing': 'जोड़ी जनरेट करें',
            'Heading Font': 'हेडिंग फ़ॉन्ट', 'Body Font': 'मुख्य फ़ॉन्ट'
        },
        'px-rem-converter.html': {
            'title': 'PX ↔ REM कनवर्टर | StudioLimb',
            'desc': 'तेजी से पिक्सेल मानों को रेम ें बदलें।',
            'h1': 'PX &harr; REM Converter', 'p': 'त्वरित रूपांतरण',
            'Pixels (px)': 'पिक्सेल (px)', 'Root font-size': 'मूल फ़ॉन्ट आकार', 'Swap Directions': 'दिशा बदलें',
            'Copy Value': 'मूल्य कॉपी करें', 'Copied!': 'कॉपी किया गया!'
        }
    },
    'pt': {
        'lang': 'pt',
        'btn_flag': '<span class="lang-flag">🇧🇷</span> PT',
        'collage-maker.html': {
            'title': 'StudioLimb | Criador de Colagens',
            'desc': 'Combine várias fotos em belos layouts de grade personalizáveis.',
            'h1': 'Photo Collage', 'p': 'Ferramenta Criadora', 'Export Image': 'Exportar Imagem',
            'Grid': 'Grade', 'Overall': 'Geral', 'Border': 'Bordas', 'Thickness (Spacing)': 'Espessura (Espaçamento)',
            'Corner Radius': 'Raio da Borda', 'Border Color': 'Cor da Borda'
        },
        'color-palette-generator.html': {
            'title': 'Gerador de Paleta | StudioLimb',
            'desc': 'Gerador de paletas de cores para design profissional.',
            'h1': 'Color Palette Gen', 'p': 'Designer Visual', 'Generate': 'Gerar Paleta',
            'Randomized': 'Aleatório', 'Analogous': 'Análogo', 'Monochromatic': 'Monocromático',
            'Triadic': 'Triádico', 'Complementary': 'Complementar', 'Shades': 'Sombras',
            'Modern UI Preview': 'Pré-visualização de UI', 'Action Button': 'Botão de Ação', 'Color copied!': 'Cor copiada!'
        },
        'contrast-checker.html': {
            'title': 'Verificar Contraste | StudioLimb',
            'desc': 'Garanta a acessibilidade verificando os níveis de contraste WCAG.',
            'h1': 'Contrast Checker', 'p': 'Acessibilidade Web', 'Text': 'Texto', 'Background': 'Fundo',
            'Fail': 'Falha', 'Pass': 'Passou', 'Great': 'Excelente'
        },
        'font-pairing.html': {
            'title': 'Combinação de Fontes | StudioLimb',
            'desc': 'Combine de maneira harmoniosa pacotes de fontes do Google na web.',
            'h1': 'Font Pairing', 'p': 'Tipografia Moderna', 'Generate Pairing': 'Gerar Combinação',
            'Heading Font': 'Fonte do Título', 'Body Font': 'Fonte do Texto'
        },
        'px-rem-converter.html': {
            'title': 'Conversor PX ↔ REM | StudioLimb',
            'desc': 'Converta instantaneamente pixels em rem para folhas de estilo flexíveis.',
            'h1': 'PX &harr; REM Converter', 'p': 'Conversão Instantânea',
            'Pixels (px)': 'Pixels (px)', 'Root font-size': 'Tam. Base (HTML)', 'Swap Directions': 'Inverter',
            'Copy Value': 'Copiar Valor', 'Copied!': 'Copiado!'
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
            dropdown_pattern = re.compile(r'<div class="lang-selector">.*?</div>\s*</div>', re.DOTALL)
            html = dropdown_pattern.sub(build_dropdown(code, f), html)

            html = re.sub(r'<title>.*?</title>', f'<title>{t_data.get("title", "")}</title>', html)
            html = re.sub(r'<meta name="description"\s+content="[^"]+">', f'<meta name="description" content="{t_data.get("desc", "")}">', html)

            if 'h1' in t_data:
                html = re.sub(r'<h1 class="text-xl font-bold">.*?</h1>', f'<h1 class="text-xl font-bold">{t_data["h1"]}</h1>', html)
            if 'p' in t_data:
                html = re.sub(r'<p class="text-sm font-medium text-slate-400">.*?</p>', f'<p class="text-sm font-medium text-slate-400">{t_data["p"]}</p>', html)

            for eng, k in t_data.items():
                if eng not in ['lang', 'btn_flag', 'title', 'desc', 'h1', 'p']:
                    html = html.replace(f'>{eng}<', f'>{k}<')
                    html = html.replace(f'{eng}</span>', f'{k}</span>')
                    html = html.replace(f'{eng}</label>', f'{k}</label>')
                    html = html.replace(f'"{eng}"', f'"{k}"')
                    if eng in ['Export Image', 'Generate', 'Copy Value', 'Generate Pairing']:
                        html = html.replace(f'{eng}', f'{k}')
                        # Revert generic matching issues
                        html = html.replace('100% free', '100% free') # placeholder
            
            # Specific elements replacement for Contrast Checker and PX Converter
            if f == 'px-rem-converter.html':
                 html = html.replace('>PX &harr; REM Converter<', f'>{t_data["h1"]}<')

            html = html.replace('href="index.html" class="flex flex-col', 'href="../index.html" class="flex flex-col')
            html = html.replace("navigator.serviceWorker.register('/sw.js')", "navigator.serviceWorker.register('../sw.js')")
            html = html.replace('href="/manifest.json"', 'href="../manifest.json"')
            html = html.replace('href="/icons/icon-192x192.png"', 'href="../icons/icon-192x192.png"')
            html = html.replace('href="index.html" class="flex items-center gap-3', 'href="index.html" class="flex items-center gap-3')

            os.makedirs(os.path.join(base_dir, code), exist_ok=True)
            with open(os.path.join(base_dir, code, f), 'w', encoding='utf-8') as out:
                out.write(html)

if __name__ == '__main__':
    process_translation()
    print("Batch 4 Translation Complete!")
