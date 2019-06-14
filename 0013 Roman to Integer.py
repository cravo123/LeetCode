# Solution 1, simulation
# We observe that if a char whose value are smaller than its successor,
# then it means subtracting
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1, 
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100, 
            'D': 500,
            'M': 1000
        }
        
        res = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        
        return res

# Solution 2, EAFP: Easier to ask for forgiveness than permission
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I':    1,
            'IV':   4,
            'V':    5,
            'IX':   9,
            'X':    10,
            'XL':   40,
            'L':    50,
            'XC':   90,
            'C':    100,
            'CD':   400,
            'D':    500,
            'CM':   900,
            'M':    1000,
        }
        
        i, n = 0, len(s)
        res = 0
        
        while i < n:
            key = s[i:(i + 2)]
            try:
                res += d[key]
                i += len(key)
            except:
                res += d[s[i]]
                i += 1
        
        return res