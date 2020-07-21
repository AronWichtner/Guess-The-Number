# level5: all levels at once
import random


def generatenumber(limit):
    random_number = random.randint(0, limit)
    return random_number


def level():
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

