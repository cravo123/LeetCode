# Solution 1
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        carry = 1
        for c in reversed(digits):
            carry += c
            carry, v = divmod(carry, 10)
            res.append(v)
        
        if carry:
            res.append(carry)
        
        res.reverse()
        
        return res

# Solution 2
class Solution(object):
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