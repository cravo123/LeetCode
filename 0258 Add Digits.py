# Solution 1, Iteration
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp = 0
            while num > 0:
                tmp += num % 10
                num //= 10
            num = tmp
        return num

# Solution 2, 
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: 
            return 0
        return (num - 1) % 9 + 1