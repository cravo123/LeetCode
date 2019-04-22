import string

class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        
        while i < n and s[i] == ' ':
            i += 1
        
        if i == n or s[i] not in '+-' + string.digits:
            return 0
        
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        j = i
        curr = 0
        while j < n and s[j].isdigit():
            curr = curr * 10 + int(s[j])
            j += 1
        
        # Actually since we return 0 if encountering any error
        # The if below is redundant since curr will be 0 if 
        # input is invalid
        if j == i or j > i + 1 and curr == 0:
            return 0
        
        curr *= sign
        
        return min(max(curr, -int(2**31)), int(2**31) - 1)
        