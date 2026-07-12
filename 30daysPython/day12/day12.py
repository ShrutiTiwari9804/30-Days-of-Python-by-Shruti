import json
import os

FILE_NAME = "movies.json"


def load_movies():
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError :
        return []
    

def save_movies(movies):
    with open(FILE_NAME, "w") as file:
        json.dump(movies, file, indent = 4)


def add_movie():
    movies = load_movies

    title = input("Enter Movie Title: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            print("Movie already exists.")
            return
        
    genre = input("Enter Genre: ")
    year = input("Enter Release Year: ")
    rating = int(input("Enter Rating (1-5): "))

    movies.append ({
        "title": title,
        "genre": genre,
        "year": year,
        "rating": rating,
        "watched": False
    })

    save_movies(movies)
    print("Movie added successfully!")


def view_movies():
    movies = load_movies()

    if not movies:
        print("No movies found.")
        return
    
    print("\n======== Movie Collection ========\n")

    for movie in movies:
        status = "Watched" if movie ["watched"] else "Not Watched"

        print(f"""
Title   :{movie['title']}
Genre   :{movie['genre']}
Year    :{movie['year']}
Rating  :{movie['rating']}/5
Status  :{status}
-----------------------------------------
""")
        

def search_movies():
    movies = load_movies()

    title = input("Enter movie title: ").strip()

    for movie in Movies:
        if movie ["title"].lower() == title.lower():
            print("\nMovie Found\n")
            print(movie)
            return

    print("Movie not found.")


def update_movie ():
    movies = load_movies()

    title = input ("Enter movie title to update: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():

            movie["genre"] = input("New Genre: ")
            movie["year"] = input("New Year: ")
            movie ["rating"] = int(input("New Rating (1-5): "))

            save_movies(movies)

            print("Movie updated successfully.")
            return

            