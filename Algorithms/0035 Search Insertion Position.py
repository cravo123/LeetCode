import bisect

# Solution 1, binary search
# All issues in implementing binary search resides in assigning value i
# Since we use mid = (i + j) // 2, so there are only two values left in 
# the searching range, then, j = i + 1, and mid = i, so if we set i = mid
# then there will be infinite loop, and cause TLE. 
# So we can never set i = mid!
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        
        while i < j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1 # gotcha, can never be i = m
            else:
                j = m
        
        return i

# Solution 2, binary search using built-in
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        
        return idx

