# Solution 1, Top-down DP
class Solution:
    def dfs(self, a, b, d):
        if (a, b) in d:
            return d[a, b]
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0
        
        res = 0.25 * ((self.dfs(a - 4, b, d) + self.dfs(a - 3, b - 1, d) 
                       + self.dfs(a - 2, b - 2, d) + self.dfs(a - 1, b - 3, d)))
        d[a, b] = res
        return res
        
    def soupServings(self, N: int) -> float:
        if N >= 5000:
            return 1
        N = (N - 1) // 25 + 1
        
        d = {}
        
        return self.dfs(N, N, d)