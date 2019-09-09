# Solution 1, change in place
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        
        for c in nums:
            if c != val:
                nums[j] = c
                j += 1
        return j

# Solution 2, similar to quick select
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        j = 0
        while i < n:
            if nums[i] != val:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            i += 1
        return j

# Solution 3, where val is rare
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return i