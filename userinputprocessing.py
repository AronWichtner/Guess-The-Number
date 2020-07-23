def check_for_intiger():
    try:
        users_input = int(input("\nGuess is the number? \n"))
    except ValueError:
        print("You may only use integer!\n")
    else:
        return users_input


def is_within_the_limit(users_input, limit):
    if users_input > limit or users_input < 0:
        print("\n{} is not within 0 to {}.\n".format(users_input, limit))
        users_input = False
        return users_input
    else:
        users_input = True
        return users_input


def is_it_higher_lower_win(users_number, random_number):
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