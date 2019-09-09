# Solution 1, optimized DP using binary search
# dp[n, k] means minimum drops to guarantee to find pivot floor
# given total n floors and k eggs
class Solution:
    def dfs(self, n, k, dp):
        if (n, k) in dp:
            return dp[n, k]
        
        if k == 1 or n <= 1:
            return n
        
        res = n
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            v_left = self.dfs(mid - 1, k - 1, dp)
            v_right = self.dfs(n - mid, k, dp)
            
            res = min(res, max(v_left, v_right) + 1)
            # Since dp[n, k] is a monotonic function of n for a given k
            if v_left == v_right:
                break
            elif v_left < v_right:
                lo = mid + 1
            else:
                hi = mid
        
        dp[n, k] = res
        
        return res
        
        
    def superEggDrop(self, K: int, N: int) -> int:
        dp = {}
        
        return self.dfs(N, K, dp)

# Solution 1.1, top-down dp, memoization (TLE)
class Solution:
    def dfs(self, n, k, dp):
        if (n, k) in dp:
            return dp[n, k]
        
        if k == 1 or n <= 1:
            return n
        
        res = n
        
        for i in range(1, n + 1):
            res = min(res, 1 + max(self.dfs(i - 1, k - 1, dp), self.dfs(n - i, k, dp)))
        
        res += 1
        dp[n, k] = res
        
        return res
        
        
    def superEggDrop(self, K: int, N: int) -> int:
        dp = {}
        
        return self.dfs(N, K, dp)

# Soluion 2, a different DP
# Look at problem from a different perspective
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # dp[d][e] means maximum floors we can cover given d drops and e eggs
        # dp[d][e] = 1 + dp[d - 1][e - 1] + dp[d - 1][e]
        # we try floor dp[d - 1][e - 1],
        #   If it breaks, then we know pivot is in dp[d - 1][e - 1]
        #   If it doesn't break, then we know pivot is in range of dp[d - 1][e - 1] + 1 to dp[d - 1][e]
        # in either case, we are guaranteed to find results!
        dp = [0 for _ in range(K + 1)]
        
        steps = 0
        while dp[-1] < N:
            for e in range(K, 0, -1):
                dp[e] = 1 + dp[e] + dp[e - 1]
            steps += 1
        
        return steps