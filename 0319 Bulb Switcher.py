# Solution 1, use built-in function
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)

# Solution 2, find square numbers
class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        
        i = 1
        
        while i * i <= n:
            res += 1
            i += 1
        
        return res