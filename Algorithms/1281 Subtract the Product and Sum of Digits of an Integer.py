# Solution 1, simulation
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        cs = [int(c) for c in str(n)]
        
        prod = 1
        total = 0
        
        for c in cs:
            prod *= c
            total += c
        
        return prod - total