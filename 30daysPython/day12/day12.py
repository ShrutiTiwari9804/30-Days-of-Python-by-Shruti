import json
import os

import os

BASE_DIR = os.path.dirname(__file__)
FILE_NAME = os.path.join(BASE_DIR, "movies.json")



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
    movies = load_movies()

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

    for movie in movies:
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
        
    print ("Movie not found.")


def delete_movie():
    movies = load_movies()

    title = input("Enter movie title to delete: ").strip()

    for movie in movies:
        if movie ["title"].lower() == title.lower():
            movies.remove(movie)
            save_movies(movies)
            print("Movie deleted successfully.")
            return

    print("Movie not found.")


def mark_watched():
    movies = load_movies()

    title = input("Enter movie title: ").strip()

    for movie in movies:
        if movie ["title"].lower() == title.lower():
            movie["watched"] = True
            save_movies(movies)
            print("Marked as watched.")
            return
        
    print("Movie not found.")

def view_watched():
    movies = load_movies()

    watched_movies = [movie for movie in movies if movie ["watched"]]

    if not watched_movies:
        print("No watched movies.")
        return
    
    print("\n====== Watched Movies ======")

    for movie in watched_movies:
        print(f"{movie['title']}({movie['year']}){movie['rating']}/5")

while True:

    print("""
========== Movie Collection Manager ==========
1. Add Movie
2.View All Movies
3. Search Movie
4. Update Movie
5. Delete Movie
6. Mark Movie as Watched
7. View Watched Movies
8. Exit
          
==============================================
""")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie()

    elif choice == "2":
        view_movies()

    elif choice == "3":
        search_movies()
    
    elif choice == "4":
        update_movie()

    elif choice == "5":
        delete_movie()

    elif choice == "6":
        mark_watched()

    elif choice == "7":
        view_watched()

    elif choice == "8":
        print("Thank You for using Movie Collection Manager!")
        break
    else:
        print("Invalid choice.")


