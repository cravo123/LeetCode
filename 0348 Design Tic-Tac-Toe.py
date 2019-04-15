import collections

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row = collections.Counter()
        self.col = collections.Counter()
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        v = 1 if player == 1 else -1
        
        self.row[row] += v
        self.col[col] += v
        
        if row == col:
            self.diag += v
        
        if row + col == self.n - 1:
            self.anti_diag += v
        
        if abs(self.row[row]) == self.n:
            return 1 if self.row[row] == self.n else 2
        
        if abs(self.col[col]) == self.n:
            return 1 if self.col[col] == self.n else 2
        
        if abs(self.diag) == self.n:
            return 1 if self.diag == self.n else 2
        
        if abs(self.anti_diag) == self.n:
            return 1 if self.anti_diag == self.n else 2
        
        return 0
        
# Solution 2, slightly more elegant
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row = collections.Counter()
        self.col = collections.Counter()
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        v = 1 if player == 1 else -1
        
        self.row[row] += v
        self.col[col] += v
        
        if row == col:
            self.diag += v
        
        if row + col == self.n - 1:
            self.anti_diag += v
        
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        
        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)