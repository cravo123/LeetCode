# Solution 1, need to consider the case 'a' and 'ab'
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, n = 0, len(typed)
        
        for c in name:
            if i >= n:
                return False
            if typed[i] == c:
                i += 1
            elif i == 0:
                return False
            else:
                while i < n and typed[i] == typed[i - 1]:
                    i += 1
                if i == n or typed[i] != c:
                    return False
                i += 1
        
        while i < n and typed[i] == typed[i - 1]:
            i += 1
        return i == n

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

# Solution 3
class Solution:
     def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)

# Solution 4, group by
# t.b.c