# Solution 1, Brute Force
class Solution:
    def dfs(self, idx, path, res, s, n, d):
        if idx == n:
            res.append(' '.join(path))
            return
        for i in range(idx + 1, n + 1):
            word = s[idx:i]
            if word in d:
                path.append(word)
                self.dfs(i, path, res, s, n, d)
                path.pop()
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = set(wordDict)
        
        path = []
        res = []
        
        n = len(s)
        
        self.dfs(0, path, res, s, n, d)
        
        return res

# Solution 2, memoization
class Solution:
    def dfs(self, idx, s, n, d, memo):
        if idx in memo:
            return memo[idx]
        
        if idx == 0:
            res = [[]]
        else:
            res = []
            for i in range(idx):
                word = s[i:idx]
                if word in d:
                    for pre in self.dfs(i, s, n, d, memo):
                        res.append(pre + [word])
        memo[idx] = res
        
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = set(wordDict)
        memo = {}
        
        n = len(s)
        
        self.dfs(n, s, n, d, memo)
        
        res = [' '.join(path) for path in memo[n]]
        
        return res