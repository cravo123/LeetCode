class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            if n & 1:
                res += 1
            n >>= 1
        return res