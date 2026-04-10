from collections import OrderedDict
import requests

BACKEND_URL: str = 'http://127.0.0.1:5000/'

# Stores a chache of genre values for easy retreval
class Genres:
    def __init__(self):
        self.load_genres()

    # Chaches genre list from server
    def load_genres(self):
        reponse = requests.get(f"{BACKEND_URL}genres")
        
        if reponse.ok:
            for genre in reponse.json():
                name: str = genre.get("name").lower()
                id: int = genre.get("id")
                
                self._genres_to_id[name] = id
                self._id_to_genres[id] = name

    # Gets a genre based on name or id
    def get(self, key: int | str) -> int | str: 
        
        # Gets genre name from id
        if isinstance(key, int):
            return self._id_to_genres.get(key)        
        # Gets genre id from a name
        if isinstance(key, str):
            return self._genres_to_id.get(key.lower().strip())

    # Checks if a specific is or genre is present in the dict
    def isValue(self, key: int | str) -> bool: 
        if isinstance(key, int):
            return key in self._id_to_genres        
        if isinstance(key, str):
            return key.lower().strip() in self._genres_to_id


    # Gets a list with the name of all genres
    def list(self) -> list:
        return self._genres_to_id.keys()

    _genres_to_id: dict = OrderedDict()
    _id_to_genres: dict = OrderedDict()

genres = Genres()