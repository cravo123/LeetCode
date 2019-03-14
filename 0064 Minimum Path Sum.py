# Solution 1, Space O(m * n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]

# Solution 2, O(n) space
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        dp = [float('inf') for _ in range(n + 1)]
        dp[1] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[j] = grid[i - 1][j - 1] + min(dp[j], dp[j - 1])
        
        return dp[-1]