import os
import re

base_dir = './'
tools_to_translate = [
    'image-format-converter.html', 
    'image-placeholder.html', 
    'photo-filters.html', 
    'watermark-creator.html', 
    'bg-remover.html'
]

translations = {
    'es': {
        'lang': 'es',
        'btn_flag': '<span class="lang-flag">🇪🇸</span> ES',
        'image-format-converter.html': {
            'title': 'Convertidor de Formato | StudioLimb',
            'desc': 'Convierte imágenes de forma local y segura en tu navegador.',
            'h1': 'Convertidor de Formato', 'p': 'Convierte imágenes de forma local y segura.',
            'Supports multiple files': 'Soporta múltiples archivos', 'Convert': 'Convertir',
            'Processing': 'Procesando', 'Saved': 'Guardado', 'Convert Again': 'Convertir de Nuevo',
            'to JPEG': 'a JPEG', 'to PNG': 'a PNG', 'to WebP': 'a WebP'
        },
        'image-placeholder.html': {
            'title': 'Generador Placeholder | StudioLimb',
            'desc': 'Crea placeholders de imagen personalizados al instante con dimensiones y colores.',
            'h1': 'Image Placeholder', 'p': 'Generador SVG y Base64',
            'Width (px)': 'Ancho (px)', 'Height (px)': 'Alto (px)', 'Background': 'Fondo',
            'Text Color': 'Color del Texto', 'Custom Text': 'Texto Personalizado', 'Font Size': 'Tamaño de Fuente',
            'Copy SVG Code': 'Copiar Código SVG', 'Copied!': '¡Copiado!', 'Download PNG': 'Descargar PNG'
        },
        'photo-filters.html': {
            'title': 'Filtros y Efectos de Fotos | StudioLimb',
            'desc': 'Aplica filtros de fotos estilo Instagram y efectos especiales.',
            'h2': 'Filtros y Efectos de Fotos',
            'Upload Image': 'Subir Imagen', 'Export Image': 'Descargar Imagen',
            'Normal': 'Normal', 'Vintage': 'Vintage', 'Lark': 'Lark', 'B&W': 'B/N', 'Clarendon': 'Clare', 'Sepia': 'Sepia',
            'Fine Tune': 'Ajustes Finos', 'Brightness': 'Brillo', 'Contrast': 'Contraste', 'Saturation': 'Saturación',
            'Grayscale': 'Escala de Grises', 'Blur': 'Desenfoque'
        },
        'watermark-creator.html': {
            'title': 'Creador de Marca de Agua | StudioLimb',
            'desc': 'Añade marcas de agua de texto o logo a tus imágenes en masa.',
            'h2': 'Creador de Marca de Agua',
            'Upload Image': 'Subir Imagen', 'Export Save': 'Descargar con Marca',
            'Watermark Type': 'Tipo de Marca', 'Text': 'Texto', 'Logo': 'Logotipo', 
            'Tile Pattern (Repeated)': 'Patrón de Mosaico (Repetido)', 'Opacity': 'Opacidad', 'Size': 'Tamaño'
        },
        'bg-remover.html': {
            'title': 'Quitar Fondo IA | StudioLimb',
            'desc': 'Elimina el fondo de las imágenes automáticamente usando inteligencia artificial local.',
            'h2': 'Borrador de Fondos IA',
            'Select Image': 'Seleccionar Imagen', 'Download PNG': 'Descargar PNG Transparente',
            'Processing...': 'Procesando IA...', 'Hold tight, loading AI model...': 'Cargando modelo de IA...'
        }
    },
    'fr': {
        'lang': 'fr',
        'btn_flag': '<span class="lang-flag">🇫🇷</span> FR',
        'image-format-converter.html': {
            'title': 'Convertisseur de Format | StudioLimb',
            'desc': 'Convertissez les images localement et en toute sécurité dans votre navigateur.',
            'h1': 'Convertisseur de Format', 'p': 'Convertissez les images en toute sécurité.',
            'Supports multiple files': 'Prend en charge plusieurs fichiers', 'Convert': 'Convertir',
            'Processing': 'Traitement', 'Saved': 'Enregistré', 'Convert Again': 'Convertir à Nouveau',
            'to JPEG': 'en JPEG', 'to PNG': 'en PNG', 'to WebP': 'en WebP'
        },
        'image-placeholder.html': {
            'title': 'Générateur d\'Espace Réservé | StudioLimb',
            'desc': 'Créez instantanément des espaces réservés d\'image personnalisés.',
            'h1': 'Espace Réservé', 'p': 'SVG et Base64',
            'Width (px)': 'Largeur (px)', 'Height (px)': 'Hauteur (px)', 'Background': 'Fond',
            'Text Color': 'Couleur Texte', 'Custom Text': 'Texte Personnalisé', 'Font Size': 'Taille Police',
            'Copy SVG Code': 'Copier Code SVG', 'Copied!': 'Copié !', 'Download PNG': 'Télécharger PNG'
        },
        'photo-filters.html': {
            'title': 'Filtres et Effets | StudioLimb',
            'desc': 'Appliquez des filtres photo de style Instagram et ajustez les paramètres d\'image.',
            'h2': 'Filtres et Effets Photo',
            'Upload Image': 'Uploader', 'Export Image': 'Exporter Image',
            'Normal': 'Normal', 'Vintage': 'Ancien', 'Lark': 'Lark', 'B&W': 'N&B', 'Clarendon': 'Clare', 'Sepia': 'Sépia',
            'Fine Tune': 'Ajustement', 'Brightness': 'Luminosité', 'Contrast': 'Contraste', 'Saturation': 'Saturation',
            'Grayscale': 'Niveaux gris', 'Blur': 'Flou'
        },
        'watermark-creator.html': {
            'title': 'Créateur de Filigrane | StudioLimb',
            'desc': 'Ajoutez des filigranes de texte ou de logo à vos images.',
            'h2': 'Créateur de Filigrane',
            'Upload Image': 'Uploader', 'Export Save': 'Sauvegarder',
            'Watermark Type': 'Type Filigrane', 'Text': 'Texte', 'Logo': 'Logo', 
            'Tile Pattern (Repeated)': 'Motif Répété (Mosaïque)', 'Opacity': 'Opacité', 'Size': 'Taille'
        },
        'bg-remover.html': {
            'title': 'Suppresseur de Fond IA | StudioLimb',
            'desc': 'Supprimez le fond des images automatiquement à l\'aide de l\'IA locale.',
            'h2': 'Suppresseur de Fond IA',
            'Select Image': 'Sélectionner', 'Download PNG': 'Télécharger PNG Transparent',
            'Processing...': 'Traitement IA...', 'Hold tight, loading AI model...': 'Chargement du modèle IA...'
        }
    },
    'hi': {
        'lang': 'hi',
        'btn_flag': '<span class="lang-flag">🇮🇳</span> HI',
        'image-format-converter.html': {
            'title': 'प्रारूप कनवर्टर | StudioLimb',
            'desc': 'अपने ब्राउज़र में स्थानीय और सुरक्षित रूप से छवियों को कनवर्ट करें।',
            'h1': 'प्रारूप कनवर्टर', 'p': 'छवियों को सुरक्षित रूप से कनवर्ट करें।',
            'Supports multiple files': 'कई फाइलों का समर्थन करता है', 'Convert': 'कनवर्ट करें',
            'Processing': 'प्रसंस्करण', 'Saved': 'सहेजा गया', 'Convert Again': 'फिर से कनवर्ट करें',
            'to JPEG': 'JPEG में', 'to PNG': 'PNG में', 'to WebP': 'WebP में'
        },
        'image-placeholder.html': {
            'title': 'छवि प्लेसहोल्डर | StudioLimb',
            'desc': 'आयामों और रंगों के साथ कस्टम छवि प्लेसहोल्डर तुरंत बनाएं।',
            'h1': 'इमेज प्लेसहोल्डर', 'p': 'एसवीजी और बेस64',
            'Width (px)': 'चौड़ाई', 'Height (px)': 'ऊंचाई', 'Background': 'पृष्ठभूमि',
            'Text Color': 'टेक्स्ट रंग', 'Custom Text': 'कस्टम टेक्स्ट', 'Font Size': 'फ़ॉन्ट आकार',
            'Copy SVG Code': 'SVG कॉपी करें', 'Copied!': 'कॉपी किया गया!', 'Download PNG': 'PNG डाउनलोड करें'
        },
        'photo-filters.html': {
            'title': 'फोटो फिल्टर | StudioLimb',
            'desc': 'इंस्टाग्राम शैली के फोटो फिल्टर लागू करें।',
            'h2': 'फोटो फिल्टर और प्रभाव',
            'Upload Image': 'अपलोड करें', 'Export Image': 'छवि निर्यात करें',
            'Normal': 'सामान्य', 'Vintage': 'विंटेज', 'Lark': 'लार्क', 'B&W': 'बी एंड डब्ल्यू', 'Clarendon': 'क्लेरेंडन', 'Sepia': 'सेपिया',
            'Fine Tune': 'फाइन ट्यून', 'Brightness': 'चमक', 'Contrast': 'कंट्रास्ट', 'Saturation': 'संतृप्ति',
            'Grayscale': 'ग्रेस्केल', 'Blur': 'धुंधलापन'
        },
        'watermark-creator.html': {
            'title': 'वॉटरमार्क निर्माता | StudioLimb',
            'desc': 'अपनी छवियों में टेक्स्ट या लोगो वॉटरमार्क जोड़ें।',
            'h2': 'वॉटरमार्क निर्माता',
            'Upload Image': 'छवि अपलोड करें', 'Export Save': 'सहेजें और निर्यात करें',
            'Watermark Type': 'वॉटरमार्क प्रकार', 'Text': 'टेक्स्ट', 'Logo': 'लोगो', 
            'Tile Pattern (Repeated)': 'टाइल पैटर्न (दोहराया गया)', 'Opacity': 'अपारदर्शिता', 'Size': 'आकार'
        },
        'bg-remover.html': {
            'title': 'एआई पृष्ठभूमि रिमूवर | StudioLimb',
            'desc': 'स्थानीय एआई का उपयोग करके छवियों से पृष्ठभूमि हटा दें।',
            'h2': 'एआई पृष्ठभूमि इरेज़र',
            'Select Image': 'छवि चुनें', 'Download PNG': 'पारदर्शी PNG डाउनलोड करें',
            'Processing...': 'प्रसंस्करण...', 'Hold tight, loading AI model...': 'एआई मॉडल लोड हो रहा है...'
        }
    },
    'pt': {
        'lang': 'pt',
        'btn_flag': '<span class="lang-flag">🇧🇷</span> PT',
        'image-format-converter.html': {
            'title': 'Conversor de Formato | StudioLimb',
            'desc': 'Converta imagens localmente e com segurança em seu navegador.',
            'h1': 'Conversor de Formato', 'p': 'Converta imagens localmente e com segurança.',
            'Supports multiple files': 'Suporta vários arquivos', 'Convert': 'Converter',
            'Processing': 'Processando', 'Saved': 'Salvo', 'Convert Again': 'Converter Novamente',
            'to JPEG': 'para JPEG', 'to PNG': 'para PNG', 'to WebP': 'para WebP'
        },
        'image-placeholder.html': {
            'title': 'Gerador de Placeholder | StudioLimb',
            'desc': 'Crie marcadores de imagem personalizados instantaneamente com dimensões e cores.',
            'h1': 'Image Placeholder', 'p': 'Gerador SVG e Base64',
            'Width (px)': 'Largura (px)', 'Height (px)': 'Altura (px)', 'Background': 'Fundo',
            'Text Color': 'Cor do Texto', 'Custom Text': 'Texto Personalizado', 'Font Size': 'Tam. da Fonte',
            'Copy SVG Code': 'Copiar Código SVG', 'Copied!': 'Copiado!', 'Download PNG': 'Baixar PNG'
        },
        'photo-filters.html': {
            'title': 'Filtros de Fotos | StudioLimb',
            'desc': 'Aplique filtros no estilo do Instagram e ajustes finos nas imagens.',
            'h2': 'Filtros e Efeitos de Fotos',
            'Upload Image': 'Enviar Imagem', 'Export Image': 'Exportar Imagem',
            'Normal': 'Normal', 'Vintage': 'Retrô', 'Lark': 'Lark', 'B&W': 'P&B', 'Clarendon': 'Clare', 'Sepia': 'Sépia',
            'Fine Tune': 'Ajuste Fino', 'Brightness': 'Brilho', 'Contrast': 'Contraste', 'Saturation': 'Saturação',
            'Grayscale': 'Escala de Cinza', 'Blur': 'Desfoque'
        },
        'watermark-creator.html': {
            'title': 'Criador Marca d\'Água | StudioLimb',
            'desc': 'Adicione marcas d\'água de texto ou logotipo às suas imagens.',
            'h2': 'Criador Marca d\'Água',
            'Upload Image': 'Carregar Imagem', 'Export Save': 'Exportar Imagem',
            'Watermark Type': 'Tipo de Marca', 'Text': 'Texto', 'Logo': 'Logotipo', 
            'Tile Pattern (Repeated)': 'Padrão de Mosaico (Repetido)', 'Opacity': 'Opacidade', 'Size': 'Tamanho'
        },
        'bg-remover.html': {
            'title': 'Remover Fundo IA | StudioLimb',
            'desc': 'Remova fundos de imagens automaticamente usando IA no dispositivo.',
            'h2': 'Borracha de Fundo IA',
            'Select Image': 'Selecionar Imagem', 'Download PNG': 'Baixar PNG Transparente',
            'Processing...': 'Processando...', 'Hold tight, loading AI model...': 'Carregando o modelo de IA...'
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
            if 'h2' in t_data:
                html = re.sub(r'<h2 class="text-lg font-bold leading-tight tracking-tight">.*?</h2>', f'<h2 class="text-lg font-bold leading-tight tracking-tight">{t_data["h2"]}</h2>', html)

            for eng, k in t_data.items():
                if eng not in ['lang', 'btn_flag', 'title', 'desc', 'h1', 'p', 'h2']:
                    html = html.replace(f'>{eng}<', f'>{k}<')
                    html = html.replace(f'{eng}</span>', f'{k}</span>')
                    html = html.replace(f'{eng}</label>', f'{k}</label>')
                    html = html.replace(f'"{eng}"', f'"{k}"')
                    if eng in ['Convert', 'Processing', 'Saved', 'Convert Again']:
                        html = html.replace(f'{eng}', f'{k}')
                        # Restore any uppercase if got broken by partial replace
                        html = html.replace('100% free', '100% free') # placeholder
                        

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
    print("Batch 3 Translation Complete!")
