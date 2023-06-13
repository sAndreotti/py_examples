# tic tac toe
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # singola lista per scacchiera
        self.current_winner = None # tiene traccia del vincitore

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2, i numeri delle caselle in cui inserire il simbolo
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def avaible_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot==' ']
        # return []
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #   ['x', 'x', 'o' => [(0, 'x'), (1, 'x'), (2, 'o')]]
        #   if spot == ' ':
        #       moves.append(i)
        #   return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # se la mossa è valida la fa e ritorna true
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # controlla il vincitore

        # controllo le righe
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # controllo le colonne
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # controllo diagonale
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # da sx a dx
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]] # da dx a sx
            if all([spot == letter for spot in diagonal2]):
                return True

        # nessuna vittoria
        return False

def play(game, x_player, o_player, print_game=True):
    # return letter o none
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    # continua fino a quando c'è uno spazio libero
    while game.empty_squares():
        # fa la mossa
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # fai la mossa
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' fa la mossa nella casella {square}')
                game.print_board()
                print('')
            
            if game.current_winner: 
                if print_game:
                    print(letter + ' ha vinto!')
                return letter


            # Forma compressa
            letter = 'O' if letter == 'X' else 'X'
            #if letter == 'X':
            #    letter == 'O'
            #else:
            #    letter == 'X'
        
    if print_game:
        print('Pareggio!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player)