# Solution 1, simulation
class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        cnt = 0
        curr = None
        
        for c in s:
            if c == curr:
                cnt += 1
            else:
                curr = c
                cnt = 1
            res = max(res, cnt)
        
        return res