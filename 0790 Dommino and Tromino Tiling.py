# Solution 1, DP
# dp[5]:
# XXXXX
# XXXXX
# tr[5]:
# XXXXX
# XXXXO
# or
# XXXXO
# XXXXX

class Solution:
    def numTilings(self, N: int) -> int:
        n = max(N, 2)
        dp = [0 for _ in range(n + 1)]
        tr = dp[::]
        dp[0] = 1
        tr[0] = 0
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 2 * tr[i - 1]
            if i > 1:
                dp[i] += dp[i - 2]
                tr[i] = dp[i - 2] + tr[i - 1]
        
        return dp[N] % (int(1e9 + 7))