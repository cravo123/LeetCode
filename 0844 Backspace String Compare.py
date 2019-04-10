# Solution 1, O(n) space
class Solution:
    def change(self, s):
        q = []
        
        for c in s:
            if c == '#':
                if q:
                    q.pop()
            else:
                q.append(c)
        return q
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.change(S) == self.change(T)    

# Solution 2, O(1) space by moving from backwaard
