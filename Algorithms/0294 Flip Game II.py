# Memoization
class Solution:
    def dfs(self, s, d):
        if s in d:
            return d[s]
        
        res = False
        for i in range(len(s) - 1):
            if s[i:(i + 2)] == '++':
                ns = s[:i] + '--' + s[(i + 2):]
                if not self.dfs(ns, d):
                    res = True
                    break
        d[s] = res
        
        return res
        
    def canWin(self, s: str) -> bool:
        d = {}
        
        return self.dfs(s, d)