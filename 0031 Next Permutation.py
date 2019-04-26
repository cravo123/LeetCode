# Solution 1, 
#   1. Find first decreasing position, i
#   2. Find first position such that nums[j] is larger than nums[i - 1]
#      Since nums[i:] are decreasing-order, nums[j] is smallest number that 
#      is larger than nums[i - 1]
#   3. Swap nums[i - 1], nums[j], then sort nums[i:]
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        i = n - 1
        
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        
        if i == 0:
            nums.sort()
            return
        else:
            j = n - 1
            while j > i and nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            nums[i:] = sorted(nums[i:]) # reverse also works