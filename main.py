from movie_console_app import add_movie, rate_movie, do_average_rating
def main():
    display = """
                MOVING RATING SYSTEM
                1.Add movie
                2.Add rating
                3.Average rating
            1
                0.Exit"
                """
    hunterly = True
    while hunterly:
        print(display)
        option = int(input("Enter movie rating: "))
        match option:
            case 1:
                print("Add movie")
                user_input = input("Enter movie name:")
                print(add_movie(user_input))
            case 2:
                print("Add rating")
                user_input = input("Enter movie name:")
                rating = int(input("Enter movie rating(0-50):"))
                print(rate_movie(user_input, rating))
            case 3:
                print("Average rating")
                user_input = input("Enter movie name:")
                print(do_average_rating(user_input))
            case 0:
                print("Exit")
                hunterly = False
            case _:
                print("Invalid input")
main()






