# Solution 1, stack
class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        q = []
        
        for c in s:
            if c not in d:
                q.append(c)
            elif not q or d[c] != q[-1]:
                return False
            else:
                q.pop()
        return len(q) == 0