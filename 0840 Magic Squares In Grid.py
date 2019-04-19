import collections

# Solution 1, brute-force
class Solution:
    def check(self, i, j, grid):
        d = collections.Counter()
        
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                c = grid[x][y]
                d[c] += 1
                if d[c] > 1 or not 1 <= c <= 9:
                    return False
        
        g = [row[j:(j + 3)] for row in grid[i:(i + 3)]]
        
        if any(sum(row) != 15 for row in g) or any(sum(col) != 15 for col in zip(*g)):
            return False
        
        if sum(g[x][x] for x in range(3)) != 15:
            return False
        if sum(g[x][2 - x] for x in range(3)) != 15:
            return False
        
        return True
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if self.check(i, j, grid):
                    res += 1
        return res

# Solution 2, precache solution
# If we have a very large grid to check, then we can precache correct magic square
# Use back-tracking to calculate correct magic matrix first
class Solution:
    def eligible(self, path):
        n = len(path)
        
        for i in range(0, n, 3):
            if i + 3 <= n and sum(path[i:(i + 3)]) != 15:
                return False
        
        for i in range(3):
            if i + 6 <= n - 1:
                if path[i] + path[i + 3] + path[i + 6] != 15:
                    return False
        if n >= 7 and path[2] + path[4] + path[6] != 15:
            return False
        
        if n == 9 and path[0] + path[4] + path[8] != 15:
            return False
        
        return True
        
    def dfs(self, q, path, res, seen):
        if len(path) == len(q):
            t = [path[i:(i + 3)] for i in range(0, 9, 3)]
            res.append(t)
            return
        
        for i, c in enumerate(q):
            if seen[i] == False:
                seen[i] = True
                path.append(c)
                
                if self.eligible(path):
                    self.dfs(q, path, res, seen)
                path.pop()
                seen[i] = False
    
    def generate_magic_matrix(self):
        path = []
        res = []
        q = list(range(1, 10))
        seen = [False for _ in q]
        
        self.dfs(q, path, res, seen)
        
        return res
    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        q = self.generate_magic_matrix()
        m, n = len(grid), len(grid[0]) if grid else 0
        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                t = [row[j:(j + 3)] for row in grid[i:(i + 3)]]
                
                if any(t == x for x in q):
                    res += 1
        return res