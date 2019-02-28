# Solution 1, manual check
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        
        i = 0
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            j = i
            while j < n and s[j] != ' ':
                j += 1
            
            if i < n:
                left, right = i, j - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
            i = j
        res = ''.join(s)
        
        return res

# Solution 2, built-in
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = [word[::-1] for word in s]
        res = ' '.join(s)
        
        return res