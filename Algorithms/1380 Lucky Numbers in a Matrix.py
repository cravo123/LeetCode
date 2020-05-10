# Solution 1, simulation
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(r) for r in matrix]
        col_max = [max(c) for c in zip(*matrix)]
        
        res = []
        
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == row_min[i] == col_max[j]:
                    res.append(matrix[i][j])
        
        return res