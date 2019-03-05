import collections

# Solution 1, DFS
class Solution:
    def dfs(self, idx, seen, d):
        if idx in seen:
            return
        seen.add(idx)
        for i in d[idx]:
            self.dfs(i, seen, d)
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = collections.defaultdict(set)
        
        for a, b in edges:
            d[a].add(b)
            d[b].add(a)
        
        res = 0
        seen = set()
        
        for i in range(n):
            if i not in seen:
                res += 1
                self.dfs(i, seen, d)
        return res

# Solution 2, BFS
class Solution:
    def bfs(self, idx, seen, d):
        q = set([idx])
        seen.add(idx)
        while q:
            tmp = set()
            for p in q:
                for x in d[p]:
                    if x not in seen:
                        tmp.add(x)
                        seen.add(x)
            q = tmp
        
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = collections.defaultdict(set)
        
        for a, b in edges:
            d[a].add(b)
            d[b].add(a)
        
        seen = set()
        res = 0
        
        for i in range(n):
            if i not in seen:
                res += 1
                self.bfs(i, seen, d)
        
        return res

# Solution 3, Union Find
class Solution:
    def parent(self, idx, d):
        if idx != d[idx]:
            d[idx] = self.parent(d[idx], d)
        return d[idx]
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {i:i for i in range(n)}
        
        for a, b in edges:
            pa, pb = self.parent(a, d), self.parent(b, d)
            d[pa] = pb
        
        res = set()
        for i in range(n):
            res.add(self.parent(i, d))
        
        return len(res)