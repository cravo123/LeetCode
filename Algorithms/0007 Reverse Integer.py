# Solution 1, simulation
class Solution:
    def reverse(self, x: int) -> int:
        sign_val = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        
        for c in reversed(str(x)):
            res = res * 10 + int(c)
        
        res *= sign_val
        
        return res if - 2 ** 31 <= res <= 2 ** 31 - 1 else 0