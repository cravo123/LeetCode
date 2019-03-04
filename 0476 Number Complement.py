# Solution 1
class Solution:
    def findComplement(self, num: int) -> int:
        q = []
        
        while num:
            q.append(num & 1)
            num >>= 1
        
        res = 0
        for v in reversed(q):
            res = res * 2 + (1 - v)
        
        return res

# Solution 2, use mask
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
