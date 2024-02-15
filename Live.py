def welcome(name):
    return (f"Hello {name} and welcome to the World of Games (WoG)." + "\n"
                                                                       "Here you can find many cool games to play.")


def load_game():
    game_choice = input("Please choose a game to play:" + "\n" +
                        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to" + "\n" +
                        "guess it back" + "\n" +
                        "2. Guess Game - guess a number and see if you chose like the computer" + "\n" +
                        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS" + "\n")
    level_of_difficulty = input("Please choose game difficulty from 1 to 5: ")

    print(f"game_choice = {game_choice}, level_of_difficulty = {level_of_difficulty} ")
