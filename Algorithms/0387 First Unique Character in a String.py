import collections

# Solution 1, two-pass, hashmap
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1