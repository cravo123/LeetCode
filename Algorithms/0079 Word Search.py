# Solution 1, back-tracking
class Solution:
    def dfs(self, idx, word, i, j, board, m, n):
        if board[i][j] != word[idx]:
            return False
        idx += 1
        if idx == len(word):
            return True
        
        c = board[i][j]
        board[i][j] = '#'
        
        res = False
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and self.dfs(idx, word, x, y, board, m, n):
                res = True
                break
        
        board[i][j] = c
        
        return res
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0]) if board else 0
        
        for i in range(m):
            for j in range(n):
                if self.dfs(0, word, i, j, board, m, n):
                    return True
        
        return False