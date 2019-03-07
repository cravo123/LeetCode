class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        
        curr = 0
        for i, c in enumerate(nums):
            if curr * 2 + c == total:
                return i
            curr += c
        return -1