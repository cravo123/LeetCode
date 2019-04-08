class Solution:
    def count(self, i, j, board, m, n):
        cnt = 0
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                x, y = i + di, j + dj
                
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                    cnt += 1
        
        return cnt
    
    def dfs(self, i, j, board, m, n):
        cnt = self.count(i, j, board, m, n)
        
        if cnt > 0:
            board[i][j] = str(cnt)
            return
        
        board[i][j] = 'B'
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'E':
                    self.dfs(x, y, board, m, n)
        
        
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0]) if board else 0
        
        i, j = click
        
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        self.dfs(i, j, board, m, n)
        
        return board