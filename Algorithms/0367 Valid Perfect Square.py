class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, j = 0, num
        
        while i < j:
            m = (i + j) // 2
            
            v = m * m
            
            if v < num:
                i = m + 1
            else:
                j = m
        
        return True if i * i == num else False