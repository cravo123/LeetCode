class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        q = []
        
        for i in range(32):
            q.append(n % 2)
            n >>= 1
        res = 0
        for c in q:
            res = res * 2 + c
        
        return res