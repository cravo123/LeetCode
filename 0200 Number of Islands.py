# Solution 1, DFS
class Solution:
    def dfs(self,i, j, grid, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            self.dfs(x, y, grid, m, n)
        return 1
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                res += self.dfs(i, j, grid, m, n)
        
        return res

# Solution 2, BFS
class Solution:
    def bfs(self,i, j, grid, m, n):
        q = set([(i, j)])
        
        while q:
            tmp = set()
            for i, j in q:
                grid[i][j] = '0'
        
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        tmp.add((x, y))
                        # the reason we use set here is because if we use list, then we might add
                        # many duplicate points to tmp
            q = tmp
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.bfs(i, j, grid, m, n)
        return res