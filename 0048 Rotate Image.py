class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(n):
            low, high = 0, n - 1
            while low < high:
                matrix[low][j], matrix[high][j] = matrix[high][j], matrix[low][j]
                low += 1
                high -= 1
        
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]