# Solution 1, hash-map
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = set()
        
        for s, e in paths:
            d.add(e)
        
        for s, e in paths:
            d.discard(s)
        
        return d.pop()