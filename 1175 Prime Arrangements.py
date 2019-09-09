import math

# Solution 1, simulation
class Solution:
    def is_prime(self, n):
        if n == 1:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def numPrimeArrangements(self, n: int) -> int:
        cnt = sum(1 if self.is_prime(i) else 0 for i in range(1, n + 1))
        
        BASE = int(10 ** 9) + 7
        
        res = int(math.factorial(cnt) * math.factorial(n - cnt))
        
        return res % BASE