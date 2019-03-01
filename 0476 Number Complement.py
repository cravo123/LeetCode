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
