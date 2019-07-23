import string

# Solution 1, symmetry
class Solution:
    def generate_min(self, curr):
        res = ''
        res_val = float('inf')
        
        for c in string.hexdigits:
            if abs(int(c + c, 16) - int(curr, 16)) < res_val:
                res = c + c
                res_val = abs(int(c + c, 16) - int(curr, 16))
        return res
        
    def similarRGB(self, color: str) -> str:
        res = ['#']
        
        for i in range(1, len(color), 2):
            res.append(self.generate_min(color[i:(i + 2)]))
        
        res = ''.join(res)
        return res

# Solution 2, brute-force, enumerate all possibilities
class Solution:
    def generate(self):
        res = []
        
        for a in string.hexdigits:
            for b in string.hexdigits:
                for c in string.hexdigits:
                    res.append(a * 2 + b * 2 + c * 2)
        return res
    
    def diff(self, a, b):
        res = 0
        
        for i in range(0, len(a), 2):
            t = int(a[i:(i + 2)], 16) - int(b[i:(i + 2)], 16)
            res += t * t
        return res
    
    def similarRGB(self, color: str) -> str:
        res = ''
        curr = float('inf')
        color = color[1:]
        
        for kk in self.generate():
            v = self.diff(kk, color)
            
            if v < curr:
                curr = v
                res = kk
        return '#' + res

