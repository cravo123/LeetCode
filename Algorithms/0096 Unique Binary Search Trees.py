class Solution:
    def numTrees(self, n: 'int') -> 'int':
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        
        for i in range(1, n + 1):
            for L in range(0, i):
                R = i - 1 - L
                dp[i] += dp[L] * dp[R]
        
        return dp[-1]