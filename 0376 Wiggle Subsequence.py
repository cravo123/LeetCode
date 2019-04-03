# Solution 1, O(n ^ 2) efficiency
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        
        dp = [[1, 1] for _ in nums]
        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                if nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            res = max(res, dp[i][0], dp[i][1])
        
        return res
