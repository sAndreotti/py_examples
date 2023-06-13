import math
import random

class Player:
    def __init__(self, letter):
        # la lettera è x o o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.avaible_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + ' è il tuo turno. \nInserisci una mossa (0-8): ')
            try:
                val = int(square)
                if val not in game.avaible_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Valore non valido')

        return val
