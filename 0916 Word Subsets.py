import collections

# Solution 1, simulation
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = collections.Counter()
        
        for word in B:
            t = collections.Counter(word)
            
            for c in t:
                d[c] = max(d[c], t[c])
        
        res = []
        
        for word in A:
            t = collections.Counter(word)
            
            if all(t[c] >= d[c] for c in d):
                res.append(word)
        
        return res