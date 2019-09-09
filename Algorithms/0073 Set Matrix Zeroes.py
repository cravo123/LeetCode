# Solution 1, use extra O(m + n) memory to store zero-existence info
# for each row and col
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        row = [False for _ in range(m)]
        col = [False for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# Solution 2, actually we could use first row and first col to store info
# memory usage will be O(1), although code is more complicated.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        # Use first row to store zero-info for each col
        # Use first col to store zero-info for each row
        # matrix[0][0] will store col info
        
        is_first_row = any(x == 0 for x in matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] * matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(1, m):
                matrix[i][0] = 0
        
        if is_first_row:
            for j in range(n):
                matrix[0][j] = 0