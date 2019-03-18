# Solution 1, Gauss Formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        return n * (n + 1) // 2 - sum(nums)

# Solution 2, XOR
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        
        for i, c in enumerate(nums):
            res ^= i ^ c
        
        return res