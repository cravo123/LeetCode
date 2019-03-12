class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        total = sum(1 if c != '-' else 0 for c in S)
        
        need = total % K or K
        curr = 0
        res = []
        tmp = []
        
        for c in S:
            if c != '-':
                curr += 1
                tmp.append(c.upper())
            
            if curr == need:
                res.append(''.join(tmp))
                tmp = []
                need = K
                curr = 0
        res = '-'.join(res)
        
        return res