class Solution:
    def dfs(self, i, j, grid, m, n):
        res = 0
        grid[i][j] = 2 # visited
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                res += 1
            elif grid[x][y] == 1:
                res += self.dfs(x, y, grid, m, n)
        return res
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += self.dfs(i, j, grid, m, n)
        
        return res