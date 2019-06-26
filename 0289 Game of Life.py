# Solution 1, simulation
class Solution:
    def calc_state(self, i, j, board, m, n):
        live = dead = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == dj == 0:
                    continue
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n:
                    if board[x][y] % 2 == 1:
                        live += 1
                    else:
                        dead += 1
        
        if board[i][j] == 1:
            if live < 2 or live > 3:
                res = 3
            else:
                res = 1
        else:
            if live == 3:
                res = 2
            else:
                res = 0
        
        return res
        
                    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0]) if board else 0
        
        for i in range(m):
            for j in range(n):
                board[i][j] = self.calc_state(i, j, board, m, n)
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1