from movie_lib import get_title_from_id
import csv

def main():
    while True:
        user_interest = input("""Please select 'm' to get the title of a movie from the movie id number,
        select 'g' to get a genres list from the movie id,
        select 'a' to get the average rating of from a movie id,
        select 'r' to get a list of rating from a movie id,
        select 'p' to get a list of ratings given by a person from thier user id,
        select 't' to get a list of top rated movies,
        select 'e' to get a list of recommended movies based on an siliar rater""")
        if user_interest.lower() == 'm':
            movie_number = input("Please enter the movie id number: ")
            if 1 <= int(movie_number) <= 1682 :
                movie_name = get_title_from_id(movie_number)
                print("The movie with id number {} is {}".format(movie_number, movie_name))
            else:
                print("That is not a movie id number.")
        elif user_interest.lower() == 'g':
            movie_number = input("Please enter the movie id number: ")
            if 1 <= int(movie_number) <= 1682 :
                genres = check_topic(movie_number)
                print("The movie with id number {} is considered {}".format(movie_number, genres))
            else:
                print("That is not a movie id number.")
        elif user_interest.lower() == 'a':
            movie_number = input("Please enter the movie id number: ")
            if 1 <= int(movie_number) <= 1682 :
                avg = average_rating(movie_number)
                print("The movie with id number {} has an average rating of {}".format(movie_number, avg))
            else:
                print("That is not a movie id number.")
        elif user_interest.lower() == 'r':
            movie_number = input("Please enter the movie id number: ")
            if 1 <= int(movie_number) <= 1682 :
                all_movie_ratings = get_ratings_for_movie(movie_number)
                print("The movie with id number {} has received the following ratings: {}".format(movie_number, all_movie_ratings))
            else:
                print("That is not a movie id number.")
        elif user_interest.lower() == 'p':
            user_number = input("Please enter the user id number: ")
            if 1 <= int(user_number) <= 943 :
                writing = ratings_written(user_number)
                print("The user with id number {} has given the following ratings: {}".format(user_number, writing))
            else:
                print("That is not a user id number.")
        elif user_interest.lower() == 't':
            user_number = input("Please enter your user id number to aviod movies you have seen and get a list of highly rated recommendations, or enter 'top' to see a list of the top rated: ")
            if user_number.lower() == 'top':
                titles_of_top = []
                top_rated = popular_movies()
                for  mov in top_rated:
                    title1 = get_title_from_id(mov)
                    titles_of_top.append(title1)
                    print("The top rated movies are {}".format(titles_of_top, top_rated))
            elif 1 <= int(user_number) <= 943 :
                recommendations = top_not_seen(user_number)
                print("Some top rated movies you have not rated are: {}".format(user_number, recommendations))
            else:
                print("That is not a user id number.")
        elif user_interest.lower() == 'e':
            user_number = input("Please enter your user id number to find the best recommendations for you: ")
            if 1 <= int(user_number) <= 943 :
                recommendations2 = euc(user_number)
                print("Some movies you might like but have not rated are: {}".format(user_number, recommendations2))
            else:
                print("That is not a user id number.")
        else:
            print("That is not a recognized option.")


list_for_ratings = []
with open('ml-100k/u.data') as f:
    reader = csv.DictReader(f, delimiter="\t", fieldnames=["user id", "item id", "rating", "timestamp"])
    for row in reader:
        list_for_ratings.append(row)

print(list_for_ratings)

list_of_people = []
with open('ml-100k/u.user') as p:
    watcher = csv.DictReader(p, delimiter="|", fieldnames=["user id", "age", "gender", "occupation", "zip code"])
    for eye in watcher:
        list_of_people.append(eye)

print(list_of_people)

list_for_movies = []
with open('ml-100k/u.item', encoding='latin_1') as m:
    vhs = csv.DictReader(m, delimiter="|", fieldnames=["movie id", "movie title", "release date", "video release date",
    "IMDb URL", "unknown", "Action", "Adventure", "Animation",
    "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
    "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
    "Thriller", "War", "Western"])
    for spool in vhs:
        list_for_movies.append(spool)

print(list_for_movies)

if __name__ == "__main__":
    main()