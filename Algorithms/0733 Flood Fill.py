import collections

# Solution 1, DFS
# If oldColor is the same as newColor, then there is no need
# to do dfs, we can just return
class Solution:
    def dfs(self, i, j, image, m, n, oldColor, newColor):
        image[i][j] = newColor
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and image[x][y] == oldColor:
                self.dfs(x, y, image, m, n, oldColor, newColor)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0]) if image else 0
        oldColor = image[sr][sc]
        
        if oldColor == newColor:
            return image
        
        self.dfs(sr, sc, image, m, n, oldColor, newColor)
        
        return image

# Solution 2, BFS
# Different traversing techniques only diff in bagging.
# Depth-First-Search, stack
# Breadth-First-Search, deque
# Best-First-Search, priority queue (Dijkstra Algorithm)
class Solution:
    def bfs(self, i, j, image, m, n, oldColor, newColor):
        q = collections.deque()
        q.append([i, j])
        image[i][j] = newColor
        
        while q:
            i, j = q.popleft()
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and image[x][y] == oldColor:
                    image[x][y] = newColor
                    q.append([x, y])
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0]) if image else 0
        oldColor = image[sr][sc]
        
        if oldColor == newColor:
            return image
        
        self.bfs(sr, sc, image, m, n, oldColor, newColor)
        
        return image