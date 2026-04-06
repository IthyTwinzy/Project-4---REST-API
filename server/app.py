from flask import Flask
from dotenv import load_dotenv
import requests
import os

# Gets API Key to validate requests to TMDB
load_dotenv()
API_KEY: str = os.environ.get("TMDB_API_KEY")

# TMDB URLs
TMDB_URL: str = "https://api.themoviedb.org/3/"
KEY_PARAM: dict = {"api_key" : API_KEY}

# Checks if a valid api key is provided
if API_KEY == None:
    raise KeyError("TMDB API Key not provided")
if requests.get(TMDB_URL + "authentication", params=KEY_PARAM).status_code == 401:
    raise KeyError("Invalid TMDB API Key")

# Starts the server
app = Flask(__name__)

# Test function
@app.route('/')
#TEST
def index():
    return {'message': 'hello flask'}

if __name__ == '__main__':
    app.run(debug=True)