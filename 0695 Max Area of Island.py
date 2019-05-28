# Solution 1, DFS
class Solution:
    def dfs(self, i, j, grid, m, n):
        area = 1
        grid[i][j] = 0
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                area += self.dfs(x, y, grid, m, n)
        return area
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = self.dfs(i, j, grid, m, n)
                    res = max(res, curr)
        
        return res

# Solution 1.1, another DFS implementation
class Solution:
    def dfs(self, i, j, A, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or A[i][j] == 0:
            return 0
        
        curr = 1
        A[i][j] = 0
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            curr += self.dfs(x, y, A, m, n)
        
        return curr
        
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        res = 0
        
        m, n = len(grid), len(grid[0]) if grid else 0
        
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(i, j, grid, m, n))
        
        return res
