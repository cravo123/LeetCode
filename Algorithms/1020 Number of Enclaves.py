import collections

# Solution 1, BFS, breadth first search
# Actually there is a gotcha as to when to add points to seen set
# Most of the time, we want to avoid adding duplicate points to queue,
# so as soon as we add a point to a queue, we should add it to the seen,
# otherwise, we may add duplicate points to the queue
class Solution:
    def bfs(self, q, seen, A, m, n):        
        while q:
            i, j = q.popleft()
            A[i][j] = 0
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and A[x][y] == 1 and (x, y) not in seen:
                    q.append([x, y])
                    seen.add((x, y))

    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0]) if A else 0
        
        q = collections.deque()
        seen = set()
        for i in range(m):
            for j in [0, n - 1]:
                if A[i][j] == 1:
                    q.append([i, j])
                    seen.add((i, j))
                    
        for j in range(1, n - 1):
            for i in [0, m - 1]:
                if A[i][j] == 1:
                    q.append([i, j])
                    seen.add((i, j))
        
        self.bfs(q, seen, A, m, n)
        
        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if A[i][j] == 1:
                    res += 1
        
        return res

# Solution 1.1, mark matrix entry to be 0 when adding to queue, so that we don't need a "seen" set any more
class Solution:
    def collect_points(self, A, m, n):
        q = collections.deque()
        
        for i in range(m):
            for j in [0, n - 1]:
                if A[i][j] == 1:
                    q.append([i, j])
                    A[i][j] = 0
        
        for j in range(n):
            for i in [0, m - 1]:
                if A[i][j] == 1:
                    q.append([i, j])
                    A[i][j] = 0
        
        return q
    
    def bfs(self, q, A, m, n):
        while q:
            i, j = q.popleft()
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                    A[x][y] = 0
                    q.append([x, y])
    
    def count_ones(self, A, m, n):
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    cnt += 1
        
        return cnt
    
    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0]) if A else 0
        
        # collection boundary entries where values are 1
        q = self.collect_points(A, m, n)
        
        self.bfs(q, A, m, n)
        
        res = self.count_ones(A, m, n)
        
        return res


# Solution 2, DFS
class Solution:
    def dfs(self, i, j, A, m, n):
        A[i][j] = 0
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                self.dfs(x, y, A, m, n)

    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0]) if A else 0
        
        for j in range(n):
            if A[0][j] == 1:
                self.dfs(0, j, A, m, n)
            if A[m - 1][j] == 1:
                self.dfs(m - 1, j, A, m, n)
        
        for i in range(1, m - 1):
            if A[i][0] == 1:
                self.dfs(i, 0, A, m, n)
            if A[i][n - 1] == 1:
                self.dfs(i, n - 1, A, m, n)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    res += 1
        
        return res