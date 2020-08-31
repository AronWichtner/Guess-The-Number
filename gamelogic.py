from userinputprocessing import *
from setalevel import *
from userlives import *


def game():
    print(introduction())
    while True:
        level = get_users_level()

        if not level.is_valid:
            continue
        elif level.level == 5:
            rannumbs = generate_random_numbers(level.limits)
            listitem = 0
            rannum = rannumbs[listitem]
            limit = level.limits[listitem]
        else:
            limit = level.limits[0]
            rannum = generate_random_numbers(level.limits)[0]

        previously_guessed_numbers = set()
        while True:
            print("\nlives: ", level.user_lives)
            users_number = read_users_number_or_none()
            if users_number is None:
                continue
            if is_number_out_of_limit(users_number, limit):
                continue
            if users_number in previously_guessed_numbers:
                print(f"Number: {users_number} was already guessed!")
                continue
            previously_guessed_numbers.add(users_number)

            solution = is_it_higher_lower_win(users_number, rannum)
            if solution[0] == False:
                level.reduce_live()
                if len(level.user_lives) == 0:
                    print("""GAME OVER! You lost all your lives
The correct answer would have been {}\n""".format(rannum))
                    return start_another_game()
                else:
                    print(solution[1])
                    continue
            else:
                if level.level == 5:
                    listitem = listitem + 1
                    if listitem == 4:
                        print(solution[1])
                        print("You completed all levels.")
                        return start_another_game()
                    else:
                        print(solution[1])
                        print("You are now entering the next level.")
                        rannum = rannumbs[listitem]
                        limit = level[listitem]
                        continue
                else:
                    print(solution[1])
                    print("You completed this level.")
                    return start_another_game()


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



