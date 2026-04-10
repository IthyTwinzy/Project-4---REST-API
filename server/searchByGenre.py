from flask import current_app
from flask import request
import requests

API_KEY: str = current_app.config.get("TMDB_API_KEY")
TMDB_URL: str = current_app.config.get("TMDB_URL")

@current_app.get('/genres')
def get_genres():
    """Returns a list of all genere names and their id numbers"""
    return requests.get(f"{TMDB_URL}genre/movie/list", params={"api_key" : API_KEY}).json().get("genres")


# Expects queries of format: url?genre=28&genre=12
# Currently returns results in the first page of data from tmdb
# Returns an empty array if no results found
@current_app.get('/search_by_genre')
def search_by_genre():
    """Returns list of most popular movies in the specified generes"""
    
    genres = request.args.getlist("genre")
    
    # Creates the request url
    url: str = f"{TMDB_URL}discover/movie?api_key={API_KEY}&with_genres="
    # Appends genre parameters
    for i in range(len(genres)):
        url += genres[i]
        if i != len(genres)-1:
            url += ","
    
    # Gets data from tmdb
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("results")
