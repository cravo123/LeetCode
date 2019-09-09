import collections

# Solution 1, BFS using hashset
class Solution:
    def bfs(self, ocean, matrix, m, n):
        q = collections.deque(ocean)
        
        while q:
            i, j = q.popleft()
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] >= matrix[i][j] and (x, y) not in ocean:
                    ocean.add((x, y))
                    q.append((x, y))
        
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        pacific = set()
        atlantic = set()
        
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n - 1))
        
        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m - 1, j))
        
        self.bfs(pacific, matrix, m, n)
        self.bfs(atlantic, matrix, m, n)
        
        res = pacific & atlantic
        
        res = [[val[0], val[1]] for val in res]
        
        return res

# Solution 2, create temp matrix to mark visited
class Solution:
    def dfs(self, i, j, matrix, ocean, m, n):
        ocean[i][j] = True
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and matrix[x][y] >= matrix[i][j] and not ocean[x][y]:
                self.dfs(x, y, matrix, ocean, m, n)
        
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        pacific = [[0 for _ in range(n)] for _ in range(m)]
        atlantic = [[0 for _ in range(n)] for _ in range(m)]
        
        for j in range(n):
            self.dfs(0, j, matrix, pacific, m, n)
            self.dfs(m - 1, j, matrix, atlantic, m, n)
            
        for i in range(m):
            self.dfs(i, 0, matrix, pacific, m, n)
            self.dfs(i, n - 1, matrix, atlantic, m, n)
        
        res = [[i, j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]
        
        return res