# Solution 1, back-tracking
class Solution:
    def dfs(self, idx, s, path, res):
        if idx == len(s) or len(path) == 4:
            if idx == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
        
        for x in range(1, min(4, len(s) - idx + 1)):
            v = s[idx:(idx + x)]
            if len(v) > 1 and v[0] == '0':
                continue
            if not 0 <= int(v) <= 255:
                return
            path.append(v)
            self.dfs(idx + x, s, path, res)
            path.pop()
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not 4 <= len(s) <= 12:
            return []
        path = []
        res = []
        
        self.dfs(0, s, path, res)
        
        return res
