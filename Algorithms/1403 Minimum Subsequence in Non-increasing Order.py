# Solution 1, sort
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        
        nums.sort(reverse=True)
        
        res = []
        curr = 0
        for c in nums:
            curr += c
            res.append(c)
            
            if curr > total / 2:
                return res