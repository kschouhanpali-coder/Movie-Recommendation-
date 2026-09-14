<div align="center" id="top">

# 🎬 MovieVibe

**AI-powered movie & TV discovery, built with Streamlit**

Browse blockbusters, explore by mood, search by genre or actor, and get smart recommendations — all in one clean, cinematic experience.

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
  <img src="https://img.shields.io/badge/PRs-welcome-2ea44f?style=flat-square" alt="PRs welcome"/>
</p>

[**🌐 Launch Live Demo**](https://cgpgfgux5zhafhokaampwu.streamlit.app/) · [Report a Bug](https://github.com/your-username/movievibe/issues) · [Request a Feature](https://github.com/your-username/movievibe/discussions)

</div>

<br/>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Cineverse Insights](#cineverse-insights)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Credits & Contact](#credits--contact)

<br/>

## Overview

**MovieVibe** is an AI-assisted movie and TV discovery platform. Explore the latest blockbusters, timeless classics, and hidden gems — filtered by genre, mood, or search query — with real posters and IMDb ratings pulled straight from TMDB.

<div align="center">

| 🔍 Smart Search | 🎭 Genre Gallery | 🎯 Mood-Based Picks | 📊 Cineverse Insights |
|:---:|:---:|:---:|:---:|
| Title, genre, or actor | Real theatrical posters | Recommendations that match how you feel | Genre & rating analytics |

</div>

<br/>

## Features

<table width="100%">
<tr>
<th align="left" width="50%">Discovery</th>
<th align="left" width="50%">Personalization</th>
</tr>
<tr>
<td valign="top">

- **Smart Search** — find titles by name, genre, or actor instantly
- **Latest Blockbusters** — curated list of top-rated recent releases
- **Modern TV & Shows** — trending series alongside movies
- **Genre Gallery** — real theatrical posters for every category

</td>
<td valign="top">

- **Mood-Based Picks** — Happy, Sad, Excited, Thoughtful, Romantic filters
- **Watchlist** — save movies to watch later
- **Cineverse Insights** — genre distribution & rating charts
- **Full Details on TMDB** — one click through to the source page

</td>
</tr>
</table>

<br/>

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | [Streamlit](https://streamlit.io/) |
| Language | Python 3.8+ |
| Data | TMDB API, local dataset (CSV / JSON) |
| Charts | Matplotlib / Plotly |
| Styling | Custom CSS |

<br/>

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/movievibe.git
cd movievibe

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

<br/>

## Project Structure

```
movievibe/
├── app.py                     # Main Streamlit app / entry point
├── pages/                     # Multi-page sections
│   ├── search.py              #   Search page
│   ├── tv.py                  #   TV shows page
│   ├── movies.py              #   Movies page
│   └── category_explorer.py   #   Genre gallery page
├── data/                      # Local movie dataset
├── components/                # Reusable UI components
├── utils/                     # Helper functions
└── requirements.txt           # Python dependencies
```

| Path | Responsibility |
|---|---|
| `app.py` | Application entry point and routing |
| `pages/` | Individual page views — search, TV, movies, genre explorer |
| `data/` | Local movie dataset used by the app |
| `components/` | Reusable UI elements shared across pages |
| `utils/` | Shared helper functions and logic |

<br/>

## How to Use

| Step | Action |
|:---:|---|
| 1 | **Home** — browse blockbusters, classics, and TV shows |
| 2 | **Search** — type any title, genre, or actor to find matches |
| 3 | **Mood Filter** — pick a mood and get matching recommendations |
| 4 | **Category Explorer** — browse by genre with real posters |
| 5 | **Watchlist** — click **+ Watchlist** to save a title for later |
| 6 | **Full Page** — open the complete TMDB entry in one click |

<br/>

## Cineverse Insights

The built-in analytics dashboard includes:

- **Genre Distribution** — donut chart of genres across the dataset
- **IMDb Rating Distribution** — histogram of rating spread across movies

<br/>

## Deployment

Deploy on Streamlit Community Cloud for free:

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and set the main file to `app.py`
4. Click **Deploy** — no extra setup needed

<br/>

## Roadmap

- [ ] User accounts & synced watchlists
- [ ] Personalized recommendations based on viewing history
- [ ] Trailer previews embedded in movie cards
- [ ] Dark/light theme toggle
- [ ] Multi-language support

<br/>

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the project
2. Create your feature branch — `git checkout -b feature/amazing-feature`
3. Commit your changes — `git commit -m 'Add some amazing feature'`
4. Push to the branch — `git push origin feature/amazing-feature`
5. Open a pull request

<br/>

## License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution. See the [`LICENSE`](LICENSE) file for full terms.

<br/>

## Credits & Contact

<div align="center">

*"Your next favorite film is one click away."*

</div>

Have a question, found a bug, or want to suggest a feature?

| Channel | Link |
|---|---|
| 🐛 Report a Bug | [Open an Issue](https://github.com/your-username/movievibe/issues) |
| 💡 Request a Feature | [Start a Discussion](https://github.com/your-username/movievibe/discussions) |
| ⭐ Show Support | Star this repo if MovieVibe helped you find your next watch |

**Acknowledgments**

| Contribution | Powered By |
|---|---|
| Movie & TV data | TMDB (The Movie Database) API |
| Posters & artwork | TMDB image library |
| Data visualization | Matplotlib, Plotly |
| UI & styling | Streamlit, custom CSS |
| Recommendations logic | AI-assisted mood & genre matching |

<div align="center">

<sub>⭐ If this project helped you discover something great, consider giving it a star.</sub>

**[⬆ Back to top](#top)**

</div>
