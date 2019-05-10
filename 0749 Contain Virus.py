# By Chong Chen, https://github.com/cravo123/LeetCode

# Solution 1, brute-force simulation
# This problem is pure implementation if you know dfs well.
# Several got-cha, neighbors and walls are different, one neighbor 
# could have 2 walls like below
# 1  1
# 0  1

class Solution:
    def dfs(self, i, j, grid, m, n, t_areas, t_neighbors, t_walls, seen):
        seen.add((i, j))
        t_areas.add((i, j))
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if (x, y) in seen:
                continue
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                self.dfs(x, y, grid, m, n, t_areas, t_neighbors, t_walls, seen)
            elif 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                t_neighbors.add((x, y))
                t_walls[-1] += 1
            
    def find_infected_areas(self, grid, m, n):
        seen = set()
        idx = 0
        areas = {}
        neighbors = {}
        walls = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    t_areas = set()
                    t_neighbors = set()
                    t_walls = [0]
                    self.dfs(i, j, grid, m, n, t_areas, t_neighbors, t_walls, seen)
                    areas[idx] = t_areas
                    neighbors[idx] = t_neighbors
                    walls[idx] = t_walls[-1]
                    idx += 1
        
        return areas, neighbors, walls
    
    def fill(self, grid, m, n, areas, tag):
        for i, j in areas:
            grid[i][j] = tag
    
    def containVirus(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        res = 0
        while True:
            areas, neighbors, walls = self.find_infected_areas(grid, m, n)
            
            if not neighbors:
                return res
            
            neighbor_cnt = {idx:len(neighbors[idx]) for idx in neighbors}
            v = list(neighbor_cnt.values())
            k = list(neighbor_cnt.keys())
            idx = k[v.index(max(v))]
            
            res += walls[idx]
            
            self.fill(grid, m, n, areas[idx], -1)
            
            for i in neighbors:
                if i != idx:
                    self.fill(grid, m, n, neighbors[i], 1)