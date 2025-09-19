from datetime import datetime
movie_file = {}
def add_movie(movie_name):
    current_time = datetime.now()
    formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
    if movie_name not in movie_file:
        movie_file[movie_name] = {
            "Time when movie was added": formatted_date,
            "rating": [],
            "average_rating": [],
        }
        return f"movie {movie_name} added successfully at {formatted_date}"
    else:
        return "movie already added"

def rate_movie(movie_name, rating):
    if movie_name in movie_file:
        movie_file[movie_name]["rating"].append(rating)
        return f"rating added for {movie_name} "
    else:
        return "movie not found"

def do_average_rating(movie_name):
     ratings =  movie_file[movie_name]["rating"]
     if ratings:
        avg = sum(ratings)/len(ratings)
        movie_file[movie_name]["average_rating"].append(avg)
        return f" Average rating for '{movie_name}': {avg:.2f}1"
     else:
        return "no rating available to calculate"














