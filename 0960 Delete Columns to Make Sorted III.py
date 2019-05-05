# Solution 1, think the other way around
# If it is not easy to compute how many columns needed to be deleted
# then we can think what is the LIS(longest Increasing Subsequence)

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0]) if A else 0
        
        dp = [1 for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if all(A[x][i] >= A[x][j] for x in range(m)):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return n - max(dp)