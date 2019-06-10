# Solution 1, 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        multi = 1
        while x >= multi:
            multi *= 10
        multi //= 10
        
        while multi > 0:
            left = x // multi
            right = x % 10
            if left != right:
                return False
            
            x %= multi
            x //= 10
            multi //= 100
        return True

# Solution 2, convert to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        i, j = 0, len(x) - 1
        
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        
        return True