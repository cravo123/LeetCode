# Solution 1, need to consider the case 'a' and 'ab'
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        n = len(typed)
        
        for c in name:
            while i < n and typed[i] != c:
                i += 1
            if i >= n:
                return False
            i += 1
        
        while 0 < i < n and typed[i] == typed[i - 1]:
            i += 1
        
        return True

# Solution 2
