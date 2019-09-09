class Solution:
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a
    
    def mirrorReflection(self, p: int, q: int) -> int:
        x = self.gcd(p, q)
        lcm = p * q // x
        
        m = lcm // q
        
        # if m % 2 == 0, left, otherwise right
        if m % 2 == 0:
            return 2
        n = lcm // p
        if n % 2 == 1:
            return 1
        return 0