# Solution 1, simulation
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                return digits
            carry += digits[i]
            carry, val = divmod(carry, 10)
            digits[i] = val
        
        if carry:
            res = [carry] + digits
        else:
            res = digits
        
        return res

# Solution 2
# Find last non-9 position first
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        j = -1
        
        for i, c in enumerate(digits):
            if c != 9:
                j = i
        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        if j == -1:
            for i in range(n):
                digits[i] = 0
            digits = [1] + digits
        else:
            digits[j] += 1
            j += 1
            while j < n:
                digits[j] = 0
                j += 1
        return digits