# Solution 1, traverse from back to front
# Fewer corner case than traversing from front to back
class Solution:
    def translate(self, v):
        return chr(int(v) - 1 + ord('a'))
        
    def freqAlphabets(self, s: str) -> str:
        q = []
        
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == '#':
                q.append(self.translate(s[(i - 2):i]))
                i -= 3
            else:
                q.append(self.translate(s[i]))
                i -= 1
        
        return ''.join(reversed(q))