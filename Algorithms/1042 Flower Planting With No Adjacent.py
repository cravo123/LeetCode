import collections

# Soltuion 1, greedy
# Because each garden has at most 3 neighbor gardens but we have 
# 4 colors available. 
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        
        for i, j in paths:
            d[i - 1].add(j - 1)
            d[j - 1].add(i - 1)
        
        res = [0 for _ in range(N)]
        
        for i in range(N):
            v = (set([1, 2, 3, 4]) - {res[j] for j in d[i]}).pop()
            res[i] = v
        
        return res

# Solution 2, vanilla dfs
class Solution:
    def dfs(self, idx, d, res):
        if res[idx] != 0:
            return
        
        neighbors = set(res[i] for i in d[idx])
        for v in range(1, 5):
            if v not in neighbors:
                res[idx] = v
        
        for i in d[idx]:
            self.dfs(i, d, res)
        
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        
        for x, y in paths:
            d[x - 1].add(y - 1)
            d[y - 1].add(x - 1)
        
        res = [0 for _ in range(N)]
        
        for i in range(N):
            self.dfs(i, d, res)
        
        return res