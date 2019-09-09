import heapq

# Solution 1, BFS implemented with priority queue
# Similar idea to The Maze I and II(LC 505, 490)
# Actually adding distance-cache d makes run-time better,
# but it also makes implementation more complext, since now
# the condition to add heapq is 
#   node is not visited
#   or new steps are less than previous steps
#   or new steps equal to previous steps but direction order is 
#   lexicographically smaller.
class Solution:
    def next_move(self, i, j, di, dj, maze, m, n, hole):
        t = 0
        while True:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n:
                if x == hole[0] and y == hole[1]:
                    return t + 1, x, y
                if maze[x][y] == 0:
                    i, j = x, y
                    t += 1
                else:
                    return t, i, j
            else:
                return t, i, j 
        
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0]) if maze else 0
        
        if hole[0] < 0 or hole[0] >= m or hole[1] < 0 or hole[1] >= n or maze[hole[0]][hole[1]] == 1:
            return 'impossible'
        
        ks = 'udlr' # direction
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = [[0, '', ball[0], ball[1]]]
        d = {}
        
        while q:
            step, curr, i, j = heapq.heappop(q)
            if (i, j) == (hole[0], hole[1]):
                return curr
            
            d[i, j] = [step, curr]
            
            for k, (di, dj) in enumerate(dirs):
                t, x, y = self.next_move(i, j, di, dj, maze, m, n, hole)
                
                if(x, y) not in d or t + step < d[x, y][0] or (t + step == d[x, y][0] and curr + ks[k] < d[x, y][1]):
                    heapq.heappush(q, [t + step, curr + ks[k], x, y])
                    d[x, y] = [t + step, curr + ks[k]]
        return 'impossible'