class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        rows = [max(row) for row in grid]
        cols = [max(col) for col in zip(*grid)]
        
        res = 0
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                res += min(rows[i], cols[j]) - val
        
        return res