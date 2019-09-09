class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        prev = curr = 0
        res = 0
        for c in nums:
            if c == 1:
                curr += 1
            else:
                res = max(res, prev + curr)
                prev, curr = curr + 1, 0
        
        res = max(res, prev + curr)
        
        return res