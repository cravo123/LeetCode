# Solution 1, lattice algorithm
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [int(c) for c in reversed(num1)]
        num2 = [int(c) for c in reversed(num2)]
        
        m, n = map(len, (num1, num2))
        
        res = [0 for _ in range(m + n)]
        
        for i in range(m):
            for j in range(n):
                res[i + j] += int(num1[i]) * int(num2[j])
                if res[i + j] > 9:
                    m, v= divmod(res[i + j], 10)
                    res[i + j] = v
                    res[i + j + 1] += m
        
        while res and res[-1] == 0:
            res.pop()
        
        if not res:
            return '0'
        
        res = ''.join(str(c) for c in reversed(res))
        
        return res