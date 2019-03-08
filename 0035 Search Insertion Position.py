import bisect

# Solution 1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        
        return idx

# Solution 2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        
        while i < j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m
        
        return i
