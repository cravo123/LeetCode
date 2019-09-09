# Solution 1, simulation
class Solution:
    def isArmstrong(self, N: int) -> bool:
        s = str(N)
        k = len(s)
        
        res = 0
        
        for c in s:
            res += int(int(c) ** k)
        
        return res == N

# Solution 1.1, pythonic way
class Solution:
    def isArmstrong(self, N: int) -> bool:
        s = str(N)
        k = len(s)
        
        return sum(int(int(c) ** k) for c in s) == N