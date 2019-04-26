import collections

# Solution 1, DP
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        v = list(sorted(d.items()))
        n = len(v)
        
        dp = [[0, 0] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = v[i - 1][0] * v[i - 1][1] + (dp[i - 1][0] if i > 1 and v[i - 1][0] == v[i - 2][0] + 1 else max(dp[i - 1]))
        
        return max(dp[-1])