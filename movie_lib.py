import math
import csv
rating_path = 'ml-100k/u.data'
movie_path = 'ml-100k/u.item'
user_path = 'ml-100k/u.user'


class Movie:
    def __init__(self, **kwargs):
        self.movie_id = kwargs["movie_id"]
        self.title = kwargs["movie_title"]
        self.date = kwargs["release_date"]
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
        self.noir = kwargs["Film_Noir"]
        self.music = kwargs["Musical"]
        self.mystery = kwargs["Mystery"]
        self.romance = kwargs["Romance"]
        self.thriller = kwargs["Thriller"]
        self.war = kwargs["War"]
        self.western = kwargs["Western"]

    def __repr__(self):
        return "{} {} {}".format(self.movie_id, self.title, self.date)

    def get_title_from_id(self, movid):
        specific = movie_table[movid]
        return specific.title

    def check_topic(self, movid):
        genres = []
        specific = movie_table[movid]
        if specific.action == "1":
            genres.append("Action")
        if specific.advent == "1":
            genres.append("Adventure")
        if specific.anime == "1":
            genres.append("Animation")
        if specific.kids == "1":
            genres.append("Children's")
        if specific.comedy == "1":
            genres.append("Comedy")
        if specific.crime == "1":
            genres.append("Crime")
        if specific.docu == "1":
            genres.append("Documentary")
        if specific.drama == "1":
            genres.append("Drama")
        if specific.fant == "1":
            genres.append("Fantasy")
        if specific.scifi == "1":
            genres.append("Sci-Fi")
        if specific.horror == "1":
            genres.append("Horror")
        if specific.noir == "1":
            genres.append("Film Noir")
        if specific.music == "1":
            genres.append("Musical")
        if specific.mystery == "1":
            genres.append("Mystery")
        if specific.romance == "1":
            genres.append("Romance")
        if specific.thriller == "1":
            genres.append("Thriller")
        if specific.war == "1":
            genres.append("War")
        if specific.western == "1":
            genres.append("Western")
        genres_str = ", ".join(genres)
        return genres_str


class User:
    def __init__(self, **kwargs):
        self.user_id = kwargs["user_id"]
        self.age = int(kwargs["age"])
        self.job = kwargs["occupation"]

    def __repr__(self):
        return "{} {} {}".format(self.user_id, self.age, self.job)


class Rating:
    def __init__(self, **kwargs):
        self.movie_id = kwargs["movie_id"]
        self.user_id = kwargs["user_id"]
        self.rating = float(kwargs["rating"])
        self.timestamp = kwargs["timestamp"]

    def __repr__(self):
        return "{} {} {}".format(self.movie_id, self.user_id, self.rating)


def average_rating(movie_id):
    ratinginfo = ratings_by_movie[movie_id]
    return sum([each.rating for each in ratinginfo])/len(ratinginfo)


def get_ratings_for_movie(movid):
    ratingsl = []
    ratinginfo = ratings_by_movie[movid]
    [(ratingsl.append(i.rating)) for i in ratinginfo]
    return ratingsl


def ratings_written(person):
    ratingsl = []
    ratinginfo = ratings_by_user[person]
    [ratingsl.append(i.rating) for i in ratinginfo]
    return ratingsl


def ratings_written_plus_title(person):
    ratingsl = []
    ratinginfo = ratings_by_user[person]
    ([(ratingsl.append(((movie_table[i.movie_id].get_title_from_id(i.movie_id))
     + ": " + str(i.rating)))) for i in ratinginfo])
    return ratingsl


def movies_seen(person):
    watchedl = []
    ratinginfo = ratings_by_user[person]
    [watchedl.append(i.movie_id) for i in ratinginfo]
    return watchedl


def movies_seen_plus(person):
    watchedl = []
    ratinginfo = ratings_by_user[person]
    [(watchedl.append([i.rating, i.movie_id])) for i in ratinginfo]
    return watchedl


