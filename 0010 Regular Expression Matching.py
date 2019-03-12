class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = map(len, (s, p))
        
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        
        dp[0][0] = True
        
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                if j > 1:
                    dp[0][j] = dp[0][j] or dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if j > 1:
                        dp[i][j] = dp[i][j] or dp[i][j - 2] # match 0 pre
                        if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                            dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        
        return dp[-1][-1]