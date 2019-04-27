# Solution 1, DP O(m * n) memory
class Node:
    def __init__(self):
        self.left = self.right = self.up = self.down = 0

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        dp = [[Node() for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                dp[i][j].left = dp[i][j - 1].left if j > 0 else 0
                dp[i][j].up = dp[i - 1][j].up if i > 0 else 0
                if grid[i][j] == 'E':
                    dp[i][j].left += 1
                    dp[i][j].up += 1
        
        res = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 'W':
                    continue
                dp[i][j].right = dp[i][j + 1].right if j < n - 1 else 0
                dp[i][j].down = dp[i + 1][j].down if i < m - 1 else 0
                
                if grid[i][j] == 'E':
                    dp[i][j].right += 1
                    dp[i][j].down += 1
                else:
                    res = max(res, sum([dp[i][j].left, dp[i][j].right, dp[i][j].up, dp[i][j].down]))
        return res

# Solution 2, DP, O(n) memory

# Solution 3, Brute-Force
class Solution:
    def calc(self, i, j, di, dj, grid, m, n):
        res = 0
        if di == 1:
            x = i - 1
            while x >= 0 and grid[x][j] != 'W':
                if grid[x][j] == 'E':
                    res += 1
                x -= 1
            x = i + 1
            while x < m and grid[x][j] != 'W':
                if grid[x][j] == 'E':
                    res += 1
                x += 1
        else:
            y = j - 1
            while y >= 0 and grid[i][y] != 'W':
                if grid[i][y] == 'E':
                    res += 1
                y -= 1
            y = j + 1
            while y < n and grid[i][y] != 'W':
                if grid[i][y] == 'E':
                    res += 1
                y += 1
        
        return res
            
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    row = self.calc(i, j, 1, 0, grid, m, n)
                    col = self.calc(i, j, 0, 1, grid, m, n)
                    res = max(res, row + col)
        return res