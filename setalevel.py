# create level 5: all levels at once
import random


def generate_number(limit):
    random_number = random.randint(0, limit)
    return random_number


def get_users_level_or_false():
    try:
        x = int(input("In what level do you want to play? Type in the number(1 for level 1, 2 for...): "))
    except ValueError:
        print("we did not understand your input")
        return False
    else:
        if x == 1:
            limit = 10
            return limit
        elif x == 2:
            limit = 20
            return limit
        elif x == 3:
            limit = 50
            return limit
        elif x == 4:
            limit = 100
            return limit
        else:
            print("there are only levels from one to five\n")
            return False

