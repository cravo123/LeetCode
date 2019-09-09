# Solution 1, elegant simulation implementation
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, n = 0, len(s)
        
        for c in t:
            if c == s[i]:
                i += 1
                if i == n:
                    return True
        return False

# Solution 2, inter-twisted loop
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        m, n = len(s), len(t)
        
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == m

# Follow-up, what if there are many s's, then it makes sense to preprocess t