class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        
        curr = 0
        res = 0
        for i, c in enumerate(nums):
            if c == 0:
                curr += 1
            else:
                curr -= 1
            
            if curr in d:
                res = max(res, i - d[curr])
            else:
                d[curr] = i
            
        return res