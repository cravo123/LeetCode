import collections

# Solution 1, sliding-window
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        d = collections.Counter()
        res = 0
        
        for i, c in enumerate(S):
            d[c] += 1
            if i >= K:
                x = S[i - K]
                d[x] -= 1
                if not d[x]:
                    del d[x]
            if len(d) == K:
                res += 1
        
        return res