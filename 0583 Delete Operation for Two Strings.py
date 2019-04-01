class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = map(len, (word1, word2))
        
        # number of steps to match till i-th char of word1 and j-th char of word2
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for j in range(1, n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            dp[i][0] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
        
        return dp[-1][-1]