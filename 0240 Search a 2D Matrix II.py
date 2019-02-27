class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        i, j = 0, n - 1
        
        while i < m and j >= 0:
            v = matrix[i][j]
            
            if v < target:
                i += 1
            elif v > target:
                j -= 1
            else:
                return True
        return False