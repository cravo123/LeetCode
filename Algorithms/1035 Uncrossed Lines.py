# Solution 1, Top-Down DP, memoization
class Solution:
    def dfs(self, i, j, A, B, d):
        # number of lines for the first i-th and j-th chars in A and B
        if (i, j) in d:
            return d[i, j]
        if i <= 0 or j <= 0:
            return 0
        
        if A[i - 1] == B[j - 1]:
            res = self.dfs(i - 1, j - 1, A, B, d) + 1
        else:
            res = max(self.dfs(i, j - 1, A, B, d), self.dfs(i - 1, j, A, B, d))
        d[i, j] = res
        
        return res
        
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = map(len, (A, B))
        
        d = {}
        
        res = self.dfs(m, n, A, B, d)
        
        return res

# Solution 2, bottom-up DP
# notice this could be optimized to O(n) memory
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = map(len, (A, B))
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                res = max(res, dp[i][j])
        
        return res