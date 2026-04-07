const CACHE_NAME = 'studiolimb-cache-v3';
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
  // PWA Icons
  '/icons/icon-192x192.png',
  '/icons/icon-512x512.png',
  '/manifest.json',
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
  // Only handle GET requests for same-origin or CDN assets
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;

      return fetch(event.request).then(response => {
        // Cache successful same-origin responses
        if (
          response.ok &&
          (event.request.url.startsWith(self.location.origin) ||
           event.request.url.includes('fonts.googleapis.com') ||
           event.request.url.includes('fonts.gstatic.com'))
        ) {
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
