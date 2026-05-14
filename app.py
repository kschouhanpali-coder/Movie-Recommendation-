"""
🎬 MovieVibe — The World-Class AI Movie Experience
Inspired by Netflix, JioHotstar & 21st.dev.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import random
import os
import sys

# Ensure local modules are found on Streamlit Cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Debug: Check if file exists
if not os.path.exists(os.path.join(current_dir, "data_preprocessing.py")):
    st.error(f"Critical Error: 'data_preprocessing.py' not found in {current_dir}. Please ensure all files are pushed to GitHub.")
    st.stop()

from data_preprocessing import (
    load_and_clean_data, get_all_genres, get_all_languages,
    get_year_range, get_rating_range, MOOD_GENRE_MAP,
)
from recommendation_engine import RecommendationEngine
from styles import MAIN_CSS, make_card_html, render_hero, REAL_POSTER_MAP, get_tmdb_data

# Global Activation State (Using Curated Collection by Default)
tmdb_k = None

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="MovieVibe — AI Movie Recommendations",
                   page_icon="🎬", layout="wide", initial_sidebar_state="collapsed")
st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Cached Data & Engine ─────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_data(v=2.4):
    """Load the full raw dataset (cached)."""
    return load_and_clean_data()

@st.cache_resource(show_spinner=False)
def build_engine(_df, v=2.4):
    """Build the recommendation engine from a specific dataframe."""
    return RecommendationEngine(_df)

with st.spinner("🎬 Initializing MovieVibe Experience…"):
    # 1. Load full data (using version 2.4 to clear cache)
    full_df = load_data(v=2.4)
    
    # 2. 🎯 Strictly Filter: Only show movies with verified high-quality posters
    # This must be outside the cache to update when REAL_POSTER_MAP changes
    verified_titles = set(REAL_POSTER_MAP.keys())
    df = full_df[full_df["movie_title"].isin(verified_titles)].copy()
    
    # 3. Build engine from FILTERED data
    engine = build_engine(df, v=2.4)

ALL_GENRES = get_all_genres(df)
ALL_LANGS = get_all_languages(df)
YR_MIN, YR_MAX = get_year_range(df)
RT_MIN, RT_MAX = get_rating_range(df)

# ── Session State ────────────────────────────────────────────────────────────
for key, default in [("watchlist", []), ("search_query", ""), ("mood", None), ("nav", "Home"), ("selected_movie", None)]:
    if key not in st.session_state:
        st.session_state[key] = default

# ── Sidebar (Premium Navigation & Settings) ──────────────────────────────────
with st.sidebar:
    st.markdown('<h1 style="color: var(--red); font-family: Montserrat; font-weight: 900; font-size: 1.8rem; margin: 10px 20px;">MOVIEVIBE</h1>', unsafe_allow_html=True)
    
    # 1. Main Menu
    st.markdown('<div class="sidebar-header">Menu</div>', unsafe_allow_html=True)
    nav_items = [
        ("Home", "🏠"),
        ("Search", "🔍"),
        ("TV", "📺"),
        ("Movie", "🎞️")
    ]
    
    for item, icon in nav_items:
        is_active = st.session_state.nav == item
        btn_class = "nav-link active" if is_active else "nav-link"
        if st.button(f"{icon} {item}", key=f"nav_{item}", use_container_width=True, type="secondary"):
            st.session_state.nav = item
            st.rerun()

    # 3. Explorer
    st.markdown('<div class="sidebar-header">Discover</div>', unsafe_allow_html=True)
    if st.button("📂 Category Explorer", key="nav_cat", use_container_width=True):
        st.session_state.nav = "Category"
        st.rerun()

    # 4. Watchlist Export
    if st.session_state.watchlist:
        st.markdown('<div class="sidebar-header">My Collection</div>', unsafe_allow_html=True)
        watchlist_df = df[df["movie_title"].isin(st.session_state.watchlist)]
        csv = watchlist_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="💾 Download Watchlist (CSV)",
            data=csv,
            file_name="movievibe_watchlist.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.sidebar.markdown('<div style="margin-top: 100%;"></div>', unsafe_allow_html=True)

# ── Main Feed Logic ──────────────────────────────────────────────────────────

if st.session_state.nav == "Home":
    # 0. Hero (Prioritize Real Posters)
    real_hits = df[df["movie_title"].isin(REAL_POSTER_MAP.keys())]
    hero_movie = real_hits.iloc[0] if not real_hits.empty else df.iloc[0]
    st.markdown(render_hero(hero_movie, tmdb_k), unsafe_allow_html=True)
    
    # 1. Latest Blockbusters (Prioritize Real Posters)
    st.markdown('<div class="section-title">🎞️ Latest Blockbusters <span class="see-all">See All →</span></div>', unsafe_allow_html=True)
    recent = pd.concat([real_hits, df[df["title_year"] >= 2015]]).drop_duplicates(subset=["movie_title"]).head(12)
    recent_html = "".join([make_card_html(row, row["movie_title"] in st.session_state.watchlist, tmdb_k, i) for i, (_, row) in enumerate(recent.iterrows())])
    st.markdown(f'<div class="scroll-container">{recent_html}</div>', unsafe_allow_html=True)

    # 2. Realistic & High-Rated
    st.markdown('<div class="section-title">💎 Masterpieces & Classics</div>', unsafe_allow_html=True)
    masterpieces = df.sort_values(by="imdb_score", ascending=False).head(15)
    # Hero Search Bar
    st.markdown('<div style="margin-top: -50px; margin-bottom: 50px;">', unsafe_allow_html=True)
    home_query = st.text_input("Search our curated masterpiece collection...", key="home_search", 
                               placeholder="🔍 Search Inception, Iron Man, RRR...", label_visibility="collapsed")
    if home_query:
        st.session_state.search_query = home_query
        st.session_state.nav = "Search"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # 1. Recently Added (Premium Hero)
    st.markdown('<div class="section-title">✨ Newly Added Masterpieces</div>', unsafe_allow_html=True)
    trending = df[df["title_year"] >= 2010].sort_values(by="imdb_score", ascending=False).head(15)
    trending_html = "".join([make_card_html(row, row["movie_title"] in st.session_state.watchlist, tmdb_k, i) for i, (_, row) in enumerate(trending.iterrows())])
    st.markdown(f'<div class="scroll-container">{trending_html}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🎭 How are you feeling today?</div>', unsafe_allow_html=True)
    moods = [("happy", "😊"), ("sad", "😢"), ("excited", "😱"), ("thoughtful", "🤔"), ("romantic", "❤️")]
    cols = st.columns(len(moods))
    for i, (m, e) in enumerate(moods):
        with cols[i]:
            if st.button(f"{e}\n{m.title()}", use_container_width=True, key=f"mood_{m}"):
                st.session_state.mood = m

    if st.session_state.mood:
        mood_res = engine.mood_recommend(st.session_state.mood, top_n=10)
        st.markdown(f'<div class="section-title">✨ Mood: {st.session_state.mood.title()} Picks</div>', unsafe_allow_html=True)
        mood_html = "".join([make_card_html(row, row["movie_title"] in st.session_state.watchlist, tmdb_k, i) for i, (_, row) in enumerate(mood_res.iterrows())])
        st.markdown(f'<div class="scroll-container">{mood_html}</div>', unsafe_allow_html=True)

elif st.session_state.nav == "Search":
    # 🔍 Premium Search Interface
    st.markdown('<div class="section-title" style="font-size: 3rem; margin-top: 5rem; text-align:center;">🔍 Explore MovieVibe</div>', unsafe_allow_html=True)
    
    # Search Row with Input and Buttons
    s_col1, s_col2, s_col3 = st.columns([6, 1, 1])
    with s_col1:
        query = st.text_input("Search", value=st.session_state.search_query, 
                              placeholder="Type a title, genre, or actor (e.g. Inception)...", 
                              key="main_search_input", label_visibility="collapsed")
    with s_col2:
        if st.button("Search", use_container_width=True, type="primary"):
            st.session_state.search_query = query
            st.rerun()
    with s_col3:
        if st.button("Clear", use_container_width=True):
            st.session_state.search_query = ""
            st.rerun()

    # Trigger search if query changed via Enter key
    if query != st.session_state.search_query:
        st.session_state.search_query = query
        st.rerun()

    if st.session_state.search_query:
        results = engine.search(st.session_state.search_query, top_n=20)
        
        if not results.empty:
            st.markdown(render_hero(results.iloc[0], tmdb_k), unsafe_allow_html=True)
            st.markdown(f'<div class="section-title">🎯 Top Results for "{st.session_state.search_query}"</div>', unsafe_allow_html=True)
            
            # Grid layout for search results
            for i in range(0, len(results), 4):
                cols = st.columns(4)
                for j in range(4):
                    if i + j < len(results):
                        row = results.iloc[i + j]
                        cols[j].markdown(make_card_html(row, row["movie_title"] in st.session_state.watchlist, tmdb_k, i+j), unsafe_allow_html=True)
        else:
            st.warning(f"No matches found for '{st.session_state.search_query}'.")
            st.info("Try searching for 'Action', 'RRR', or 'Christopher Nolan'.")
    else:
        # Show some trending suggestions when search is empty
        st.markdown('<div class="section-title">🔥 Trending Suggestions</div>', unsafe_allow_html=True)
        trending = df.sample(8)
        trending_html = "".join([make_card_html(row, row["movie_title"] in st.session_state.watchlist, tmdb_k, i) for i, (_, row) in enumerate(trending.iterrows())])
        st.markdown(f'<div class="scroll-container">{trending_html}</div>', unsafe_allow_html=True)

elif st.session_state.nav == "TV":
    # Modern Hero for TV (2010+)
    tv_genres = ['Animation', 'Documentary', 'Family', 'Reality-TV', 'Game-Show']
    tv_df_full = df[(df["title_year"] >= 2005) & (df["genre_list"].apply(lambda l: any(g in l for g in tv_genres)))].sort_values(by="imdb_score", ascending=False)
    
    if not tv_df_full.empty:
        st.markdown(render_hero(tv_df_full.iloc[0], tmdb_k), unsafe_allow_html=True)
        st.markdown('<div class="section-title">📺 Modern TV & Shows</div>', unsafe_allow_html=True)
        tv_df = tv_df_full.head(20)
        tv_html = "".join([make_card_html(row, row["movie_title"] in st.session_state.watchlist, tmdb_k, i) for i, (_, row) in enumerate(tv_df.iterrows())])
        st.markdown(f'<div class="scroll-container">{tv_html}</div>', unsafe_allow_html=True)
    else:
        st.info("No modern TV shows found in the current dataset.")

elif st.session_state.nav == "Movie":
    # Modern Hero for Movie (2010+)
    movie_df_full = df[df["title_year"] >= 2010].sort_values(by="imdb_score", ascending=False)
    
    if not movie_df_full.empty:
        st.markdown(render_hero(movie_df_full.iloc[0], tmdb_k), unsafe_allow_html=True)
        st.markdown('<div class="section-title">🎞️ Modern Blockbusters</div>', unsafe_allow_html=True)
        movie_df = movie_df_full.head(20)
        movie_html = "".join([make_card_html(row, row["movie_title"] in st.session_state.watchlist, tmdb_k, i) for i, (_, row) in enumerate(movie_df.iterrows())])
        st.markdown(f'<div class="scroll-container">{movie_html}</div>', unsafe_allow_html=True)

elif st.session_state.nav == "Category":
    st.markdown('<div class="section-title" style="font-size: 3.5rem; margin-top: 5rem; text-align: center;">🎞️ Real-Life Genre Gallery</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: var(--text-secondary); margin-bottom: 3rem; font-size: 1.2rem;">Authentic theatrical posters for every cinematic category.</p>', unsafe_allow_html=True)
    
    # Map Genres to Hero Movies with Real Posters
    GENRE_HERO_MAP = {
        "Action": "The Avengers",
        "Adventure": "Interstellar",
        "Animation": "Toy Story",
        "Comedy": "Deadpool",
        "Crime": "Se7en",
        "Drama": "The Shawshank Redemption",
        "Family": "Finding Nemo",
        "Fantasy": "Maleficent",
        "Mystery": "Inception",
        "Romance": "Titanic",
        "Sci-Fi": "Avengers: Endgame",
        "Thriller": "Fight Club",
        "Bollywood": "RRR"
    }
    
    cols = st.columns(4)
    # Iterate over our curated hero map to ensure quality
    for i, genre in enumerate(GENRE_HERO_MAP.keys()):
        hero_title = GENRE_HERO_MAP[genre]
        # Get the real poster URL from our map
        hero_img = REAL_POSTER_MAP.get(hero_title, "https://loremflickr.com/600/900/cinema,poster/all?lock=1")
        
        with cols[i % 4]:
            st.markdown(f'''
                <div style="
                    background: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.9)), url('{hero_img}');
                    background-size: cover;
                    background-position: center;
                    height: 380px;
                    border-radius: 24px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: flex-end;
                    padding: 30px;
                    margin-bottom: 30px;
                    transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
                    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
                    border: 1px solid rgba(255,255,255,0.08);
                    cursor: pointer;
                " onmouseover="this.style.transform='translateY(-15px) scale(1.03)'; this.style.boxShadow='0 30px 60px rgba(229,9,20,0.4)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.5)';">
                    <p style="color: white; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 10px 20px rgba(0,0,0,0.9); font-family: 'Bebas Neue'; letter-spacing: 4px;">{genre.upper()}</p>
                    <p style="color: var(--red); font-weight: 700; font-size: 0.9rem; margin-top: 8px; text-transform: uppercase; letter-spacing: 3px; opacity: 0.8;">{hero_title}</p>
                </div>
            ''', unsafe_allow_html=True)
            if st.button(f"Explore {genre}", use_container_width=True, key=f"hero_btn_{genre}"):
                st.session_state.search_query = genre
                st.session_state.nav = "Search"
                st.rerun()

elif st.session_state.nav == "Detail" and st.session_state.selected_movie is not None:
    movie = st.session_state.selected_movie
    title = movie["movie_title"]
    m_year = movie.get("title_year", 0)
    m_year = int(m_year) if not pd.isna(m_year) else 0
    
    st.markdown(render_hero(movie, tmdb_k), unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    data = get_tmdb_data(title, m_year, tmdb_k)
    with col1:
        st.markdown(f'<img src="{data["poster"]}" style="width:100%; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.5);">', unsafe_allow_html=True)
        if st.button("⬅️ Back to Browse", use_container_width=True):
            st.session_state.nav = "Home"
            st.rerun()
    with col2:
        st.markdown(f"## {title}")
        st.markdown(f"#### {m_year} • ★ {movie['imdb_score']} • {movie['genres'].split('|')[0]}")
        st.write(data["overview"])
        st.divider()
        st.write(f"**Director:** {movie['director_name']}")
        st.write(f"**Cast:** {movie['actor_1_name']}, {movie['actor_2_name']}, {movie['actor_3_name']}")
        st.divider()
        cols = st.columns(3)
        cols[0].metric("IMDb Score", f"★ {movie['imdb_score']}")
        cols[1].metric("Duration", f"{int(movie['duration'])} Min" if not pd.isna(movie['duration']) else "N/A")
        cols[2].metric("Budget", f"${int(movie['budget'])/1e6:.1f}M" if not pd.isna(movie['budget']) else "N/A")

    st.divider()
    st.markdown('<div class="section-title">✨ You Might Also Like</div>', unsafe_allow_html=True)
    recs = engine.find_similar(title, top_n=10)
    if not recs.empty:
        rec_html = "".join([make_card_html(row, row["movie_title"] in st.session_state.watchlist, tmdb_k, i) for i, (_, row) in enumerate(recs.iterrows())])
        st.markdown(f'<div class="scroll-container">{rec_html}</div>', unsafe_allow_html=True)

# ── Analytics & Stats (Always Visible at Bottom or specific tab) ─────────────
if st.session_state.nav == "Home":
    st.divider()
    st.markdown('<div class="section-title">📊 CineVerse Insights</div>', unsafe_allow_html=True)
    
    # Custom Styling for Plotly
    PT = dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#FFFFFF", font_family="Inter")

    c1, c2 = st.columns(2)
    with c1:
        gc = df["genre_list"].explode().value_counts().head(10)
        fig = px.pie(values=gc.values, names=gc.index, title="Genre Distribution", hole=0.5,
                     color_discrete_sequence=px.colors.sequential.Reds_r)
        fig.update_layout(**PT)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig2 = px.histogram(df, x="imdb_score", nbins=30, title="IMDb Rating Distribution", color_discrete_sequence=["#E50914"])
        fig2.update_layout(**PT, bargap=0.05)
        st.plotly_chart(fig2, use_container_width=True)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown(
    '<div style="text-align: center; padding: 5rem 2rem; color: #444; background: #080808;">'
    '<h1 style="color: #666; font-family: Montserrat; font-weight: 900; letter-spacing: 5px;">MOVIEVIBE</h1>'
    '<p>© 2026 MovieVibe AI. Powered by Advanced ML & Vector Embedding.</p>'
    '<p style="font-size: 0.8rem; margin-top: 10px;">Inspired by Netflix, JioHotstar & 21st.dev Design Language.</p>'
    '</div>', unsafe_allow_html=True)
