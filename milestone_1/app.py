# Create and search a list of movies

movies = list()
search_by = [
    {"X" : "Exiting search..."},
    {"N" : "Enter the movie name: "},
    {"D" : "Enter the directors name: "},
    {"Y" : "Enter the year the movie premiered: "}
]

# Prompt for movie info and return a dictionary
def create_movie():
    name = input("Enter the movie name: ")
    year = input(f"What year did {name} premier?: " )
    director = input(f"Who directed {name}?: ")
    return {
        "movie" : {name},
        "year" : {year},
        "director" : {director}
    }
# Take a movie name, search list and return the dictonary
def find_movie(name):
    print(name)

def list_movies():
    for movie in movies:
        print(movie)

def search_movies():
    action = input("What do you want to search for, Name of movie (N), Year (Y), Director (D), Exit (X)?: ")
    if action.upper() == "X":
        print("Exiting search...")
    elif action.upper() == "N":
        name = input("Enter the movie name: ")
    elif action.upper() == "Y":
        year = input("Enter the premier year: ")
    elif action.upper() == "D":
        director = input("Enter the directors name: ")
    else:
        print("Invalid value, exiting search...")


def movie_fun():
    print("Welcome to my movie app!!!")
    while True:
        action = input("What do you want to do? Add a movie (A), Search for a movie (S), List Movies (L), Exit (X): ")

        if action.upper() == "X":
            print("Thanks for playing, exiting")
            break;
        if action.upper() == "A":
            movie = create_movie()
            movies.append(movie)
        elif action.upper() == "L":
            list_movies()
        elif action.upper() == "S":
            movie = search_movies()
        else:
            print("ERROR: Invalid entry, try again")


movie_fun()



