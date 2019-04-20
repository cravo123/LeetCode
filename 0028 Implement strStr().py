# Solution 1, Rabin-Karp

class Solution:
    def calc(self, s, multi, base):
        curr = 0
        for c in s:
            curr = (curr * multi + ord(c)) % base
        
        return curr % base
        
    def strStr(self, haystack: str, needle: str) -> int:
        # Rabin-Karp Algorithm
        if needle == '':
            return 0
        base = int(10**7)
        multi = 31
        
        target = self.calc(needle, multi, base)
        
        curr = 0
        n = len(needle)
        for i, c in enumerate(haystack):
            curr = curr * multi + ord(c)
            if i >= n:
                curr -= ord(haystack[i - n]) * int(multi ** n)
            curr %= base
            
            if i >= n - 1 and curr == target and haystack[(i - n + 1):(i + 1)]:
                return i - n + 1
        return -1

# Solution 2, built-in function
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)