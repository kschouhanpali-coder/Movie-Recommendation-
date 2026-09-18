<div align="center">

# 🎬 MovieVibe

**Pick something worth watching.**

A single-page movie discovery app — browse trending titles, search the catalogue, get picks by mood, and explore a small analytics dashboard over the collection.

![No build step](https://img.shields.io/badge/build-none-D9A441?style=flat-square)
![Vanilla JS](https://img.shields.io/badge/javascript-vanilla-B5384B?style=flat-square)
![Single file](https://img.shields.io/badge/files-1%20html-4C8577?style=flat-square)
![License MIT](https://img.shields.io/badge/license-MIT-8C5A1E?style=flat-square)

</div>

---

## ✨ Features

| | |
|---|---|
| 🏠 **Home** | A featured title of the day, plus "Trending picks" and "Newly added" rows |
| 🔍 **Search** | Live filter across title and genre as you type |
| 🎭 **Moods** | Five mood chips — Happy, Sad, Excited, Thoughtful, Romantic — each surfacing a matching shortlist |
| 📊 **Insights** | Catalogue stats, a genre-mix doughnut chart, and a rating-distribution bar chart |
| ⭐ **Watchlist** | Add titles from the hero or detail view; saved locally and persists on reload |
| 🌗 **Theme toggle** | Switch between dark and light in one click |

---

## 🛠️ Tech stack

- **Plain HTML, CSS, and vanilla JavaScript** — no framework, no build tools
- **[Chart.js](https://www.chartjs.org/)** (via CDN) for the Insights charts
- **Google Fonts** — Bebas Neue for headlines, Manrope for body text
- **`localStorage`** for watchlist persistence — data stays on your device only

---

## 📁 Files

```
movievibe.html   the entire app — structure, styles, data, and logic in one file
README.md        this file
```

---

## 🚀 Running it

No install required.

**Quickest** — double-click `movievibe.html`, or open it from your browser's File → Open menu.

**Local server** (recommended if fonts or scripts don't load from a `file://` path):
```bash
cd path/to/project
python3 -m http.server 8000
# then open http://localhost:8000/movievibe.html
```

**Deploy** — since it's one static file, it works as-is on GitHub Pages, Netlify, Vercel, or any static host.

---

## 🎞️ Customizing the catalogue

All movie data lives in one array near the top of the `<script>` block:

```js
var MOVIES = [
  {id:1, title:"...", year:1994, genre:"Drama", runtime:142, rating:9.3,
   moods:["thoughtful","sad"], blurb:"..."},
  ...
];
```

To add a title, append an object with a unique `id`.

- `genre` should match one of the keys in `GENRE_STYLE` — it drives the poster color and icon
- `moods` should be a subset of the keys in `MOOD_META`

Everything else — hero rotation, search, mood filtering, and the Insights charts — recomputes automatically from this array, so nothing else needs to change for ordinary edits.

> Posters are generated, not photographed: each is a colored gradient (keyed by genre) with the title's first letter set in the display typeface — so there are no external image files or licensing concerns to manage.

---

## 📝 Notes

- Everything runs client-side — no server, database, or API key involved
- The watchlist is stored per-browser via `localStorage`, so it won't sync across devices and clears if you clear browser data
- Chart colors and fonts follow the app's CSS custom properties, so they adapt automatically when you switch the light/dark theme

<div align="center">

Made for movie nights. 🍿

</div>
