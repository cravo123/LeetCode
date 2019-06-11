# Solution 1, simulation
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        
        i = j = 0
        di, dj = 0, 1
        
        obstacles = set((x, y) for x, y in obstacles)
        
        for c in commands:
            if c == -1:
                di, dj = dj, -di
            elif c == -2:
                di, dj = -dj, di
            else:
                for _ in range(c):
                    if (i + di, j + dj) in obstacles:
                        break
                    i += di
                    j += dj
                res = max(res, i * i + j * j)
        
        return res