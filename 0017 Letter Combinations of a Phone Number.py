class Solution:
    def dfs(self, idx, digits, path, res, d):
        if idx == len(digits):
            if path:
                res.append(''.join(path))
            return
        
        for c in d[digits[idx]]:
            path.append(c)
            self.dfs(idx + 1, digits, path, res, d)
            path.pop()
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        path = []
        res = []
        
        self.dfs(0, digits, path, res, d)
        
        return res