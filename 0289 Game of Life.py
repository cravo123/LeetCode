class Solution:
    def check_status(self, i, j, board, m, n):
        cnt = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and board[x][y] % 2 == 1:
                    cnt += 1
        
        curr = board[i][j]
        if curr == 1:
            if cnt not in (2, 3):
                board[i][j] = 3
        else:
            if cnt == 3:
                board[i][j] = 2
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0]) if board else 0
        
        for i in range(m):
            for j in range(n):
                self.check_status(i, j, board, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1