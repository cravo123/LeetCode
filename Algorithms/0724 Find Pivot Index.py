# Solution 1, simulating using prefix sum
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0
        
        for i, c in enumerate(nums):
            if curr * 2 + c == total:
                return i
            curr += c
        
        return -1