class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        rows = [max(row) for row in grid]
        cols = [max(col) for col in zip(*grid)]
        
        area = 0
        for row in grid:
            for v in row:
                area += 1 if v > 0 else 0
        
        area += sum(rows) + sum(cols)
        
        return area