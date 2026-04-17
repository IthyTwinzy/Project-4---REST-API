import requests
from genres import genres

BACKEND_URL: str = 'http://127.0.0.1:5000/'
GENRE_URL = f'{BACKEND_URL}search_by_genre'
TITLES_URL = f'{BACKEND_URL}search_by_title'
RELEASE_URL = f'{BACKEND_URL}search_by_release'
POPULARITY_URL = f'{BACKEND_URL}search_by_popularity'

# Runs the client
def main():
    # Attribution
    print("This product uses the TMDB API but is not endorsed or certified by TMDB.\n")

    # Displays functionality
    not_exiting = True
    while not_exiting:
        print("Welcome to our the our movie finder app!!!")
        print("1. Find movies that match a specific name")
        print("2. Find movies in a certain genre")
        print("3. Find the movies that are most popular")
        print("4. Find movies with a specific release date")
        print("5. Exit")
        user_response = input("Enter the number of the command you want to execute: ")
        
        match user_response.strip().rstrip('.'):
            case "1":
                find_by_name()        
            case "2":
                find_by_genre()
            case "3":
                find_by_popularity()
            case "4":
                find_by_release()
            case "5":
                not_exiting = False
            case _:
                continue

# Prints out movies in a movie list one at a time
def _display_movies(movie_list: list) -> None:
    for i in range(len(movie_list)):
        movie = movie_list[i]

        print(movie["title"])
        if movie["overview"] == "":
            print("<no description>")
        else:
            print(movie["overview"])
        print()

        # Lets user exit early
        if i != len(movie_list) - 1:
            end_str: str = input("Press enter to view next. Press X to exit ")
            if end_str.lower() == 'x':
                break
        else:
            input("End of movies reached. Press enter to continue ")
        print()

# Lets user search for movies by name
def find_by_name():
    movie = input("Enter movie title: ")
    print()
    _display_movies(requests.get(TITLES_URL + f"?original_title={movie}").json())

# Lets users search for movies by Genre
def find_by_genre():
    # Displays list of valid genres to user
    print()
    genre_list = genres.list()
    genre_message: str = "Avalible Movie Genres: "
    for i in range(len(genre_list)):
        genre_message += genre_list[i]
        if i != len(genre_list) - 1:
            genre_message += ", "
        else:
            genre_message += "."
    print(genre_message)
    print()

    # Gets genre list from user
    user_input: str = input("Enter movie genre(s). If entering multiple genres, seperate with commas: ")
    user_genres: list = [x.strip().lower() for x in user_input.split(',')]

    # Converts user genre list into genre id list (invalid genres skiped)
    user_genre_ids: list = [genres.get(x) for x in user_genres if genres.get(x) is not None]

    # Displays results to user
    if len(user_genre_ids) == 0:
        print("No valid genres entered")
        print()
    else:
        print()
        _display_movies(requests.get(GENRE_URL, params={"genre" : user_genre_ids}).json())

# Lets users find most popular movies
def find_by_popularity():
    print()
    _display_movies(requests.get(POPULARITY_URL).json())

# Lets user search for movies by release date
def find_by_release():
    release = input("Enter movie release date (format: YEAR-MO-DAY): ")
    print()
    _display_movies(requests.get(RELEASE_URL + f"?date={release}").json())

if __name__ == "__main__":
    main()