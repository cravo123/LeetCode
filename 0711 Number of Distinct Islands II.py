# Solution 1, DFS
# if we can do rotation (90, 180, or 270 degrees only)
# or reflection (left/right direction or up/down direction),
# then (x, y) can be (x, y), (-x, y), (x, -y), (-x, -y), 
# (y, x), (-y, x), (-y, -x), (y, -x)
class Solution:
    def dfs(self, i, j, grid, m, n, path):
        grid[i][j] = 0
        path.append([i, j])
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                self.dfs(x, y, grid, m, n, path)
    
    def normalize(self, path):
        q = [[] for _ in range(8)]
        
        for x, y in path:
            q[0].append([x, y])
            q[1].append([-x, y])
            q[2].append([x, -y])
            q[3].append([-x, -y])
            q[4].append([y, x])
            q[5].append([-y, x])
            q[6].append([-y, -x])
            q[7].append([y, -x])
        
        for i in range(8):
            q[i].sort()
            q[i] = [(q[i][j][0] - q[i][0][0], q[i][j][1] - q[i][0][1]) for j in range(len(q[i]))]
        
        # gotcha, need to sort q also
        q.sort()
        return q
        
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(i, j, grid, m, n, path)
                    paths = self.normalize(path)
                    
                    res.add(tuple(paths[0]))
        
        return len(res)

# Solution 1.1, similar idea, different implementation
class Solution:
    def dfs(self, path, i, j, grid, m, n):
        path.append((i, j))
        grid[i][j] = 0
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                self.dfs(path, x, y, grid, m, n)
    
    def normalize(self, path):
        res = set()
        
        for _ in range(2):
            path = [[y, x] for x, y in path]
            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    t = [(x * dx, y * dy) for x, y in path]
                    t.sort()
                    t = [(x - t[0][0], y - t[0][1]) for x, y in t]
                    res.add(tuple(t))
        
        return res
        
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        curr = set()
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(path, i, j, grid, m, n)
                    qs = self.normalize(path)
                    if all(q not in curr for q in qs):
                        res += 1
                    curr |= qs
        return res