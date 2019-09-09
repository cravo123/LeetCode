# Solution 1, two-pointer
class Solution:
    def reverseOnlyLetters(self, S: 'str') -> 'str':
        S = list(S)
        i, j = 0, len(S) - 1
        
        while i < j:
            while i < j and not S[i].isalpha():
                i += 1
            
            while i < j and not S[j].isalpha():
                j -= 1
            
            if i < j:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
        return ''.join(S)

# Solution 2, stack
# Interesting idea, but not as efficient as Solution 1
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        q = [c for c in S if c.isalpha()]
        
        res = []
        
        for c in S:
            if c.isalpha():
                res.append(q.pop())
            else:
                res.append(c)
        
        res = ''.join(res)
        
        return res