from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from CurrencyRouletteGame import play as play_currency_roulette_game


class Constants:
    GAME_CHOICES = 3
    LEVELS_OF_DIFFICULTY = 5
    MEMORY_GAME = '1'
    GUESS_GAME = '2'
    CURRENCY_ROULETTE = '3'


class OutOfLegalGameChoiceValueRangeException(Exception):
    """Exception raised for integer value out of legal game choice value range"""

    def __init__(self, game_choice,
                 message=f"Legal game choice can be in 1-{Constants.GAME_CHOICES} range only"):
        super().__init__(message)
        self.game_choice = game_choice
        self.message = message

    def __str__(self):
        return (f"game choice {self.game_choice} is out of legal range. \n {self.message}. "
                f"Please try again. \n")


class OutOfLegalLevelOfDifficultyValueRangeException(Exception):
    """Exception raised for integer value out of legal level of difficulty value range"""

    def __init__(self, level_of_difficulty,
                 message=f"Legal level of difficulty can be in 1-{Constants.LEVELS_OF_DIFFICULTY} range only"):
        super().__init__(message)
        self.level_of_difficulty = level_of_difficulty
        self.message = message

    def __str__(self):
        return (f"level_of_difficulty {self.level_of_difficulty} is out of legal range. \n {self.message} \n"
                f"Please try again.")


def welcome(name):
    return (f"Hello {name} and welcome to the World of Games (WoG)." + "\n"
                                                                       "Here you can find many cool games to play.")


def is_game_choice_legal(game_choice):
    return game_choice in range(1, Constants.GAME_CHOICES + 1)


def is_level_of_difficulty_legal(level_of_difficulty):
    return level_of_difficulty in range(1, Constants.LEVELS_OF_DIFFICULTY + 1)


def load_game():
    while True:
        try:
            game_choice = int(input("Please choose a game to play:" + "\n" +
                                    "1. Memory Game - a sequence of numbers will appear for 1 second and you have to" + "\n" +
                                    "guess it back" + "\n" +
                                    "2. Guess Game - guess a number and see if you chose like the computer" + "\n" +
                                    "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"
                                    + "\n"))
            if not is_game_choice_legal(game_choice):
                raise OutOfLegalGameChoiceValueRangeException(game_choice)

            level_of_difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if not is_level_of_difficulty_legal(level_of_difficulty):
                raise OutOfLegalLevelOfDifficultyValueRangeException(level_of_difficulty)

        except ValueError as e:
            print("Not numerical input is illegal. Please try again." + "\n")
            continue

        except OutOfLegalGameChoiceValueRangeException as e:
            print(e)
            continue

        except OutOfLegalLevelOfDifficultyValueRangeException as e:
            print(e)
            continue

        print(f"game_choice = {game_choice}, level_of_difficulty = {level_of_difficulty} ")

        match str(game_choice):
            case Constants.MEMORY_GAME:
                return play_memory_game(difficulty=level_of_difficulty)
            case Constants.GUESS_GAME:
                return play_guess_game(difficulty=level_of_difficulty)
            case Constants.CURRENCY_ROULETTE:
                return play_currency_roulette_game(difficulty=level_of_difficulty)

        return False
