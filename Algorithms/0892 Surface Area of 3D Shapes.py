# Solution 1, simulation
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

# Solution 2, a more efficient implementation 
# Similar to LC 0463, only check right and down
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += 2 + 4 * grid[i][j]
                    
                    # right
                    if j + 1 < n:
                        res -= 2 * min(grid[i][j], grid[i][j + 1])
                    
                    # down
                    if i + 1 < m:
                        res -= 2 * min(grid[i][j], grid[i + 1][j])
            
        return res