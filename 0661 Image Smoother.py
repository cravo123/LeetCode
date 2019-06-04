# Solution 1, simulation
class Solution:
    def average(self, i, j, M, m, n):
        cnt = curr = 0
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n:
                    cnt += 1
                    curr += M[x][y]
        return curr // cnt
        
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0]) if M else 0
        
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                res[i][j] = self.average(i, j, M, m, n)
        
        return res