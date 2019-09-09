import itertools

# Solution 1, simulation
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = [int(c) for c in reversed(num1)]
        num2 = [int(c) for c in reversed(num2)]
        
        res = []
        carry = 0
        i = j = 0
        m, n = len(num1), len(num2)
        
        while i < m or j < n or carry:
            if i < m:
                carry += num1[i]
                i += 1
            if j < n:
                carry += num2[j]
                j += 1
            carry, v = divmod(carry, 10)
            res.append(v)
        
        res = ''.join(str(c) for c in reversed(res))
        
        return res

# Solution 2, same idea, using itertools.zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        for a, b in itertools.zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
            carry += int(a) + int(b)
            carry, val = divmod(carry, 10)
            res.append(str(val))
        
        if carry:
            res.append(str(carry))
        
        res = ''.join(reversed(res))
        
        return res