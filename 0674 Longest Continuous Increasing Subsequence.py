# Typical DP problem
# Solution 1, memory O(n)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1 for _ in nums]
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                res = max(res, dp[i])
        
        return res

# Solution 2, memory O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        prev = float('-inf')
        
        for c in nums:
            if c > prev:
                cnt += 1
            else:
                cnt = 1
            prev = c
            res = max(res, cnt)
        
        return res