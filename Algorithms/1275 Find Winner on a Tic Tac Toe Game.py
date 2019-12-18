# Solution 1, simulation
class Solution:
    def check(self, i, j, tag):
        # return 1 if wins, 0 if draw, -1 if pending
        
        self.count += 1
        self.grid[i][j] = tag
        
        if all(self.grid[i][k] == tag for k in range(3)):
            return 1
        
        if all(self.grid[k][j] == tag for k in range(3)):
            return 1
        
        if all(self.grid[k][k] == tag for k in range(3)):
            return 1
        
        if all(self.grid[k][2 - k] == tag for k in range(3)):
            return 1
        
        if self.count == 9:
            return 0
        
        return -1
        
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        self.count = 0
        self.grid = [['' for _ in range(3)] for _ in range(3)]
        
        for idx, (i, j) in enumerate(moves):
            tag = 'X' if idx % 2 == 0 else 'O'
            res = self.check(i, j, tag)
            
            if res == 0:
                return 'Draw'
            if res == 1:
                return 'A' if tag == 'X' else 'B'
        
        return 'Pending'