# Solution 1, simulation
# Treat differently when n is even and odd
# If n is even, we use [1, -1, 2, -2, ...]
# If n is odd, we append 0 at the end
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [i * flag for i in range(1, n // 2 + 1) for flag in [-1, 1]]
        
        if n % 2 == 1:
            res.append(0)
        
        return res