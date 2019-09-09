import math

# Solution 1, O(M * N) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][1] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]

# Solution 2, O(N) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1 # gotcha, dp[0] = 1 is not correct
        
        for _ in range(m):
            for j in range(1, n + 1):
                dp[j] += dp[j - 1]
        
        return dp[-1]

# Solution 3, mathematical solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // math.factorial(m - 1) // math.factorial(n - 1)