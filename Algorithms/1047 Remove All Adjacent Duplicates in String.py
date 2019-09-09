# Solution 1, stack idea
class Solution:
    def removeDuplicates(self, S: str) -> str:
        q = []
        
        for c in S:
            if q and q[-1] == c:
                q.pop()
            else:
                q.append(c)
        
        res = ''.join(q)
        
        return res

# Solutio 1.1, same idea, but push to stack first
class Solution:
    def removeDuplicates(self, S: str) -> str:
        q = []
        
        for c in S:
            q.append(c)
            
            while len(q) > 1 and q[-1] == q[-2]:
                q.pop()
                q.pop()
        
        res = ''.join(q)
        
        return res