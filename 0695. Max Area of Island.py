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