# Cache to reduce running time
# The reason we can cache is because it is an increasing path
class Solution:
    def dfs(self, i, j, matrix, m, n, d):
        if (i, j) in d:
            return d[(i, j)]
        v = matrix[i][j]
        matrix[i][j] = '#'
        curr = 0
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and matrix[x][y] != '#' and matrix[x][y] > v:
                curr = max(curr, self.dfs(x, y, matrix, m, n, d))
        curr += 1
        matrix[i][j] = v
        d[(i, j)] = curr
        return curr
            
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        res = 0
        d = {}
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(i, j, matrix, m, n, d))
        
        return res