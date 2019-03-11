class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(max(n + 1, 2))]
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]