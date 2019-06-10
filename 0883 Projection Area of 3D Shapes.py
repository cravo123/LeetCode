# Solution 1, simulation
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        xy = sum(sum(1 if c else 0 for c in row) for row in grid)
        xz = sum(max(row) for row in grid)
        yz = sum(max(col) for col in zip(*grid))
        
        res = xy + xz + yz
        
        return res