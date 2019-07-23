import collections

# Solution 1, real BFS, breadth-first-search
# Collect all 0-value points, and do BFS
class Solution:
    def bfs(self, matrix, m, n):
        q = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
        
        while q:
            i, j = q.popleft()
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j] + 1:
                    matrix[x][y] = matrix[i][j] + 1
                    q.append((x, y))

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = float('inf')
        
        self.bfs(matrix, m, n)
        
        return matrix

# Solution 1.1, real Breadth-First-Search, level traversal
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        q = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append([i, j])
                else:
                    matrix[i][j] = -1
        
        steps = 1
        
        while q:
            tmp = []
            
            for i, j in q:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] == -1:
                        matrix[x][y] = steps
                        tmp.append([x, y])
            q = tmp
            steps += 1
        
        return matrix

# Solution 1.2, more elegant solution
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        q = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append([i, j])
                else:
                    matrix[i][j] = -1
        
        steps = 1
        
        while q:
            i, j = q.popleft()            
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] == -1:
                    matrix[x][y] = matrix[i][j] + 1
                    q.append([x, y])
        
        return matrix

# Solution 2, Best-First-Search, here use set as the 'bag'
class Solution:
    def bfs(self, matrix, m, n):
        q = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.add((i, j))
        
        while q:
            i, j = q.pop()
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j] + 1:
                    matrix[x][y] = matrix[i][j] + 1
                    q.add((x, y))

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = float('inf')
        
        self.bfs(matrix, m, n)
        
        return matrix
