class Solution:
    def dfs(self, i, j, board, m, n):
        board[i][j] = '#'
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                self.dfs(x, y, board, m, n)
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0]) if board else 0
        
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    self.dfs(i, j, board, m, n)
        
        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == 'O':
                    self.dfs(i, j, board, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'