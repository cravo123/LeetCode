# Solution 1, DP
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # dp[n][k] means separate first n elements by k groups
        # dp[n][k] = max(dp[i][k - 1] + average(A[i] to A[n - 1])) for all i
        
        n = len(A)
        dp = [[0 for _ in range(K + 1)] for _ in range(n + 1)]
        
        curr = 0
        for i in range(1, n + 1):
            curr += A[i - 1]
            dp[i][1] = curr / i
        
        for i in range(1, n + 1):
            for k in range(2, min(K, i) + 1):
                for j in range(k - 1, i):
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + sum(A[j:i]) / (i - j))
        
        return dp[-1][K]

# Solution 1.1, DP with O(k) memory and cached prefix-sum
# t.b.c