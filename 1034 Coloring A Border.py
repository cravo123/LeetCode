# Solution 1, find component and border at the same time
class Solution:
    def dfs(self, i, j, grid, m, n, old_color, seen, border):
        seen.add((i, j))
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == old_color:
                if (x, y) not in seen:
                    self.dfs(x, y, grid, m, n, old_color, seen, border)
            else:
                border.add((i, j))
        
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        seen = set()
        border = set()
        
        self.dfs(r0, c0, grid, m, n, grid[r0][c0], seen, border)
        
        for i, j in border:
            grid[i][j] = color
        
        return grid