import random
from os import system, name
from time import sleep

RANDOM_RANGE_MAX = 101

ILLEGAL_USER_GUESS = 0


class OutOfLegalRangeSequenceValueException(Exception):
    """Exception raised for integer sequence value out of legal range"""

    def __init__(self, sequence_value,
                 message=f"Legal sequence value can be in 1-{RANDOM_RANGE_MAX} range only"):
        super().__init__(message)
        self.sequence_value = sequence_value
        self.message = message

    def __str__(self):
        return f" {self.sequence_value} is out of legal range. \n {self.message}. \n"


def is_legal_sequence_value(sequence_value):
    if sequence_value not in range(1, RANDOM_RANGE_MAX):
        raise OutOfLegalRangeSequenceValueException(sequence_value)
    return sequence_value


def clear():
    """
    define our clear function
    @link: https://www.geeksforgeeks.org/clear-screen-python/
    :return:
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def generate_sequence(difficulty):
    """
    Will generate a list of random numbers between 1 and 101.
    The list length will be difficulty.
    :param difficulty:
    :return: [int]
    """
    sequence = random.sample(range(1, RANDOM_RANGE_MAX), difficulty)
    print(sequence)
    sleep(3)
    clear()
    return sequence


def get_list_from_user(difficulty):
    """
    Will return a list of numbers prompted from the user.
    The list length will be in the size of difficulty.
    :param difficulty:
    :return: [int]
    """
    try:
        user_guess_string = input(f"Please enter {difficulty} numbers were displayed to you"
                                  f"separated with spaces"
                                  f" Illegal format input means automatic technical loss ")
        strings_list = str.split(user_guess_string, " ")
        if len(strings_list) != difficulty:
            return ILLEGAL_USER_GUESS
        answer_sequence = list(map(is_legal_sequence_value, map(lambda x: int(x), strings_list)))
        # print(answer_sequence)  # [1, 8, 27, 64, 125]

    except ValueError as e:
        return ILLEGAL_USER_GUESS
    except OutOfLegalRangeSequenceValueException as e:
        # print(e)
        return ILLEGAL_USER_GUESS

    return answer_sequence


def is_list_equal(question_sequence, answer_sequence):
    """
    A function to compare two lists if they are equal. The function will return
    True / False.
    :param question_sequence:
    :param answer_sequence:
    :return: True / False
    """
    # print('MEMORY_GAME')
    # print(f'question_sequence = {question_sequence}, answer_sequence = {answer_sequence}')
    return question_sequence == answer_sequence


def play(difficulty):
    """
    The purpose of memory game is to display an amount of random numbers to the users for 0.7
    seconds and then prompt them from the user for the numbers that he remember.
    If he was right with all the numbers the user will win otherwise he will lose.
    Will call the functions above and play the game.
    Will return True / False if the user lost or won.
    :param difficulty:
    :return: Boolean
    """
    question_sequence = generate_sequence(difficulty)
    answer_sequence = get_list_from_user(difficulty)
    if answer_sequence == ILLEGAL_USER_GUESS:
        # print(f'Illegal user guess input. You lost!')
        return False

    return is_list_equal(question_sequence, answer_sequence)
