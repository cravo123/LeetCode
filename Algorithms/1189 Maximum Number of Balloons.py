import collections

# Solution 1, simulation
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = collections.Counter(text)
        
        res = float('inf')
        
        for c, cnt in collections.Counter('balloon').items():
            res = min(res, d[c] // cnt)
        
        return res