# Solution 1, DFS
class Solution:
    def dfs(self, i, j, grid, m, n):
        grid[i][j] = '0'
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                self.dfs(x, y, grid, m, n)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0]) if grid else 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(i, j, grid, m, n)
        
        return cnt

# Solution 2, BFS
class Solution:
    def bfs(self,i, j, grid, m, n):
        q = [[i, j]]
        grid[i][j] = '0'
        
        while q:
            tmp = []
            for i, j in q:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        tmp.append([x, y])
                        grid[x][y] = '0' # mark it is visited
            q = tmp
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.bfs(i, j, grid, m, n)
        return cnt