# Solution 1, manual check
class Solution:
    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
    def reverseWords(self, s: str) -> str:
        s = list(s)
        i, n = 0, len(s)
        
        while i < n:
            j = i
            while j < n and s[j] != ' ':
                j += 1
            
            self.reverse(s, i, j - 1)
            
            i = j
            while i < n and s[i] == ' ':
                i += 1
        
        res = ''.join(s)
        
        return res

# Solution 2, built-in
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = [word[::-1] for word in s]
        res = ' '.join(s)
        
        return res