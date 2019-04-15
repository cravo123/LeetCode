import collections
# similar to LC 0873, LC 0306, LC 1027
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        d = {c:i for i, c in enumerate(A)}
        n = len(A)
        res = 0
        dp = collections.Counter()
        
        for i in range(n):
            for j in range(i):
                v = A[i] - A[j]
                if v in d and d[v] < j:
                    # k, j, i
                    dp[j, i] = max(dp[j, i], dp[d[v], j] + 1)
                    res = max(res, dp[j, i])
        
        return res + 2 if res > 0 else 0