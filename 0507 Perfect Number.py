class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        res = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                a, b = i, num // i
                if a == b:
                    res += a
                else:
                    res += a + b
        return res == num * 2