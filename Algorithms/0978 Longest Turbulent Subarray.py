# Solution 1, dp with O(n) memory
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        dp = [[1, 1] for _ in range(n)] # dp[i][0] decreasing at i, dp[i][1] increasing at i
        res = 1
        for i in range(1, n):
            if A[i] > A[i - 1]:
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = 1
            elif A[i] < A[i - 1]:
                dp[i][0] = dp[i - 1][1] + 1
                dp[i][1] = 1
            res = max(res, dp[i][0], dp[i][1])
        
        return res
# Solution 2, dp with O(1) memory
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        # increase means current subarray ending with increase
        # decrease means current subarray with decrease
        res = increase = decrease = 1
        
        n = len(A)
        
        for i in range(1, n):
            if A[i] > A[i - 1]:
                increase = decrease + 1
                decrease = 1
            elif A[i] < A[i - 1]:
                decrease = increase + 1
                increase = 1
            else:
                increase = decrease = 1
            res = max(res, decrease, increase)
        
        return res