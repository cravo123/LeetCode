# Solution 1, DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = map(len, (word1, word2))
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # dp[i][j] means we match the first i and j characters
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + 1
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i - 1][j - 1]: replace
                    # dp[i - 1][j]: delete a char from word1, because we are matching
                    #               word1[:i - 1] and word2[:j]
                    # dp[i][j - 1]: Insert a char
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]