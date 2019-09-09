class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = collections.Counter()
        res = 0
        j = 0
        for i, c in enumerate(s):
            d[c] += 1
            
            while len(d) > k:
                c = s[j]
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
                j += 1
            res = max(res, i - j + 1)
        return res
