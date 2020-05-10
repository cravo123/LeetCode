import collections

# Solution 1, DFS
class Solution:
    def dfs(self, idx, d, informTime):
        if idx not in d:
            return 0
        
        return informTime[idx] + max(self.dfs(i, d, informTime) for i in d[idx])
        
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = collections.defaultdict(list) # manager -> subordinates
        
        for i, j in enumerate(manager):
            d[j].append(i)
        
        return self.dfs(headID, d, informTime)

# Solution 2, BFS
class Solution:
    def bfs(self, idx, d, informTime):
        res = 0
        
        q = [[idx, 0]] # index, and time spent to arrive at idx
        
        while q:
            tmp = []
            
            for i, t in q:
                t += informTime[i]
                res = max(res, t)
                
                for j in d[i]:
                    tmp.append([j, t])
            q = tmp
        
        return res
            
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = collections.defaultdict(list) # manager -> subordinates
        
        for i, j in enumerate(manager):
            d[j].append(i)
        
        return self.bfs(headID, d, informTime)