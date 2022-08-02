def welcome(name):
    #Get the name of the user and print Message
    #Ensure string input
    try:
            name = str(name)
    except ValueError:
            print("Please input string only...")

    return print(f" Hello {name} and welcome to the world Games (WoG). \n Here you can find many cool games to play")

def load_game():
    #Input of game
    optionsg = [1,2,3]
    which_game = input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n 2. Guess Game - guess a number and see if you chose like the computer \n 3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    while len(which_game) != 1 or (not which_game.isdigit()) or (not int(which_game) in optionsg):
        print ('Not a 1 digit number or you did not enter a number between 1-3')
        which_game = input('Please enter only 1 digit number between 1-3:')
    which_game = int(which_game)
    if which_game == 1:
        from MemoryGame import play
        play()
    elif which_game == 2:
        from GuessGame import play
        play()
    elif which_game == 3:
        from CurrencyRouletteGame import play
        play()

def load_Difficulty():
    #Input of the difficulty:
    optionsd = [1, 2, 3, 4, 5]
    difficulty = input('Please choose game difficulty from 1 to 5:')
    while len(difficulty) != 1 or (not difficulty.isdigit()) or (not int(difficulty) in optionsd):
        print('Not a 1 digit number or you did not enter a number between 1-5')
        difficulty = input('Please enter only 1 digit number between 1-5:')
    difficulty = int(difficulty)
    return difficulty



