import collections

# Solution 1, DFS
class Solution:
    def dfs(self, x, y, rows, cols, seen):
        seen.add((x, y))
        
        for j in rows[x]:
            if (x, j) not in seen:
                self.dfs(x, j, rows, cols, seen)
        
        for i in cols[y]:
            if (i, y) not in seen:
                self.dfs(i, y, rows, cols, seen)
        
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        
        for x, y in stones:
            rows[x].append(y)
            cols[y].append(x)
        
        seen = set()
        cnt = 0
        
        for x, y in stones:
            if (x, y) not in seen:
                cnt += 1
                self.dfs(x, y, rows, cols, seen)
        
        return n - cnt

# Solution 2, Union-Find
class UFS:
    def __init__(self):
        self.d = {} # pos -> idx
        self.parents = {} # idx -> parent
        self.count = 0
        self.rank = {}
    
    def add(self, x, y):
        self.d[x, y] = self.count
        self.parents[self.count] = self.count
        self.rank[self.count] = 1
        self.count += 1
    
    def find_parent(self, x, y):
        idx = self.d[x, y]
        v_idx = idx
        while v_idx != self.parents[v_idx]:
            v_idx = self.parents[v_idx]
            # path splitting
            #self.parents[v_idx], v_idx = self.parents[self.parents[v_idx]], self.parents[v_idx]
        self.parents[idx] = v_idx
        
        return v_idx
    
    def union(self, x1, y1, x2, y2):
        p1 = self.find_parent(x1, y1)
        p2 = self.find_parent(x2, y2)
        
        if p1 != p2:
            if self.rank[p1] < self.rank[p2]:
                p1, p2 = p2, p1
            self.rank[p1] += self.rank[p2]
            self.parents[p2] = p1
            self.count -= 1
        
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        ufs = UFS()
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        
        for i, j in stones:
            ufs.add(i, j)
            rows[i].add(j)
            cols[j].add(i)
        
        
        for i in rows:
            j = rows[i].pop()
            for k in rows[i]:
                ufs.union(i, j, i, k)
        
        for j in cols:
            i = cols[j].pop()
            for k in cols[j]:
                ufs.union(i, j, k, j)
        
        return len(stones) - ufs.count