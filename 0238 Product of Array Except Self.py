class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums[::]
        prev = 1
        
        for i, v in enumerate(nums):
            res[i] = prev
            prev *= v
        
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prev
            prev *= nums[i]
        return res