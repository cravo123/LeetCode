from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        for c1, c2 in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            carry += int(c1) + int(c2)
            carry, v = divmod(carry, 2)
            res.append(v)
        if carry:
            res.append(carry)
        
        res = ''.join(str(x) for x in reversed(res))
        return res