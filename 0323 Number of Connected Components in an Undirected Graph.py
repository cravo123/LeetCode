import collections

# Solution 1, DFS
class Solution:
    def dfs(self, u, d, seen):
        seen.add(u)
        
        for v in d[u]:
            if v not in seen:
                self.dfs(v, d, seen)
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = collections.defaultdict(set)
        
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)
        
        cnt = 0
        seen = set()
        for u in range(n):
            if u not in seen:
                cnt += 1
                self.dfs(u, d, seen)
        
        return cnt

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
# We can abstract Union Find logic out as a separate class
# This will make our implementation easier.
class UFS:
    def __init__(self):
        self.idx = 0
        self.d = {} # data -> idx
        self.parent = {} # idx -> ulti-parent
        self.size = 0
        
    def add_point(self, p):
        if p not in self.d:
            self.d[p] = self.idx
            self.parent[self.idx] = self.idx
            self.idx += 1
            self.size += 1
    
    def find_parent(self, p):
        i = self.d[p]
        j = i
        while j != self.parent[j]:
            j = self.parent[j] # can be optimized by path-halving or path-compression

            # path compression
            #self.parent[j] = self.parent[self.parent[j]]
            #j = self.parent[j]

        self.parent[i] = j
        
        return j
    
    def union(self, p, q):
        i, j = self.find_parent(p), self.find_parent(q)
        if i != j:
            self.parent[i] = j # can be optimized by using ranking, i.e. make tree as short as possible
            self.size -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ufs = UFS()
        
        for i in range(n):
            ufs.add_point(i)
        
        for u, v in edges:
            ufs.union(u, v)
        
        return ufs.size


# Solution 3.1 Union Find
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