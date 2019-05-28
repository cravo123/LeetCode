# Solution 1, implement to_lower
class Solution:
    def change(self, c):
        return chr(ord(c) - ord('A') + ord('a')) if 'A' <= c <= 'Z' else c
        
    def toLowerCase(self, s: 'str') -> 'str':
        s = list(s)
        
        res = map(self.change, s)
        return ''.join(res)

# Solution 2, built-in
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()