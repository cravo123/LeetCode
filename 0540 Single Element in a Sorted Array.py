# Solution 1
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        
        for c in nums:
            res ^= c
        
        return res

# Solution 2
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        
        while i < j:
            m = (i + j) // 2
            if m % 2 == 1:
                m -= 1
            
            if nums[m] == nums[m + 1]:
                i = m + 2
            else:
                j = m
        return nums[i]