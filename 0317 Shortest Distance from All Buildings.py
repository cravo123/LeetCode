import collections

# Move from buildings to empty land instead, 
# similar to LC 0417 Pacific Atlantic Water Flow

# Solution 1.1, BFS traversal
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        
        curr = []
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr.append((i, j, cnt)) # cnt as building tag
                    cnt += 1
        
        target = cnt
        seen = set(curr)
        steps = 1
        res = float('inf')
        d = {} # cache total distance for each building
        
        while curr:
            tmp = []
            
            for i, j, idx in curr:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y, idx) not in seen:
                        tmp.append((x, y, idx))
                        seen.add((x, y, idx))
                        if (x, y) not in d:
                            d[x, y] = [1, steps]
                        else:
                            d[x, y] = [d[x, y][0] + 1, d[x, y][1] + steps]
                        
                        if d[x, y][0] == target:
                            res = min(res, d[x, y][1])
            steps += 1
            curr = tmp
        return res if res < float('inf') else -1

# Solution 1.2, BFS traversal by iterating each building
# pruning in between, we only test those points which are 
# accessible for all buildings till now
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        cans = collections.Counter()
        buildings = []
        # gather buildinds and candidate empty cells
        m, n = len(grid), len(grid[0]) if grid else 0
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == 0:
                    cans[i, j] = 0
                elif c == 1:
                    buildings.append((i, j))
        
        res = float('inf')
        for i, j in buildings:
            # distance from current building
            dist = collections.Counter()
            q = collections.deque()
            q.append((i, j, 0))
            
            while q:
                i, j, steps = q.popleft()
                steps += 1
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if (0 <= x < m and 0 <= y < n and grid[x][y] == 0 
                        and (x, y) not in dist and (x, y) in cans):
                        dist[x, y] = steps
                        q.append((x, y, steps))
            
            # Filter out those empty cells which are not accessible from 
            # current building
            tmp = collections.Counter()
            for x, y in dist:
                if (x, y) not in cans:
                    continue
                tmp[x, y] = cans[x, y] + dist[x, y]
            cans = tmp
        
        for v in cans.values():
            res = min(res, v)
        
        return res if res < float('inf') else -1