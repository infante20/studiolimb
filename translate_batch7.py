import os
import re

base_dir = './'
tools_to_translate = [
    'url-encode-decode.html', 
    'qr-code-generator.html', 
    'snowfall-generator.html', 
    'snowfall-premier.html'
]

translations = {
    'es': {
        'lang': 'es',
        'btn_flag': '<span class="lang-flag">🇪🇸</span> ES',
        'url-encode-decode.html': {
            'title': 'URL Encoder & Decoder | StudioLimb',
            'desc': 'Codificador y decodificador de URL online. Procesa tus parámetros de manera segura.',
            'h1': 'URL Encoder / Decoder', 'p': 'Herramienta Segura', 'Clear': 'Limpiar',
            'Text to Encode': 'Texto a Codificar', 'URL Encoded Output': 'Salida Codificada',
            'URL Encoded Input': 'Entrada Codificada', 'Decoded Plain Text': 'Texto Plano Decodificado',
            'Result will appear here...': 'El resultado aparecerá aquí...'
        },
        'qr-code-generator.html': {
            'title': 'StudioLimb | Generador QR Premier',
            'desc': 'Genera códigos QR personalizados de alta calidad al instante.',
            'h1': 'QR Code Generator', 'p': 'Generador de Imágenes', 'Link or Data': 'Enlace o Datos',
            'Colors &': 'Colores y', 'Data Blocks': 'Bloques de Datos', 'Background': 'Fondo',
            'Raster': 'Formato', 'Download QR': 'Descargar QR'
        },
        'snowfall-generator.html': {
            'title': 'StudioLimb | Efecto Nieve Premier',
            'desc': 'Generador avanzado de copos de nieve (snowfall effect) en CSS/JS.',
            'h1': 'Snowfall Gen', 'p': 'Generador Visual', 'Organic Particles': 'Partículas Orgánicas',
            'Count': 'Cantidad', 'Fall Speed': 'Velocidad Caída', 'Flake Size': 'Tamaño',
            'Wind Drift': 'Efecto Viento', 'Export': 'Exportar'
        },
        'snowfall-premier.html': {
            'title': 'StudioLimb | Efecto Nieve Premier',
            'desc': 'Generador avanzado de copos de nieve (snowfall effect) en CSS/JS.',
            'h1': 'Snowfall Gen', 'p': 'Generador Visual', 'Organic Particles': 'Partículas Orgánicas',
            'Count': 'Cantidad', 'Fall Speed': 'Velocidad Caída', 'Flake Size': 'Tamaño',
            'Wind Drift': 'Efecto Viento', 'Export': 'Exportar'
        }
    },
    'fr': {
        'lang': 'fr',
        'btn_flag': '<span class="lang-flag">🇫🇷</span> FR',
        'url-encode-decode.html': {
            'title': 'URL Encodeur / Decodeur | StudioLimb',
            'desc': 'Encodeur et décodeur d\'URL en ligne.',
            'h1': 'URL Encoder / Decoder', 'p': 'Outil Sécurisé', 'Clear': 'Effacer',
            'Text to Encode': 'Texte à Encoder', 'URL Encoded Output': 'Sortie Encodée',
            'URL Encoded Input': 'Entrée Encodée', 'Decoded Plain Text': 'Texte Décodé',
            'Result will appear here...': 'Le résultat apparaîtra ici...'
        },
        'qr-code-generator.html': {
            'title': 'Générateur Code QR | StudioLimb',
            'desc': 'Générez des codes QR de haute qualité personnalisés.',
            'h1': 'QR Code Generator', 'p': 'Générateur d\'Images', 'Link or Data': 'Lien ou Données',
            'Colors &': 'Couleurs &', 'Data Blocks': 'Blocs', 'Background': 'Fond',
            'Raster': 'Format', 'Download QR': 'Télécharger QR'
        },
        'snowfall-generator.html': {
            'title': 'Générateur de Neige | StudioLimb',
            'desc': 'Générateur CSS/JS avancé de chutes de neige.',
            'h1': 'Snowfall Gen', 'p': 'Générateur Visuel', 'Organic Particles': 'Particules Organiques',
            'Count': 'Quantité', 'Fall Speed': 'Vitesse', 'Flake Size': 'Taille Flocon',
            'Wind Drift': 'Vent', 'Export': 'Exporter'
        },
        'snowfall-premier.html': {
            'title': 'Générateur de Neige | StudioLimb',
            'desc': 'Générateur CSS/JS avancé de chutes de neige.',
            'h1': 'Snowfall Gen', 'p': 'Générateur Visuel', 'Organic Particles': 'Particules Organiques',
            'Count': 'Quantité', 'Fall Speed': 'Vitesse', 'Flake Size': 'Taille Flocon',
            'Wind Drift': 'Vent', 'Export': 'Exporter'
        }
    },
    'hi': {
        'lang': 'hi',
        'btn_flag': '<span class="lang-flag">🇮🇳</span> HI',
        'url-encode-decode.html': {
            'title': 'यूआरएल एनकोडर | StudioLimb',
            'desc': 'मुफ्त ऑनलाइन यूआरएल एनकोडर और डिकोडर।',
            'h1': 'URL Encoder / Decoder', 'p': 'सुरक्षित उपकरण', 'Clear': 'साफ़ करें',
            'Text to Encode': 'एनकोड करने के लिए टेक्स्ट', 'URL Encoded Output': 'एनकोडेड आउटपुट',
            'URL Encoded Input': 'एनकोडेड इनपुट', 'Decoded Plain Text': 'डिकोड किया गया टेक्स्ट',
            'Result will appear here...': 'परिणाम यहाँ दिखाई देगा...'
        },
        'qr-code-generator.html': {
            'title': 'क्यूआर कोड जनरेटर | StudioLimb',
            'desc': 'उच्च गुणवत्ता वाले कस्टम क्यूआर कोड उत्पन्न करें।',
            'h1': 'QR Code Generator', 'p': 'छवि जनरेटर', 'Link or Data': 'लिंक या डेटा',
            'Colors &': 'रंग और', 'Data Blocks': 'डेटा ब्लॉक', 'Background': 'पृष्ठभूमि',
            'Raster': 'प्रारूप', 'Download QR': 'क्यूआर डाउनलोड करें'
        },
        'snowfall-generator.html': {
            'title': 'स्नोफॉल जनरेटर | StudioLimb',
            'desc': 'उन्नत स्नोफॉल जनरेटर उपकरण।',
            'h1': 'Snowfall Gen', 'p': 'दृश्य जनरेटर', 'Organic Particles': 'जैविक कण',
            'Count': 'मात्रा', 'Fall Speed': 'गिरने की गति', 'Flake Size': 'आकार',
            'Wind Drift': 'हवा का प्रभाव', 'Export': 'निर्यात'
        },
        'snowfall-premier.html': {
            'title': 'स्नोफॉल जनरेटर | StudioLimb',
            'desc': 'उन्नत स्नोफॉल जनरेटर उपकरण।',
            'h1': 'Snowfall Gen', 'p': 'दृश्य जनरेटर', 'Organic Particles': 'जैविक कण',
            'Count': 'मात्रा', 'Fall Speed': 'गिरने की गति', 'Flake Size': 'आकार',
            'Wind Drift': 'हवा का प्रभाव', 'Export': 'निर्यात'
        }
    },
    'pt': {
        'lang': 'pt',
        'btn_flag': '<span class="lang-flag">🇧🇷</span> PT',
        'url-encode-decode.html': {
            'title': 'Codificador de URL | StudioLimb',
            'desc': 'Codificador e decodificador de URL online.',
            'h1': 'URL Encoder / Decoder', 'p': 'Ferramenta Online', 'Clear': 'Limpar',
            'Text to Encode': 'Texto para Codificar', 'URL Encoded Output': 'Saída Codificada',
            'URL Encoded Input': 'Entrada Codificada', 'Decoded Plain Text': 'Texto Decodificado',
            'Result will appear here...': 'O resultado aparecerá aqui...'
        },
        'qr-code-generator.html': {
            'title': 'Gerador de QR | StudioLimb',
            'desc': 'Gere códigos QR de alta qualidade.',
            'h1': 'QR Code Generator', 'p': 'Gerador de Imagem', 'Link or Data': 'Link ou Dados',
            'Colors &': 'Cores &', 'Data Blocks': 'Blocos de Dados', 'Background': 'Fundo',
            'Raster': 'Formato', 'Download QR': 'Baixar QR'
        },
        'snowfall-generator.html': {
            'title': 'Gerador de Neve | StudioLimb',
            'desc': 'Gerador de neve avançado CSS/JS.',
            'h1': 'Snowfall Gen', 'p': 'Gerador Visual', 'Organic Particles': 'Partículas Orgânicas',
            'Count': 'Quantidade', 'Fall Speed': 'Velocidade', 'Flake Size': 'Tamanho do Floco',
            'Wind Drift': 'Efeito Vento', 'Export': 'Exportar'
        },
        'snowfall-premier.html': {
            'title': 'Gerador de Neve | StudioLimb',
            'desc': 'Gerador de neve avançado CSS/JS.',
            'h1': 'Snowfall Gen', 'p': 'Gerador Visual', 'Organic Particles': 'Partículas Orgânicas',
            'Count': 'Quantidade', 'Fall Speed': 'Velocidade', 'Flake Size': 'Tamanho do Floco',
            'Wind Drift': 'Efeito Vento', 'Export': 'Exportar'
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
                html = re.sub(r'<h1 class="text-xl font-bold.*?>.*?</h1>', f'<h1 class="text-xl font-bold mb-1">{t_data["h1"]}</h1>', html)
            if 'p' in t_data:
                 html = re.sub(r'<p class="text-sm font-medium text-slate-400">.*?<span\s+class="text-primary">(.*?)</span>.*?</p>', f'<p class="text-sm font-medium text-slate-400">{t_data["p"]} <span class="text-primary">\\1</span></p>', html)

            for eng, k in t_data.items():
                if eng not in ['lang', 'btn_flag', 'title', 'desc', 'h1', 'p']:
                    html = html.replace(f'>{eng}<', f'>{k}<')
                    html = html.replace(f'{eng}</span>', f'{k}</span>')
                    html = html.replace(f'{eng}</label>', f'{k}</label>')
                    html = html.replace(f'"{eng}"', f'"{k}"')
            
            if 'Result will appear here...' in t_data:
                 html = html.replace('Result will appear here...', t_data['Result will appear here...'])
            
            # Additional strings that could be tricky:
            if eng in ['Text to Encode', 'URL Encoded Output', 'URL Encoded Input', 'Decoded Plain Text']:
                html = html.replace(f'></span>{eng}`', f'></span>{k}`')

            html = html.replace('href="index.html" class="flex flex-col', 'href="../index.html" class="flex flex-col')
            html = html.replace("navigator.serviceWorker.register('/sw.js')", "navigator.serviceWorker.register('../sw.js')")
            html = html.replace('href="/manifest.json"', 'href="../manifest.json"')
            html = html.replace('href="/icons/icon-192x192.png"', 'href="../icons/icon-192x192.png"')
            html = html.replace('href="index.html" class="flex items-center gap-3', 'href="index.html" class="flex items-center gap-3')
            html = html.replace('href="index.html" class="hover:text-white transition-colors"', 'href="../index.html" class="hover:text-white transition-colors"')

            os.makedirs(os.path.join(base_dir, code), exist_ok=True)
            with open(os.path.join(base_dir, code, f), 'w', encoding='utf-8') as out:
                out.write(html)

if __name__ == '__main__':
    process_translation()
    print("Batch 7 Translation Complete!")
