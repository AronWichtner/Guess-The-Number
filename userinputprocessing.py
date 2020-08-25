def read_users_number_or_none():
    try:
        users_number = int(input("Guess is the number: \n"))
        return users_number
    except ValueError:
        print("You may only use integer!\n")
        return None

def is_number_out_of_limit(users_input, limit):
    is_out_of_limit = users_input > limit or users_input < 0
    if is_out_of_limit:
        print("\n{} is not within 0 to {}.\n".format(users_input, limit))
    return is_out_of_limit

def is_it_higher_lower_win(users_number, random_number):
    if users_number < random_number:
        users_number = False
        tipp = "\nguess higher!\n"
        solution = [users_number, tipp]
        return solution
    elif users_number > random_number:
        users_number = False
        tipp = "\nguess lower!\n"
        solution = [users_number, tipp]
        return solution
    else:
        return "\nYou win! The number equals to {}.\n".format(users_number)