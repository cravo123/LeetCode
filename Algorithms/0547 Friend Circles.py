import collections

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

# Solution 1.1, DFS, building graph first
class Solution:
    def dfs(self, idx, seen, d):
        seen.add(idx)
        
        for j in d[idx]:
            if j not in seen:
                self.dfs(j, seen, d)
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        d = collections.defaultdict(set)
        
        for i in range(n):
            for j in range(i):
                if M[i][j] == 1:
                    d[i].add(j)
                    d[j].add(i)
        
        seen = set()
        cnt = 0
        
        for i in range(n):
            if i not in seen:
                self.dfs(i, seen, d)
                cnt += 1
        
        return cnt

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

# Solution 3, Union Find
# For Union-Find and Trie problem, it is always better to decouple the logic
# and implement Union Find and Trie as separate classes. You will find it it
# much easier and less error-prone to implement!
class UFS:
    def __init__(self):
        self.size = 0
        self.idx = 0
        self.d = {} # data -> idx
        self.parent = {} # idx -> its parent
    
    def add_point(self, v):
        if v not in self.d:
            self.d[v] = self.idx
            self.parent[self.idx] = self.idx
            self.idx += 1
            self.size += 1
    
    def dfs(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.dfs(self.parent[i])
        return self.parent[i]
    
    def find_parent(self, v):
        i = self.d[v]
        p_i = self.dfs(i)
        
        return p_i
    
    def union(self, u, v):
        p_u, p_v = self.find_parent(u), self.find_parent(v)
        
        if p_u != p_v:
            self.parent[p_u] = p_v
            self.size -= 1
    
    def get_size(self):
        return self.size

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ufs = UFS()
        
        n = len(M)
        
        for i in range(n):
            ufs.add_point(i)
        
        for i in range(n):
            for j in range(i):
                if M[i][j] == 1:
                    ufs.union(i, j)
        
        return ufs.get_size()