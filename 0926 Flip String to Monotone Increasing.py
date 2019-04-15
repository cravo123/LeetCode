# Solution 1, O(n) DP
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        
        dp = [[0, 0] for _ in range(n + 1)]
        
        # dp[i][0] ends with zero
        # dp[i][1] ends with one
        
        for i in range(1, n + 1):
            c = S[i - 1]
            
            if c == '0':
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = min(dp[i - 1]) + 1
            else:
                dp[i][1] = min(dp[i - 1])
                dp[i][0] = dp[i - 1][0] + 1
        
        return min(dp[-1])

# Solution 2, O(1) DP
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        
        zero = one = 0
        
        # zero: ends with zero
        # one: ends with one
        
        for i in range(n):
            c = S[i]
            
            if c == '0':
                zero, one = zero, min(zero, one) + 1
            else:
                zero, one = zero + 1, min(zero, one)
        
        return min(zero, one)