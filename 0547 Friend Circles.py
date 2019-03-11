# Solution 1, DFS
class Solution:
    def dfs(self, idx, seen, M, n):
        seen.add(idx)
        
        for i in range(n):
            if i not in seen and M[idx][i] == 1:
                self.dfs(i, seen, M, n)
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        
        seen = set()
        res = 0
        
        for i in range(n):
            if i not in seen:
                res += 1
                self.dfs(i, seen, M, n)
        
        return res

# Solution 2, BFS
class Solution:
    def bfs(self, idx, seen, M, n):
        q = [idx]
        seen.add(idx)
        
        while q:
            tmp = []
            for idx in q:
                for i in range(n):
                    if M[idx][i] == 1 and i not in seen:
                        tmp.append(i)
                        seen.add(i)
            q = tmp
        
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        
        res = 0
        seen = set()
        
        for i in range(n):
            if i not in seen:
                res += 1
                self.bfs(i, seen, M, n)
        
        return res