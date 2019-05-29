import collections

# Solution 1, count char occurrence
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)

# Solution 1.1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = collections.Counter(s)
        
        for c in t:
            d[c] -= 1
            if d[c] < 0:
                return False
        return True

# Solution 2, sort
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)