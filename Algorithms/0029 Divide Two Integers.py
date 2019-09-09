# Solution 1, similar to Binary Search
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_neg = (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        
        while dividend >= divisor:
            curr = divisor
            idx = 1
            
            while dividend >= curr:
                dividend -= curr
                res += idx
                idx <<= 1
                curr <<= 1
        
        res = -res if is_neg else res
        
        return min(max(res, int(-2 ** 31)), int(2 ** 31) - 1)