def popular_movies(list_len, user_number):
    top_movies = []
    movie_id_list = []
    movies_rated = []
    if user_number != 'top':
        [movies_rated.append(i.movie_id) for i in ratings_by_user[user_number]]
    smaller_movie_id_list = []
    i = 1
    while True:
        if str(i) in ratings_by_movie:
            if str(i) not in movies_rated:
                smaller_movie_id_list.append(str(i))
            movie_id_list.append(str(i))
            i += 1
        if len(movie_id_list) == len(ratings_by_movie):
            break
    list_three = []
    if user_number == 'top':
        ([list_three.append([average_rating(m), m,
         len(get_ratings_for_movie(m))]) for m in movie_id_list])
    else:
        ([list_three.append([average_rating(m), m,
         len(get_ratings_for_movie(m))]) for m in smaller_movie_id_list])
    list_two = []
    [list_two.append([j[0], j[1]]) for j in list_three if j[2] > 10]
    list_two.sort(reverse=True)
    ([top_movies.append((movie_table[i[1]].get_title_from_id(i[1]) + ": " +
     str(round(i[0], 2)))) for i in list_two])
    top = top_movies[:list_len]
    string_top = """
    """.join(top)
    return string_top


def euc(user_number):
    list_user_movieid_ratings = []
    user_list = []
    i = 1
    while str(i) in ratings_by_user:
        ratingsl = []
        ([ratingsl.append(([j.movie_id, j.rating, i])) if str(i) != user_number
         else user_list.append(([j.movie_id, j.rating, i])) for j in
         ratings_by_user[str(i)]])
        if len(ratingsl) != 0:
            list_user_movieid_ratings.append(ratingsl)
        i += 1
    euclidean_user = []
    for item in list_user_movieid_ratings:
        v = []
        w = []
        for entry in user_list:
            for each in item:
                if entry[0] == each[0]:
                    v.append(entry[1])
                    w.append(each[1])
        dist = euclidean_distance(v, w)
        euclidean_user.append([dist, item[0][2]])
    euclidean_user.sort(reverse=True)
    z = 0
    while True:
        closest_user = euclidean_user[z][1]
        other_movies = movies_seen_plus(str(closest_user))
        your_movies = movies_seen(str(user_number))
        new_possible = []
        for om in other_movies:
            if om[1] in your_movies:
                pass
            else:
                new_possible.append(om)
        new_possible.sort(reverse=True)
        if len(new_possible) == 0:
            z += 1
        else:
            pretty_list = []
            for np in new_possible:
                title = movie_table[np[1]].get_title_from_id(np[1])
                title += ': rating from similar user was  ' + str(np[0])
                pretty_list.append(title)
            euc_list = """
            """.join(pretty_list)
            return euc_list


def euclidean_distance(v, w):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """
    if len(v) is 0:
        return 0
    # Note that this is the same as vector subtraction.
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)
    return 1 / (1 + math.sqrt(sum_of_squares))


def open_ratings_data(rating_path):
    organize_ratings_data = {}
    ratings_ordered_by_user = {}
    with open(rating_path, encoding="latin-1") as f:
        ratings_headers = ["user_id", "movie_id", "rating", "timestamp"]
        reader = csv.DictReader(f, delimiter="\t", fieldnames=ratings_headers)
        for row in reader:
            i = Rating(**row)
            organize_ratings_data.setdefault(i.movie_id, []).append(i)
            ratings_ordered_by_user.setdefault(i.user_id, []).append(i)
    return organize_ratings_data, ratings_ordered_by_user


def open_rater_data(user_path):
    demographics = {}
    with open(user_path, encoding='latin_1') as p:
        rater_headers = ["user_id", "age", "gender", "occupation", "zip_code"]
        reader = csv.DictReader(p, delimiter="|", fieldnames=rater_headers)
        for row in reader:
            each_user = User(**row)
            demographics[each_user.user_id] = each_user
    return demographics


def open_movie_data(movie_path):
    movies = {}
    with open(movie_path, encoding='latin_1') as m:
        movie_headers = ["movie_id", "movie_title", "release_date",
                         "video_release_date", "IMDb_URL", "unknown", "Action",
                         "Adventure", "Animation", "Childrens", "Comedy",
                         "Crime", "Documentary", "Drama", "Fantasy",
                         "Film_Noir", "Horror", "Musical", "Mystery",
                         "Romance", "Sci_Fi", "Thriller", "War", "Western"]
        reader = csv.DictReader(m, delimiter="|", fieldnames=movie_headers)
        for row in reader:
            each_movie = Movie(**row)
            movies[each_movie.movie_id] = each_movie
    return movies


movie_table = open_movie_data(movie_path)
rater_table = open_rater_data(user_path)
ratings_by_movie, ratings_by_user = open_ratings_data(rating_path)
