import collections

# Solution 1, use dict to cache recurrence.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = collections.Counter()
        j = 0
        res = 0
        for i, c in enumerate(s):
            d[c] += 1
            while d[c] > 1:
                d[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res

# Solution 2, use dict to cache the last occurrence index
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        j = 0
        for i, c in enumerate(s):
            if c in d:
                j = max(j, d[c] + 1)
            res = max(res, i - j + 1)
            d[c] = i
        return res