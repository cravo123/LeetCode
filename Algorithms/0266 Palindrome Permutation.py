import collections

# Solution 1, count occurrence
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return True
        d = collections.Counter(s)
        res = sum(1 if d[c] % 2 else 0 for c in d)
        
        return res <= 1