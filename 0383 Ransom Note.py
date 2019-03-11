import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        for c in ransomNote:
            d[c] -= 1
            if d[c] < 0:
                return False
        return True