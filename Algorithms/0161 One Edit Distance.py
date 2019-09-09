# Solution 1, try all possibilities
class Solution:
    def is_valid(self, i, j, s, t, m, n):
        while i < m and j < n and s[i] == t[j]:
            i += 1
            j += 1
        
        return i == m and j == n
        
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = map(len, (s, t))
        
        if abs(m - n) > 1:
            return False
        
        i = j = 0
        
        while i < m and j < n and s[i] == t[j]:
            i += 1
            j += 1
        
        # insert one char into s
        if (self.is_valid(i, j + 1, s, t, m, n)         # insert
            or self.is_valid(i + 1, j, s, t, m, n)      # delete
            or self.is_valid(i + 1, j + 1, s, t, m, n)  # replace
            ):
            return True
        
        return False

# Solution 2, reuse Edit Distance, but get TLE
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = map(len, (s, t))
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for j in range(1, n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            dp[i][0] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        
        return dp[-1][-1] == 1