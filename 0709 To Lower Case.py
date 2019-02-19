class Solution:
    def change(self, c):
        return chr(ord(c) - ord('A') + ord('a')) if 'A' <= c <= 'Z' else c
        
    def toLowerCase(self, str: 'str') -> 'str':
        s = list(str)
        
        res = map(self.change, s)
        return ''.join(res)
