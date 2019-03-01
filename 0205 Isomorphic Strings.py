# Solution 1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d, seen = {}, set()
        
        for a, b in zip(s, t):
            if a in d and d[a] != b:
                return False
            if a not in d and b in seen:
                return False
            d[a] = b
            seen.add(b)
        return True
 
 # Solution 2
 class Solution:
    def change(self, s):
        d = {}
        
        res = []
        for c in s:
            res.append(d.setdefault(c, len(d)))
        
        res = ','.join(str(x) for x in res)
        
        return res
        
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        return self.change(s) == self.change(t)
