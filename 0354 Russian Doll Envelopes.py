import bisect
# Solution 1, Longest-Increasing-Subsequence(LIS) for width after sorting height
# O(nlog(n))
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        q = [float('inf') for _ in envelopes]
        res = 0
        
        for w, h in envelopes:
            idx = bisect.bisect_left(q, h)
            q[idx] = h
        
        j = len(q) - 1
        
        while j >= 0 and q[j] == float('inf'):
            j -= 1
        
        return j + 1

# Solution 2, same idea but use DP to calculate LIS
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        q = envelopes
        n = len(q)
        
        dp = [1 for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if q[i][1] > q[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp) if dp else 0