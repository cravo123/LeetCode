# Solution 1, simulation
# The reason we use a separate function is we can early
# terminate two for loops
class Solution:
    def find_rook(self, board, m, n):
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    return i, j   
                
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0]) if board else 0
        i, j = self.find_rook(board, m, n)
        
        res = 0
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            while 0 <= x < m and 0 <= y < n:
                if board[x][y] == 'p':
                    res += 1
                if board[x][y] != '.':
                    break
                x += di
                y += dj
        
        return res