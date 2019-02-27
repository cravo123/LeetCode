class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x + 1
        
        while i < j:
            m = (i + j) // 2
            if m * m <= x:
                i = m + 1
            else:
                j = m
        return i - 1