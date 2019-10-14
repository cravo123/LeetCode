# Solution 1, greedy
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        curr = 0
        
        for c in s:
            if c == 'L':
                curr += 1
            else:
                curr -= 1
            
            if curr == 0:
                res += 1
        
        return res