class Solution:
    def build_counter(self, A, B):
        d = collections.Counter()
        
        for a in A:
            for b in B:
                d[a + b] += 1
        
        return d
        
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d1, d2 = self.build_counter(A, B), self.build_counter(C, D)
        
        res = 0
        for k1 in d1:    
            k2 = -k1
            res += d1[k1] * d2[k2]
        
        return res