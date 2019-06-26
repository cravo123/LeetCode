# Solution 1, simulation
# Similar to LC 0006 ZigZag Conversion,
# in a sense that save each diagonal values in a separate list
# and merge at the end.
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        t = [[] for _ in range(m + n - 1)]
        
        for i in range(m):
            for j in range(n):
                t[i + j].append(matrix[i][j])
        
        for i in range(0, m + n - 1, 2):
            t[i] = t[i][::-1]
        
        res = []
        for row in t:
            res.extend(row)
        
        return res