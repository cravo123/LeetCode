class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s.strip())
        
        i, n = 0, len(s)
        
        res = []
        
        while i < n:
            j = i
            while j < n and s[j] != ' ':
                j += 1
            
            res.append(''.join(s[i:j]))
            
            while j < n and s[j] == ' ':
                j += 1
            i = j
        
        res = ' '.join(reversed(res))
        
        return res