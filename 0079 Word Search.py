class Solution:
    def dfs(self, idx, word, i, j, board, m, n):
        if idx == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or word[idx] != board[i][j]:
            return False
        c = board[i][j]
        board[i][j] = '#'
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            
            if self.dfs(idx + 1, word, x, y, board, m, n):
                board[i][j] = c
                return True
        board[i][j] = c
        return False
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0]) if board else 0
        
        for i in range(m):
            for j in range(n):
                if self.dfs(0, word, i, j, board, m, n):
                    return True
        return False