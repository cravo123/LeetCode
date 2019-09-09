class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i, j = 0, int(c**0.5) + 1
        
        while i <= j:
            v = i * i + j * j
            if v < c:
                i += 1
            elif v > c:
                j -= 1
            else:
                return True
        return False   