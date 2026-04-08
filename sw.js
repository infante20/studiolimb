const CACHE_NAME = 'studiolimb-cache-v5';
const urlsToCache = [
  '/',
  '/index.html',
  '/shared.js',
  // CSS Generators
  '/gradient-generator.html',
  '/glassmorphism-generator.html',
  '/box-shadow-generator.html',
  '/border-radius-visualizer.html',
  '/css-triangle-generator.html',
  '/snowfall-premier.html',
  // Typography & Layout
  '/flexbox-playground.html',
  '/grid-generator.html',
  '/font-pairing.html',
  '/type-scale-generator.html',
  '/lorem-ipsum-premier.html',
  // Image & Assets
  '/image-compressor.html',
  '/image-resizer.html',
  '/image-cropper.html',
  '/image-format-converter.html',
  '/bg-remover.html',
  '/photo-filters.html',
  '/watermark-creator.html',
  '/collage-maker.html',
  '/image-placeholder.html',
  // SVG
  '/svg-optimizer.html',
  '/svg-wave-generator.html',
  '/svg-path-editor.html',
  // Developer Utilities
  '/qr-code-generator.html',
  '/regex-tester.html',
  '/json-formatter.html',
  '/base64-encode-decode.html',
  '/url-encode-decode.html',
  // Color & Utilities
  '/color-palette-generator.html',
  '/contrast-checker.html',
  '/px-rem-converter.html',
  '/social-media-sizes.html',
  // Guides
  '/guides/index.html',
  '/guides/modern-web-design-essentials.html',
  '/guides/css-box-shadow-techniques.html',
  '/guides/css-flexbox-vs-grid.html',
  '/guides/glassmorphism-css-tutorial.html',
  '/guides/optimize-images-for-web.html',
  '/guides/svg-vs-png-vs-webp.html',
  '/guides/wcag-color-contrast-guide.html',
  // Legal & Info
  '/contact.html',
  '/privacy-policy.html',
  '/terms.html',
  // PWA Icons
  '/icons/icon-192x192.png',
  '/icons/icon-512x512.png',
  '/manifest.json',
];

// CDN assets to cache on first fetch (network-first, then cache)
const CDN_CACHE_PATTERNS = [
  'cdn.tailwindcss.com',
  'fonts.googleapis.com',
  'fonts.gstatic.com',
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(names =>
      Promise.all(
        names
          .filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  const url = event.request.url;
  const isCDN = CDN_CACHE_PATTERNS.some(pattern => url.includes(pattern));

  if (isCDN) {
    // Stale-while-revalidate for CDN assets (fonts, Tailwind)
    // Serve from cache immediately, update cache in background
    event.respondWith(
      caches.open(CACHE_NAME).then(cache =>
        cache.match(event.request).then(cached => {
          const fetchPromise = fetch(event.request).then(response => {
            if (response.ok) {
              cache.put(event.request, response.clone());
            }
            return response;
          }).catch(() => cached);

          return cached || fetchPromise;
        })
      )
    );
    return;
  }

  // Cache-first for same-origin assets
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;

      return fetch(event.request).then(response => {
        if (response.ok && url.startsWith(self.location.origin)) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        }
        return response;
      }).catch(() => {
        // Offline fallback for navigation requests
        if (event.request.mode === 'navigate') {
          return caches.match('/index.html');
        }
      });
    })
  );
});
