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