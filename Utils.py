from os import system, name


# A string representing a file name.
SCORES_FILE_NAME = "scores.txt"
# A number representing a bad return code for a function.
BAD_RETURN_CODE = -1


# Screen_cleaner - A function to clear the screen
# (useful when playing memory game or
# before a new game starts).
def screen_cleaner():
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
