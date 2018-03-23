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
        "name" : {name},
        "year" : {year},
        "director" : {director}
    }
# Take a movie name, search list and return the dictonary
def find_movie(name):
    print(name)


def display_movie(movie):
    print(f'Name: {movie[name]}, Director: {movie[director]}, Year: {movie[year]}')


def list_movies():
    for movie in movies:
        display_movie(movie)


def search_movies():
    find_by = input("What do you want to search for Name, Year , Director , or Exit?: ")
    if find_by.lower != "exit":
        looking_for = input("What are you searching for?: ")
        for movie in movies:
            if movie[find_by.lower()] == looking_for:
                display_movie(movie)


def movie_fun():
    print("Welcome to my movie app!!!")
    while True:
        action = input("What do you want to do? Add a movie (A), Search for a movie (S), List Movies (L), Exit (X): ")

        if action.upper() == "X":
            print("Thanks for playing, exiting")
            break;
        if action.upper() == "A":
            movies.append(create_movie())
        elif action.upper() == "L":
            list_movies()
        elif action.upper() == "S":
            movie = search_movies()
        else:
            print("ERROR: Invalid entry, try again")


movie_fun()



