# Solution 1, similar to LC 0031 Next Permutation
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        
        m = len(s)
        j = m - 1
        while j > 0 and s[j] <= s[j - 1]:
            j -= 1
        
        if j == 0:
            return -1
        j -= 1
        i = m - 1
        while i > j and s[i] <= s[j]:
            i -= 1
        
        s[i], s[j] = s[j], s[i]
        s[(j + 1):] = sorted(s[(j + 1):])
        
        v = int(''.join(s))
        
        return v if v < int(2 ** 31) else -1