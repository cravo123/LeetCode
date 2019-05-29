import collections

# Solution 1, sliding-window
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        res_len = float('inf')
        
        need = collections.Counter(t)
        curr = collections.Counter()
        match = 0
        n = len(t)
        
        j = 0
        for i, c in enumerate(s):
            if c in need:
                curr[c] += 1
                if curr[c] <= need[c]:
                    match += 1
            
            while match == n:
                if i - j + 1 < res_len:
                    res_len = i - j + 1
                    res = s[j:(i + 1)]
                c = s[j]
                if c in need:
                    curr[c] -= 1
                    if curr[c] < need[c]:
                        match -= 1
                j += 1
        return res