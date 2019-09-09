# Solution 1, DFS
class Solution:
    def dfs(self, i, j, grid, m, n):
        res = 0
        grid[i][j] = 2 # visited
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                res += 1
            elif grid[x][y] == 1:
                res += self.dfs(x, y, grid, m, n)
        return res
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += self.dfs(i, j, grid, m, n)
        
        return res

# Solution 2, mathematical solution
# Check number of islands and number of neighbors
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        islands = neighbors = 0
        
        m, n = len(grid), len(grid[0]) if grid else 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands += 1
                    
                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            neighbors += 1
        return islands * 4 - neighbors

# Solution 2.1, a better mathematical solution
# Only check right and down neighbors
# res = islands * 4 - neighbors * 2
# The reason why we multiply 2 for neighbors is because we only check right and down neighbors
# Say we have cell A be 1, and its right neighbor B is also 1
# We time 2 in order to take into consideration edge between A and B when we check cell B
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        islands = neighbors = 0
        
        m, n = len(grid), len(grid[0]) if grid else 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands += 1
                    
                    for di, dj in [[1, 0], [0, 1]]:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            neighbors += 1
        return islands * 4 - neighbors * 2