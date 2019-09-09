# Solution 1, binary search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        i, j = 0, n - 1
        
        while i < j:
            m = (i + j) // 2
            
            if nums[m] < nums[m + 1]:
                i = m + 1
            elif nums[m] > nums[m + 1]:
                j = m
        return i

# Solution 2, brute-force
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1
        
        for i in range(n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

# Solution 3, elegant brute-force
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return i
        return n - 1