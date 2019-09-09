# Solution 1, stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        q = []
        
        for name in path:
            if name == '' or name == '.':
                continue
            if name == '..':
                if q:
                    q.pop()
            else:
                q.append(name)
        
        res = '/' + '/'.join(q) # Add root dir '/', gotcha
        
        return res