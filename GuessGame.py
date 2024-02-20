import random

ILLEGAL_USER_GUESS = 0


def generate_number(difficulty):
    """
    generate_number - Will generate number between 1 to difficulty and save it to
    secret_number.
    :param difficulty:
    :return: int
    """
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    """
    Will prompt the user for a number between 1 to difficulty and
    return the number.
    :param difficulty:
    :return: int
    """
    try:
        user_guess = int(input(f"Please guess a number between 1 to {difficulty}."
                               f" Illegal input means automatic technical loss "))
    except ValueError as e:
        return ILLEGAL_USER_GUESS

    if user_guess not in range(1, difficulty + 1):
        return ILLEGAL_USER_GUESS

    return user_guess


def compare_results(secret_number, user_guess):
    """
    Will compare the secret generated number to the one prompted
    by the get_guess_from_user.
    :param secret_number:
    :param user_guess:
    :return:
    """
    print('GUESS_GAME')
    print(f'secret_number = {secret_number}, user_guess = {user_guess}')
    return secret_number == user_guess


def play(difficulty):
    """
    Will call the functions above and play the game. Will return True / False if the user
    lost or won.
    :param difficulty:
    :return: Boolean
    """
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)

    if user_guess == ILLEGAL_USER_GUESS:
        print(f'Illegal user guess input. You lost!')
        return False

    return compare_results(secret_number, user_guess)
