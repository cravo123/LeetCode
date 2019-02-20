class Solution:
    def imageSmoother(self, A: 'List[List[int]]') -> 'List[List[int]]':
        m, n = len(A), len(A[0]) if A else 0
        
        res = [row[::] for row in A]
        
        for i in range(m):
            for j in range(n):
                tmp = []
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n:
                            tmp.append(A[x][y])
                res[i][j] = sum(tmp) // len(tmp)
        return res