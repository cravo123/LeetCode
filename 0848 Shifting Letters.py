# Solution 1, moving backward, suffix sum
class Solution(object):
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        S = list(S)
        
        n = len(S)
        
        curr = 0
        for i in range(n - 1, -1, -1):
            curr = curr + shifts[i]
            S[i] = chr((ord(S[i]) + curr - ord('a')) % 26 + ord('a'))
        
        res = ''.join(S)
        
        return res

# Solution 2, moving forward
class Solution:
    def generate(self, c, move):
        x = chr((ord(c) + move - ord('a')) % 26 + ord('a'))
        return x
        
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        curr = sum(shifts) % 26
        
        q = []
        
        for c, v in zip(S, shifts):
            q.append(self.generate(c, curr))
            curr = (curr - v) % 26
        
        res = ''.join(q)
        
        return res