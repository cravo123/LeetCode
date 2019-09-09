# Solution 1, simulation
class Solution:
    def countLetters(self, S: str) -> int:
        cnt = 0
        curr = None
        res = 0
        
        for c in S:
            if c != curr:
                curr = c
                cnt = 0
            cnt += 1
            res += cnt
        
        return res