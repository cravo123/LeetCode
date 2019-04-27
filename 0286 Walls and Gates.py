# Solution 1, Breadth-First-Search
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0]) if rooms else 0
        
        q = []
        seen = set()
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i, j])
                    seen.add((i, j))
        
        steps = 1
        while q:
            tmp = []
            
            for i, j in q:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen and rooms[x][y] > steps:
                        rooms[x][y] = steps
                        tmp.append([x, y])
                        seen.add((x, y))
            q = tmp
            steps += 1

# Solution 1.1, no need to maintain seen set
# Since we can use distance to mark nodes we have visited
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0]) if rooms else 0
        
        q = []
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i, j])
        
        steps = 1
        while q:
            tmp = []
            
            for i, j in q:
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] > steps:
                        rooms[x][y] = steps
                        tmp.append([x, y])
            q = tmp
            steps += 1