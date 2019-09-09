from heapq import heappush, heappop, heapify

# Solution 1, use Best-First-Search(priority queue) to find shortest path
# A good example to use priority queue to find shortest path
# It is Best-First-Search, and use priority queue as the "bag"
# We first push all points of the format (0, (i, j)) in one island to a priority.
# 0 means current steps, and (i, j) is the coordinates.
# Then run Best-First-Search to search shortest path.
class Solution(object):
    def dfs(self, i, j, A, m, n, tag, q):
        q.append([0, (i, j)])
        A[i][j] = tag
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                self.dfs(x, y, A, m, n, tag, q)
    
    def paint(self, A):
        m, n = len(A), len(A[0]) if A else 0
        tag = -1
        q = []
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(i, j, A, m, n, tag, q)
                    return q    
    
    def best_first_search(self, q, A, m, n):
        seen = set(x[1] for x in q)
        heapify(q)
        
        while q:
            curr, (i, j) = heappop(q)
            if A[i][j] == 1:
                break
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    seen.add((x, y))
                    heappush(q, [curr + 1, (x, y)])
        return curr - 1
    
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0]) if A else 0
        
        # paint island
        q = self.paint(A)
        
        return self.best_first_search(q, A, m, n)

# Soltuion 2, use Breadth-First-Search to find shortest path
# Breadth-First-Search could be one-end or double-end, similar to 
# LC 126 and 127
class Solution(object):
    def dfs(self, i, j, A, m, n, tag, q):
        q.append((i, j))
        A[i][j] = tag
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                self.dfs(x, y, A, m, n, tag, q)
    
    def paint(self, A):
        m, n = len(A), len(A[0]) if A else 0
        tag = -1
        q = []
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(i, j, A, m, n, tag, q)
                    return q    
    
    def breadth_first_search(self, q, A, m, n):
        seen = set(q)
        steps = 0
        while q:
            tmp = []
            
            for i, j in q:
                if A[i][j] == 1:
                    return steps - 1
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                        seen.add((x, y))
                        tmp.append((x, y))
            q = tmp
            steps += 1
    
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0]) if A else 0
        
        # paint island
        q = self.paint(A)
        
        return self.breadth_first_search(q, A, m, n)

# Solution 3, double-end Breadth-First-Search
class Solution(object):
    def dfs(self, i, j, A, m, n, tag, q):
        q.add((i, j))
        A[i][j] = tag
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                self.dfs(x, y, A, m, n, tag, q)
    
    def paint(self, A, tag):
        m, n = len(A), len(A[0]) if A else 0
        q = set()
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(i, j, A, m, n, tag, q)
                    return q    
    
    def de_bfs(self, left, right, A, m, n):
        steps = 0
        seen = left | right
        while left and right:
            tmp = set()
            
            for i, j in left:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if (x, y) in right:
                        return steps
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                        seen.add((x, y))
                        tmp.add((x, y))
            left, right = right, tmp
            steps += 1
    
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0]) if A else 0
        
        # paint island
        left = self.paint(A, 2)
        right = self.paint(A, 3)
        
        return self.de_bfs(left, right, A, m, n)