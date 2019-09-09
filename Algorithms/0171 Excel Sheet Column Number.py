# Solution 1, simulation
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        
        for c in s:
            # there is no zero in Excel column, so we need to add 1 here
            res = res * 26 + ord(c) - ord('A') + 1
            
        return res