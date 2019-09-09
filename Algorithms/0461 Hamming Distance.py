# Solution 1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x > 0 or y > 0:
            a, b = x % 2, y % 2
            x //= 2
            y //= 2
            res += a ^ b
        return res

# Solution 2, bit manipulation
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        v = x ^ y
        
        while v:
            res += 1
            v &= v - 1
        return res