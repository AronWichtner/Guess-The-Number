from userinputprocessing import *
from setalevel import *
from userlives import *


def game():
    print(introduction())
    while True:


        # which level
        x = get_users_level()
        userslives = get_users_lives()
        if x == False:
            continue


        # set up for level 5
        elif type(x) == list:
            rannumbs = generate_random_numbers(x)
            listitem = 0
            rannum = rannumbs[listitem]
            limit = x[listitem]
            userslives = userslives[4]


        # set up for level 1 to 4
        else:
            rannum = generate_random_number(x)
            limit = x
            if limit == 10:
                userslives = userslives[0]
            elif limit == 20:
                userslives = userslives[1]
            elif limit == 50:
                userslives = userslives[2]
            elif limit == 100:
                userslives = userslives[3]
        previously_guessed_numbers = set()


        while True:


            # life status
            print("\nlives: ", userslives)


            # get users guess
            users_number = read_users_number_or_none()


            # does users number count
            if users_number is None:
                continue
            if is_number_out_of_limit(users_number, limit):
                continue
            if users_number in previously_guessed_numbers:
                print(f"Number: {users_number} was already guessed!")
                continue
            previously_guessed_numbers.add(users_number)


            # answer to given guess if wrong
            solution = is_it_higher_lower_win(users_number, rannum)
            if solution[0] == False:
                reducelive(userslives, 0)
                if len(userslives) == 0:
                    print("""GAME OVER! You lost all your lives
The correct answer would have been {}\n""".format(rannum))
                    return start_another_game()
                else:
                    print(solution[1])
                    continue


            # answer to given guess if right
            else:


                # for lvl 5
                if type(x) == list:
                    listitem = listitem + 1
                    if listitem == 4:
                        print(solution)
                        print("You completed all levels.")
                        return start_another_game()
                    else:
                        print(solution)
                        print("You are now entering the next level.")
                        rannum = rannumbs[listitem]
                        limit = x[listitem]
                        continue


                # for lvl 1 to 4
                else:
                    print(solution)
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