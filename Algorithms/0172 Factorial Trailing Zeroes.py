# Solution 1, simulation
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        
        while n > 0:
            n //= 5
            res += n
        
        return res