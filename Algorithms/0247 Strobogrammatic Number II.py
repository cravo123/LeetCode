# Solution 1, typical back-tracking
class Solution:
    def dfs(self, idx, path, res, d):
        n = len(path)
        if idx >= (n - 1) // 2 + 1:
            res.append(''.join(path))
            return
        
        if n % 2 == 1 and idx == n // 2:
            for v in ['0', '1', '8']:
                path[idx] = v
                self.dfs(idx + 1, path, res, d)
                path[idx] = ''
        else:
            for v in d:
                # cannot have leading '0'
                if idx == 0 and v == '0':
                    continue
                path[idx] = v
                path[n - 1 - idx] = d[v]
                self.dfs(idx + 1, path, res, d)
                path[idx] = ''
                path[n - 1 - idx] = ''
        
    def findStrobogrammatic(self, n: int) -> List[str]:
        d = {}
        d['0'] = '0'
        d['1'] = '1'
        d['6'] = '9'
        d['8'] = '8'
        d['9'] = '6'
        
        res = []
        path = ['' for _ in range(n)]
        
        self.dfs(0, path, res, d)
        
        return res

# Solution 2, recursion
# t.b.c