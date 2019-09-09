# Solution 1, DP with O(n) space
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # if dp[left][right] means longest palindromic subsequence in s[left:(right + 1)]
        # dp[left][right] depends on
        #   dp[left + 1][right - 1]
        #   dp[left][right - 1]
        #   dp[left + 1][right]
        # This means we should fill "left" in decreasing order(cuz dp[left] depends on d[left + 1])
        # and fill "right" in increasing order(dp[left][right] depends on dp[left][right - 1])
        
        n = len(s)
        
        dp = [0 for _ in range(n)]
        dp[n - 1] = 1
        
        for i in range(n - 2, -1, -1):
            tmp = [0 for _ in range(n)]
            tmp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    tmp[j] = dp[j - 1] + 2
                else:
                    tmp[j] = max(tmp[j - 1], dp[j])
            dp = tmp
        
        return dp[-1]

# Solution 2, top-down DP(memoization), 
# Implementation is much easier, no need to take care of index
class Solution:
    def dfs(self, i, j, s, d):
        if (i, j) in d:
            return d[i, j]
        if i == j:
            res = 1
        elif i > j:
            res = 0
        elif s[i] == s[j]:
            res = 2 + self.dfs(i + 1, j - 1, s, d)
        else:
            res = max(self.dfs(i, j - 1, s, d), self.dfs(i + 1, j, s, d))
        
        d[i, j] = res
        return res
        
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        d = {}
        
        return self.dfs(0, n - 1, s, d)

# Solution 3.1, DP (TLE)
# The reason why it is TLE is because it is very expensive
# to create a n * n list of list.
class Solution:
   def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
     
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                left, right = i, i + length - 1
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                dp[left][right] = max(dp[left][right], dp[left + 1][right], dp[left][right - 1])
        
        return dp[0][n - 1]

# Solution 3.2, DP
# From transition matrix in Solution 3.1 we know that
# dp[left][right] depends on dp[left + 1] and dp[left]
# so we can actually reverse fill dp
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
     
        for length in range(2, n + 1):
            for i in range(n - length, -1, -1):
                left, right = i, i + length - 1
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])
        
        return dp[0][n - 1]