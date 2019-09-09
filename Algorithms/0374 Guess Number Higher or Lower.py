# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

# Solution 1, binary search
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            m = (i + j) // 2
            v = guess(m)
            if v == -1:
                j = m - 1
            elif v == 1:
                i = m + 1
            else:
                return m

# Solution 1.1, a more general binary search template
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        
        while i < j:
            m = (i + j) // 2
            
            if guess(m) == 1:
                i = m + 1
            else:
                j = m
        return i