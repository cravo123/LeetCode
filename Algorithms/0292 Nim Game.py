# Solution 1, DP, although TLE
class Solution:
    def canWinNim(self, n: int) -> bool:
        # dp[i] means whether player can win by starting with n stones
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        
        for i in range(1, n + 1):
            if any(i - k <= 0 or dp[i - k] is False for k in range(1, 4)):
                dp[i] = True
            else:
                dp[i] = False
        
        return dp[n]

# Solution 2, Mathematics
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0