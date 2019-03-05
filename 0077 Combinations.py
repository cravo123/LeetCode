class Solution:
    def dfs(self, idx, n, k, path, res):
        if k == 0:
            res.append(path[::])
            return
        
        for i in range(idx, n + 1):
            path.append(i)
            self.dfs(i + 1, n, k - 1, path, res)
            path.pop()
        
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        
        self.dfs(1, n, k, path, res)
        
        return res