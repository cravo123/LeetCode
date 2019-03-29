# Solution 1, dp
class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def get_cnt(self, n, d):
        if n in d:
            return d[n]
        
        res = 1 if n % 2 else 0
        res += self.get_cnt(n // 2, d)
        
        d[n] = res
        
        return res
    
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        d = {} # value: count of 1
        d[0] = 0
        d[1] = 1
        res = 0
        for i in range(max(L, 2), R + 1):
            cnt = (1 if i % 2 else 0) + self.get_cnt(i // 2, d)
            if self.is_prime(cnt):
                res += 1
            d[i] = cnt
        
        return res

# Solutin 2, Brute-Force, just iterate all scenarios
class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        
        res = 0
        for i in range(max(L, 2), R + 1):
            v = bin(i)[2:].count('1')
            if self.is_prime(v):
                res += 1
        
        return res