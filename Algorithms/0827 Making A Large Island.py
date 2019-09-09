class Solution(object):
    def dfs(self, i, j, grid, m, n, idx):
        res = 1
        grid[i][j] = idx
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                res += self.dfs(x, y, grid, m, n, idx)
        
        return res
        
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0
        d = {0:0}
        idx = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Mark and calc block area
                    d[idx] = self.dfs(i, j, grid, m, n, idx)
                    idx += 1
        
        res = max(d.values())
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grps = set()
                    
                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n and grid[x][y] > 1:
                            grps.add(grid[x][y])
                    curr = 0
                    for v in grps:
                        curr += d[v]
                    res = max(res, curr + 1)
        
        return res