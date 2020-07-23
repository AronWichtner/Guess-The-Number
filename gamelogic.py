from userinputprocessing import *
from setalevel import *


def game():
    print(introduction())
    while True:
        x = get_users_level_or_false()
        if x == False:
            continue
        else:
            rannum = generate_number(x)
        while True:
            i = check_for_intiger()
            if type(i) == int:
                a = is_within_the_limit(i, x)
                if a == False:
                    continue
                else:
                    solution = is_it_higher_lower_win(i, rannum)
                    if solution == False:
                        continue
                    else:
                        print(solution)
                        return start_another_game()
            else:
                continue


def introduction():
    return """\nIn this game you have to guess a random number between 0 and another number.
There are five difficulty levels.
->0-10 (level 1)
->0-20 (level 2)
->0-50 (level 3)
->0-100 (level 4)
->all levels at once (level 5)\n"""


def start_another_game():
    while True:
        ans = input("Do you want to play another game?\nType Y for yes or N for no: ")
        if ans == "y" or ans == "Y":
            return game()
        elif ans == "n" or ans == "N":
            return "\nok bye:(\n"
        else:
            print("\nWe do not understand your input\n")
            continue


print(game())



