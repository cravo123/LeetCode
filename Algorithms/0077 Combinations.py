# Solution 1, back-tracking
class Solution:
    def dfs(self, idx, n, k, path, res):
        if len(path) == k:
            res.append(path[::])
            return
        
        for i in range(idx, n + 1):
            path.append(i)
            self.dfs(i + 1, n, k, path, res)
            path.pop()
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
        
        self.dfs(1, n, k, path, res)
        
        return res