class Solution:
    def simplifyPath(self, path: str) -> str:
        q = ['']
        
        path = path.split('/')
        
        for v in path:
            if v == '..':
                if q and q[-1]:
                    q.pop()
            elif v in [ '', '.', '/']:
                continue
            else:
                q.append(v)
        
        res = '/'.join(q)
        
        return res or '/'