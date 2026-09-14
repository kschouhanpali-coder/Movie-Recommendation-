<div align="center" id="top">

# 🎬 MOVIEVIBE

<img src="https://img.shields.io/badge/-%F0%9F%8E%AC%20AI--POWERED%20MOVIE%20%26%20TV%20DISCOVERY%20%F0%9F%8E%AC-1a1a1a?style=flat-square&labelColor=1a1a1a&color=FF4B4B" alt="AI-Powered Movie & TV Discovery"/>

### 🍿 Discover your next favorite film

Browse blockbusters, explore by mood, search by genre or actor, and get AI-powered recommendations — all in one cinematic experience.

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib"/>
  <img src="https://img.shields.io/badge/TMDB-01D277?style=for-the-badge&logo=themoviedatabase&logoColor=white" alt="TMDB"/>
</p>

<p>
  <img src="https://img.shields.io/badge/status-live-2ea44f?style=flat-square" alt="status"/>
  <img src="https://img.shields.io/badge/license-MIT-FF4B4B?style=flat-square" alt="license"/>
  <img src="https://img.shields.io/badge/data-TMDB%20API-01D277?style=flat-square" alt="TMDB data"/>
  <img src="https://img.shields.io/badge/AI--assisted-recommendations-2ea44f?style=flat-square" alt="AI-assisted recommendations"/>
  <img src="https://img.shields.io/badge/PRs-welcome-FF4B4B?style=flat-square" alt="PRs welcome"/>
</p>

<br/>

### 🌐 Live Demo

