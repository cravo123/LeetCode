# Solution 1, DP
# Fibonacci sequence though
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(max(n + 1, 2))]
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# Solution 1.1, O(1) memory DP
class Solution:
    def climbStairs(self, n: int) -> int:
        prev = curr = 1
        idx = 1
        
        while idx < n:
            curr, prev = curr + prev, curr
            idx += 1
        
        return curr

# Solution 2, top-down DP, memoization
class Solution:
    def dfs(self, n, d):
        if n in d:
            return d[n]
        res = self.dfs(n - 1, d) + self.dfs(n - 2, d)
        d[n] = res
        return res
        
    def climbStairs(self, n: int) -> int:
        d = {}
        d[0] = d[1] = 1
        
        return self.dfs(n, d)