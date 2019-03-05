class Solution:
    def dfs(self, idx, k, n, path, res):
        if idx > 9 or k <= 0 or n <= 0:
            if k == 0 and n == 0:
                res.append(path[::])
            return
        k -= 1
        for i in range(idx, 10):
            path.append(i)
            self.dfs(i + 1, k, n - i, path, res)
            path.pop()
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        
        self.dfs(1, k, n, path, res)
        
        return res