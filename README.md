# Movie-Recommendation-

AI-powered movie discovery app. Browse blockbusters, TV shows & classics. Search by title, genre, or actor. Explore mood-based picks, genre galleries, and real-time IMDb insights. Add to watchlist & find your next watch instantly. Built with real TMDB data.

# 🎬 MovieVibe — AI Movie Recommendation App

> *Discover your next favorite film. Browse blockbusters, explore by mood, search by genre or actor, and get AI-powered recommendations — all in one cinematic experience.*

![MovieVibe](https://img.shields.io/badge/status-live-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

---

## 🌐 Live Demo

**👉 [Launch MovieVibe](https://cgpgfgux5zhafhokaampwu.streamlit.app/)**

> Runs live in your browser — no installation required.

---

## 🎥 What is MovieVibe?

**MovieVibe** is an AI-powered movie and TV show discovery platform. Explore the latest blockbusters, timeless classics, and hidden gems — filtered by genre, mood, or search query. With real movie posters and IMDb data built-in, it brings the cinema straight to your browser.

---

## ✨ Features

- 🔍 **Smart Search** — Search by title, genre, or actor instantly
- 🏆 **Latest Blockbusters** — Curated list of top-rated recent releases
- 📺 **Modern TV & Shows** — Discover trending series alongside movies
- 🎭 **Genre Gallery** — Real theatrical posters for every cinematic category
- 😊 **Mood-Based Picks** — Happy, Sad, Excited, Thoughtful, Romantic filters
- 📊 **Cineverse Insights** — Genre distribution & IMDb rating charts
- ❤️ **Watchlist** — Save movies to watch later
- 🔗 **Watch Real Page** — Direct links to TMDB for full movie details

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | [Streamlit](https://streamlit.io/) |
| Language | Python |
| Data | Built-in movie dataset (CSV / JSON) |
| Charts | Matplotlib / Plotly |
| Styling | Custom CSS |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movievibe.git
cd movievibe
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🗂️ Project Structure

```
movievibe/
├── app.py                    # Main Streamlit app
├── pages/                    # Multi-page sections
│   ├── search.py             # Search page
│   ├── tv.py                 # TV Shows page
│   ├── movies.py             # Movies page
│   └── category_explorer.py  # Genre gallery page
├── data/                     # Local movie dataset
├── components/               # Reusable UI components
├── utils/                    # Helper functions
└── requirements.txt          # Python dependencies
```

---

## 🎯 How to Use

1. **Home** — Browse blockbusters, classics, and TV shows
2. **Search** — Type any title, genre, or actor to find movies
3. **Mood Filter** — Pick your mood and get matching recommendations
4. **Category Explorer** — Browse by genre with real movie posters
5. **Watchlist** — Click `+ Watchlist` to save movies for later
6. **Watch Real Page** — Click to open the full TMDB movie page

---

## 📊 Cineverse Insights

The built-in analytics dashboard includes:

- **Genre Distribution** — Donut chart of genres across the dataset
- **IMDb Rating Distribution** — Histogram of rating spread across movies

---

## 🌐 Deployment

### Deploy on Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and set the main file as `app.py`
4. Click **Deploy** — that's it, no extra setup needed!

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

---

## 📄 License

MIT © 2026 — Built with ❤️ and a love for cinema.
