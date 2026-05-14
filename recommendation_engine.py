"""
recommendation_engine.py
────────────────────────
Content-based movie recommendation engine built on
TF-IDF vectorisation + cosine similarity.

No external APIs required — runs entirely offline.
"""

import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data_preprocessing import MOOD_GENRE_MAP


class RecommendationEngine:
    """
    Local, offline movie recommendation engine.

    Workflow
    --------
    1. Fit a TF-IDF matrix over the ``combined_features`` column.
    2. For free-text queries, transform the query into the same TF-IDF space
       and compute cosine similarity against every movie.
    3. For "find similar" lookups, use pre-computed pairwise similarity.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self._build_tfidf()

    # ── internal ─────────────────────────────────────────────────────────
    def _build_tfidf(self) -> None:
        """Fit the TF-IDF model on the combined features column."""
        self.vectorizer = TfidfVectorizer(
            max_features=10_000,
            stop_words="english",
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.85,
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.df["combined_features"]
        )

    # ── public API ───────────────────────────────────────────────────────

    def search(
        self,
        query: str,
        top_n: int = 12,
        genre_filter: list[str] | None = None,
        year_range: tuple[int, int] | None = None,
        rating_range: tuple[float, float] | None = None,
        language_filter: str | None = None,
    ) -> pd.DataFrame:
        """
        Search for movies matching a free-text query.
        Prioritises title matching before falling back to TF-IDF.
        """
        q = query.strip().lower()
        
        # 1. Exact Title Match
        exact_mask = self.df["movie_title"].str.lower() == q
        if exact_mask.any():
            res = self.df[exact_mask].copy()
            res["match_score"] = 100.0
            return res.head(1)

        # 2. Partial Title Match (Contains)
        partial_mask = self.df["movie_title"].str.lower().str.contains(re.escape(q), na=False)
        if partial_mask.any():
            res = self.df[partial_mask].copy()
            res["match_score"] = 90.0
            # Apply filters to partial matches too
            res = self._apply_filters(res, genre_filter, year_range, rating_range, language_filter)
            return res.sort_values(by="imdb_score", ascending=False).head(top_n)

        # 3. Fallback: Semantic Search (TF-IDF)
        clean_query = self._normalise_query(query)
        query_vec   = self.vectorizer.transform([clean_query])
        scores      = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        results = self.df.copy()
        results["match_score"] = (scores * 100).round(1)

        # ── apply filters ────────────────────────────────────────────────
        results = self._apply_filters(
            results, genre_filter, year_range, rating_range, language_filter
        )

        results = results.sort_values("match_score", ascending=False)
        results = results[results["match_score"] > 0]
        return results.head(top_n).reset_index(drop=True)

    def find_similar(
        self,
        movie_title: str,
        top_n: int = 12,
        genre_filter: list[str] | None = None,
        year_range: tuple[int, int] | None = None,
        rating_range: tuple[float, float] | None = None,
        language_filter: str | None = None,
    ) -> pd.DataFrame:
        """
        Given an exact movie title, find the most similar movies.
        """
        mask = self.df["movie_title"].str.lower() == movie_title.strip().lower()
        if not mask.any():
            # fuzzy fallback – partial match
            mask = self.df["movie_title"].str.lower().str.contains(
                re.escape(movie_title.strip().lower()), na=False
            )
        if not mask.any():
            return pd.DataFrame()

        idx = mask.idxmax()
        movie_vec = self.tfidf_matrix[idx]
        scores = cosine_similarity(movie_vec, self.tfidf_matrix).flatten()

        results = self.df.copy()
        results["match_score"] = (scores * 100).round(1)

        # exclude the movie itself
        results = results.drop(index=idx, errors="ignore")

        results = self._apply_filters(
            results, genre_filter, year_range, rating_range, language_filter
        )

        return (
            results.sort_values("match_score", ascending=False)
            .head(top_n)
            .reset_index(drop=True)
        )

    def mood_recommend(
        self,
        mood: str,
        top_n: int = 12,
        year_range: tuple[int, int] | None = None,
        rating_range: tuple[float, float] | None = None,
        language_filter: str | None = None,
    ) -> pd.DataFrame:
        """
        Recommend movies based on a mood keyword.
        Maps mood → genres then runs a TF-IDF search weighted towards those genres.
        """
        mood_lower = mood.strip().lower()
        target_genres = MOOD_GENRE_MAP.get(mood_lower, [])

        if not target_genres:
            # try partial match
            for key, genres in MOOD_GENRE_MAP.items():
                if key in mood_lower or mood_lower in key:
                    target_genres = genres
                    break

        if not target_genres:
            # fallback – treat mood as a free-text query
            return self.search(mood, top_n=top_n, year_range=year_range,
                               rating_range=rating_range, language_filter=language_filter)

        query = " ".join(target_genres).lower()
        return self.search(query, top_n=top_n, genre_filter=None,
                           year_range=year_range, rating_range=rating_range,
                           language_filter=language_filter)

    def get_trending(self, top_n: int = 12) -> pd.DataFrame:
        """Top movies by popularity (vote count)."""
        return (
            self.df.sort_values("popularity", ascending=False)
            .head(top_n)
            .reset_index(drop=True)
        )

    def get_top_rated(self, top_n: int = 12, min_votes: int = 5000) -> pd.DataFrame:
        """Top movies by IMDB score, filtered by minimum vote count."""
        filtered = self.df[self.df["num_voted_users"] >= min_votes]
        return (
            filtered.sort_values("imdb_score", ascending=False)
            .head(top_n)
            .reset_index(drop=True)
        )

    def autocomplete(self, partial: str, limit: int = 8) -> list[str]:
        """Return movie titles matching the partial input."""
        if not partial:
            return []
        pattern = re.escape(partial.strip().lower())
        mask = self.df["movie_title"].str.lower().str.contains(pattern, na=False)
        return self.df.loc[mask, "movie_title"].head(limit).tolist()

    # ── helpers ──────────────────────────────────────────────────────────

    @staticmethod
    def _normalise_query(query: str) -> str:
        """Clean and expand a user query for better matching."""
        q = query.lower().strip()
        q = re.sub(r"[^a-z0-9\s]", " ", q)
        return re.sub(r"\s+", " ", q).strip()

    @staticmethod
    def _apply_filters(
        df: pd.DataFrame,
        genre_filter: list[str] | None,
        year_range: tuple[int, int] | None,
        rating_range: tuple[float, float] | None,
        language_filter: str | None,
    ) -> pd.DataFrame:
        """Apply optional sidebar filters."""
        if genre_filter:
            mask = df["genre_list"].apply(
                lambda gl: any(g in gl for g in genre_filter)
            )
            df = df[mask]

        if year_range:
            lo, hi = year_range
            df = df[(df["title_year"] >= lo) & (df["title_year"] <= hi)]

        if rating_range:
            lo, hi = rating_range
            df = df[(df["imdb_score"] >= lo) & (df["imdb_score"] <= hi)]

        if language_filter and language_filter != "All":
            df = df[df["language"] == language_filter]

        return df
