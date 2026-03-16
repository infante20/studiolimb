import os
import re

base_dir = './'
tools_to_translate = [
    'type-scale-generator.html', 
    'lorem-ipsum-generator.html', 
    'lorem-ipsum-premier.html', 
    'json-formatter.html', 
    'base64-encode-decode.html'
]

translations = {
    'es': {
        'lang': 'es',
        'btn_flag': '<span class="lang-flag">🇪🇸</span> ES',
        'type-scale-generator.html': {
            'title': 'StudioLimb | Type Scale Premier',
            'desc': 'Generador de escala tipográfica para ritmos armónicos y rems responsivos.',
            'h1': 'Escala Tipográfica', 'p': 'Herramienta Premier', 'Base Size': 'Tamaño Base',
            'Scale': 'Escala', 'Preview': 'Previa', 'Minor Second': 'Segunda Menor', 'Major Second': 'Segunda Mayor',
            'Minor Third': 'Tercera Menor', 'Major Third': 'Tercera Mayor', 'Perfect Fourth': 'Cuarta Justa',
            'Augmented Fourth': 'Cuarta Aumentada', 'Perfect Fifth': 'Quinta Justa', 'Golden Ratio': 'Proporción Áurea',
            'Code Export Output': 'Exportar Código', 'Copied!': '¡Copiado!'
        },
        'lorem-ipsum-generator.html': {
            'title': 'Lorem Ipsum Premier — StudioLimb',
            'desc': 'Generador premium de texto de prueba para diseñadores.',
            'h1': 'Lorem Ipsum Premier', 'p': 'Generador de texto visual.', 'Structure': 'Estructura',
            'Quantity': 'Cantidad', 'Vocabulary Style': 'Estilo de Vocabulario', 'Regenerate Feed': 'Generar Texto',
            'Isolated Words': 'Palabras Sueltas', 'Draft Sentences': 'Oraciones Breves', 'Full Paragraphs': 'Párrafos Completos',
            'HTML Tags Mode': 'Modo Etiquetas HTML', 'Copy All Content': 'Copiar Todo', 'Export File': 'Exportar Archivo',
            'Copied to clipboard!': '¡Copiado al portapapeles!'
        },
        'lorem-ipsum-premier.html': {
            'title': 'Lorem Ipsum Premier — StudioLimb',
            'desc': 'Generador premium de texto de prueba para diseñadores.',
            'h1': 'Lorem Ipsum Premier', 'p': 'Generador de texto visual.', 'Structure': 'Estructura',
            'Quantity': 'Cantidad', 'Vocabulary Style': 'Estilo de Vocabulario', 'Regenerate Feed': 'Generar Texto',
            'Isolated Words': 'Palabras Sueltas', 'Draft Sentences': 'Oraciones Breves', 'Full Paragraphs': 'Párrafos Completos',
            'HTML Tags Mode': 'Modo Etiquetas HTML', 'Copy All Content': 'Copiar Todo', 'Export File': 'Exportar Archivo',
            'Copied to clipboard!': '¡Copiado al portapapeles!'
        },
        'json-formatter.html': {
            'title': 'Formateador JSON | StudioLimb',
            'desc': 'Formateador, validador y minificador JSON online gratuito.',
            'h1': 'Formateador JSON', 'p': 'Validador JSON', 'Clear': 'Limpiar', 'Paste': 'Pegar',
            'Indent:': 'Sangría:', '2 Spaces': '2 Espacios', '4 Spaces': '4 Espacios', 'Tab': 'Tabulador',
            'Minify': 'Minificar', 'Format': 'Formatear'
        },
        'base64-encode-decode.html': {
            'title': 'Codificador Base64 | StudioLimb',
            'desc': 'Codifica y decodifica Base64 instantáneamente en tu navegador.',
            'h1': 'Codificador Base64', 'p': 'Herramienta Segura', 'Encode': 'Codificar', 'Decode': 'Decodificar',
            'Upload File': 'Subir Archivo', 'Clear': 'Limpiar', 'Copy text to clipboard': 'Copiar texto',
            'Remove': 'Quitar'
        }
    },
    'fr': {
        'lang': 'fr',
        'btn_flag': '<span class="lang-flag">🇫🇷</span> FR',
        'type-scale-generator.html': {
            'title': 'Échelle Typographique | StudioLimb',
            'desc': 'Générateur d\'échelle typographique pour des rythmes harmonieux.',
            'h1': 'Échelle Typo.', 'p': 'Outil Premier', 'Base Size': 'Taille Base',
            'Scale': 'Échelle', 'Preview': 'Aperçu', 'Minor Second': 'Seconde mineure', 'Major Second': 'Seconde majeure',
            'Minor Third': 'Tierce mineure', 'Major Third': 'Tierce majeure', 'Perfect Fourth': 'Quarte juste',
            'Augmented Fourth': 'Quarte augmentée', 'Perfect Fifth': 'Quinte juste', 'Golden Ratio': 'Nombre d\'or',
            'Code Export Output': 'Export CSS', 'Copied!': 'Copié !'
        },
        'lorem-ipsum-generator.html': {
            'title': 'Lorem Ipsum Premier — StudioLimb',
            'desc': 'Générateur premium de texte factice.',
            'h1': 'Lorem Ipsum Premier', 'p': 'Générateur texte.', 'Structure': 'Structure',
            'Quantity': 'Quantité', 'Vocabulary Style': 'Style du Texte', 'Regenerate Feed': 'Générer Texte',
            'Isolated Words': 'Mots Isolés', 'Draft Sentences': 'Phrases Courtes', 'Full Paragraphs': 'Paragraphes Entiers',
            'HTML Tags Mode': 'Mode Balises HTML', 'Copy All Content': 'Tout Copier', 'Export File': 'Exporter Fichier',
            'Copied to clipboard!': 'Copié dans le presse-papiers !'
        },
        'lorem-ipsum-premier.html': {
            'title': 'Lorem Ipsum Premier — StudioLimb',
            'desc': 'Générateur premium de texte factice.',
            'h1': 'Lorem Ipsum Premier', 'p': 'Générateur texte.', 'Structure': 'Structure',
            'Quantity': 'Quantité', 'Vocabulary Style': 'Style du Texte', 'Regenerate Feed': 'Générer Texte',
            'Isolated Words': 'Mots Isolés', 'Draft Sentences': 'Phrases Courtes', 'Full Paragraphs': 'Paragraphes Entiers',
            'HTML Tags Mode': 'Mode Balises HTML', 'Copy All Content': 'Tout Copier', 'Export File': 'Exporter Fichier',
            'Copied to clipboard!': 'Copié !'
        },
        'json-formatter.html': {
            'title': 'Outil Formatage JSON | StudioLimb',
            'desc': 'Outil gratuit de formatage, de validation et de minification JSON en ligne.',
            'h1': 'Formateur JSON', 'p': 'Validateur JSON', 'Clear': 'Effacer', 'Paste': 'Coller',
            'Indent:': 'Retrait :', '2 Spaces': '2 Espaces', '4 Spaces': '4 Espaces', 'Tab': 'Tabulation',
            'Minify': 'Minifier', 'Format': 'Formater'
        },
        'base64-encode-decode.html': {
            'title': 'Encodeur Base64 | StudioLimb',
            'desc': 'Encodez et décodez instantanément en Base64 dans votre navigateur.',
            'h1': 'Encodeur Base64', 'p': 'Outil Sécurisé', 'Encode': 'Encoder', 'Decode': 'Décoder',
            'Upload File': 'Fichier', 'Clear': 'Effacer', 'Copy text to clipboard': 'Copier texte',
            'Remove': 'Retirer'
        }
    },
    'hi': {
        'lang': 'hi',
        'btn_flag': '<span class="lang-flag">🇮🇳</span> HI',
        'type-scale-generator.html': {
            'title': 'टाइप स्केल | StudioLimb',
            'desc': 'सामंजस्यपूर्ण लय के लिए टाइपोग्राफी स्केल जनरेटर।',
            'h1': 'टाइप स्केल', 'p': 'टाइपोग्राफी टूल', 'Base Size': 'आधार आकार',
            'Scale': 'पैमाना', 'Preview': 'पूर्वावलोकन', 'Minor Second': 'माइनर सेकंड', 'Major Second': 'मेजर सेकंड',
            'Minor Third': 'माइनर थर्ड', 'Major Third': 'मेजर थर्ड', 'Perfect Fourth': 'पर्फेक्ट फोर्थ',
            'Augmented Fourth': 'ऑग्मेंटेड फोर्थ', 'Perfect Fifth': 'पर्फेक्ट फिफ्थ', 'Golden Ratio': 'गोल्डन रेशियो',
            'Code Export Output': 'कोड निर्यात करें', 'Copied!': 'कॉपी किया गया!'
        },
        'lorem-ipsum-generator.html': {
            'title': 'लोरेम इप्सम जनरेटर | StudioLimb',
            'desc': 'डिजाइनरों के लिए प्रीमियम लोरेम इप्सम जनरेटर।',
            'h1': 'लोरेम इप्सम', 'p': 'टेक्स्ट जनरेटर।', 'Structure': 'संरचना',
            'Quantity': 'मात्रा', 'Vocabulary Style': 'शब्दावली शैली', 'Regenerate Feed': 'उत्पन्न करें',
            'Isolated Words': 'अलग शब्द', 'Draft Sentences': 'वाक्य', 'Full Paragraphs': 'अनुच्छेद',
            'HTML Tags Mode': 'HTML टैग', 'Copy All Content': 'सभी कॉपी करें', 'Export File': 'फ़ाइल निर्यात करें',
            'Copied to clipboard!': 'क्लिपबोर्ड पर कॉपी किया गया!'
        },
        'lorem-ipsum-premier.html': {
            'title': 'लोरेम इप्सम जनरेटर | StudioLimb',
            'desc': 'डिजाइनरों के लिए प्रीमियम लोरेम इप्सम जनरेटर।',
            'h1': 'लोरेम इप्सम', 'p': 'टेक्स्ट जनरेटर।', 'Structure': 'संरचना',
            'Quantity': 'मात्रा', 'Vocabulary Style': 'शब्दावली शैली', 'Regenerate Feed': 'उत्पन्न करें',
            'Isolated Words': 'अलग शब्द', 'Draft Sentences': 'वाक्य', 'Full Paragraphs': 'अनुच्छेद',
            'HTML Tags Mode': 'HTML टैग', 'Copy All Content': 'सभी कॉपी करें', 'Export File': 'फ़ाइल निर्यात करें',
            'Copied to clipboard!': 'क्लिपबोर्ड पर कॉपी किया गया!'
        },
        'json-formatter.html': {
            'title': 'JSON फ़ॉर्मेटर | StudioLimb',
            'desc': 'मुफ़्त ऑनलाइन JSON फ़ॉर्मेटर और वैलिडेटर।',
            'h1': 'JSON फ़ॉर्मेटर', 'p': 'JSON वैलिडेटर', 'Clear': 'साफ़ करें', 'Paste': 'चिपकाएं',
            'Indent:': 'इंडेंट:', '2 Spaces': '2 स्पेस', '4 Spaces': '4 स्पेस', 'Tab': 'टैब',
            'Minify': 'छोटा करें', 'Format': 'प्रारूप'
        },
        'base64-encode-decode.html': {
            'title': 'Base64 एनकोड और डिकोड | StudioLimb',
            'desc': 'Base64 एनकोड और डिकोड करें।',
            'h1': 'Base64 कनवर्टर', 'p': 'सुरक्षित उपकरण', 'Encode': 'एनकोड', 'Decode': 'डिकोड',
            'Upload File': 'फ़ाइल अपलोड', 'Clear': 'साफ़ करें', 'Copy text to clipboard': 'टेक्स्ट कॉपी करें',
            'Remove': 'हटाएं'
        }
    },
    'pt': {
        'lang': 'pt',
        'btn_flag': '<span class="lang-flag">🇧🇷</span> PT',
        'type-scale-generator.html': {
            'title': 'Escala Tipográfica | StudioLimb',
            'desc': 'Gerador de escala tipográfica para ritmos adequados.',
            'h1': 'Escala de Tipo', 'p': 'Visualizador', 'Base Size': 'Tam. Base',
            'Scale': 'Escala', 'Preview': 'Visualização', 'Minor Second': 'Segunda menor', 'Major Second': 'Segunda maior',
            'Minor Third': 'Terça menor', 'Major Third': 'Terça maior', 'Perfect Fourth': 'Quarta justa',
            'Augmented Fourth': 'Quarta aumentada', 'Perfect Fifth': 'Quinta justa', 'Golden Ratio': 'Aurea',
            'Code Export Output': 'Exportar Código', 'Copied!': 'Copiado!'
        },
        'lorem-ipsum-generator.html': {
            'title': 'Lorem Ipsum Premier — StudioLimb',
            'desc': 'Gerador premium de lorem ipsum.',
            'h1': 'Lorem Ipsum Premier', 'p': 'Gerador de texto.', 'Structure': 'Estrutura',
            'Quantity': 'Quantidade', 'Vocabulary Style': 'Estilo de Palavras', 'Regenerate Feed': 'Gerar Texto',
            'Isolated Words': 'Palavras', 'Draft Sentences': 'Frases', 'Full Paragraphs': 'Parágrafos',
            'HTML Tags Mode': 'Modo HTML', 'Copy All Content': 'Copiar Tudo', 'Export File': 'Exportar Arquivo',
            'Copied to clipboard!': 'Copiado para a área de transferência!'
        },
        'lorem-ipsum-premier.html': {
            'title': 'Lorem Ipsum Premier — StudioLimb',
            'desc': 'Gerador premium de lorem ipsum.',
            'h1': 'Lorem Ipsum Premier', 'p': 'Gerador de texto.', 'Structure': 'Estrutura',
            'Quantity': 'Quantidade', 'Vocabulary Style': 'Estilo de Palavras', 'Regenerate Feed': 'Gerar Texto',
            'Isolated Words': 'Palavras', 'Draft Sentences': 'Frases', 'Full Paragraphs': 'Parágrafos',
            'HTML Tags Mode': 'Modo HTML', 'Copy All Content': 'Copiar Tudo', 'Export File': 'Exportar Arquivo',
            'Copied to clipboard!': 'Copiado!'
        },
        'json-formatter.html': {
            'title': 'Formatador JSON | StudioLimb',
            'desc': 'Formatador de JSON gratuito.',
            'h1': 'Formatador JSON', 'p': 'Validador JSON', 'Clear': 'Limpar', 'Paste': 'Colar',
            'Indent:': 'Recuo:', '2 Spaces': '2 Espaços', '4 Spaces': '4 Espaços', 'Tab': 'Tabulação',
            'Minify': 'Minificar', 'Format': 'Formatar'
        },
        'base64-encode-decode.html': {
            'title': 'Base64 | StudioLimb',
            'desc': 'Codifique e decodifique em Base64.',
            'h1': 'Conversor Base64', 'p': 'Ferramenta Online', 'Encode': 'Codificar', 'Decode': 'Decodificar',
            'Upload File': 'Arquivo', 'Clear': 'Limpar', 'Copy text to clipboard': 'Copiar texto',
            'Remove': 'Remover'
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

            # Some files use h1 tags, some have h1 inside <h1> directly (lorem ipsum)
            if 'h1' in t_data:
                html = re.sub(r'<h1 class="text-xl font-bold mb-1">.*?</h1>', f'<h1 class="text-xl font-bold mb-1">{t_data["h1"]}</h1>', html)
                html = re.sub(r'<h1>.*?</h1>', f'<h1>{t_data["h1"]}</h1>', html)
            
            # Lorem ipsum specific replacements
            if 'p' in t_data and 'lorem-ipsum' in f:
                html = re.sub(r'<p>Visual content generator for specialists.</p>', f'<p>{t_data["p"]}</p>', html)

            for eng, k in t_data.items():
                if eng not in ['lang', 'btn_flag', 'title', 'desc', 'h1', 'p']:
                    html = html.replace(f'>{eng}<', f'>{k}<')
                    html = html.replace(f'{eng}</span>', f'{k}</span>')
                    html = html.replace(f'{eng}</label>', f'{k}</label>')
                    html = html.replace(f'"{eng}"', f'"{k}"')
                    if eng in ['Regenerate Feed', 'Copy All Content', 'Export File', 'Minify', 'Format', 'Encode', 'Decode']:
                        html = html.replace(f'{eng}', f'{k}')
                        # Revert generic matching issues
                        html = html.replace('100% free', '100% free') # placeholder
            
            if 'Copied!' in t_data:
                 html = html.replace('check</span> Copied!', f'check</span> {t_data["Copied!"]}')

            html = html.replace('href="index.html" class="flex flex-col', 'href="../index.html" class="flex flex-col')
            html = html.replace("navigator.serviceWorker.register('/sw.js')", "navigator.serviceWorker.register('../sw.js')")
            html = html.replace('href="/manifest.json"', 'href="../manifest.json"')
            html = html.replace('href="/icons/icon-192x192.png"', 'href="../icons/icon-192x192.png"')
            html = html.replace('href="index.html" class="flex items-center gap-3', 'href="index.html" class="flex items-center gap-3')
            html = html.replace('href="index.html" class="hover:text-white transition-colors"', 'href="../index.html" class="hover:text-white transition-colors"') # JSON Formatter

            os.makedirs(os.path.join(base_dir, code), exist_ok=True)
            with open(os.path.join(base_dir, code, f), 'w', encoding='utf-8') as out:
                out.write(html)

if __name__ == '__main__':
    process_translation()
    print("Batch 5 Translation Complete!")
