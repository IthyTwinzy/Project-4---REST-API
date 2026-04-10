import requests

response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=c25bd37ebae9256a378c86b9df1b50ca&query=Coco')
movie = input("Enter Movie Title: ")
data = response.json()


def searchByTitle(movie):
    ### This function takes a user-inputted movie and returns the following:
    ## "Movie not found" if the field is empty, or not in the database.
    ## "Movie" found if the user-inputted movie is found and returns the title and description
    if movie == "":
        print("Movie not found")
    if movie not in data["results"][0]["original_title"]:
        print("Movie not found")
    else:
        print("Movie found")
        print("\nMovie Title: ")
        print(data["results"][0]["title"])
        print("Description: ")
        print(data["results"][0]["overview"])

searchByTitle(movie)






        
