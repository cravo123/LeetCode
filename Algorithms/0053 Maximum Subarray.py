# Solution 1, prefix sum
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_min = 0
        curr = 0
        res = float('-inf')
        
        for c in nums:
            curr += c    
            res = max(res, curr - curr_min)
            curr_min = min(curr_min, curr)
        
        return res

# Solution 2, DP
# dp[i] means maximum subarray sum ending with i
# LC 0121 Buy and Sell stock can be solved by this algorithm also.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        
        for i in range(n):
            dp[i + 1] = max(dp[i], 0) + nums[i]
        
        return max(dp[1:])