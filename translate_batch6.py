import os
import re

base_dir = './'
tools_to_translate = [
    'regex-tester.html', 
    'social-media-sizes.html', 
    'svg-optimizer.html', 
    'svg-path-editor.html', 
    'svg-wave-generator.html'
]

translations = {
    'es': {
        'lang': 'es',
        'btn_flag': '<span class="lang-flag">🇪🇸</span> ES',
        'regex-tester.html': {
            'title': 'Probador de Regex | StudioLimb',
            'desc': 'Prueba y depura tus expresiones regulares (Regex) gratuitamente.',
            'h1': 'Regex Tester & Debugger', 'p': 'Validador Online', 'Common Flags:': 'Banderas Comunes:',
            'Waiting for valid regex...': 'Esperando expresión regular válida...', 'No matches found.': 'Sin coincidencias.',
            'Global match': 'Búsqueda Global', 'Multiline': 'Multilínea', 'Ignore case': 'Ignorar Mayúsculas'
        },
        'social-media-sizes.html': {
            'title': 'StudioLimb | Tamaños Redes Sociales',
            'desc': 'Guía actualizada de tamaños para imágenes en Instagram, TikTok, LinkedIn, Twitter/X.',
            'h1': 'Social Media Size Guide', 'p': 'Encuentra las medidas perfectas', 'All Platforms': 'Todas',
            'Instagram': 'Instagram', 'TikTok': 'TikTok', 'LinkedIn': 'LinkedIn', 'Twitter/X': 'Twitter/X',
            'Dimension copied!': '¡Tamaño Copiado!'
        },
        'svg-optimizer.html': {
            'title': 'Optimizador SVG | StudioLimb',
            'desc': 'Minimiza archivos SVG online de forma segura y rápida.',
            'h1': 'SVG Optimizer', 'p': 'Herramienta de Compresión', 'Upload SVG': 'Subir SVG',
            'Optimize': 'Optimizar', 'Copy SVG': 'Copiar SVG', 'Download SVG': 'Descargar SVG'
        },
        'svg-path-editor.html': {
            'title': 'Editor Path SVG | StudioLimb',
            'desc': 'Editor interactivo de rutas (paths) para SVG. Modifica d="" instantáneamente.',
            'h1': 'Path Editor', 'p': 'Visualizador', 'Transform': 'Transformar', 'Scale': 'Escalar', 
            'Clean &': 'Limpiar y'
        },
        'svg-wave-generator.html': {
            'title': 'Generador Ondas SVG | StudioLimb',
            'desc': 'Generador visual de ondas curvas (waves) exportables a SVG/CSS.',
            'h1': 'Wave Generator', 'p': 'Herramienta Premier', 'Points': 'Puntos', 'Variance': 'Variación',
            'Fill': 'Relleno', 'Shape': 'Forma', 'Copy SVG Code': 'Copiar Código SVG'
        }
    },
    'fr': {
        'lang': 'fr',
        'btn_flag': '<span class="lang-flag">🇫🇷</span> FR',
        'regex-tester.html': {
            'title': 'Testeur d\'Expressions Régulières | StudioLimb',
            'desc': 'Testez et déboguez vos expressions régulières (Regex) en ligne.',
            'h1': 'Testeur Regex', 'p': 'Validateur en Ligne', 'Common Flags:': 'Indicateurs:',
            'Waiting for valid regex...': 'En attente...', 'No matches found.': 'Aucun résultat.',
            'Global match': 'Recherche Globale', 'Multiline': 'Multiligne', 'Ignore case': 'Ignorer Casse'
        },
        'social-media-sizes.html': {
            'title': 'Tailles Réseaux Sociaux | StudioLimb',
            'desc': 'Guide des tailles d\'images pour Instagram, TikTok, Twitter/X.',
            'h1': 'Social Media Size Guide', 'p': 'Trouvez les bonnes dimensions.', 'All Platforms': 'Toutes',
            'Instagram': 'Instagram', 'TikTok': 'TikTok', 'LinkedIn': 'LinkedIn', 'Twitter/X': 'Twitter/X',
            'Dimension copied!': 'Taille copiée !'
        },
        'svg-optimizer.html': {
            'title': 'Optimiseur SVG | StudioLimb',
            'desc': 'Minimisez vos fichiers SVG en ligne.',
            'h1': 'SVG Optimizer', 'p': 'Outil de Compression', 'Upload SVG': 'Uploader',
            'Optimize': 'Optimiser', 'Copy SVG': 'Copier SVG', 'Download SVG': 'Télécharger SVG'
        },
        'svg-path-editor.html': {
            'title': 'Éditeur Path SVG | StudioLimb',
            'desc': 'Éditeur interactif de chemins SVG.',
            'h1': 'Path Editor', 'p': 'Visualiseur', 'Transform': 'Transformer', 'Scale': 'Échelle', 
            'Clean &': 'Nettoyer et'
        },
        'svg-wave-generator.html': {
            'title': 'Générateur de Vagues SVG | StudioLimb',
            'desc': 'Générez des vagues (waves) SVG ou CSS.',
            'h1': 'Wave Generator', 'p': 'Outil Premium', 'Points': 'Points', 'Variance': 'Variation',
            'Fill': 'Remplissage', 'Shape': 'Forme', 'Copy SVG Code': 'Copier Code SVG'
        }
    },
    'hi': {
        'lang': 'hi',
        'btn_flag': '<span class="lang-flag">🇮🇳</span> HI',
        'regex-tester.html': {
            'title': 'रेगेक्स परीक्षक | StudioLimb',
            'desc': 'नियमित अभिव्यक्तियों (रेगेक्स) का परीक्षण और डिबग करें।',
            'h1': 'रेगेक्स टेस्ट', 'p': 'ऑनलाइन उपकरण', 'Common Flags:': 'सामान्य झंडे:',
            'Waiting for valid regex...': 'प्रतीक्षा कर रहा है...', 'No matches found.': 'कोई मेल नहीं।',
            'Global match': 'वैश्विक', 'Multiline': 'मल्टीलाइन', 'Ignore case': 'केस बदलें'
        },
        'social-media-sizes.html': {
            'title': 'सोशल मीडिया आकार | StudioLimb',
            'desc': 'इंस्टाग्राम, टिकटॉक, ट्विटर के लिए आकार मार्गदर्शिका।',
            'h1': 'सोशल मीडिया आकार', 'p': 'सही आयाम खोजें।', 'All Platforms': 'सभी',
            'Instagram': 'Instagram', 'TikTok': 'TikTok', 'LinkedIn': 'LinkedIn', 'Twitter/X': 'Twitter/X',
            'Dimension copied!': 'आयाम कॉपी किया गया!'
        },
        'svg-optimizer.html': {
            'title': 'एसवीजी ऑप्टिमाइज़र | StudioLimb',
            'desc': 'अपनी एसवीजी फाइलों को ऑनलाइन छोटा करें।',
            'h1': 'एसवीजी अनुकूलक', 'p': 'संपीड़न उपकरण', 'Upload SVG': 'एसवीजी अपलोड करें',
            'Optimize': 'अनुकूलन करें', 'Copy SVG': 'एसवीजी कॉपी करें', 'Download SVG': 'एसवीजी डाउनलोड करें'
        },
        'svg-path-editor.html': {
            'title': 'एसवीजी पाथ संपादक | StudioLimb',
            'desc': 'इंटरएक्टिव एसवीजी पाथ संपादक।',
            'h1': 'पाथ संपादक', 'p': 'दृश्य उपकरण', 'Transform': 'बदलें', 'Scale': 'स्केल', 
            'Clean &': 'साफ़ करें और'
        },
        'svg-wave-generator.html': {
            'title': 'एसवीजी वेव जनरेटर | StudioLimb',
            'desc': 'एसवीजी या सीएसएस के लिए तरंगें उत्पन्न करें।',
            'h1': 'वेव जनरेटर', 'p': 'प्रीमियम उपकरण', 'Points': 'अंक', 'Variance': 'भिन्नता',
            'Fill': 'भरें', 'Shape': 'आकार', 'Copy SVG Code': 'कोड कॉपी करें'
        }
    },
    'pt': {
        'lang': 'pt',
        'btn_flag': '<span class="lang-flag">🇧🇷</span> PT',
        'regex-tester.html': {
            'title': 'Testador de Regex | StudioLimb',
            'desc': 'Teste e depure expressões regulares online.',
            'h1': 'Regex Tester', 'p': 'Validador Online', 'Common Flags:': 'Bandeiras Comuns:',
            'Waiting for valid regex...': 'Aguardando regex válido...', 'No matches found.': 'Sem resultados.',
            'Global match': 'Busca Global', 'Multiline': 'Múltiplas Linhas', 'Ignore case': 'Ignorar Maiúsculas'
        },
        'social-media-sizes.html': {
            'title': 'Tamanhos Redes Sociais | StudioLimb',
            'desc': 'Guia de tamanhos para Instagram, TikTok, Twitter/X.',
            'h1': 'Social Media Size Guide', 'p': 'Encontre as medidas ideais.', 'All Platforms': 'Todas',
            'Instagram': 'Instagram', 'TikTok': 'TikTok', 'LinkedIn': 'LinkedIn', 'Twitter/X': 'Twitter/X',
            'Dimension copied!': 'Tamanho Copiado!'
        },
        'svg-optimizer.html': {
            'title': 'Otimizador de SVG | StudioLimb',
            'desc': 'Otimize seus arquivos SVG com segurança.',
            'h1': 'SVG Optimizer', 'p': 'Ferramenta de Compressão', 'Upload SVG': 'Enviar Arquivo',
            'Optimize': 'Otimizar', 'Copy SVG': 'Copiar SVG', 'Download SVG': 'Baixar SVG'
        },
        'svg-path-editor.html': {
            'title': 'Editor de Path SVG | StudioLimb',
            'desc': 'Editor visual de caminhos SVG.',
            'h1': 'Path Editor', 'p': 'Visualizador SVG', 'Transform': 'Transformar', 'Scale': 'Escalar', 
            'Clean &': 'Limpar e'
        },
        'svg-wave-generator.html': {
            'title': 'Gerador de Ondas SVG | StudioLimb',
            'desc': 'Gere ondas (waves) em SVG ou código CSS.',
            'h1': 'Wave Generator', 'p': 'Visualizador Online', 'Points': 'Pontos', 'Variance': 'Variação',
            'Fill': 'Preenchimento', 'Shape': 'Forma', 'Copy SVG Code': 'Copiar Código'
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
                 html = re.sub(r'<p class="text-sm font-medium text-slate-400">.*?</p>', f'<p class="text-sm font-medium text-slate-400">{t_data["p"]}</p>', html)

            for eng, k in t_data.items():
                if eng not in ['lang', 'btn_flag', 'title', 'desc', 'h1', 'p']:
                    html = html.replace(f'>{eng}<', f'>{k}<')
                    html = html.replace(f'{eng}</span>', f'{k}</span>')
                    html = html.replace(f'{eng}</label>', f'{k}</label>')
                    html = html.replace(f'"{eng}"', f'"{k}"')
                    if eng in ['All Platforms', 'Instagram', 'TikTok', 'LinkedIn', 'Twitter/X', 'Optimize']:
                        html = html.replace(f'{eng}', f'{k}')
            
            if 'Dimension copied!' in t_data:
                 html = html.replace('Dimension copied!', t_data['Dimension copied!'])

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
    print("Batch 6 Translation Complete!")
