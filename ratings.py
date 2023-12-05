"""Restaurant rating lister."""

#create function
def abc_order_reviews(filename):
    """Restaurant rating lister. In abc order"""
#get each line from file
    file = open(filename)


    lines_dict = {}

    for lines in file:
        lines = lines.rstrip()
        name, rating = lines.split(":")
        lines_dict[name] = rating

    file.close()

    for name, rating in sorted(lines_dict.items()):
        print(f"{name} is rated at {rating}")

# abc_order_reviews("scores.txt")



def add_user_ratings(filename):
    """it prompts the user for a new restaurant and rating"""

    file = open(filename)
    lines_dict = {}

    name_input = input("Please give us a restaurant name: ").title()
    rating_input = input("What is your rating for this restaurant?: ")

    lines_dict[name_input] = rating_input

    for lines in file:
        lines = lines.rstrip()
        name, rating = lines.split(":")
        lines_dict[name] = rating
    print(lines_dict)

    for name, rating in sorted(lines_dict.items()):
        print(f"{name} is rated at {rating}")

    file.close()

    # return lines_dict

add_user_ratings("scores.txt")