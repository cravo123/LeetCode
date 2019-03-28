# Moore Voting Algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v, cnt = nums[0], 0
        
        for c in nums:
            if c == v:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt < 0:
                v, cnt = c, 1
        
        return v