# Solution 1, use while loop
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        
        return n == 1

# Solution 2, recursion
class Solution:
    def dfs(self, n):
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.dfs(n // 3)
    
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return self.dfs(n)

# Solution 3, find maximum value
# Find maximum value that is a power of 3, then check if this number is a factor 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return int(3 ** 19) % n == 0