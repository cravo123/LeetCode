class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        
        target = n * n
        idx = 1
        
        i = j = 0
        di, dj = 0, 1
        
        while idx <= target:
            res[i][j] = idx
            
            x, y = i + di, j + dj
            
            # whenever we walk out of boundary or meet non-zero value
            # we need to change direction then
            if x < 0 or x >= n or y < 0 or y >= n or res[x][y] != 0:
                di, dj = dj, -di
            
            i, j = i + di, j + dj
            
            idx += 1
        
        return res