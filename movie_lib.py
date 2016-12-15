import math
import csv


class Movie:
    def __init__(self, **kwargs):
        self.movie_id = kwargs["movie_id"]
        self.title = kwargs["movie_title"]
        self.action = kwargs["Action"]
        self.advent = kwargs["Adventure"]
        self.anime = kwargs["Animation"]
        self.kids = kwargs["Childrens"]
        self.comedy = kwargs["Comedy"]
        self.crime = kwargs["Crime"]
        self.docu = kwargs["Documentary"]
        self.drama = kwargs["Drama"]
        self.fant = kwargs["Fantasy"]
        self.scifi = kwargs["Sci_Fi"]
        self.horror = kwargs["Horror"]

    def __repr__(self):
        return "{} {}".format(self.movie_id, self.title)

    def get_title_from_id(self, movid):
        if Movie[movie_id] == movid:
            return Movie[title]

    def check_topic(self, movid):
        genres = []
        if Movie[movie_id] == movid:
            if Movie[action] == "1":
                genres.append("Action ")
            if Movie[advent] == "1":
                genres.append("Adventure ")
            if Movie[anime] == "1":
                genres.append("Anime ")
            if Movie[kids] == "1":
                genres.append("Children's ")
            if Movie[comedy] == "1":
                genres.append("Comedy ")
            if Movie[crime] == "1":
                genres.append("Crime ")
            if Movie[docu] == "1":
                genres.append("Documentary ")
            if Movie[drama] == "1":
                genres.append("Drama ")
            if Movie[fant] == "1":
                genres.append("Fantasy ")
            if Movie[scifi] == "1":
                genres.append("Sci-Fi ")
            if Movie[horror] == "1":
                genres.append("Horror ")
            return genres


class User:
    def __init__(self, **kwargs):
        self.user_id = kwargs["user_id"]
        self.age = int(kwargs["age"])
        self.job = kwargs["occupation"]

    def __repr__(self):
        return "{} {} {}".format(self.user_id, self.age, self.job)


class Rating:
    def __init__(self, **kwargs):
        self.movie_id = kwargs["item_id"]
        self.user_id = kwargs["user_id"]
        self.rating = float(kwargs["rating"])
        self.timestamp = kwargs["timestamp"]

    def __repr__(self):
        return "{} {} {}".format(self.movie_id, self.user_id, self.rating)

    def average_rating(self, movid):
        ratingsl = []
        if Movie[movie_id] == movid:
            ratingsl.append(Movie[rating])
        return sum(ratingsl)/len(ratingsl)

    def get_ratings_for_movie(self, movid):
        ratingsl2 = []
        if Movie[movie_id] == movid:
            ratingsl2.append(Movie[rating])
        return ratingsl2

    def ratings_written(self, person):
        ratingsl3 = []
        if Movie[user_id] == person:
            ratingsl3.append(Movie[rating])
        return ratingsl3

    def movies_seen(self, person):
        watchedl = []
        if Movie[user_id] == person:
            watchedl.append(Movie[movie_id])
        return watchedl

    def popular_movies(self):
        top_movies = []
        list_of_ave_rating = ([average_rating(m) for m in movielistcouldmake if
                              len(get_ratings_for_movie()) > 20])
        list_of_ave_rating.sort()

    def top_not_seen(self):
        pass

    def euc(self):
        pass


def open_ratings_data():
    organize_ratings_data = {}
    ratings_ordered_by_user = {}
    with open('ml-100k/u.data', encoding="latin-1") as f:
        ratings_headers = ["user_id", "item_id", "rating", "timestamp"]
        reader = csv.DictReader(f, delimiter="\t", fieldnames=ratings_headers)
        for row in reader:
            del row[None]
            each_rating = Rating(**row)
            organize_ratings_data.append({key: row[key] for key in ratings_headers})
            page = range(len(marks))
            for line in page:
                Rating(**marks[line])
    return organize_ratings_data, ratings_ordered_by_user


def open_rater_data():
    demographics = {}
    with open('ml-100k/u.user') as p:
        rater_headers = ["user_id", "age", "gender", "occupation", "zip_code"]
        reader = csv.DictReader(p, delimiter="|", fieldnames=rater_headers)
        for row in reader:
            del row[None]
            each_user = User(**row)
            demographics.append({key: row[key] for key in ["user_id", "age",
                                                           "occupation"]})
    return demographics


def open_movie_data():
    movies = {}
    with open('ml-100k/u.item', encoding='latin_1') as m:
        movie_headers = ["movie_id", "movie_title", "release_date",
                         "video_release_date", "IMDb_URL", "unknown", "Action",
                         "Adventure", "Animation", "Childrens", "Comedy",
                         "Crime", "Documentary", "Drama", "Fantasy",
                         "Film_Noir", "Horror", "Musical", "Mystery",
                         "Romance", "Sci_Fi", "Thriller", "War", "Western"]
        reader = csv.DictReader(m, delimiter="|", fieldnames=movie_headers)
        for row in reader:
            del row[None]
            each_movie = Movie(**row)
            movies.append({key: row[key] for key in ["movie_id", "movie_title",
                                                     "Action", "Adventure",
                                                     "Animation", "Childrens",
                                                     "Comedy", "Crime",
                                                     "Documentary", "Drama",
                                                     "Fantasy", "Sci_Fi",
                                                     "Horror"]})
    return movies
