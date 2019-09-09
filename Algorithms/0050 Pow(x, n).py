# Solution 1, recursion
class Solution:
    def dfs(self, x, n):
        if n == 0:
            return 1
        res = self.dfs(x, n // 2)
        res *= res
        
        return res if n % 2 == 0 else res * x
        
    def myPow(self, x: float, n: int) -> float:
        is_neg = n < 0
        n = abs(n)
        
        res = self.dfs(x, n)
        
        return 1 / res if is_neg else res

# Solution 2, Peasant multiplication
class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_neg = n < 0
        n = abs(n)
        
        res = 1
        v = x
        while n > 0:
            if n % 2:
                res *= v
            v *= v
            n //= 2
        return 1 / res if is_neg else res