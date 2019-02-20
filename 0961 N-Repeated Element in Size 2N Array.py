class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = set()
        for c in A:
            if c in seen:
                return c
            seen.add(c)