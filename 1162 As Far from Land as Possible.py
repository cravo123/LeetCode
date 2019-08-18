# Solution 1, BFS
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        # collect lands
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                
        # BFS from lands
        level = 1
        res = -1
        
        while q:
            tmp = []
            for i, j in q:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                        res = max(res, level)
                        grid[x][y] = level
                        tmp.append((x, y))
            q = tmp
            level += 1
        return res