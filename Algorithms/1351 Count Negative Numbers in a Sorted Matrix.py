# Solution 1, simulation, O(m + n) similar to L 0240 Search a 2D Matrix II
# Can start from top-right or bottom-left corner.
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        i, j = 0, n - 1
        
        res = 0
        
        while i < m and j >= 0:
            if grid[i][j] < 0:
                res += (m - i)
                j -= 1
            else:
                i += 1
        
        return res