# Solution 1, DFS
# First mark all islands that are connectec to edges to 1's
# Then count how many islands inside.
class Solution:
    def dfs(self, i, j, grid, m, n):
        grid[i][j] = 1
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                self.dfs(x, y, grid, m, n)
        
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        # Mark all 0's in edges to be 1
        for j in range(n):
            for i in [0, m - 1]:
                if grid[i][j] == 0:
                    self.dfs(i, j, grid, m, n)
        
        for i in range(m):
            for j in [0, n - 1]:
                if grid[i][j] == 0:
                    self.dfs(i, j, grid, m, n)
        
        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(i, j, grid, m, n)
        
        return res
