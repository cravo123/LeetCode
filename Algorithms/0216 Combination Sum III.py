# Solution 1, BFS, back-tracking
class Solution:
    def dfs(self, idx, path, res, k, n):
        if len(path) > k or sum(path) > n:
            return
        if len(path) == k and sum(path) == n:
            res.append(path[::])
            return
        
        if idx > 9:
            return
        for i in range(idx, 10):
            path.append(i)
            self.dfs(i + 1, path, res, k, n)
            path.pop()
        
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        
        self.dfs(1, path, res, k, n)
        
        return res