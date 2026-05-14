"""
data_preprocessing.py
─────────────────────
Loads, cleans and engineers features from the IMDB 5000 movie dataset
so the recommendation engine can consume a ready-to-use DataFrame.
"""

import os
import pandas as pd
import numpy as np
import re


# ── paths ────────────────────────────────────────────────────────────────────
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset")
CSV_PATH = os.path.join(DATA_DIR, "movie_metadata.csv")


# ── genre colour palette (for poster placeholders) ──────────────────────────
GENRE_COLORS: dict[str, tuple[str, str]] = {
    "Action":      ("#e53935", "#ff7043"),
    "Adventure":   ("#fb8c00", "#ffc107"),
    "Animation":   ("#7cb342", "#c0ca33"),
    "Biography":   ("#8d6e63", "#bcaaa4"),
    "Comedy":      ("#ffb300", "#ffe082"),
    "Crime":       ("#37474f", "#78909c"),
    "Documentary": ("#00897b", "#4db6ac"),
    "Drama":       ("#5c6bc0", "#9fa8da"),
    "Family":      ("#ec407a", "#f48fb1"),
    "Fantasy":     ("#ab47bc", "#ce93d8"),
    "Film-Noir":   ("#212121", "#616161"),
    "History":     ("#6d4c41", "#a1887f"),
    "Horror":      ("#b71c1c", "#e57373"),
    "Music":       ("#00acc1", "#4dd0e1"),
    "Musical":     ("#d81b60", "#f06292"),
    "Mystery":     ("#283593", "#7986cb"),
    "Romance":     ("#e91e63", "#f48fb1"),
    "Sci-Fi":      ("#00bcd4", "#80deea"),
    "Short":       ("#78909c", "#b0bec5"),
    "Sport":       ("#43a047", "#81c784"),
    "Thriller":    ("#4a148c", "#9c27b0"),
    "War":         ("#455a64", "#90a4ae"),
    "Western":     ("#bf360c", "#ff8a65"),
}

# ── mood → genre mapping ────────────────────────────────────────────────────
MOOD_GENRE_MAP: dict[str, list[str]] = {
    "happy":       ["Comedy", "Family", "Animation", "Musical", "Music"],
    "sad":         ["Drama", "Romance", "War", "Biography"],
    "excited":     ["Action", "Adventure", "Sci-Fi", "Thriller"],
    "scared":      ["Horror", "Thriller", "Mystery"],
    "romantic":    ["Romance", "Drama", "Comedy"],
    "thoughtful":  ["Documentary", "Drama", "Mystery", "Biography", "History"],
    "nostalgic":   ["Family", "Animation", "Fantasy", "Adventure"],
    "adventurous": ["Adventure", "Action", "Fantasy", "Sci-Fi", "Western"],
    "dark":        ["Crime", "Thriller", "Horror", "Film-Noir", "Mystery"],
    "inspirational": ["Biography", "Drama", "Sport", "History"],
    "chill":       ["Comedy", "Animation", "Family", "Music"],
    "mind-bending": ["Sci-Fi", "Mystery", "Thriller", "Fantasy"],
}


def _clean_text(text: str) -> str:
    """Lower-case, strip whitespace and special characters."""
    if pd.isna(text):
        return ""
    text = str(text).lower().strip()
    text = text.replace("|", " ")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _extract_keywords(kw_string: str) -> str:
    """Turn pipe-delimited keywords into a clean space-separated string."""
    if pd.isna(kw_string):
        return ""
    return " ".join(k.strip().replace(" ", "") for k in str(kw_string).split("|") if k.strip())


