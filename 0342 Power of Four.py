# Solution 1, naive checking power of 4
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        
        while num > 1 and num % 4 == 0:
            num //= 4
        
        return num == 1

# Solution 2, find the largest multiplier of power 4