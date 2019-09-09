# Solution 1, DP
class Solution:
    def maxA(self, N: int) -> int:
        if N <= 2:
            return N
        dp = [i for i in range(N + 1)]
        for i in range(3, N + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        
        return dp[-1]
        