def load_and_clean_data() -> pd.DataFrame:
    """
    Main preprocessing pipeline.
    Returns a cleaned DataFrame with an extra ``combined_features`` column
    ready for TF-IDF vectorisation.
    """
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CRITICAL ERROR: Movie dataset not found at {CSV_PATH}. Please ensure the 'dataset' folder and 'movie_metadata.csv' are uploaded to GitHub.")

    df = pd.read_csv(CSV_PATH, encoding="latin-1")

    # ── strip whitespace and fix encoding from movie titles ───────────────────────────────
    df["movie_title"] = df["movie_title"].astype(str).apply(lambda x: x.encode('ascii', 'ignore').decode('ascii')).str.strip().str.rstrip("\xa0")

    # ── drop exact duplicates on title + year ────────────────────────────
    df = df.drop_duplicates(subset=["movie_title", "title_year"], keep="first")

    # ── fill missing numerics ────────────────────────────────────────────
    df["imdb_score"]  = pd.to_numeric(df["imdb_score"], errors="coerce")
    df["title_year"]  = pd.to_numeric(df["title_year"], errors="coerce")
    df["budget"]      = pd.to_numeric(df["budget"], errors="coerce")
    df["gross"]       = pd.to_numeric(df["gross"], errors="coerce")
    df["duration"]    = pd.to_numeric(df["duration"], errors="coerce")
    df["num_voted_users"] = pd.to_numeric(df["num_voted_users"], errors="coerce")

    df["imdb_score"]      = df["imdb_score"].fillna(df["imdb_score"].median())
    df["title_year"]      = df["title_year"].fillna(0)
    df["budget"]          = df["budget"].fillna(0)
    df["gross"]           = df["gross"].fillna(0)
    df["duration"]        = df["duration"].fillna(df["duration"].median())
    df["num_voted_users"] = df["num_voted_users"].fillna(0)

    # ── fill missing strings ─────────────────────────────────────────────
    str_cols = [
        "genres", "plot_keywords", "director_name",
        "actor_1_name", "actor_2_name", "actor_3_name",
        "language", "country", "content_rating", "color",
    ]
    for col in str_cols:
        if col in df.columns:
            df[col] = df[col].fillna("")

    # ── genre list (original, for filters) ───────────────────────────────
    df["genre_list"] = df["genres"].apply(
        lambda x: [g.strip() for g in str(x).split("|") if g.strip()] if pd.notna(x) else []
    )

    # ── primary genre ────────────────────────────────────────────────────
    df["primary_genre"] = df["genre_list"].apply(lambda g: g[0] if g else "Unknown")

    # ── poster gradient colours based on primary genre ───────────────────
    df["poster_color_start"] = df["primary_genre"].apply(
        lambda g: GENRE_COLORS.get(g, ("#6366f1", "#8b5cf6"))[0]
    )
    df["poster_color_end"] = df["primary_genre"].apply(
        lambda g: GENRE_COLORS.get(g, ("#6366f1", "#8b5cf6"))[1]
    )

    # ── movie initials (for placeholder posters) ─────────────────────────
    df["initials"] = df["movie_title"].apply(
        lambda t: "".join(w[0].upper() for w in str(t).split() if w)[:3]
    )

    # ── combined features for TF-IDF ─────────────────────────────────────
    df["clean_genres"]   = df["genres"].apply(_clean_text)
    df["clean_keywords"] = df["plot_keywords"].apply(_extract_keywords)
    df["clean_director"] = df["director_name"].apply(_clean_text)
    df["clean_actors"]   = (
        df["actor_1_name"].apply(_clean_text) + " " +
        df["actor_2_name"].apply(_clean_text) + " " +
        df["actor_3_name"].apply(_clean_text)
    )

    df["combined_features"] = (
        df["clean_genres"]   + " " +
        df["clean_genres"]   + " " +   # double-weight genres
        df["clean_keywords"] + " " +
        df["clean_director"] + " " +
        df["clean_actors"]
    ).str.strip()

    # ── drop rows with no useful text ────────────────────────────────────
    df = df[df["combined_features"].str.len() > 2].reset_index(drop=True)

    # ── popularity score (normalised 0-100) ──────────────────────────────
    if df["num_voted_users"].max() > 0:
        df["popularity"] = (
            df["num_voted_users"] / df["num_voted_users"].max() * 100
        ).round(1)
    else:
        df["popularity"] = 0

    # ── year as int ──────────────────────────────────────────────────────
    df["title_year"] = df["title_year"].astype(int)

    return df


def get_all_genres(df: pd.DataFrame) -> list[str]:
    """Return a sorted list of every unique genre in the dataset."""
    genres: set[str] = set()
    for gl in df["genre_list"]:
        genres.update(gl)
    genres.discard("")
    genres.discard("Unknown")
    return sorted(genres)


def get_all_languages(df: pd.DataFrame) -> list[str]:
    """Return sorted unique languages."""
    langs = df["language"].dropna().unique().tolist()
    langs = [l for l in langs if l.strip()]
    return sorted(set(langs))


def get_year_range(df: pd.DataFrame) -> tuple[int, int]:
    """Min and max release year."""
    valid = df[df["title_year"] > 0]["title_year"]
    return int(valid.min()), int(valid.max())


def get_rating_range(df: pd.DataFrame) -> tuple[float, float]:
    """Min and max IMDB score."""
    return float(df["imdb_score"].min()), float(df["imdb_score"].max())
