import collections

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = collections.Counter()
        d[0] = 1
        res = 0
        curr = 0
        for c in A:
            curr += c
            res += d[curr % K]
            d[curr % K] += 1
        
        return res