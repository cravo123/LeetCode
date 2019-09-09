# Solution 1, classification
# We move i to the right as long as it is non-decreasing array
# so i could stop at two cases,
#   1. 0, 1, 2, -5, 3
#       Stops at value -5
#   2. 0, 1, 2, 10, 3
#       Stops at value 10
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        
        prev = float('-inf')
        i = 0
        
        while i < n and nums[i] >= prev:
            prev = nums[i]
            i += 1
        
        # Already sorted
        if i == n:
            return True
        
        # i stops at position right after abnormal high point
        j = i
        prev = nums[j - 2] if j >= 2 else float('-inf')
        while j < n and nums[j] >= prev:
            prev = nums[j]
            j += 1
        if j == n:
            return True
        
        # i stops at position right after abnormal low point
        j = i + 1
        prev = nums[j - 2] if j >= 2 else float('-inf')
        while j < n and nums[j] >= prev:
            prev = nums[j]
            j += 1
        if j == n:
            return True
        
        return False

# Solution 2, locate error position
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        
        p = None
        
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if p is None:
                    p = i
                else:
                    return False
        if p is None or p == 0 or p == n - 2 or nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2]:
            return True
        return False