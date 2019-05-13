# Solution 1, DP
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        
        dp = [0 for _ in A]
        
        for i in range(n):
            curr = 0
            # k is length, and we need i - k + 1 >= 0
            # so k <= i + 1
            for k in range(1, min(K, i + 1) + 1):
                j = i - k + 1
                curr = max(curr, A[j])
                dp[i] = max(dp[i], curr * k + (dp[j - 1] if j - 1 >= 0 else 0))
        
        return dp[-1]

# Follow-up, what if we can cut array at most k times instead of 
# maximum length of k?
# DP similar idea