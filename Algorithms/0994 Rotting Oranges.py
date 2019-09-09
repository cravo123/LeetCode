import collections
# Solution 1, BFS, Breadth First Search is suitable for finding shortest path
class Solution:
    def bfs(self, q, grid, m, n):
        steps = 0
        while q:
            k = len(q)
            steps += 1
            for _ in range(k):
                i, j = q.popleft()
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == -1:
                        grid[x][y] = steps
                        q.append([x, y])
        
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        q = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                if grid[i][j] == 2:
                    q.append([i, j])
                    grid[i][j] = 0
        
        self.bfs(q, grid, m, n)
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    return -1
                res = max(res, grid[i][j])
        
        return res
                    
# Solution 2, Solution 1 is not elegant in a sense that we need to change
# input grid. Solution 2 doesn't change input grid.
class Solution:
    def collect_rotten_orange(self, grid, m, n):
        q = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
        return q
    
    def count_minutes(self, q, grid, m, n):
        curr = 0
         
        while q:
            tmp = []
            
            for i, j in q:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        tmp.append([x, y])
                        grid[x][y] = 2
            if not tmp:
                break
            q = tmp
            curr += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return curr
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        q = self.collect_rotten_orange(grid, m, n)
        
        res = self.count_minutes(q, grid, m, n)
        
        return res