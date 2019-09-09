# Solution 1, back-tracking
# template problem as LC 0039 combination sum
# moving index forward
class Solution:
    def dfs(self, idx, S, path, res):
        if idx == len(S):
            res.append(path[::])
            return
        if S[idx].isalpha():
            cans = [S[idx].lower(), S[idx].upper()]
        else:
            cans = [S[idx]]
        
        for c in cans:
            path.append(c)
            self.dfs(idx + 1, S, path, res)
            path.pop()

        
    def letterCasePermutation(self, S: str) -> List[str]:
        S = list(S)
        path = []
        res = []
        
        self.dfs(0, S, path, res)
        
        res = [''.join(path) for path in res]
        
        return res

# Solution 2, recursion
# moving index backward
# self.dfs(idx, S) is the result of all the combination for S[idx:]
class Solution:
    def dfs(self, idx, S):
        if idx == len(S):
            return ['']
        
        res = []
        if S[idx].isalpha():
            cans = [S[idx].lower(), S[idx].upper()]
        else:
            cans = [S[idx]]
        
        for c in cans:
            for path in self.dfs(idx + 1, S):
                res.append(c + path)
        
        return res
        
    def letterCasePermutation(self, S: str) -> List[str]:
        
        return self.dfs(0, S)