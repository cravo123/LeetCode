# Solution 1, DP
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        res = 0
        for length in range(1, n + 1):
            for left in range(0, n - length + 1):
                i, j = left, left + length - 1
                if length == 1:
                    dp[i][j] = 1
                    res += 1
                elif length == 2:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        res += 1
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                        res += 1
        return res

# Solution 1.1, DP, elegant implementation
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        res = 0
        for length in range(1, n + 1):
            for left in range(0, n - length + 1):
                i, j = left, left + length - 1
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                res += dp[i][j]
        return res