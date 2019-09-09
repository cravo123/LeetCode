# Solution 1, simulation
# By rotate board clock-wise, we can simulate "crushing" by move zeros to the end for each row
class Solution:
    def candyCrush(self, board: 'List[List[int]]') -> 'List[List[int]]':
        board = [list(x) for x in zip(*reversed(board))]
        
        m, n = len(board), len(board[0]) if board else 0
        
        while True:
            cancel = set()
            
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0:
                        continue
                    if i < m - 2 and board[i][j] == board[i + 1][j] == board[i + 2][j]:
                        cancel |= set([(i, j), (i + 1, j), (i + 2, j)])
                    if j < n - 2 and board[i][j] == board[i][j + 1] == board[i][j + 2]:
                        cancel |= set([(i, j), (i, j + 1), (i, j + 2)])
            
            if not cancel:
                break
            
            for i, j in cancel:
                board[i][j] = 0
            
            for i in range(m):
                tmp = [c for c in board[i] if c]
                board[i] = tmp + [0] * (n - len(tmp))
        
        board = [list(x) for x in zip(*board)]
        board = list(reversed(board))
        return board

# Solution 1.1, same idea but without rotating board
class Solution:
    def move(self, board, m, n):
        for j in range(n):
            idx = i = m - 1
            while i >= 0:
                if board[i][j] != 0:
                    board[idx][j] = board[i][j]
                    idx -= 1
                i -= 1
            while idx >= 0:
                board[idx][j] = 0
                idx -= 1
                
    def candyCrush(self, board: 'List[List[int]]') -> 'List[List[int]]':
        m, n = len(board), len(board[0]) if board else 0
        
        while True:
            cancel = set()
            
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0: # gotcha
                        continue
                    if i < m - 2 and board[i][j] == board[i + 1][j] == board[i + 2][j]:
                        cancel |= set([(i, j), (i + 1, j), (i + 2, j)])
                    if j < n - 2 and board[i][j] == board[i][j + 1] == board[i][j + 2]:
                        cancel |= set([(i, j), (i, j + 1), (i, j + 2)])
            
            if not cancel:
                break
            
            for i, j in cancel:
                board[i][j] = 0
            
            self.move(board, m, n)
            
        return board