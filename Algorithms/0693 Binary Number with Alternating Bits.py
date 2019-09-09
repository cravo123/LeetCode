# Solution 1, simulation
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = -1

        while n > 0:
            n, v = divmod(n, 2)
            if v == pre:
                return False
            pre = v
        return True

# Solution 1.1, bit-operation
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1
        
        while n > 0:
            curr = n & 1
            if curr == prev:
                return False
            prev = curr
            n >>= 1
        
        return True

# Solution 2, built-in function
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        
        for a, b in zip(s, s[1:]):
            if a == b:
                return False
        return True