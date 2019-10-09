# Solution 1, DFS, backtracking
class Solution:
    def dfs(self, i, j, grid, m, n):
        if not (0 <= i < m and 0 <= j < n and grid[i][j] != 0):
            return 0
        
        v = grid[i][j]
        grid[i][j] = 0 # mark visited
        res = 0
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            res = max(res, self.dfs(x, y, grid, m, n))
        
        res += v
        grid[i][j] = v
        
        return res
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        return max(self.dfs(i, j, grid, m, n) for i in range(m) for j in range(n))

# Solution 2, memoization, TLE
# need to cache both grid and current position(i, j)

class Solution:
    def dfs(self, i, j, grid, m, n, d):
        key = tuple([tuple(row) for row in grid] + [i, j])
        if key in d:
            return d[key]
        
        if not (0 <= i < m and 0 <= j < n and grid[i][j] != 0):
            return 0
        
        v = grid[i][j]
        grid[i][j] = 0 # mark visited
        res = 0
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            res = max(res, self.dfs(x, y, grid, m, n, d))
        
        res += v
        grid[i][j] = v
        
        d[key] = res
        
        return res
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        d = {}
        
        return max(self.dfs(i, j, grid, m, n, d) for i in range(m) for j in range(n))