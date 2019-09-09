# Solution 1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

# Solution 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 1:
                return False
            x = 2
            while n % x == 0:
                n //= x
                x *= x
        return n == 1