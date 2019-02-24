class Solution:
    def dfs(self, curr_x, curr_y, end_x, end_y, grid, m, n, total):
        if curr_x == end_x and curr_y == end_y:
            return 1 if total == 0 else 0
        c = grid[curr_x][curr_y]
        grid[curr_x][curr_y] = -1
        
        if c == 0:
            total -= 1
        res = 0
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            i, j = curr_x + dx, curr_y + dy
            if 0 <= i < m and 0 <= j < n and grid[i][j] != -1:
                res += self.dfs(i, j, end_x, end_y, grid, m, n, total)
        
        grid[curr_x][curr_y] = c
        
        return res
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        # Find start and end
        total = 0
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == 1:
                    start_x, start_y = i, j
                elif c == 2:
                    end_x, end_y = i, j
                elif c == 0:
                    total += 1
        res = self.dfs(start_x, start_y, end_x, end_y, grid, m, n, total)
        
        return res
        