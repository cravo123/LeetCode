# Solution 1, cache row_max and col_max
# Note zip(*matrix) is a shortcut for transposing matrix

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        rows = [max(row) for row in grid]
        cols = [max(col) for col in zip(*grid)]
        
        res = 0
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                res += min(rows[i], cols[j]) - val
        
        return res