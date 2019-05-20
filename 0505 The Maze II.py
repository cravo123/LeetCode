import heapq

# Solution 1, BFS implemented with priority queue
# But it still entails some duplicate nodes in heapq
class Solution:
    def next_steps(self, i, j, di, dj, maze, m, n):
        steps = 0
        while True:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                i, j = x, y
                steps += 1
            else:
                return i, j, steps
        
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0]) if maze else 0
        q = [[0, start[0], start[1]]]
        seen = set()
        
        while q:
            steps, i, j = heapq.heappop(q)
            seen.add((i, j))
            if (i, j) == (destination[0], destination[1]):
                return steps
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y, t = self.next_steps(i, j, di, dj, maze, m, n)
                if (x, y) not in seen:
                    heapq.heappush(q, [t + steps, x, y])
        
        return -1

# Solution 2, BFS with priority queue
# Rememer shortest distance so far
class Solution:
    def next_steps(self, i, j, di, dj, maze, m, n):
        steps = 0
        while True:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                i, j = x, y
                steps += 1
            else:
                return i, j, steps
        
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0]) if maze else 0
        q = [[0, start[0], start[1]]]
        d = {}
        d[start[0], start[1]] = 0
        
        while q:
            steps, i, j = heapq.heappop(q)
            if (i, j) == (destination[0], destination[1]):
                return steps
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y, t = self.next_steps(i, j, di, dj, maze, m, n)
                if (x, y) not in d or t + steps < d[x, y]:
                    heapq.heappush(q, [t + steps, x, y])
                    d[x, y] = t + steps
        
        return -1