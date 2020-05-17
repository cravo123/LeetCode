# Solution 1, simulation
class Solution:
    def reformat(self, s: str) -> str:
        a_s = [c for c in s if c.isalpha()]
        n_s = [c for c in s if c.isdigit()]
        
        if abs(len(a_s) - len(n_s)) > 1:
            return ''
        
        if len(a_s) < len(n_s):
            a_s, n_s = n_s, a_s
        
        res = []
        
        while a_s or n_s:
            if a_s:
                res.append(a_s.pop())
            if n_s:
                res.append(n_s.pop())
        
        return ''.join(res)