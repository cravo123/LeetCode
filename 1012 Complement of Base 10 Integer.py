class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        res = 0
        mult = 1
        
        while N > 0:
            v = N & 1
            res += (1 - v) * mult
            mult <<= 1
            N >>= 1
        
        return res