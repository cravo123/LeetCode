import collections
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = collections.Counter()
        j = 0
        res = 0
        for i, c in enumerate(s):
            d[c] += 1
            while len(d) > 2:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    del d[s[j]]
                j += 1
            res = max(res, i - j + 1)
        return res