# Solution 1, simulation
class Solution:
    def mask_email(self, S):
        S = S.lower()
        name, domain = S.split('@')
        name = name[0] + '*' * 5 + name[-1]
        return '@'.join([name, domain])
    
    def mask_phone(self, S):
        S = [c for c in S if c.isdigit()]
        res = []
        if len(S) > 10:
            res = ['+' + '*' * (len(S) - 10)]
        res.append('***-***')
        res.append(''.join(S[-4:]))
        res = '-'.join(res)
        
        return res
        
    def maskPII(self, S: str) -> str:
        if '@' in S:
            res = self.mask_email(S)
        else:
            res = self.mask_phone(S)
        
        return res