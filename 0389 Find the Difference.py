import collections
# Solution 1, dict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = collections.Counter(s)
        
        for c in t:
            d[c] -= 1
            if d[c] < 0:
                return c

# Solution 2, XOR
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        
        for c in s + t:
            res ^= ord(c)
        
        res = chr(res)
        
        return res