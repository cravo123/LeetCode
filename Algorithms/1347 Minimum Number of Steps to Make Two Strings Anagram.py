import collections

# Solution 1, hash-map
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = collections.Counter(s) - collections.Counter(t) # only keep positive values
        
        return sum(d.values())