# Solution 1, loop through dict
# Idea is similar to LC 273, but this problem is much easier
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {}
        d[1000] = 'M'
        d[900] = 'CM'
        d[500] = 'D'
        d[400] = 'CD'
        d[100] = 'C'
        d[90] = 'XC'
        d[50] = 'L'
        d[40] = 'XL'
        d[10] = 'X'
        d[9] = 'IX'
        d[5] = 'V'
        d[4] = 'IV'
        d[1] = 'I'
        
        q = []
        
        for c in sorted(d, reverse=True):
            while num >= c:
                q.append(d[c])
                num -= c
        
        res = ''.join(q)
        
        return res