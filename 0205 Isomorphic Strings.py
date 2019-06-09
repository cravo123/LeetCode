# Solution 1, use hashmap and hashset
# hashmap maintains the mapping, 
# and hashset caches all chars we have used till so far
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
 
 # Solution 2, standardize the each string by occurrence
class Solution:
    def standardize(self, s):
        d = {}
        
        res = []
        for c in s:
            res.append(d.setdefault(c, len(d)))
        
        return res
        
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        return self.standardize(s) == self.standardize(t)
