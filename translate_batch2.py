import os
import re

base_dir = './'
tools_to_translate = [
    'flexbox-playground.html', 
    'grid-generator.html', 
    'image-compressor.html', 
    'image-resizer.html', 
    'image-cropper.html'
]

translations = {
    'es': {
        'lang': 'es',
        'btn_flag': '<span class="lang-flag">🇪🇸</span> ES',
        'flexbox-playground.html': {
            'title': 'StudioLimb | Flexbox Gen Premier',
            'desc': 'Generador Flexbox interactivo para diseño web. Ajusta propiedades visualmente.',
            'h1': 'Flexbox Gen', 'p': 'Constructor de Layouts',
            'add': '+ Añadir Item', 'remove': '- Eliminar', 'copy': 'Copiar CSS', 'copied': '¡Copiado!'
        },
        'grid-generator.html': {
            'title': 'StudioLimb | Grid Gen Premier',
            'desc': 'Generador de CSS Grid interactivo. Crea layouts complejos en segundos.',
            'h1': 'Grid Gen', 'p': 'Constructor de Layouts',
            'rows': 'Filas (Rows)', 'columns': 'Columnas (Cols)', 'gap': 'Espaciado (Gap)',
            'generate': 'Copiar CSS', 'copied': '¡Copiado!', 'copy': 'Copiar CSS'
        },
        'image-compressor.html': {
            'title': 'StudioLimb | Compressor Premier',
            'desc': 'Reduce el tamaño de tus imágenes sin perder calidad visible directamente en tu navegador.',
            'h1': 'Compressor', 'p': 'Reductor de Tamaño',
            'drop': 'Suelta tu imagen aquí', 'browse': 'o haz clic para explorar',
            'quality': 'Calidad de Compresión', 'download': 'Descargar Imagen', 'original': 'Original:', 'compressed': 'Comprimido:'
        },
        'image-resizer.html': {
            'title': 'StudioLimb | Resizer Premier',
            'desc': 'Redimensiona imágenes en píxeles de forma rápida conservando el aspect ratio.',
            'h1': 'Resizer', 'p': 'Escalado de Imagen',
            'drop': 'Suelta tu imagen aquí', 'browse': 'o haz clic para explorar',
            'width': 'Ancho (px)', 'height': 'Alto (px)', 'lock': 'Bloquear Relación de Aspecto',
            'resize_btn': 'Redimensionar y Descargar'
        },
        'image-cropper.html': {
            'title': 'StudioLimb | Photo Cropper Premier',
            'desc': 'Recorta imágenes a proporciones específicas (16:9, 4:3, 1:1) o libremente.',
            'h1': 'Photo Cropper', 'p': 'Herramienta de Recorte',
            'drop': 'Suelta tu imagen aquí', 'browse': 'o haz clic para explorar',
            'ratio': 'Relación de Aspecto:', 'free': 'Libre', 'square': 'Cuadrado 1:1',
            'download': 'Descargar Recorte'
        }
    },
    'fr': {
        'lang': 'fr',
        'btn_flag': '<span class="lang-flag">🇫🇷</span> FR',
        'flexbox-playground.html': {
            'title': 'StudioLimb | Flexbox Gen Premier',
            'desc': 'Générateur interactif Flexbox pour la conception web. Ajustez les propriétés visuellement.',
            'h1': 'Flexbox Gen', 'p': 'Constructeur de Layouts',
            'add': '+ Ajouter un Item', 'remove': '- Supprimer', 'copy': 'Copier CSS', 'copied': 'Copié !'
        },
        'grid-generator.html': {
            'title': 'StudioLimb | Grid Gen Premier',
            'desc': 'Générateur interactif CSS Grid. Créez des mises en page complexes en quelques secondes.',
            'h1': 'Grid Gen', 'p': 'Constructeur de Layouts',
            'rows': 'Lignes (Rows)', 'columns': 'Colonnes (Cols)', 'gap': 'Espacement (Gap)',
            'generate': 'Copier CSS', 'copied': 'Copié !', 'copy': 'Copier CSS'
        },
        'image-compressor.html': {
            'title': 'StudioLimb | Compressor Premier',
            'desc': 'Réduisez la taille de vos images sans perte de qualité visible directement dans le navigateur.',
            'h1': 'Compressor', 'p': 'Réducteur de Taille',
            'drop': 'Déposez votre image ici', 'browse': 'ou cliquez pour parcourir',
            'quality': 'Qualité de Compression', 'download': 'Télécharger l\'Image', 'original': 'Original:', 'compressed': 'Compressé:'
        },
        'image-resizer.html': {
            'title': 'StudioLimb | Resizer Premier',
            'desc': 'Redimensionnez rapidement vos images en pixels en conservant le format d\'image.',
            'h1': 'Resizer', 'p': 'Mise à l\'Échelle',
            'drop': 'Déposez votre image ici', 'browse': 'ou cliquez pour parcourir',
            'width': 'Largeur (px)', 'height': 'Hauteur (px)', 'lock': 'Verrouiller le ratio',
            'resize_btn': 'Redimensionner et Télécharger'
        },
        'image-cropper.html': {
            'title': 'StudioLimb | Photo Cropper Premier',
            'desc': 'Recadrez les images selon des proportions spécifiques (16:9, 4:3, 1:1) ou librement.',
            'h1': 'Photo Cropper', 'p': 'Outil de Recadrage',
            'drop': 'Déposez votre image ici', 'browse': 'ou cliquez pour parcourir',
            'ratio': 'Format d\'Image:', 'free': 'Libre', 'square': 'Carré 1:1',
            'download': 'Télécharger Recadrage'
        }
    },
    'hi': {
        'lang': 'hi',
        'btn_flag': '<span class="lang-flag">🇮🇳</span> HI',
        'flexbox-playground.html': {
            'title': 'StudioLimb | Flexbox Gen Premier',
            'desc': 'वेब डिजाइन के लिए इंटरएक्टिव फ्लेक्सबॉक्स जनरेटर।',
            'h1': 'Flexbox Gen', 'p': 'लेआउट बिल्डर',
            'add': '+ आइटम जोड़ें', 'remove': '- निकालें', 'copy': 'CSS कॉपी करें', 'copied': 'कॉपी किया गया!'
        },
        'grid-generator.html': {
            'title': 'StudioLimb | Grid Gen Premier',
            'desc': 'इंटरएक्टिव सीएसएस ग्रिड जनरेटर। सेकंड में जटिल लेआउट बनाएं।',
            'h1': 'Grid Gen', 'p': 'लेआउट बिल्डर',
            'rows': 'पंक्तियाँ (Rows)', 'columns': 'कॉलम (Cols)', 'gap': 'अंतर (Gap)',
            'generate': 'CSS कॉपी करें', 'copied': 'कॉपी किया गया!', 'copy': 'CSS कॉपी करें'
        },
        'image-compressor.html': {
            'title': 'StudioLimb | Compressor Premier',
            'desc': 'सीधे अपने ब्राउज़र में गुणवत्ता खोए बिना अपनी छवियों का आकार कम करें।',
            'h1': 'Compressor', 'p': 'आकार कम करने वाला',
            'drop': 'अपनी छवि यहाँ छोड़ें', 'browse': 'या ब्राउज़ करने के लिए क्लिक करें',
            'quality': 'संपीड़न गुणवत्ता', 'download': 'छवि डाउनलोड', 'original': 'मूल:', 'compressed': 'संपीड़ित:'
        },
        'image-resizer.html': {
            'title': 'StudioLimb | Resizer Premier',
            'desc': 'पहलू अनुपात को बनाए रखते हुए छवियों को पिक्सेल में तेजी से आकार दें।',
            'h1': 'Resizer', 'p': 'इमेज स्केलिंग',
            'drop': 'अपनी छवि यहाँ छोड़ें', 'browse': 'या ब्राउज़ करने के लिए क्लिक करें',
            'width': 'चौड़ाई (px)', 'height': 'ऊंचाई (px)', 'lock': 'पहलू अनुपात लॉक करें',
            'resize_btn': 'आकार बदलें और डाउनलोड करें'
        },
        'image-cropper.html': {
            'title': 'StudioLimb | Photo Cropper Premier',
            'desc': 'छवियों को विशिष्ट अनुपात (16:9, 4:3, 1:1) या स्वतंत्र रूप से क्रॉप करें।',
            'h1': 'Photo Cropper', 'p': 'क्रॉप टूल',
            'drop': 'अपनी छवि यहाँ छोड़ें', 'browse': 'या ब्राउज़ करने के लिए क्लिक करें',
            'ratio': 'पहलू अनुपात:', 'free': 'निःशुल्क', 'square': 'वर्ग 1:1',
            'download': 'क्रॉप डाउनलोड करें'
        }
    },
    'pt': {
        'lang': 'pt',
        'btn_flag': '<span class="lang-flag">🇧🇷</span> PT',
        'flexbox-playground.html': {
            'title': 'StudioLimb | Flexbox Gen Premier',
            'desc': 'Gerador Flexbox interativo para web design. Ajuste visualmente as propriedades.',
            'h1': 'Flexbox Gen', 'p': 'Construtor de Layouts',
            'add': '+ Adicionar Item', 'remove': '- Remover', 'copy': 'Copiar CSS', 'copied': 'Copiado!'
        },
        'grid-generator.html': {
            'title': 'StudioLimb | Grid Gen Premier',
            'desc': 'Gerador CSS Grid interativo. Crie layouts complexos em segundos.',
            'h1': 'Grid Gen', 'p': 'Construtor de Layouts',
            'rows': 'Linhas (Rows)', 'columns': 'Colunas (Cols)', 'gap': 'Espaçamento (Gap)',
            'generate': 'Copiar CSS', 'copied': 'Copiado!', 'copy': 'Copiar CSS'
        },
        'image-compressor.html': {
            'title': 'StudioLimb | Compressor Premier',
            'desc': 'Reduza o tamanho das suas imagens sem perder qualidade visível diretamente no navegador.',
            'h1': 'Compressor', 'p': 'Redutor de Tamanho',
            'drop': 'Solte sua imagem aqui', 'browse': 'ou clique para procurar',
            'quality': 'Qualidade de Compressão', 'download': 'Baixar Imagem', 'original': 'Original:', 'compressed': 'Comprimido:'
        },
        'image-resizer.html': {
            'title': 'StudioLimb | Resizer Premier',
            'desc': 'Redimensione rapidamente imagens em pixels mantendo a proporção de aspecto.',
            'h1': 'Resizer', 'p': 'Escalonamento de Imagem',
            'drop': 'Solte sua imagem aqui', 'browse': 'ou clique para procurar',
            'width': 'Largura (px)', 'height': 'Altura (px)', 'lock': 'Bloquear Proporção',
            'resize_btn': 'Redimensionar e Baixar'
        },
        'image-cropper.html': {
            'title': 'StudioLimb | Photo Cropper Premier',
            'desc': 'Corte imagens para proporções específicas (16:9, 4:3, 1:1) ou livremente.',
            'h1': 'Photo Cropper', 'p': 'Ferramenta de Recorte',
            'drop': 'Solte sua imagem aqui', 'browse': 'ou clique para procurar',
            'ratio': 'Proporção da Imagem:', 'free': 'Livre', 'square': 'Quadrado 1:1',
            'download': 'Baixar Recorte'
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
            dropdown_pattern = re.compile(r'<div class="lang-selector">.*?</div>\s*</div>', re.DOTALL)
            html = dropdown_pattern.sub(build_dropdown(code, f), html)

            # --- TOOLS TRANSLATIONS ---
            html = re.sub(r'<title>.*?</title>', f'<title>{t_data.get("title", "")}</title>', html)
            html = re.sub(r'<meta name="description"\s+content="[^"]+">', f'<meta name="description" content="{t_data.get("desc", "")}">', html)

            if 'h1' in t_data:
                html = re.sub(r'<h1 class="text-xl font-bold">.*?</h1>', f'<h1 class="text-xl font-bold">{t_data["h1"]}</h1>', html)
            if 'p' in t_data:
                html = re.sub(r'<p class="text-sm font-medium text-slate-400">.*?</p>', f'<p class="text-sm font-medium text-slate-400">{t_data["p"]}</p>', html)

            # Replacements
            replacements = {
                '+ Add Item': 'add', '- Remove': 'remove', 'Copy CSS': 'copy', 'Copied!': 'copied',
                'Rows': 'rows', 'Columns': 'columns', 'Gap': 'gap',
                'Drop your image here': 'drop', 'or click to browse': 'browse',
                'Quality': 'quality', 'Download': 'download', 'Original:': 'original', 'Compressed:': 'compressed',
                'Width': 'width', 'Height': 'height', 'Lock Aspect Ratio': 'lock', 'Resize & Download': 'resize_btn',
                'Aspect Ratio:': 'ratio', 'Free': 'free', 'Square': 'square', 'Download Cropped': 'download'
            }
            
            for eng, k in replacements.items():
                if k in t_data:
                    # Target exact words
                    html = html.replace(f'>{eng}<', f'>{t_data[k]}<')
                    html = html.replace(f'{eng}</span>', f'{t_data[k]}</span>')
                    html = html.replace(f'{eng}</button>', f'{t_data[k]}</button>')
                    html = html.replace(f'"{eng}"', f'"{t_data[k]}"')
                    if eng == 'Copy CSS': # For the flexbox specific copy button logic
                        html = html.replace('Copy CSS', t_data[k])

            # Fix relative links
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
    print("Batch 2 Translation Complete!")
