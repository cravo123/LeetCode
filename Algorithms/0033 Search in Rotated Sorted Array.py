# Solution 1, Binary Search
# The idea is to use binary search to determine which half is
# in increasing order
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        i, j = 0, len(nums) - 1
        
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            
            # i to m is increasing
            if nums[i] <= nums[m]:
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            else:
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
        return -1