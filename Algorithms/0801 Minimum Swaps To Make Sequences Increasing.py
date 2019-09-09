# Solution 1, O(n) memory
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        
        dp = [[float('inf'), float('inf')] for _ in A]
        dp[0] = [0, 1]
        
        for i in range(1, n):
            # dp[i][0], not swap
            # dp[i][1], swap
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                dp[i][0] = min(dp[i][0], dp[i - 1][1])
                dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)
        
        return min(dp[-1])

# Solution 2, O(1) memory
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        swap = 1
        not_swap = 0
        
        for i in range(1, n):
            t_swap = t_not_swap = float('inf')
            
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                t_swap = min(t_swap, swap + 1)
                t_not_swap = min(t_not_swap, not_swap)
            
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                t_swap = min(t_swap, not_swap + 1)
                t_not_swap = min(t_not_swap, swap)
            swap, not_swap = t_swap, t_not_swap
        
        return min(swap, not_swap)