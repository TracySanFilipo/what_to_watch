import math
import csv


class Movie:
    def __init__(self, **kwargs):
        self.movieid = kwargs["movie id"]
        self.title = kwargs["movie title"]
        self.action = kwargs["Action"]
        self.advent = kwargs["Adventure"]
        self.anime = kwargs["Animation"]
        self.kids = kwargs["Children's"]
        self.comedy = kwargs["Comedy"]
        self.crime = kwargs["Crime"]
        self.docu = kwargs["Documentary"]
        self.drama = kwargs["Drama"]
        self.fant = kwargs["Fantasy"]
        self.scifi = kwargs["Sci-Fi"]
        self.horror = kwargs["Horror"]

    def __repr__(self):
        return "{} {}".format(self.movieid, self.title)

    def get_title_from_id(self, movid):
        if Movie[movieid] == movid:
            return Movie[title]

    def check_topic(self, movid):
        genres = []
        if Movie[movieid] == movid:
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
        self.userid = kwargs["user id"]
        self.age = int(kwargs["age"])
        self.job = kwargs["occupation"]

    def __repr__(self):
        return "{} {} {}".format(self.userid, self.age, self.job)


class Rating:
    def __init__(self, **kwargs):
        self.timestamp = kwargs("timestamp")
        self.movieid = kwargs("item id")
        self.userid = kwargs("user id")
        self.rating = float(kwargs("rating"))

    def __repr__(self):
        return "{} {} {}".format(self.movieid, self.userid, self.rating)

    def average_rating(self, movid):
        ratingsl = []
        if Movie[movieid] == movid:
            ratingsl.append(Movie[rating])
        return sum(ratingsl)/len(ratingsl)

    def get_ratings_for_movie(self, movid):
        ratingsl2 = []
        if Movie[movieid] == movid:
            ratingsl2.append(Movie[rating])
        return ratingsl2

    def ratings_written(self, person):
        ratingsl3 = []
        if Movie[userid] == person:
            ratingsl3.append(Movie[rating])
        return ratingsl3

    def movies_seen(self, person):
        watchedl = []
        if Movie[userid] == person:
            watchedl.append(Movie[movieid])
        return watchedl

    def popular_movies(self):
        top_movies = []
        list_of_ave_rating = [average_rating(m) for m in movielistcouldmake if len(get_ratings_for_movie()) > 20]
        list_of_ave_rating.sort()

    def top_not_seen(self):
        pass

    def euc(self):
        pass

with open('ml-100k/u.data') as f:
    reader = csv.DictReader(f, delimiter="\t", fieldnames=["user id", "item id", "rating", "timestamp"])
    for row in reader:
        rating_data = Rating(**row)


with open('ml-100k/u.user') as p:
    watcher = csv.DictReader(p, delimiter="|", fieldnames=["user id", "age", "gender", "occupation", "zip code"])
    for eye in watcher:
        user_data = User(**eye)


with open('ml-100k/u.item', encoding='latin_1') as m:
    vhs = csv.DictReader(m, delimiter="|", fieldnames=["movie id", "movie title", "release date", "video release date",
    "IMDb URL", "unknown", "Action", "Adventure", "Animation",
    "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
    "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
    "Thriller", "War", "Western"])
    for spool in vhs:
        movie_data = Movie(**spool)
