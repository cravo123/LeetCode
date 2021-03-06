# Solution 1,
class Solution:
    def binaryGap(self, N: int) -> int:
        res = 0
        curr = float('-inf')
        
        while N > 0:
            if N & 1:
                res = max(res, curr + 1)
                curr = 0
            else:
                curr += 1
            N >>= 1
        
        return res

# Solution 2,
class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N)[2:]
        
        res = 0
        prev = float('inf')
        
        for i, c in enumerate(s):
            if c == '1':
                res = max(res, i - prev)
                prev = i
        
        return res