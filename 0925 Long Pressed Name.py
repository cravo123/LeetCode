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
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        j = 0
        
        for i, c in enumerate(typed):
            if j == n:
                if i > 0 and typed[i] != typed[i - 1]:
                    return False
            else:
                if typed[i] == name[j]:
                    j += 1
                elif i == 0 or typed[i] != typed[i - 1]:
                    return False
        return j == n
     
     def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)