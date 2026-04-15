from flask import current_app
from flask import request
import requests

API_KEY: str = current_app.config.get("TMDB_API_KEY")
TMDB_URL: str = current_app.config.get("TMDB_URL")

#requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}")


@current_app.get('/search_by_popularity')
def search_by_Popularity():
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&sort_by=popularity.desc"

    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("results")