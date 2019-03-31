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