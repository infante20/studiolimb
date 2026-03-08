const CACHE_NAME = 'studiolimb-cache-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/bg-remover.html',
    '/collage-maker.html',
    '/image-cropper.html',
    '/photo-filters.html',
    '/watermark-creator.html',
    '/gradient-generator.html',
    '/glassmorphism-generator.html',
    '/box-shadow-generator.html',
    '/border-radius-visualizer.html',
    '/snowfall-premier.html',
    '/flexbox-playground.html',
    '/grid-generator.html',
    '/font-pairing.html',
    '/type-scale-generator.html',
    '/lorem-ipsum-premier.html',
    '/image-compressor.html',
    '/image-format-converter.html',
    '/image-resizer.html',
    '/svg-optimizer.html',
    '/svg-wave-generator.html',
    '/qr-code-generator.html',
    '/color-palette-generator.html',
    '/contrast-checker.html',
    '/px-rem-converter.html',
    '/social-media-sizes.html',
    '/icons/icon-192x192.png',
    '/icons/icon-512x512.png'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Cache hit - return response
                if (response) {
                    return response;
                }
                return fetch(event.request);
            }
            )
    );
});

self.addEventListener('activate', event => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
