# Solution 1, binary search
# A bit tricky...
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        
        while i < j:
            if nums[i] == nums[j]:
                j -= 1
                continue
            
            m = (i + j) // 2
            if nums[m] <= nums[j]:
                j = m
            else:
                i = m + 1
        return nums[i]