class Solution:
    def eligible(self, path, i):
        n = len(path)
        
        for j in range(n):
            if i == path[j] or i - n == path[j] - j or i + n == path[j] + j:
                return False
        return True
        
    def dfs(self, idx, n, path):
        if idx == n:
            return 1 if len(path) == n else 0
        res = 0
        for i in range(n):
            if self.eligible(path, i):
                path.append(i)
                res += self.dfs(idx + 1, n, path)
                path.pop()
        return res
    
    def totalNQueens(self, n: int) -> int:
        path = []
        
        res = self.dfs(0, n, path)
        
        return res