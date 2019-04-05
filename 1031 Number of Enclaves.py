import collections
# Solution 1, best-first-search
# Notice that we use a set as a "bag" here to collect points to be iterated
# We can use deque as well, but it may get TLE
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0]) if A else 0
        
        q = set()
        
        for j in range(n):
            if A[0][j] == 1:
                q.add((0, j))
            if A[m - 1][j] == 1:
                q.add((m - 1, j))
        
        for i in range(1, m - 1):
            if A[i][0] == 1:
                q.add((i, 0))
            if A[i][n - 1] == 1:
                q.add((i, n - 1))
        
        while q:
            i, j = q.pop()
            A[i][j] = 0
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                    q.add((x, y))
        
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    res += 1
        
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

# Solution 3, BFS, breadth first search
# Actually there is a gotcha as to when to add points to seen set
# Most of the time, we want to avoid adding duplicate points to queue,
# so as soon as we add a point to a queue, we should add it to the seen,
# otherwise, we may add duplicate points to the queue
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0]) if A else 0
        
        q = collections.deque()
        seen = set()
        
        for j in range(n):
            if A[0][j] == 1 and (0, j) not in seen:
                q.append([0, j])
                seen.add((0, j))
            if A[m - 1][j] == 1 and (m - 1, j) not in seen:
                q.append([m - 1, j])
                seen.add((m - 1, j))
        
        for i in range(1, m - 1):
            if A[i][0] == 1 and (i, 0) not in seen:
                q.append([i, 0])
                seen.add((i, 0))
            if A[i][n - 1] == 1 and (i, n - 1) not in seen:
                q.append([i, n - 1])
                seen.add((i, n - 1))
        
        while q:
            i, j = q.popleft()
            A[i][j] = 0
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and A[x][y] == 1 and (x, y) not in seen:
                    q.append([x, y])
                    seen.add((x, y))
        
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    res += 1
        
        return res