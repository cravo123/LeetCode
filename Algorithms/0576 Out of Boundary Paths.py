# Solution 1, DP
# Idea is pretty similar to LC 0935
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if not (0 <= i < m and 0 <= j < n):
            return 0
        
        BASE = int(1e9) + 7
        res = 0
        curr = [[0 for _ in range(n)] for _ in range(m)]
        
        curr[i][j] = 1
        
        for _ in range(N):
            tmp = [[0 for _ in range(n)] for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if curr[i][j] > 0:
                        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            x, y = i + di, j + dj
                            if 0 <= x < m and 0 <= y < n:
                                tmp[x][y] += curr[i][j]
                            else:
                                res += curr[i][j]
                    res %= BASE
            curr = tmp
        return res % BASE