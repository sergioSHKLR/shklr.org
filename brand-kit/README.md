# SHKLR — brand kit

From the SHKLR brand kit (rev 4, 22 Nov 2026: Chief’s icon revision, stroke 2, grey plates, Martian Mono brand font; rev 3 approved 19 Nov 2026). Generated; update from the kit, not by hand.

## SHKLR

- Tagline: “Educação moral e ética.”
- Mode: dual (light + dark plates)
- Plate light **#ffffff** — glyph #7c3aed ring 5.7:1
- Plate dark **#1a1a1a** — glyph #a78bfa ring 6.4:1

Files in `shklr/`:
- `icons/` master SVGs (glyph, tile, square, maskable, mono); `icons/flat/` flat copies for simple SVG tools (no groups, transforms, clips or arcs).
- `png/` tile PNGs 16–1024, maskable and apple-touch.
- `web/` site drop-ins: favicon.svg (bare stroke glyph, transparent, dark-tab colours via prefers-color-scheme) + favicon.ico/16/32/48 (transparent), apple-touch-icon, icon-192/512, maskable, monochrome, manifest.webmanifest, meta-head.html, splash/ (iOS).
- `wordmark/` wordmark and lockups (SVG, flat SVG, PNG), all text outlined.
- `social/` og-1200x630, x-card-1200x600, github-card-1280x640 (repo social preview), whatsapp, Instagram sizes.

## Type
- Brand (`--font-brand`: wordmarks, logo text, brand titles): **Martian Mono 1.000, condensed** (wdth 75; `fonts/martian-mono/`, OFL 1.1, self-hosted — no Google Fonts CDN). Replaces SHKLR Mono Narrow.
- UI (`--font-ui`: controls, nav, labels, body UI text): system stack `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif` — no webfont.
- Reading serif: `ui-serif, Georgia, Cambria, "Times New Roman", serif`.

## Rules
- The plate is the app’s real surface colour; glyph colours ≥ 3:1 against it, text ≥ 4.5:1.
- Wordmarks: uppercase Martian Mono Bold (condensed), +0.02em, ink #111111 on light / #f2f2f2 on dark.
- Clear space 25% of the tile; minimum tile 16 px.

`tokens/` holds the colour and type tokens for SHKLR only.
