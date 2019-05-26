# Solution 1, 2D prefix sum
# prefix-sum of rectangle
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            curr_row_sum = 0
            for j in range(1, n + 1):
                curr_row_sum += matrix[i - 1][j - 1]
                dp[i][j] = curr_row_sum + dp[i - 1][j]
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
        
        return res

# Solution 2, other caching method
# caching each row. t.b.c



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)