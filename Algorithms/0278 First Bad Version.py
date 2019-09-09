# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Solution 1, binary search
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        
        while i < j:
            m = (i + j) // 2
            
            if isBadVersion(m):
                j = m
            else:
                i = m + 1
        return i