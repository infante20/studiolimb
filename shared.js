/**
 * StudioLimb — shared.js
 * Injects: Back-nav, Share button, Related Tools panel, PWA Install banner
 * across all tool pages.
 */
(function () {
  'use strict';

  // ─── Tool Registry ────────────────────────────────────────────────────────
  const TOOLS = [
    { slug: 'gradient-generator',       title: 'Gradient Generator',    icon: 'palette',              cat: 'css',       desc: 'CSS linear & radial gradients' },
    { slug: 'glassmorphism-generator',  title: 'Glassmorphism',         icon: 'layers',               cat: 'css',       desc: 'Frosted glass UI effects' },
    { slug: 'box-shadow-generator',     title: 'Box Shadow',            icon: 'shadow',               cat: 'css',       desc: 'CSS box shadow builder' },
    { slug: 'border-radius-visualizer', title: 'Border Radius',         icon: 'rounded_corner',       cat: 'css',       desc: '8-point border radius' },
    { slug: 'css-triangle-generator',   title: 'CSS Triangle',          icon: 'change_history',       cat: 'css',       desc: 'Pure CSS triangles' },
    { slug: 'snowfall-premier',         title: 'Snowfall Effect',       icon: 'ac_unit',              cat: 'css',       desc: 'CSS particle snow' },
    { slug: 'flexbox-playground',       title: 'Flexbox Playground',    icon: 'view_column',          cat: 'layout',    desc: 'Visual flexbox builder' },
    { slug: 'grid-generator',           title: 'CSS Grid Gen',          icon: 'grid_4x4',             cat: 'layout',    desc: 'Grid layout builder' },
    { slug: 'font-pairing',             title: 'Font Pairing',          icon: 'match_case',           cat: 'layout',    desc: 'Google Font combinations' },
    { slug: 'type-scale-generator',     title: 'Type Scale',            icon: 'format_size',          cat: 'layout',    desc: 'Typography scale ratios' },
    { slug: 'lorem-ipsum-premier',      title: 'Lorem Ipsum',           icon: 'subject',              cat: 'layout',    desc: 'Placeholder text generator' },
    { slug: 'image-compressor',         title: 'Image Compressor',      icon: 'compress',             cat: 'image',     desc: 'Compress images in browser' },
    { slug: 'image-resizer',            title: 'Image Resizer',         icon: 'crop',                 cat: 'image',     desc: 'Resize with aspect ratio' },
    { slug: 'image-cropper',            title: 'Image Cropper',         icon: 'crop_free',            cat: 'image',     desc: 'Custom crop & aspect ratios' },
    { slug: 'image-format-converter',   title: 'Format Converter',      icon: 'transform',            cat: 'image',     desc: 'WebP, PNG, JPG converter' },
    { slug: 'bg-remover',               title: 'BG Remover',            icon: 'person_cancel',        cat: 'image',     desc: 'Remove backgrounds on-device' },
    { slug: 'photo-filters',            title: 'Photo Filters',         icon: 'auto_fix_high',        cat: 'image',     desc: 'Instagram-style filters' },
    { slug: 'watermark-creator',        title: 'Watermark Creator',     icon: 'branding_watermark',   cat: 'image',     desc: 'Add text/logo watermarks' },
    { slug: 'collage-maker',            title: 'Collage Maker',         icon: 'dashboard_customize',  cat: 'image',     desc: 'Multi-photo grid layouts' },
    { slug: 'image-placeholder',        title: 'Image Placeholder',     icon: 'image',                cat: 'image',     desc: 'Wireframe dummy images' },
    { slug: 'svg-optimizer',            title: 'SVG Optimizer',         icon: 'cleaning_services',    cat: 'svg',       desc: 'Clean SVG for production' },
    { slug: 'svg-wave-generator',       title: 'SVG Waves',             icon: 'water',                cat: 'svg',       desc: 'Wave section dividers' },
    { slug: 'svg-path-editor',          title: 'SVG Path Editor',       icon: 'edit',                 cat: 'svg',       desc: 'Edit SVG path data visually' },
    { slug: 'qr-code-generator',        title: 'QR Code Gen',           icon: 'qr_code_2',            cat: 'developer', desc: 'Custom QR codes with logos' },
    { slug: 'regex-tester',             title: 'Regex Tester',          icon: 'code',                 cat: 'developer', desc: 'Test & debug regex patterns' },
    { slug: 'json-formatter',           title: 'JSON Formatter',        icon: 'data_object',          cat: 'developer', desc: 'Beautify & validate JSON' },
    { slug: 'base64-encode-decode',     title: 'Base64 Encoder',        icon: 'code_blocks',          cat: 'developer', desc: 'Encode/decode Base64' },
    { slug: 'url-encode-decode',        title: 'URL Encoder',           icon: 'link',                 cat: 'developer', desc: 'Encode/decode URLs safely' },
    { slug: 'color-palette-generator',  title: 'Color Palette',         icon: 'color_lens',           cat: 'color',     desc: 'Generate color combos' },
    { slug: 'contrast-checker',         title: 'Contrast Checker',      icon: 'contrast',             cat: 'color',     desc: 'WCAG accessibility check' },
    { slug: 'px-rem-converter',         title: 'PX to REM',             icon: 'calculate',            cat: 'color',     desc: 'Convert px to rem units' },
    { slug: 'social-media-sizes',       title: 'Social Sizes',          icon: 'share',                cat: 'color',     desc: 'Platform image dimensions' },
  ];

  // ─── Detect current tool ──────────────────────────────────────────────────
  const pathname = window.location.pathname;
  const segments = pathname.split('/').filter(Boolean);
  const filename = segments[segments.length - 1] || '';
  const slug = filename.replace('.html', '');
  const currentTool = TOOLS.find(t => t.slug === slug);

  // Only run on known tool pages (not on homepage or guides)
  if (!currentTool) return;

  // Base path relative to domain root (handles /es/, /fr/, etc.)
  const isSubdir = segments.length > 1;
  const base = isSubdir ? '../' : '/';

  // ─── Inject styles ────────────────────────────────────────────────────────
  const style = document.createElement('style');
  style.textContent = `
    .sl-back-btn, .sl-share-btn {
      display: inline-flex; align-items: center; gap: 6px;
      height: 36px; padding: 0 14px; border-radius: 10px;
      background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12);
      color: #e2e8f0; font-size: 0.75rem; font-weight: 600;
      cursor: pointer; text-decoration: none; transition: all 0.2s;
      font-family: inherit; white-space: nowrap;
    }
    .sl-back-btn:hover, .sl-share-btn:hover {
      background: rgba(124,92,252,0.15); border-color: rgba(124,92,252,0.4);
      color: #fff;
    }
    .sl-back-btn .material-symbols-outlined,
    .sl-share-btn .material-symbols-outlined { font-size: 16px; }

    .sl-fab {
      position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 9000;
      display: inline-flex; align-items: center; gap: 8px;
      height: 44px; padding: 0 18px; border-radius: 9999px;
      background: linear-gradient(135deg, #7c5cfc, #a855f7);
      box-shadow: 0 8px 32px rgba(124,92,252,0.45);
      color: #fff; font-size: 0.8rem; font-weight: 700;
      cursor: pointer; border: none; transition: transform 0.2s, box-shadow 0.2s;
      font-family: inherit;
    }
    .sl-fab:hover { transform: scale(1.05); box-shadow: 0 12px 40px rgba(124,92,252,0.6); }
    .sl-fab .material-symbols-outlined { font-size: 20px; }

    .sl-panel {
      position: fixed; bottom: 0; left: 0; right: 0; z-index: 9999;
      background: rgba(8,8,20,0.97); backdrop-filter: blur(24px);
      border-top: 1px solid rgba(255,255,255,0.1);
      padding: 1.25rem 1.5rem 1.5rem;
      transform: translateY(100%); transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);
    }
    .sl-panel.sl-open { transform: translateY(0); }
    .sl-panel-inner { max-width: 80rem; margin: 0 auto; }
    .sl-panel-header {
      display: flex; align-items: center; justify-content: space-between;
      margin-bottom: 1rem;
    }
    .sl-panel-title { font-size: 0.9rem; font-weight: 700; color: #fff; margin: 0; }
    .sl-panel-close {
      background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1);
      border-radius: 8px; width: 32px; height: 32px; color: #94a3b8;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      font-size: 1rem; transition: all 0.2s;
    }
    .sl-panel-close:hover { background: rgba(255,255,255,0.1); color: #fff; }
    .sl-tools-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
      gap: 0.625rem;
    }
    .sl-tool-card {
      display: flex; flex-direction: column; gap: 6px;
      padding: 0.75rem; border-radius: 12px;
      background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
      text-decoration: none; transition: all 0.2s; cursor: pointer;
    }
    .sl-tool-card:hover {
      background: rgba(124,92,252,0.1); border-color: rgba(124,92,252,0.3);
    }
    .sl-tool-card .material-symbols-outlined { color: #7c5cfc; font-size: 20px; }
    .sl-tool-card-name { font-size: 0.75rem; font-weight: 700; color: #fff; }
    .sl-tool-card-desc { font-size: 0.68rem; color: #94a3b8; line-height: 1.3; }
    .sl-all-tools-card {
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      gap: 6px; padding: 0.75rem; border-radius: 12px;
      background: rgba(124,92,252,0.07); border: 1px solid rgba(124,92,252,0.2);
      text-decoration: none; transition: all 0.2s;
    }
    .sl-all-tools-card:hover { background: rgba(124,92,252,0.15); border-color: rgba(124,92,252,0.4); }
    .sl-all-tools-card .material-symbols-outlined { color: #7c5cfc; font-size: 24px; }
    .sl-all-tools-card span:last-child { font-size: 0.75rem; font-weight: 700; color: #7c5cfc; }

    .sl-pwa-banner {
      position: fixed; bottom: 0; left: 0; right: 0; z-index: 8999;
      background: rgba(12,12,28,0.96); backdrop-filter: blur(16px);
      border-top: 1px solid rgba(124,92,252,0.2);
      padding: 0.875rem 1.5rem;
      display: flex; align-items: center; justify-content: space-between; gap: 1rem;
      transform: translateY(0); transition: transform 0.3s ease;
    }
    .sl-pwa-banner.sl-hidden { transform: translateY(100%); }
    .sl-pwa-banner-text {
      display: flex; align-items: center; gap: 0.75rem;
      font-size: 0.82rem; color: #e2e8f0; font-weight: 500;
    }
    .sl-pwa-banner-text .material-symbols-outlined { color: #7c5cfc; font-size: 20px; flex-shrink: 0; }
    .sl-pwa-btns { display: flex; gap: 0.5rem; flex-shrink: 0; }
    .sl-pwa-install {
      background: #7c5cfc; color: #fff; border: none;
      border-radius: 8px; padding: 0.4rem 1rem;
      font-size: 0.78rem; font-weight: 700; cursor: pointer; font-family: inherit;
      transition: opacity 0.2s;
    }
    .sl-pwa-install:hover { opacity: 0.85; }
    .sl-pwa-dismiss {
      background: rgba(255,255,255,0.05); color: #94a3b8;
      border: 1px solid rgba(255,255,255,0.1); border-radius: 8px;
      padding: 0.4rem 0.75rem; font-size: 0.78rem; cursor: pointer; font-family: inherit;
    }
    @media (max-width: 480px) {
      .sl-fab span:not(.material-symbols-outlined) { display: none; }
      .sl-back-btn span:not(.material-symbols-outlined) { display: none; }
      .sl-share-btn span:not(.material-symbols-outlined) { display: none; }
      .sl-pwa-banner { flex-wrap: wrap; }
    }
  `;
  document.head.appendChild(style);

  // ─── DOM-ready actions ────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', function () {

    // 1. Inject "All Tools" + "Share" into the header
    const header = document.querySelector('header');
    if (header && !header.querySelector('.sl-back-btn')) {
      const btnGroup = document.createElement('div');
      btnGroup.style.cssText = 'display:flex;align-items:center;gap:8px;';

      // Back button
      const backBtn = document.createElement('a');
      backBtn.href = base + 'index.html';
      backBtn.className = 'sl-back-btn';
      backBtn.innerHTML = '<span class="material-symbols-outlined">arrow_back</span><span>All Tools</span>';
      btnGroup.appendChild(backBtn);

      // Share button
      const shareBtn = document.createElement('button');
      shareBtn.className = 'sl-share-btn';
      shareBtn.innerHTML = '<span class="material-symbols-outlined">share</span><span>Share</span>';
      shareBtn.addEventListener('click', function () {
        const url = window.location.href;
        const shareData = {
          title: currentTool.title + ' — StudioLimb',
          text: currentTool.desc + '. Free browser-based tool on StudioLimb.',
          url
        };
        if (navigator.share) {
          navigator.share(shareData).catch(() => {});
        } else {
          navigator.clipboard.writeText(url).then(function () {
            shareBtn.innerHTML = '<span class="material-symbols-outlined" style="color:#34d399">check</span><span style="color:#34d399">Copied!</span>';
            setTimeout(function () {
              shareBtn.innerHTML = '<span class="material-symbols-outlined">share</span><span>Share</span>';
            }, 2000);
          }).catch(() => {});
        }
      });
      btnGroup.appendChild(shareBtn);

      // Insert between first and last child of header
      const kids = Array.from(header.children);
      if (kids.length >= 2) {
        header.insertBefore(btnGroup, kids[kids.length - 1]);
      } else {
        header.appendChild(btnGroup);
      }
    }

    // 2. Make logo link back to home (if not already wrapped in an anchor)
    const logoDiv = header && header.querySelector('div.flex.items-center');
    if (logoDiv && logoDiv.tagName !== 'A' && !logoDiv.closest('a')) {
      const anchor = document.createElement('a');
      anchor.href = base + 'index.html';
      anchor.style.cssText = 'text-decoration:none;display:flex;align-items:center;gap:inherit;';
      logoDiv.parentNode.insertBefore(anchor, logoDiv);
      anchor.appendChild(logoDiv);
    }

    // 3. Build Related Tools panel
    const related = TOOLS.filter(t => t.cat === currentTool.cat && t.slug !== currentTool.slug).slice(0, 8);

    const panel = document.createElement('div');
    panel.className = 'sl-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Related Tools');
    panel.setAttribute('aria-hidden', 'true');

    let panelHTML = `
      <div class="sl-panel-inner">
        <div class="sl-panel-header">
          <p class="sl-panel-title">Related Tools</p>
          <button class="sl-panel-close" id="sl-close-panel" aria-label="Close panel">✕</button>
        </div>
        <div class="sl-tools-grid">
    `;

    related.forEach(function (tool) {
      panelHTML += `
        <a href="${base}${tool.slug}.html" class="sl-tool-card">
          <span class="material-symbols-outlined">${tool.icon}</span>
          <span class="sl-tool-card-name">${tool.title}</span>
          <span class="sl-tool-card-desc">${tool.desc}</span>
        </a>
      `;
    });

    panelHTML += `
          <a href="${base}index.html" class="sl-all-tools-card">
            <span class="material-symbols-outlined">grid_view</span>
            <span>All Tools</span>
          </a>
        </div>
      </div>
    `;

    panel.innerHTML = panelHTML;
    document.body.appendChild(panel);

    // FAB trigger
    const fab = document.createElement('button');
    fab.className = 'sl-fab';
    fab.setAttribute('aria-label', 'Show related tools');
    fab.innerHTML = '<span class="material-symbols-outlined">apps</span><span>More Tools</span>';
    document.body.appendChild(fab);

    function openPanel() {
      panel.classList.add('sl-open');
      panel.setAttribute('aria-hidden', 'false');
      fab.setAttribute('aria-expanded', 'true');
    }
    function closePanel() {
      panel.classList.remove('sl-open');
      panel.setAttribute('aria-hidden', 'true');
      fab.setAttribute('aria-expanded', 'false');
    }

    fab.addEventListener('click', openPanel);

    panel.querySelector('#sl-close-panel').addEventListener('click', closePanel);

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closePanel();
    });

    document.addEventListener('click', function (e) {
      if (panel.classList.contains('sl-open') && !panel.contains(e.target) && !fab.contains(e.target)) {
        closePanel();
      }
    });

    // 4. PWA Install Banner
    var deferredPrompt = null;
    window.addEventListener('beforeinstallprompt', function (e) {
      e.preventDefault();
      deferredPrompt = e;

      if (localStorage.getItem('sl_pwa_dismissed')) return;

      var banner = document.createElement('div');
      banner.className = 'sl-pwa-banner';
      banner.innerHTML = `
        <div class="sl-pwa-banner-text">
          <span class="material-symbols-outlined">install_desktop</span>
          Install StudioLimb for instant offline access to all 32+ tools
        </div>
        <div class="sl-pwa-btns">
          <button class="sl-pwa-install" id="sl-pwa-install">Install App</button>
          <button class="sl-pwa-dismiss" id="sl-pwa-dismiss">✕</button>
        </div>
      `;
      document.body.appendChild(banner);

      document.getElementById('sl-pwa-install').addEventListener('click', function () {
        if (deferredPrompt) {
          deferredPrompt.prompt();
          deferredPrompt.userChoice.then(function () { banner.remove(); });
        }
      });
      document.getElementById('sl-pwa-dismiss').addEventListener('click', function () {
        localStorage.setItem('sl_pwa_dismissed', '1');
        banner.classList.add('sl-hidden');
        setTimeout(function () { banner.remove(); }, 300);
      });
    });

  }); // end DOMContentLoaded

}());
