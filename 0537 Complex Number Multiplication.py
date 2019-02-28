class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        r_a, c_a = a.split('+')
        r_b, c_b = b.split('+')
        
        r_a, r_b = map(int, (r_a, r_b))
        c_a, c_b = map(int, (c_a[:-1], c_b[:-1]))
        
        r_res = r_a * r_b - c_a * c_b
        c_res = r_a * c_b + c_a * r_b
        
        return '%d+%di' % (r_res, c_res)