class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        for c in [5, 3, 2]:
            while num > 1 and num % c == 0:
                num //= c
        
        return num == 1