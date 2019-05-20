# Solution 1, chain of responsibility
# Use 
class Solution:
    def check_sign(self, s):
        i, n = 0, len(s)
        
        while i < n and s[i] in '+-':
            i += 1
        if i > 1:
            return False, s
        
        s = s[i:]
        return True, s  
        
    def check_int(self, s):
        flag, s = self.check_sign(s)
        if not flag:
            return False
        if not s or any(not c.isdigit() for c in s):
            return False
        
        return True
    
    def check_float(self, s):
        flag, s = self.check_sign(s)
        if not flag:
            return False
        
        v = s.split('.')
        if len(v) != 2:
            return False
        if not v[0] and not v[1]:
            return False
        
        return (self.check_int(v[0]) or not v[0]) and all(c.isdigit() for c in v[1])
    
    def check_nums(self, s):
        if not s:
            return False
        
        if '.' in s:
            return self.check_float(s)
        return self.check_int(s)
    
    def check_exponential(self, s):
        v = s.split('e')
        if len(v) != 2:
            return False
        
        return self.check_nums(v[0]) and self.check_int(v[1])
    
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        if 'e' in s:
            return self.check_exponential(s)
        return self.check_nums(s)