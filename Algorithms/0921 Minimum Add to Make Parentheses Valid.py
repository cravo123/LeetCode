# Solution 1, greedy, O(n)
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        cnt = 0
        res = 0
        
        for c in S:
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            
            if cnt < 0:
                res += 1
                cnt = 0
        
        return res + cnt