# Solution 1, elegant solution 
class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        
        for i, c in enumerate(s):
            if (i == 0 or s[i - 1] == ' ') and c != ' ':
                res += 1
        
        return res

# Solution 2, verbose one without using built-in
class Solution:
    def countSegments(self, s: str) -> int:
        n = len(s)
        i = 0
        res = 0
        
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i < n:
                res += 1
            
            while i < n and s[i] != ' ':
                i += 1
        
        return res

# Solution 3, use built-in
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())