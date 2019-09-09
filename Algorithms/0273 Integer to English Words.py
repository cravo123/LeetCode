# Solution 1, Recursion
# Key is to find the pattern that we parse integer every 3 digits,
# then add unit to it. So the problem drills down to how to represent
# 3 digits number in English
class Solution:
    def translate(self, num):
        d = {}
        d[90] = 'Ninety'
        d[80] = 'Eighty'
        d[70] = 'Seventy'
        d[60] = 'Sixty'
        d[50] = 'Fifty'
        d[40] = 'Forty'
        d[30] = 'Thirty'
        d[20] = 'Twenty'
        d[19] = 'Nineteen'
        d[18] = 'Eighteen'
        d[17] = 'Seventeen'
        d[16] = 'Sixteen'
        d[15] = 'Fifteen'
        d[14] = 'Fourteen'
        d[13] = 'Thirteen'
        d[12] = 'Twelve'
        d[11] = 'Eleven'
        d[10] = 'Ten'
        d[9] = 'Nine'
        d[8] = 'Eight'
        d[7] = 'Seven'
        d[6] = 'Six'
        d[5] = 'Five'
        d[4] = 'Four'
        d[3] = 'Three'
        d[2] = 'Two'
        d[1] = 'One'
        
        if num == 0:
            return ''
        
        if num >= 100:
            q = [d[num // 100], 'Hundred', self.translate(num % 100)]
        else:
            q = []
            for c in sorted(d, reverse=True):
                if num >= c:
                    q.append(d[c])
                    num = num % c
        
        while q and q[-1] == '':
            q.pop()
        res = ' '.join(q)
        
        return res
        
    def numberToWords(self, num: int) -> str:
        units = {}
        units[int(1e9)] = 'Billion'
        units[int(1e6)] = 'Million'
        units[int(1e3)] = 'Thousand'
        
        res = []
        
        for u in sorted(units, reverse=True):
            if num >= u:
                res.append(self.translate(num // u))
                res.append(units[u])
                num = num % u
        if num:
            res.append(self.translate(num))
        res = ' '.join(res)
        
        return res or 'Zero'