<div align="center">

# 🎬 MovieVibe

**AI-Powered Movie & TV Discovery**

Discover your next favorite film. Browse blockbusters, explore by mood, search by genre or actor, and get AI-powered recommendations — all in one cinematic experience.

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Launch_App-FF4B4B?style=for-the-badge)](https://cgpgfgux5zhafhokaampwu.streamlit.app/)
![Status](https://img.shields.io/badge/status-live-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#️-project-structure)
- [How to Use](#-how-to-use)
- [Cineverse Insights](#-cineverse-insights)
- [Deployment](#-deployment)
- [Contributing](#-contributing)

---

## 🎥 Overview

**MovieVibe** is an AI-powered movie and TV show discovery platform. Explore the latest blockbusters, timeless classics, and hidden gems — filtered by genre, mood, or search query. With real movie posters and IMDb data built in, it brings the cinema straight to your browser.

---

## 🌐 Live Demo

<div align="center">

### 👉 [**Launch MovieVibe**](https://cgpgfgux5zhafhokaampwu.streamlit.app/)

*Runs live in your browser — no installation required.*

</div>

---

## ✨ Features

<table>
<tr>
<td valign="top" width="50%">

### 🔍 Discovery
- **Smart Search** — search by title, genre, or actor instantly
- **Latest Blockbusters** — curated list of top-rated recent releases
- **Modern TV & Shows** — trending series alongside movies
- **Genre Gallery** — real theatrical posters for every category

</td>
<td valign="top" width="50%">

### 🎯 Personalization
- **Mood-Based Picks** — Happy, Sad, Excited, Thoughtful, Romantic filters
- **Watchlist** — save movies to watch later
- **Cineverse Insights** — genre distribution & IMDb rating charts
- **Watch Real Page** — direct links to TMDB for full movie details

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Framework** | [Streamlit](https://streamlit.io/) |
| **Language** | Python |
| **Data** | Built-in movie dataset (CSV / JSON) |
| **Charts** | Matplotlib / Plotly |
| **Styling** | Custom CSS |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

**1. Clone the repository**
```bash
git clone https://github.com/your-username/movievibe.git
cd movievibe
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` 🎬

---

## 🗂️ Project Structure

```bash
movievibe/
├── app.py                    # Main Streamlit app
├── pages/                    # Multi-page sections
│   ├── search.py             # Search page
│   ├── tv.py                 # TV Shows page
│   ├── movies.py             # Movies page
│   └── category_explorer.py  # Genre gallery page
├── data/                     # Local movie dataset
├── components/                # Reusable UI components
├── utils/                     # Helper functions
└── requirements.txt           # Python dependencies
```

---

## 🎯 How to Use

| Step | Action |
|---|---|
| 1️⃣ | **Home** — Browse blockbusters, classics, and TV shows |
| 2️⃣ | **Search** — Type any title, genre, or actor to find movies |
| 3️⃣ | **Mood Filter** — Pick your mood and get matching recommendations |
| 4️⃣ | **Category Explorer** — Browse by genre with real movie posters |
| 5️⃣ | **Watchlist** — Click `+ Watchlist` to save movies for later |
| 6️⃣ | **Watch Real Page** — Click to open the full TMDB movie page |

---

## 📊 Cineverse Insights

The built-in analytics dashboard includes:

- **Genre Distribution** — donut chart of genres across the dataset
- **IMDb Rating Distribution** — histogram of rating spread across movies

---

## ☁️ Deployment

**Deploy on Streamlit Cloud (Free):**

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and set the main file as `app.py`
4. Click **Deploy** — that's it, no extra setup needed! 🚀

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request
