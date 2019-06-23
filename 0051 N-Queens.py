# Solution 1, back-tracking
class Solution:
    def eligible(self, path, i):
        n = len(path)
        
        for j in range(len(path)):
            if i == path[j] or i - n == path[j] - j or i + n == path[j] + j:
                return False
        return True

    def dfs(self, idx, n, path, res):
        if idx == n:
            if len(path) == n:
                res.append(path[::])
            return
        
        for i in range(n):
            if self.eligible(path, i):
                path.append(i)
                self.dfs(idx + 1, n, path, res)
                path.pop()
    
    def draw(self, cols):
        n = len(cols)
        board = [['.'] * n for _ in range(n)]
        
        for i, j in enumerate(cols):
            board[i][j] = 'Q'
        board = [''.join(row) for row in board]
        return board
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = []
        res = []
        
        self.dfs(0, n, path, res)
        
        res = [self.draw(cols) for cols in res]
        
        return res