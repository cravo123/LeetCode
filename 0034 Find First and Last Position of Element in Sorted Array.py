import bisect

# Solution 1, implement bisect functions
class Solution:
    def lower_bound(self, nums, target):
        i, j = 0, len(nums) - 1
        
        while i < j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m
        return i if nums[i] == target else -1
        
    def upper_bound(self, nums, target):
        i, j = 0, len(nums)
        
        while i < j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m
        return i - 1 if nums[i - 1] == target else -1
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        i, j = self.lower_bound(nums, target), self.upper_bound(nums, target)
        
        return [i, j]

# Solution 2, use bisect directly
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect.bisect_left(nums, target)
        j = bisect.bisect_right(nums, target)
        
        if i == len(nums) or nums[i] != target:
            return [-1, -1]
        return [i, j - 1]