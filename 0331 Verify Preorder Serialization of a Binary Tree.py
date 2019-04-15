class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        q = []
        s = preorder.split(',')
        
        for c in s:
            q.append(c)
            
            while len(q) > 2 and q[-1] == '#' and q[-2] == '#':
                q.pop()
                q.pop()
                if q.pop() == '#':
                    return False
                q.append('#')
        
        return len(q) == 1 and q[0] == '#'