# Solution 1, Stack
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        q = []
        res = [-1 for _ in nums]
        for i, c in enumerate(nums + nums):
            while q and nums[q[-1]] < c:
                res[q.pop()] = c
            q.append(i % n)
        return res