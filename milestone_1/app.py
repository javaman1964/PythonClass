# Create and search a list of movies

movies = list()

# Prompt for movie info and return a dictionary
def create_movie():
    name = input("Enter the movie name: ")
    year = input(f"What year did {name} premier?: " )
    director = input(f"Who directed {name}?: ")
    return {
        "movie":{name},
        "year":{year},
        "director":{director}
    }
# Take a movie name, search list and return the dictonary
def find_movie(name):
    print(name)

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
        print(movies)
    elif action.upper() == "S":
        print("search")
    else:
        print("ERROR: Invalid entry, try again")


