# Solution 1, back-tracking
class Solution:
    def dfs(self, idx, s, path, res):
        if idx == len(s):
            res.append(path[::])
            return
        
        for k in range(1, len(s) - idx + 1):
            v = s[idx:(idx + k)]
            if v == v[::-1]:
                path.append(v)
                self.dfs(idx + k, s, path, res)
                path.pop()
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path = []
        res = []
        
        self.dfs(0, s, path, res)
        
        return res

# Solution 2, memoization
class Solution:
    def dfs(self, idx, s, d):
        if idx in d:
            return d[idx]
        if idx == len(s):
            d[idx] = [[]]
            return d[idx]
        
        res = []
        for k in range(1, len(s) - idx + 1):
            v = s[idx:(idx + k)]
            if v == v[::-1]:
                for x in self.dfs(idx + k, s, d):
                    res.append([v] + x)
        d[idx] = res
        return res
        
    def partition(self, s: str) -> List[List[str]]:
        d = {}
        
        self.dfs(0, s, d)
        
        return d[0]