[![🌐 Launch MovieVibe](https://img.shields.io/badge/🌐_LAUNCH_MOVIEVIBE-FF4B4B?style=for-the-badge&labelColor=1a1a1a)](https://cgpgfgux5zhafhokaampwu.streamlit.app/)

<sub>🎞️ Runs live in your browser · No installation required</sub>

</div>

<br/>

## 📖 Table of Contents

| | | |
|---|---|---|
| [🎥 Overview](#-overview) | [✨ Features](#-features) | [🛠️ Tech Stack](#️-tech-stack) |
| [🚀 Getting Started](#-getting-started) | [🗂️ Project Structure](#️-project-structure) | [🎯 How to Use](#-how-to-use) |
| [📊 Cineverse Insights](#-cineverse-insights) | [☁️ Deployment](#️-deployment) | [🧭 Roadmap](#-roadmap) |
| [🌐 Live Demo](#-live-demo) | [🤝 Contributing](#-contributing) | [📄 License](#-license) |
| [👤 Credits & Contact](#-credits--contact) | | |

<br/>

---

## 🎥 Overview

**MovieVibe** is an AI-powered movie and TV show discovery platform. Explore the latest blockbusters, timeless classics, and hidden gems — filtered by genre, mood, or search query. With real movie posters and IMDb data built in, it brings the cinema straight to your browser.

<div align="center">

| 🔍 | 🎭 | 🎯 | 📊 |
|:---:|:---:|:---:|:---:|
| **Smart Search**<br/>Title, genre, or actor | **Genre Gallery**<br/>Real theatrical posters | **Mood-Based Picks**<br/>Recommendations that match how you feel | **Cineverse Insights**<br/>Genre & rating analytics |

</div>

<br/>

---

## ✨ Features

<table width="100%">
<tr>
<th align="left" width="50%">🔍 Discovery</th>
<th align="left" width="50%">🎯 Personalization</th>
</tr>
<tr>
<td valign="top">

- 🔎 **Smart Search** — search by title, genre, or actor instantly
- 🎬 **Latest Blockbusters** — curated list of top-rated recent releases
- 📺 **Modern TV & Shows** — trending series alongside movies
- 🖼️ **Genre Gallery** — real theatrical posters for every category

</td>
<td valign="top">

- 🎭 **Mood-Based Picks** — Happy, Sad, Excited, Thoughtful, Romantic filters
- ⭐ **Watchlist** — save movies to watch later
- 📊 **Cineverse Insights** — genre distribution & IMDb rating charts
- 🔗 **Watch Real Page** — direct links to TMDB for full movie details

</td>
</tr>
</table>

<br/>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---:|---|
| 🎈 **Framework** | [Streamlit](https://streamlit.io/) |
| 🐍 **Language** | Python |
| 🗃️ **Data** | Built-in movie dataset (CSV / JSON) |
| 📊 **Charts** | Matplotlib / Plotly |
| 🎨 **Styling** | Custom CSS |

</div>

<br/>

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.8+
- pip

<table>
<tr><td>

**1️⃣ Clone the repository**
```bash
git clone https://github.com/your-username/movievibe.git
cd movievibe
```

**2️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**3️⃣ Run the app**
```bash
streamlit run app.py
```

🎬 The app will open at `http://localhost:8501`

</td></tr>
</table>

<br/>

---

## 🗂️ Project Structure

```bash
movievibe/
├── app.py                     # 🎬 Main Streamlit app
├── pages/                     # 📄 Multi-page sections
│   ├── search.py              #   ├─ Search page
│   ├── tv.py                  #   ├─ TV Shows page
│   ├── movies.py              #   ├─ Movies page
│   └── category_explorer.py   #   └─ Genre gallery page
├── data/                      # 🗃️ Local movie dataset
├── components/                # 🧩 Reusable UI components
├── utils/                     # 🔧 Helper functions
└── requirements.txt           # 📦 Python dependencies
```

<div align="center">

| Path | Responsibility |
|---|---|
| `app.py` | Application entry point and routing |
| `pages/` | Individual page views — search, TV, movies, genre explorer |
| `data/` | Local movie dataset used by the app |
| `components/` | Reusable UI elements shared across pages |
| `utils/` | Shared helper functions and logic |

</div>

<br/>

---

## 🎯 How to Use

<div align="center">

| Step | Action |
|:---:|---|
| 1️⃣ | **Home** — Browse blockbusters, classics, and TV shows |
| 2️⃣ | **Search** — Type any title, genre, or actor to find movies |
| 3️⃣ | **Mood Filter** — Pick your mood and get matching recommendations |
| 4️⃣ | **Category Explorer** — Browse by genre with real movie posters |
| 5️⃣ | **Watchlist** — Click `+ Watchlist` to save movies for later |
| 6️⃣ | **Watch Real Page** — Click to open the full TMDB movie page |

</div>

<br/>

---

## 📊 Cineverse Insights

The built-in analytics dashboard includes:

- 🍩 **Genre Distribution** — donut chart of genres across the dataset
- 📈 **IMDb Rating Distribution** — histogram of rating spread across movies

<br/>

---

## ☁️ Deployment

**Deploy on Streamlit Cloud (Free):**

1. 🚀 Push your code to GitHub
2. 🌐 Go to [share.streamlit.io](https://share.streamlit.io)
3. ➕ Connect your repo and set the main file as `app.py`
4. ✅ Click **Deploy** — that's it, no extra setup needed!

<br/>

---

## 🌐 Live Demo

<div align="center">

### 🌐 Live Demo

[![🌐 Launch MovieVibe](https://img.shields.io/badge/🌐_LAUNCH_MOVIEVIBE-FF4B4B?style=for-the-badge&labelColor=1a1a1a)](https://cgpgfgux5zhafhokaampwu.streamlit.app/)

<sub>🎞️ Runs live in your browser · No installation required</sub>

</div>

<br/>

---

## 🧭 Roadmap

| Status | Feature |
|:---:|---|
| ⏳ | User accounts & synced watchlists |
| ⏳ | Personalized recommendations via viewing history |
| ⏳ | Trailer previews embedded in movie cards |
| ⏳ | Dark/light theme toggle |
| ⏳ | Multi-language support |

<br/>

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

<table>
<tr><td>

1. 🍴 Fork the project
2. 🌱 Create your feature branch — `git checkout -b feature/amazing-feature`
3. 💾 Commit your changes — `git commit -m 'Add some amazing feature'`
4. 🚀 Push to the branch — `git push origin feature/amazing-feature`
5. 🔁 Open a pull request

</td></tr>
</table>

<br/>

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution. See the `LICENSE` file for full terms.

<br/>

---

## 👤 Credits & Contact

<div align="center">

### 🎬 Made with precision — MovieVibe

*"Your next favorite film is one click away."*

<br/>

</div>

**Have a question, found a bug, or want to suggest a feature?**

| Channel | Link |
|:---:|---|
| 🐛 Report a Bug | [Open an Issue](https://github.com/your-username/movievibe/issues) |
| 💡 Request a Feature | [Start a Discussion](https://github.com/your-username/movievibe/discussions) |
| ⭐ Show Support | Star this repo if MovieVibe helped you find your next watch! |

**Acknowledgments**

| Contribution | Powered By |
|---|---|
| 🎞️ Movie & TV Data | TMDB (The Movie Database) API |
| 🖼️ Posters & Artwork | TMDB image library |
| 📈 Data Visualization | Matplotlib, Plotly |
| 🎨 UI & Styling | Streamlit, Custom CSS |
| 🤖 Recommendations Logic | AI-assisted mood & genre matching |

<div align="center">

<br/>

<img src="https://img.shields.io/badge/Made_with-🎬_MovieVibe-1a1a1a?style=for-the-badge&labelColor=1a1a1a&color=FF4B4B" alt="Made with MovieVibe"/>

<sub>⭐ If this project helped you discover something great, consider giving it a star.</sub>

<br/>

**[⬆ Back to top](#top)**

</div>
