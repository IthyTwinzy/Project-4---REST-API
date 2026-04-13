

import requests
import os
from flask import current_app
from flask import request
API_KEY: str = os.environ.get("TMDB_API_KEY")

TMDB_URL: str = "https://api.themoviedb.org/3/search/movie"

@current_app.get('/titles')
def titles():
    movie_title = request.args.get('original_title')
    response = requests.get(TMDB_URL, params = {"api_key" : API_KEY, "query" : movie_title})
    return response.json()


@current_app.get('/search_by_title')
def search_by_title():
    movie_title = request.args.get('original_title')
    response = requests.get(TMDB_URL, params = {"api_key" : API_KEY, "query": movie_title}).json()
    for result in response["results"]:
        if result["original_title"] == movie_title:

            return {"overview": result["overview"]}
    return {"not found"}

