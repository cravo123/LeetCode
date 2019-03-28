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