from movie_lib import Movie, User, Rating, movie_table
from movie_lib import rater_table, ratings_by_movie, ratings_by_user
from movie_lib import average_rating, get_ratings_for_movie, ratings_written
from movie_lib import ratings_written_plus_title, popular_movies, euc


def choice_m():
    movie_number = input("Please enter the movie id number: ")
    if movie_number in movie_table:
        movie_name = movie_table[movie_number].get_title_from_id(movie_number)
        print("""The movie with id number {} is:
              {}""".format(movie_number, movie_name))
    else:
        print("That is not a movie id number.")


def choice_g():
    movie_number = input("Please enter the movie id number: ")
    if movie_number in movie_table:
        genres = movie_table[movie_number].check_topic(movie_number)
        print("""The movie with id number {} is considered:
              {}""".format(movie_number, genres))
    else:
        print("That is not a movie id number.")


def choice_a():
    movie_number = input("Please enter the movie id number: ")
    if movie_number in ratings_by_movie:
        avg = round(average_rating(movie_number), 2)
        print("""The movie with id number {} has an average rating of:
              {}""".format(movie_number, avg))
    else:
        print("That is not a movie id number.")


def choice_r():
    movie_number = input("Please enter the movie id number: ")
    if movie_number in ratings_by_movie:
        all_movie_ratings = get_ratings_for_movie(movie_number)
        print("""The movie with id number {} has received the following ratings:
              {}""".format(movie_number, all_movie_ratings))
    else:
        print("That is not a movie id number.")


def choice_p():
    user_number = input("Please enter the user id number: ")
    add_titles = input("""Enter 'm' to see the titles with the rating or
                        anything else for just the ratings: """)
    if user_number in ratings_by_user and add_titles.lower() == 'm':
        writingp = ratings_written_plus_title(user_number)
        print("""The user with id number {} has given the following ratings:
              {}""".format(user_number, writingp))
    elif user_number in ratings_by_user:
        writing = ratings_written(user_number)
        print("""The user with id number {} has given the following ratings:
              {}""".format(user_number, writing))
    else:
        print("That is not a user id number.")


def choice_t():
    while True:
        number_top = input("""Please enter a number between 1 and 100 for the number
                            of movies on the list: """)
        try:
            list_len = int(number_top)
        except ValueError:
            print("That is not an acceptable length")
        else:
            if list_len <= len(ratings_by_user):
                break
    user_number = input("""Please enter 'top' to see a list of the top rated,
                        or enter your user id number to get this list with
                        movies you have rated removed:  """)
    if user_number.lower() == 'top':
        top_rated = popular_movies(list_len, user_number)
        print("""The top rated movies are:
        {}""".format(top_rated))
    elif user_number in ratings_by_user:
        recommendations = popular_movies(list_len, user_number)
        print("""Some top rated movies you have not rated are:
              {}""".format(recommendations))
    else:
        print("That is not a user id number.")


def choice_e():
    user_number = input("""Please enter your user id number
                        to find the best recommendations for you: """)
    if user_number in ratings_by_user:
        recommendations = euc(user_number)
        print("""The following movies were rated by a user with a similar rating
              history as yours. It is recommended that you watch the highly
              rated ones, and aviod those with low ratings:
              {}""".format(recommendations))
    else:
        print("That is not a user id number.")


def main():
    while True:
        user_interest = input("""Please select one of the following:
                              'm' for the title from the movie id,
                              'g' for a genres list from the movie id,
                              'a' for the average rating from a movie id,
                              'r' for a list of rating from a movie id,
                              'p' for a list of ratings from a user id,
                              't' for a list of top rated movies,
                              'e' for a list of recommended movies
                                    based on an similiar rater, or
                              'q' to quit
                                                                        """)
        if user_interest.lower() == 'm':
            choice_m()
        elif user_interest.lower() == 'g':
            choice_g()
        elif user_interest.lower() == 'a':
            choice_a()
        elif user_interest.lower() == 'r':
            choice_r()
        elif user_interest.lower() == 'p':
            choice_p()
        elif user_interest.lower() == 't':
            choice_t()
        elif user_interest.lower() == 'e':
            choice_e()
        elif user_interest.lower() in ['q', 'quit']:
            print("Farewell")
            quit()
        else:
            print("That is not a recognized option.")


if __name__ == "__main__":
    main()
