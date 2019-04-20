# Solution 1, same idea as LC 0264 Ugle Number II
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1 for _ in range(n)]
        
        idx = [0 for _ in primes]
        
        for i in range(1, n):
            v = min(primes[j] * dp[idx[j]] for j in range(len(primes)))
            dp[i] = v
            
            for j in range(len(primes)):
                if primes[j] * dp[idx[j]] == v:
                    idx[j] += 1
        
        return dp[-1]