import random


def gamee():
    print(start())
    rannum = generatenumber()
    while True:
        i = intiger()
        if type(i) == int:
            a = within_the_limit(i)
            if a == False:
                continue
            else:
                solution = higher_lower_win(i, rannum)
                if solution == False:
                    continue
                else:
                    print(solution)
                    return anothergame()
        else:
            continue


def generatenumber():
    random_number = random.randint(0, 20)
    return random_number


def start():
    return """\nIn this game you have to guess a random number between 0 and 20.\n"""


def intiger():
    try:
        users_input = int(input("\nWhat is the number? \n"))
    except ValueError:
        print("You may only use integer!\n")
    else:
        return users_input


def within_the_limit(users_input):
    if users_input > 20 or users_input < 0:
        print("\n{} is not within 0 to 20.\n".format(users_input))
        users_input = False
        return users_input
    else:
        users_input = True
        return users_input


def higher_lower_win(users_number, random_number):
    if users_number < random_number:
        users_number = False
        print("\nguess higher!\n")
        return users_number
    elif users_number > random_number:
        users_number = False
        print("\nguess lower!\n")
        return users_number
    else:
        return "\nYou win! The number equals to {}.\n".format(users_number)


def anothergame():
    while True:
        ans = input("Do you want to play another game?\nType Y for yes or N for no: ")
        if ans == "y" or ans == "Y":
            return gamee()
        elif ans == "n" or ans == "N":
            return "\nok bye:(\n"
        else:
            print("\nWe do not understand your input\n")
            continue


print(gamee())