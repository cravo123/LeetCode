# Solution 1, DFS
class Solution:
    def dfs(self, n, path, res):
        upper = int(n ** 0.5) + 1
        
        for i in range(2, upper):
            # Avoid duplicates
            if path and i < path[-1]:
                continue
            if n % i == 0:
                res.append(path + [i, n // i])
                path.append(i)
                self.dfs(n // i, path, res)
                path.pop()
        
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        path = []
        
        self.dfs(n, path, res)
        
        return res

# Solution 1.1, optimized DFS
class Solution:
    def dfs(self, n, path, res, start):
        upper = int(n ** 0.5) + 1
        
        for i in range(start, upper):
            if n % i == 0:
                res.append(path + [i, n // i])
                path.append(i)
                self.dfs(n // i, path, res, i)
                path.pop()
        
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        path = []
        
        self.dfs(n, path, res, 2)
        
        return res

# Solution 1.2, another DFS
class Solution:
    def dfs(self, n, path, res, start):
        if n <= 1:
            if len(path) > 1:
                res.append(path[::])
            return 
        
        for i in range(start, n + 1):
            if n % i == 0:
                path.append(i)
                self.dfs(n // i, path, res, i)
                path.pop()
        
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        path = []
        
        self.dfs(n, path, res, 2)
        
        return res