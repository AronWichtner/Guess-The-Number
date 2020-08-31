import random

from UserLevelInput import UserLevelInput


def generate_random_numbers(limits: [int]):
    return [random.randint(0, limit) for limit in limits]


def get_level_limits(level: int) -> [int]:
    return {
        1: [10],
        2: [20],
        3: [50],
        4: [100],
        5: [10, 20, 50, 100]
    }.get(level)


def get_users_level() -> UserLevelInput:
    try:
        level_input = int(input("In what level do you want to play? Type in the number(1 for level 1, 2 for...): "))
        if not 1 <= level_input <= 5:
            print("there are only levels from one to five\n")
            return UserLevelInput(is_valid=False)
    except ValueError:
        print("We did not understand your input.")
        return UserLevelInput(is_valid=False)

    return UserLevelInput(
        level=level_input,
        limits=get_level_limits(level_input),
        is_valid=True
    )
