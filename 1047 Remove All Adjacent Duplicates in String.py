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