# Solution 1, back-tracking
class Solution:
    def is_eligible(self, i, path):
        curr_row = len(path)
        for r, c in enumerate(path):
            # same col or diagonal or anti-diagonal
            if c == i or curr_row - r == i - c or curr_row + i == r + c:
                return False
        return True
        
    def dfs(self, path, n):
        if len(path) == n:
            return 1
        
        res = 0
        for i in range(n):
            if self.is_eligible(i, path):
                path.append(i)
                res += self.dfs(path, n)
                path.pop()
        return res
        
    def totalNQueens(self, n: int) -> int:
        path = []
        
        res = self.dfs(path, n)
        
        return res