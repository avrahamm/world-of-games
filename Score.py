"""
A package that is in charge of managing the scores file.
The scores file at this point will consist of only a number. That number is the accumulation of the
winnings of the user. Amount of points for winning a game is as follows:
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
Each time the user is winning a game, the points he one will be added to his current amount of
point saved in a file.
"""

from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(difficulty):
    """
    - The function’s input is a variable called difficulty. The function will try to read
    the current score in the scores file, if it fails it will create a new one and will use it to save
    the current score.
    """

    current_score = get_current_score()
    if current_score == BAD_RETURN_CODE:
        current_score = 0

    with open(SCORES_FILE_NAME, "w") as scores_file:
        points_of_winning = (int(difficulty) * 3) + 5
        updated_score = str(current_score + points_of_winning)
        scores_file.write(updated_score)

    scores_file.close()

    return updated_score


def get_current_score():
    try:
        scores_file = open(SCORES_FILE_NAME, "r")
        current_score = int(scores_file.read())
        return current_score

    except (
            FileNotFoundError
    ):
        scores_file = open(SCORES_FILE_NAME, "x")
        updated_score = 0
        scores_file.write(str(updated_score))
        return updated_score

    except (
            ValueError,
            PermissionError,
            Exception
    ):
        return BAD_RETURN_CODE

