class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        res = 0
        while i < n:
            while i < n and nums[i] == 0:
                i += 1
            
            j = i
            while j < n and nums[j] == 1:
                j += 1
            
            res = max(res, j - i)
            i = j
        
        return res