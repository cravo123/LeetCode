import bisect

# Solution 1, binary search
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        
        return (right - left) > len(nums) // 2