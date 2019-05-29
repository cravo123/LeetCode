import collections
# Solution 1, check counter equality, brute-force
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        curr = collections.Counter()
        
        res = []
        n = len(p)
        for i, c in enumerate(s):
            curr[c] += 1
            if curr == target:
                res.append(i - n + 1)
            prev = i - n + 1
            if prev >= 0:
                curr[s[prev]] -= 1
                if not curr[s[prev]]:
                    del curr[s[prev]]
        return res

# Solution 2, sliding-window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = collections.Counter(p)
        need = len(p)
        curr = collections.Counter()
        res = []
        j = 0
        for i, c in enumerate(s):
            curr[c] += 1
            
            if curr[c] <= d[c]:
                need -= 1
            
            if i - j + 1 > len(p):
                v = s[j]
                curr[v] -= 1
                if curr[v] < d[v]:
                    need += 1
                j += 1
            
            if need == 0:
                res.append(j)
        
        return res