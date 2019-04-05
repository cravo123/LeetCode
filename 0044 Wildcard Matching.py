# This problem is easier comapring to LC 0010 Regular Expression Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = map(len, (s, p))
        
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        
        for j in range(1, n + 1):
            if p[j - 1] == '*' and dp[0][j - 1]:
                dp[0][j] = True
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] not in '?*':
                    dp[i][j] = False if s[i - 1] != p[j - 1] else dp[i - 1][j - 1]
                elif p[j - 1] == '?':
                    # Match a single char
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # since '*' can match empty string,
                    # so dp[i][j - 1] means matching empty string
                    # dp[i - 1][j] means matching one but j stays the same
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[-1][-1]