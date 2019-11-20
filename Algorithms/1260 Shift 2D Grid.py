# Solution 1, simulation using mod
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        k = k % (m * n)
        
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                idx = (i * n + j + k) % (m * n)
                x, y = idx // n, idx % n
                res[x][y] = v
        
        return res