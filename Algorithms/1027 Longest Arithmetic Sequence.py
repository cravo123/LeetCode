import collections

# Solution 1, DP solution, similar to LC 0873, LC 0306
# dp[prev_idx, curr_idx]
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        d = collections.defaultdict(list)
        
        n = len(A)
        dp = collections.Counter()
        res = 0
        
        for i in range(n):
            d[A[i]].append(i)
            for j in range(i):
                v = 2 * A[j] - A[i]
                for k in d[v]:
                    if k < j:
                        dp[j, i] = max(dp[j, i], dp[k, j] + 1)
                        res = max(res, dp[j, i])
        
        return res + 2

# Solution 2, dp[diff, idx]
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = collections.Counter()
        res = 0
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[diff, i] = max(dp[diff, i], dp[diff, j] + 1)
                res = max(dp[diff, i], res)
        
        return res + 1