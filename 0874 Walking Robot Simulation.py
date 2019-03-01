class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        obs = set(tuple(x) for x in obstacles)
        
        i, j = 0, 0
        di, dj = 0, 1
        
        for c in commands:
            if c == -2:
                di, dj = -dj, di
            elif c == -1:
                di, dj = dj, -di
            else:
                while c > 0 and (i + di, j + dj) not in obs:
                    i += di
                    j += dj
                    c -= 1
                    res = max(res, i * i + j * j)
        
        return res