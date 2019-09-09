# Solution 1, Binary Search on results
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n + 1
        
        while left < right:
            mid = (left + right) // 2
            total = (mid + 1) * mid // 2
            
            if total <= n:
                left = mid + 1
            else:
                right = mid
        
        return left - 1

# Solution 2, Brute-Force
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        
        while n - i >= 0:
            n -= i
            i += 1
        return i - 1