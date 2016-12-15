from movie_lib import get_title_from_id
import csv


def choice_m():
    movie_number = input("Please enter the movie id number: ")
    if 1 <= int(movie_number) <= 1682:
        movie_name = get_title_from_id(movie_number)
        print("The movie with id number {} is {}".format(movie_number, movie_name))
    else:
        print("That is not a movie id number.")


def choice_g():
    movie_number = input("Please enter the movie id number: ")
    if 1 <= int(movie_number) <= 1682:
        genres = check_topic(movie_number)
        print("The movie with id number {} is considered {}".format(movie_number, genres))
    else:
        print("That is not a movie id number.")


def choice_a():
    movie_number = input("Please enter the movie id number: ")
    if 1 <= int(movie_number) <= 1682:
        avg = average_rating(movie_number)
        print("The movie with id number {} has an average rating of {}".format(movie_number, avg))
    else:
        print("That is not a movie id number.")


def choice_r():
    movie_number = input("Please enter the movie id number: ")
    if 1 <= int(movie_number) <= 1682:
        all_movie_ratings = get_ratings_for_movie(movie_number)
        print("The movie with id number {} has received the following ratings: {}".format(movie_number, all_movie_ratings))
    else:
        print("That is not a movie id number.")


def choice_p():
    user_number = input("Please enter the user id number: ")
    if 1 <= int(user_number) <= 943:
        writing = ratings_written(user_number)
        print("The user with id number {} has given the following ratings: {}".format(user_number, writing))
    else:
        print("That is not a user id number.")


def choice_t():
    user_number = input("Please enter your user id number to aviod movies you have seen and get a list of highly rated recommendations, or enter 'top' to see a list of the top rated: ")
    if user_number.lower() == 'top':
        titles_of_top = []
        top_rated = popular_movies()
        for mov in top_rated:
            title1 = get_title_from_id(mov)
            titles_of_top.append(title1)
            print("The top rated movies are {}".format(titles_of_top, top_rated))
    elif 1 <= int(user_number) <= 943:
        recommendations = top_not_seen(user_number)
        print("Some top rated movies you have not rated are: {}".format(user_number, recommendations))
    else:
        print("That is not a user id number.")


def choice_e():
    user_number = input("Please enter your user id number to find the best recommendations for you: ")
    if 1 <= int(user_number) <= 943:
        recommendations2 = euc(user_number)
        print("Some movies you might like but have not rated are: {}".format(user_number, recommendations2))
    else:
        print("That is not a user id number.")

def main():
    while True:
        user_interest = input("""Please select 'm' to get the title of a movie
                                from the movie id number, select 'g' to get a
                                genres list from the movie id, select 'a' to
                                get the average rating of from a movie id,
                                select 'r' to get a list of rating from a movie
                                id, select 'p' to get a list of ratings given
                                by a person from their user id, select 't' to
                                get a list of top rated movies, select 'e' to
                                get a list of recommended movies based on an
                                similiar rater""")
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
        else:
            print("That is not a recognized option.")


if __name__ == "__main__":
    main()
