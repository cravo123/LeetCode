# Solution 1, DFS
class Solution:
    def dfs(self, s_i, s_j, e_i, e_j, cnt, grid, m, n):
        if (s_i, s_j) == (e_i, e_j):
            return cnt == 0
        res = 0
        c = grid[s_i][s_j]
        if c == -1:
            return res
        grid[s_i][s_j] = -1
        cnt -= 1
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = s_i + di, s_j + dj
            if 0 <= x < m and 0 <= y < n:
                res += self.dfs(x, y, e_i, e_j, cnt, grid, m, n)
        
        grid[s_i][s_j] = c
        cnt += 1
        
        return res
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s_i, s_j = i, j
                elif grid[i][j] == 2:
                    e_i, e_j = i, j
                elif grid[i][j] == 0:
                    cnt += 1
        
        return self.dfs(s_i, s_j, e_i, e_j, cnt + 1, grid, m, n) # need to count start point

# Solution 1.1, similar idea, but use global variable
class Solution:
    def dfs(self, s_i, s_j, e_i, e_j, cnt, grid, m, n):
        if (s_i, s_j) == (e_i, e_j):
            if cnt == 0:
                self.res += 1
            return
        
        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            x, y = s_i + di, s_j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                c = grid[x][y]
                if c == 0:
                    cnt -= 1
                grid[x][y] = -1
                self.dfs(x, y, e_i, e_j, cnt, grid, m, n)
                grid[x][y] = c
                if c == 0:
                    cnt += 1
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s_i, s_j = i, j
                elif grid[i][j] == 2:
                    e_i, e_j = i, j
                elif grid[i][j] == 0:
                    cnt += 1
        
        self.res = 0
        grid[s_i][s_j] = -1
        self.dfs(s_i, s_j, e_i, e_j, cnt, grid, m, n)
        
        return self.res