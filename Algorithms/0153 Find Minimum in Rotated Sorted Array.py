# Solution 1, 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[-1]: # notice need to compare with last element
                i = m + 1
            else:
                j = m
        return nums[i]

# Solution 2, 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[-1]: # notice need to compare with last element
                i = m + 1
            else:
                j = m
        return nums[i]

# Solution 3, 
