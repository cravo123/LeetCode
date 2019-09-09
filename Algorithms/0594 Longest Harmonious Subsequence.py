import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.Counter(nums)
        res = 0
        
        for c in d:
            if c + 1 in d:
                res = max(res, d[c] + d[c + 1])
        return res

# Note that since it is length of subsequence, so order doesn't matter
# we can then sort nums directly.