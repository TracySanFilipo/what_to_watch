What to Watch
This program is designed to be used through the movie interface file. The user can choose from seven options (plus quit) in the main function of the movie interface file. The first option calls the get_title_from_id() method from in the Movie class. The second calls the check_topic() method from the Movie class. The third calls the average_rating() function using ratings data. The fourth calls the get_ratings_for_movie() function using ratings data. The fifth calls the ratings_written() function using ratings data. The sixth calls the popular_movies() function using ratings data. The seventh calls the euc() function using ratings data.

Movie Class
The movie class contains instances that have a movie id number, a movie title, and a boolean value for several genres. There are two methods for this class other than init. The first, get_title_from_id(), looks up and returns the title of the movie based on the movie id number. The second, check_topic(), returns a list of the genres that the movie has a positive boolean for.
