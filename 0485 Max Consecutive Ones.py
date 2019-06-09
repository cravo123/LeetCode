# Solution 1, simulation
# This type of question focuses on testing your micro-management on loop.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i, n = 0, len(nums)
        
        while i < n:
            while i < n and nums[i] == 0:
                i += 1
            
            cnt = 0
            while i < n and nums[i] == 1:
                cnt += 1
                i += 1
            res = max(res, cnt)
        
        return res

# Solution 1.1, elegant implementation
# reset curr to be 0 when c is 0
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = curr = 0
        
        for c in nums:
            if c == 0:
                curr = 0
            else:
                curr += 1
            res = max(res, curr)
        
        return res