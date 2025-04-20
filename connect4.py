# requirements:
# constructor to make new environment (default state?)
# .reset() to reset environment to initial state
# .print() to print the board state

SYMBOLS = [' ', 'X', 'O'] # blank, player, bot

class Connect4():
    def __init__(self):
        self.board: list[int][int] = [[0 for j in range(6)] for i in range(7)]
        self.winner: bool = False # True if the bot won else False
    
    def reset(self):
        self.__init__()
    
    def print(self):
        """
          0   1   2   3   4   5   6
        _   _   _   _   _   _   _   _
        |   |   |   |   |   |   |   |
        |   |   |   |   |   |   | O |
        |   |   |   | X |   |   | O |
        |   |   | X | O |   |   | X |
        | X |   | O | x | X |   | X |
        | O | O | X | X | X |   | X |
        o---------------------------o
        """
        print('  0   1   2   3   4   5   6')
        print('_   _   _   _   _   _   _   _')
        print('\n'.join([''.join([f'| {SYMBOLS[self.board[i][j]]} ' for i in range(7)]) + '|' for j in range(6)]))
        print('o---------------------------o')
    
    def check_win(self):
        return True
    
    def step(self, action, player):
        # action: column to drop piece
        # player: True if player else False
        if 0 in self.board[action]:
            self.board[action][self.board[action].index(0)] = 2 if player else 1
        if self.check_win():
            return self.board, 100 if self.winner else -100, True
        else:
            return self.board, 0, False