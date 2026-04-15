from flask import current_app
from flask import request
import requests

API_KEY: str = current_app.config.get("TMDB_API_KEY")
TMDB_URL: str = current_app.config.get("TMDB_URL")

@current_app.get('/search_by_release')
def search_by_release(): # Enter in format: YEAR-MO-DY (EX. 2026-04-13)
    """Returns a list of movies released on the specified date"""
    date = requests.args.get("date")
    
    data = requests.get("f{TMDB_URL}discover/movie?api_key={API_KEY}&primary_release_date.lte={date}&primary_release_date.gte={date}")
    print(data.json["results"])