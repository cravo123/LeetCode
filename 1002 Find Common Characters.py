import collections

# Solution 1, simulation
# & operator and elements() method for Counter()
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d = collections.Counter(A[0])
        
        for a in A:
            d &= collections.Counter(a)
        
        res = list(d.elements())
        
        return res