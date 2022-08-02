"""
The purpose of guess game is to start a new game, cast a random number between 1 to a
variable called ​difficulty​. The game will get a number input from the
Properties
1. Difficulty
2. Secret number
Methods
1. generate_number - Will generate number between 1 to difficulty and save it to
secret_number.
2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
return the number.
3. compare_results - Will compare the the secret generated number to the one prompted
by the get_guess_from_user.
4. play - Will call the functions above and play the game. Will return True / False if the user
lost or won
"""
from Live import load_Difficulty
class WorldOfGames:
    Difficulty = load_Difficulty()
from random import randrange
#-------------------------------------------#
class GuessGame(WorldOfGames):
    secret_word = randrange(1,WorldOfGames.Difficulty)
    list_guess = list(range(1,WorldOfGames.Difficulty))
    #print(secret_word)
    def get_guess_from_user(self):
        self.Guess = input(f"Please enter your guess between 1 to {WorldOfGames.Difficulty}")
        while len(self.Guess) != 1 or (not self.Guess.isdigit()) or (not int(self.Guess) in GuessGame.list_guess):
            print("Please enter a number Between 1 to to difficulty you chose earlier")
            self.Guess = input(f"Please enter your guess between 1 to {WorldOfGames.Difficulty}")
        print(f"Your Guess is {self.Guess}")
        return int(self.Guess)

    def compare_results(self):
        if GuessGame.secret_word == self.get_guess_from_user():
            return True
        else:
            return False


def play():
    My_Guess = GuessGame()
    print(My_Guess.compare_results())
