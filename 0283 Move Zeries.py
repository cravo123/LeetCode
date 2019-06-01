# Solution 1, fill tail with 0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        
        for c in nums:
            if c != 0:
                nums[j] = c
                j += 1
        
        while j < n:
            nums[j] = 0
            j += 1