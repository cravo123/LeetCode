# Solution 1, simulation
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        curr = 0
        
        for c in S:
            if c.isdigit():
                curr *= int(c)
            else:
                curr += 1
        
        i = len(S) - 1
        
        while i >= 0:
            K %= curr
            if K == 0 and S[i].isalpha():
                return S[i]
            
            if S[i].isdigit():
                curr //= int(S[i])
            else:
                curr -= 1    
            i -= 1