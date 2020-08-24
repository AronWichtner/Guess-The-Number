from userinputprocessing import *
from setalevel import *


def game():
    print(introduction())
    while True:
        x = get_users_level_or_false()
        if x == False:
            continue
        elif type(x) == list:
            rannumbs = generate_number_for_five(x)
            listitem = 0
            rannum = rannumbs[listitem]
            limit = x[listitem]
        else:
            rannum = generate_number_for_onetofour(x)
            limit = x
        while True:
            i = check_for_integer()
            if type(i) == int:
                a = is_within_the_limit(i, limit)
                if a == False:
                    continue
                else:
                    solution = is_it_higher_lower_win(i, rannum)
                    if solution == False:
                        continue
                    else:
                        if type(x) == list:
                            listitem = listitem + 1
                            if listitem == 4:
                                print(solution)
                                print("You completed all levels.")
                                return start_another_game()
                            else:
                                print(solution)
                                print("You are entering the next level.")
                                rannum = rannumbs[listitem]
                                limit = x[listitem]
                                continue
                        else:
                            print(solution)
                            print("You completed this level.")
                            return start_another_game()
            else:
                continue


def introduction():
    return """\nIn this game you have to guess a random number between 0 and another number.
There are five difficulty levels and each time you guess wrong you lose one live.
->0-10 (level 1, 4 lives)
->0-20 (level 2, 5 lives)
->0-50 (level 3, 6 lives)
->0-100 (level 4, 7 lives)
->all levels at once (level 5, 22 lives)\n"""


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



