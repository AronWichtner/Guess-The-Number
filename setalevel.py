import random


def generate_number_for_onetofour(limit):
    random_number = random.randint(0, limit)
    return random_number


def generate_number_for_five(limits):
    rannum1 = random.randint(0, limits[0])
    rannum2 = random.randint(0, limits[1])
    rannum3 = random.randint(0, limits[2])
    rannum4 = random.randint(0, limits[3])
    rannumbs = [rannum1, rannum2, rannum3, rannum4]
    return rannumbs


def get_users_level_or_false():
    try:
        x = int(input("In what level do you want to play? Type in the number(1 for level 1, 2 for...): "))
    except ValueError:
        print("We did not understand your input.")
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
        elif x == 5:
            limit1 = 10
            limit2 = 20
            limit3 = 50
            limit4 = 100
            limits = [limit1, limit2, limit3, limit4]
            return limits
        else:
            print("there are only levels from one to five\n")
            return False

