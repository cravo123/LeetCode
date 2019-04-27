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

# Solution 2, DP, O(1) memory, similar to House Robber (LC 0337, 0198, 0213)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        
        do = not_do = 0
        prev = float('-inf')
        
        for c in sorted(d):
            cnt = d[c]
            
            new_not_do = max(do, not_do)
            new_do = c * cnt + (not_do if prev == c - 1 else new_not_do)
            
            do, not_do = new_do, new_not_do
            prev = c
        
        return max(do, not_do)