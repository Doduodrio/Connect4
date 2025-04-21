import numpy as np

SYMBOLS = [' ', 'O', 'X'] # blank, bot, player

def generate_wins():
    wins = []
    # horizontal
    for i in range(4):
        for j in range(6):
            wins.append(((i, j), (i+1, j), (i+2, j), (i+3, j)))
    # vertical
    for i in range(7):
        for j in range(3):
            wins.append(((i, j), (i, j+1), (i, j+2), (i, j+3)))
    # diagonal \
    for i in range(4):
        for j in range(3):
            wins.append(((i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3)))
    # diagonal /
    for i in range(4):
        for j in (5, 4, 3):
            wins.append(((i, j), (i+1, j-1), (i+2, j-2), (i+3, j-3)))
    return wins

class Connect4():
    def __init__(self):
        self.board = np.array([[0 for j in range(6)] for i in range(7)])
        self.winner = False # True if the bot won else False
        self.win_states = generate_wins()
    
    def reset(self):
        self.__init__()
        return self.board
    
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
        for w in self.win_states:
            if self.board[w[0][0]][w[0][1]]!=0:
                try:
                    for i in (1, 2, 3):
                        assert self.board[w[0][0]][w[0][1]]!=self.board[w[i][0]][w[i][1]]
                    self.winner = self.board[w[0][0]][w[0][1]]==1
                    return True
                except AssertionError:
                    pass
        self.winner = False
        return False

    
    def step(self, action, bot):
        # action: column to drop piece
        # bot: place bot piece if True, player piece if False
        if 0 in self.board[action]:
            for row in range(5, -1, -1):
                if self.board[action][row]==0:
                    self.board[action][row] = 1 if bot else 2
                    break
        if self.check_win():
            return np.array([b for a in self.board for b in a]), (100 if self.winner else -100), True
        else:
            return np.array([b for a in self.board for b in a]), -1, False
    
    def reverse_board(self):
        # return board state from perspective of player
        return np.array([[(2 if self.board[i][j]==1 else 1 if self.board[i][j]==2 else 0) for j in range(6)] for i in range(7)])