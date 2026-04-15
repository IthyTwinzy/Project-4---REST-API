from flask import Flask
from dotenv import dotenv_values
import requests

# Gets API Key to validate requests to TMDB
API_KEY: str = dotenv_values().get("TMDB_API_KEY")
TMDB_URL: str = "https://api.themoviedb.org/3/"

# Validates API Key
if API_KEY == None:
    raise KeyError("TMDB API Key not provided")
if requests.get(TMDB_URL + "authentication", params={"api_key" : API_KEY}).status_code == 401:
    raise KeyError("Invalid TMDB API Key")

# Starts the server
app = Flask(__name__)

# Intializes envornmental variables
app.config["TMDB_API_KEY"] = API_KEY
app.config["TMDB_URL"] = TMDB_URL

# Imports routed functions
with app.app_context():
    import searchByGenre

    import searchByTitle

    import searchByPopularity
# Test function
@app.route('/')
#TEST
def index():
    return {'message': 'hello flask'}

if __name__ == '__main__':
    app.run(debug=True)