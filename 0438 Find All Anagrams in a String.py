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
        target = collections.Counter(p)
        curr = collections.Counter()
        cnt = 0
        
        res = []
        n = len(p)
        
        for i, c in enumerate(s):
            if c in target:
                curr[c] += 1
                if curr[c] <= target[c]:
                    cnt += 1
            
            prev = i - n + 1
            if prev >= 0 and cnt == n:
                res.append(i - n + 1)
            
            if prev >= 0 and s[prev] in target:
                curr[s[prev]] -= 1
                if 0 <= curr[s[prev]] < target[s[prev]]:
                    cnt -= 1
           
        return res