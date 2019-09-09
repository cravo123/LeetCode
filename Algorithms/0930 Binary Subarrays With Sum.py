import collections
# Prefix Sum
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        d = collections.Counter()
        d[0] = 1
        res = 0
        
        curr = 0
        
        for c in A:
            curr += c
            res += d[curr - S]
            d[curr] += 1
        return res