# Solution 1, back-tracking
# Similar to LC 1087 Brace Expansion
class Solution:
    def dfs(self, idx, digits, path, res, d):
        if idx == len(digits):
            if path:
                res.append(''.join(path))
            return
        
        v = int(digits[idx])
        
        for c in d[v]:
            path.append(c)
            self.dfs(idx + 1, digits, path, res, d)
            path.pop()
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        d = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        path = []
        res = []
        
        self.dfs(0, digits, path, res, d)
        
        return res

# Solution 2, similar idea but with iteration BFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        res = [[]]
        
        for v in digits:
            v = int(v)
            res = [path + [c] for path in res for c in d[v]]
        
        res = [''.join(path) for path in res if path]
        
        return res