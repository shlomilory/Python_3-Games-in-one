"""
MemoryGame.py
The purpose of memory game is to display an amount of random numbers to the users for 0.7
seconds and then prompt them from the user for the numbers that he remember. If he was right
with all the numbers the user will win otherwise he will lose.
Properties
1. Difficulty
Methods
1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
length will be ​difficulty​.
2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
will be in the size of ​difficulty​.
3. is_list_equal - A function to compare two lists if they are equal. The function will return
True / False.
4. play - Will call the functions above and play the game. Will return True / False if the user
lost or won.
"""
import collections
import sys
import time
from Live import load_Difficulty
class WorldOfGames:
    Difficulty = load_Difficulty()
#---------------------------------------#
class MemoryGame(WorldOfGames):
    def generate_sequence(self):
        import random
        self.list = random.sample(range(1, 101), WorldOfGames.Difficulty)
        sys.stdout.write(f'{self.list}')
        time.sleep(0.7)
        sys.stdout.write(f'\r            ')
        time.sleep(0.7)
        return self.list
    def get_list_from_user(self):
        list = []
        for n in range(WorldOfGames.Difficulty):
            num = int(input("Input numbers equal to the number of the Difficulty"))
            list.append(num)
        return list
    def is_list_equal(self):
        if (collections.Counter(self.generate_sequence()) == collections.Counter(self.get_list_from_user())):
            return True
        else:
            return False
def play():
    run = MemoryGame()
    print(run.is_list_equal())






