# Solution 1, vanilla dfs, TLE because we didn't memoization
class Solution:
    def dfs(self, i, j, di, dj, M, m, n):
        if M[i][j] == 0:
            return 0
        
        curr = 1
        x, y = i + di, j + dj
        if 0 <= x < m and 0 <= y < n:
            curr += self.dfs(x, y, di, dj, M, m, n)
        
        return curr
        
    def longestLine(self, M: List[List[int]]) -> int:
        res = 0
        m, n = len(M), len(M[0]) if M else 0
        
        for i in range(m):
            for j in range(n):
                for di, dj in [[1, 0], [0, 1], [1, 1], [1, -1]]:
                    res = max(res, self.dfs(i, j, di, dj, M, m, n))
        
        return res

# Solution 2, memoization, essentially top-down dp
class Solution:
    def dfs(self, i, j, di, dj, M, m, n, d):
        if (i, j, di, dj) in d:
            return d[(i, j, di, dj)]
        if M[i][j] == 0:
            return 0
        
        curr = 1
        x, y = i + di, j + dj
        if 0 <= x < m and 0 <= y < n:
            curr += self.dfs(x, y, di, dj, M, m, n, d)
        
        d[(i, j, di, dj)] = curr
        return curr
        
    def longestLine(self, M: List[List[int]]) -> int:
        res = 0
        m, n = len(M), len(M[0]) if M else 0
        d = {}
        for i in range(m):
            for j in range(n):
                for di, dj in [[1, 0], [0, 1], [1, 1], [1, -1]]:
                    res = max(res, self.dfs(i, j, di, dj, M, m, n, d))
        
        return res

# Solution 3, bottom-up dp
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        res = 0
        m, n = len(M), len(M[0]) if M else 0
        
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                for idx, (di, dj) in enumerate([[-1, 0], [0, -1], [-1, -1], [-1, 1]]):
                    if M[i][j] == 1:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n: 
                            dp[i][j][idx] = 1 + dp[x][y][idx]
                        else:
                            dp[i][j][idx] = 1
                        
                        res = max(res, dp[i][j][idx])
        
        return res