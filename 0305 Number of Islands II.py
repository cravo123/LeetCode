# Solution 1, Union-Find
class Solution:
    def find(self, i, j, m, n, d):
        # Find all idx
        res = set()
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and (x, y) in d:
                res.add(d[x, y])
        
        return res
    
    def find_parent(self, idx, parents):
        if parents[idx] != idx:
            parents[idx] = self.find_parent(parents[idx], parents)
        return parents[idx]
    
    def union(self, curr_parents, parents):
        curr_parents = set(curr_parents)
        x = curr_parents.pop()
        v = self.find_parent(x, parents)
        
        for y in curr_parents:
            parents[y] = v
    
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        cnt = 0
        d = {} # position -> idx
        parents = {}
        res = []
        total = 0
        
        for i, j in positions:
            curr = self.find(i, j, m, n, d)
            curr_parents = set(self.find_parent(x, parents) for x in curr)
            
            length = len(curr_parents)
            
            if length == 0:
                d[i, j] = cnt
                parents[cnt] = cnt
                cnt += 1
                total += 1
            else:
                total -= length - 1
                self.union(curr_parents, parents)
                d[i, j] = self.find_parent(curr_parents.pop(), parents)
            res.append(total)
        return res

# Solution 2, Union-Find elegant solution
# Notice that in Solution 1, Union-Find logic could be extracted as a separate class
class UFS:
    def __init__(self):
        self.d = {} # pos -> idx
        self.parents = {} # idx -> parent
        self.ranks = {}
        self.idx = 0
        self.cnt = 0
        
    def add_point(self, x, y):
        if (x, y) not in self.d:
            self.d[x, y] = self.idx
            self.parents[self.idx] = self.idx
            self.ranks[self.idx] = 1
            self.idx += 1
            self.cnt += 1
            
    def find_parent(self, x, y):
        i = self.d[x, y]
        v_i = i
        while v_i != self.parents[v_i]:
            self.parents[v_i] = self.parents[self.parents[v_i]]
            v_i = self.parents[v_i]
        self.parents[i] = v_i
        
        return v_i
        
    def union(self, i, j, x, y):
        p1 = self.find_parent(i, j)
        p2 = self.find_parent(x, y)
        
        if p1 != p2:
            if self.ranks[p1] < self.ranks[p2]:
                p1, p2 = p2, p1
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
            self.cnt -= 1
    
    def union_neighbor(self, i, j):
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if (x, y) in self.d:
                self.union(i, j, x, y)
    
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UFS()
        
        res = []
        for i, j in positions:
            uf.add_point(i, j)
            uf.union_neighbor(i, j)
            res.append(uf.cnt)
        
        return res