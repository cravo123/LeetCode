# Solution 1, simulation

class Solution:
    def parse(self, s):
        real, imag = s.split('+')
        imag = imag[:-1]
        real, imag = map(int, (real, imag))
        
        return real, imag
        
    def complexNumberMultiply(self, a: str, b: str) -> str:
        
        r1, i1 = self.parse(a)
        r2, i2 = self.parse(b)
        
        r = r1 * r2 - i1 * i2
        i = r1 * i2 + r2 * i1
        
        res = '%d+%di' % (r, i)
        
        return res