import collections

class Solution:
    def check(self, cans):
        d = collections.Counter(cans)
        
        for c, v in d.items():
            if c != '.' and v > 1:
                return False
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if any(not self.check(row) for row in board):
            return False
        
        if any(not self.check(col) for col in zip(*board)):
            return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp = []
                for di in range(3):
                    for dj in range(3):
                        tmp.append(board[i + di][j + dj])
                        if not self.check(tmp):
                            return False
        return True