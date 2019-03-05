class Solution:
    def rob_helper(self, nums):
        do = not_do = 0
        for c in nums:
            do, not_do = c + not_do, max(do, not_do)
        
        return max(do, not_do)
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums) if nums else 0
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))