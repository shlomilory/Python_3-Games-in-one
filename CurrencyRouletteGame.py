from Live import load_Difficulty
class WorldOfGames:
    Difficulty = load_Difficulty()
#----------------------------------------#

class CurrencyRouletteGame(WorldOfGames):
    from random import randrange
    Difficulty = WorldOfGames.Difficulty
    from currency_converter import CurrencyConverter
    data = CurrencyConverter()
    random = randrange(1, 100)
    def get_money_interval(self):
        currentC = CurrencyRouletteGame.data.convert(CurrencyRouletteGame.random,'USD','ILS')
        self.interval = (currentC - (5 - CurrencyRouletteGame.Difficulty), currentC +(5 - CurrencyRouletteGame.Difficulty))
        return self.interval
    def get_guess_from_user(self):
        Guess = int(input(f"Guess the amount of USD "))
        if self.get_money_interval()[0] <= Guess <= self.get_money_interval()[1]:
            return True
        else:
            return False

def play():
    Currency = CurrencyRouletteGame()
    print(Currency.get_guess_from_user())

