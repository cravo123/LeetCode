import collections

# Solution 1, DFS with memoization
class Solution:
    def dfs(self, curr, target, d, seen, maze, m, n):
        if curr == target:
            return True
        if curr in seen:
            return False
        
        seen.add(curr)
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            i, j = curr
            
            while 0 <= i + di < m and 0 <= j + dj < n and maze[i + di][j + dj] == 0:
                i += di
                j += dj
            
            if self.dfs((i, j), target, d, seen, maze, m, n):
                d[curr] = True
                return True
        d[curr] = False
        return False
        
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0]) if maze else 0
        
        d = {}
        seen = set()
        
        start, target = map(tuple, (start, destination))
        
        return self.dfs(start, target, d, seen, maze, m, n)

# Solution 2, BFS
class Solution:
    def bfs(self, start, target, maze, m, n):
        curr = collections.deque([start])
        seen = set(start)
        
        while curr:
            p = curr.popleft()
            
            if p == target:
                return True
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                i, j = p
                
                while 0 <= i + di < m and 0 <= j + dj < n and maze[i + di][j + dj] == 0:
                    i += di
                    j += dj
                if (i, j) not in seen:
                    seen.add((i, j))
                    curr.append((i, j))
        
        return False
        
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0]) if maze else 0
        
        start, target = map(tuple, (start, destination))
        
        return self.bfs(start, target, maze, m, n)