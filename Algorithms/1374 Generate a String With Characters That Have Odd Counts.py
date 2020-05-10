# Solution 1, simulation
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n
        
        return 'a' + 'b' * (n - 1)