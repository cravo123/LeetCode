# Solution 1, dp
class Solution:
    def fib(self, N: 'int') -> 'int':
        if N <= 1:
            return N
        idx = 1
        prev, curr = 0, 1
        
        while idx < N:
            prev, curr = curr, prev + curr
            idx += 1
        return curr

# Solution 1.1, dp with O(n) memory
class Solution:
    def fib(self, N: int) -> int:
        size = max(N, 2)
        dp = [0 for _ in range(size + 1)]
        dp[1] = 1
        
        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[N]

# Solution 1.2, top-down dp, memoization
class Solution:
    def dfs(self, idx, d):
        if idx in d:
            return d[idx]
        if idx <= 1:
            return idx
        
        d[idx] = self.dfs(idx - 1, d) + self.dfs(idx - 2, d)
        return d[idx]
        
    def fib(self, N: int) -> int:
        d = {}
        
        return self.dfs(N, d)