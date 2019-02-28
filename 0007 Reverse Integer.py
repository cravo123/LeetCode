class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = x < 0
        x = abs(x)
        
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        
        res = -res if is_neg else res
        
        if int(-2**31) <= res <= int(2**31 - 1):
            return res
        return 0