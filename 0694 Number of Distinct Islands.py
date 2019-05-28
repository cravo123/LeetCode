# Solution 1, DFS
# First gather indices for each island and standardize indices
class Solution:
    def dfs(self, i, j, A, m, n, path):
        path.append([i, j])
        A[i][j] = 0
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                self.dfs(x, y, A, m, n, path)
    
    def transform(self, path):
        # Normalize island coordinates
        path.sort()
        res = tuple([(x - path[0][0], y - path[0][1]) for x, y in path])
        
        return res
        
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = set()
        
        # Search island
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(i, j, grid, m, n, path)
                    path = self.transform(path)
                    res.add(path)
        
        return len(res)
                    