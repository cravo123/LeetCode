class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    res += 2 # top and bottom  
                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n:
                            neighbor = grid[x][y]
                        else:
                            neighbor = 0
                        res += max(0, grid[i][j] - neighbor) 
        return res