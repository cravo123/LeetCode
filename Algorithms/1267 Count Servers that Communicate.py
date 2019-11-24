import collections

# Solution 1, simulation
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = collections.Counter()
        cols = collections.Counter()
        
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
                    rows[i] += 1
                    cols[j] += 1 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and rows[i] == cols[j] == 1:
                    res -= 1
        return res