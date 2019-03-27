class Solution:
    def calc(self, n):
        res = 0
        while n > 0:
            res += (n % 10) * (n % 10)
            n //= 10
        
        return res
        
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        
        seen = set()
        
        while n > 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.calc(n)
        return True