class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        i, j = 0, m * n - 1
        
        while i <= j:
            mid = (i + j) // 2
            r, c = mid // n, mid % n
            
            v = matrix[r][c]
            if v > target:
                j = mid - 1
            elif v < target:
                i = mid + 1
            else:
                return True
        return False