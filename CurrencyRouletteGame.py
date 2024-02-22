import random

import everapi.exceptions
import freecurrencyapi

API_KEY = "fca_live_ljth3fhuWB9zTpUzp2IJ2STZ07BMvbPG4WsbiZx8"
NO_CONNECTIVITY_DEFAULT_FROM_USD_TO_ILS_RATE = 3
RANDOM_RANGE_MAX = 101
ILLEGAL_USER_GUESS = 0


def get_usd_random_amount():
    return random.randint(1, RANDOM_RANGE_MAX)


def get_money_interval(usd_random_amount, difficulty):
    """
    Will get the current currency rate from USD to ILS and will
    generate an interval as follows:
    a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
    (5 - d))
    :return: range array
    """
    try:
        client = freecurrencyapi.Client(API_KEY)
        result = client.latest(currencies=['ILS'])
        from_usd_to_ils_rate = result['data']['ILS']
        print(from_usd_to_ils_rate)
    except (
            everapi.exceptions.IncorrectApikey,
            everapi.exceptions.RateLimitExceeded,
            everapi.exceptions.ApiError,
            everapi.exceptions.NotAllowed,
            everapi.exceptions.QuotaExceeded
    ) as e:
        # print(e.__class__)
        # print('NO_CONNECTIVITY_DEFAULT_FROM_USD_TO_ILS_RATE')
        from_usd_to_ils_rate = NO_CONNECTIVITY_DEFAULT_FROM_USD_TO_ILS_RATE

    total_ils_value = round(usd_random_amount * from_usd_to_ils_rate)
    low_limit = (total_ils_value - (5 - difficulty)) if ((total_ils_value - (5 - difficulty)) > 0) else 1
    high_limit = total_ils_value + (5 - difficulty) + 1
    success_range = {
        'low_limit': low_limit,
        'high_limit': high_limit
    }
    return success_range


def get_guess_from_user(usd_random_amount):
    """
    A method to prompt a guess from the user to enter a guess of
    value to a given amount of USD
    :return: int
    """
    try:
        user_guess = int(input(f"Please guess a ILS number value of  {usd_random_amount} USD."
                               f" Illegal input means automatic technical loss "))
    except ValueError as e:
        return ILLEGAL_USER_GUESS

    return user_guess


def play(difficulty):
    """
    Will call the functions above and play the game. Will return True / False if the user
    lost or won.
    :return: Boolean
    """
    usd_random_amount = get_usd_random_amount()
    success_interval = get_money_interval(usd_random_amount, difficulty)
    print(success_interval)
    user_guess = get_guess_from_user(usd_random_amount)
    if user_guess == ILLEGAL_USER_GUESS:
        print(f'Illegal user guess input. You lost!')
        return False

    return user_guess in range(success_interval['low_limit'],
                               success_interval['high_limit']
                               )
