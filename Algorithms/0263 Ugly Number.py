# Solution 1, simulation
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        
        for c in [2, 3, 5]:
            while num % c == 0:
                num //= c
        
        return num == 1