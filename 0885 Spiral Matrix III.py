class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        idx = 0
        target = R * C
        
        i, j = r0, c0
        steps = 1
        di, dj = 0, 1
        curr = 0 # number of walking steps in current direction
        dir_cnt = 0 # direction counter, need to change steps number every two direction changes

        
        while idx < target:
            #print(i, j)
            if 0 <= i < R and 0 <= j < C:
                idx += 1
                res.append([i, j])
            i += di
            j += dj
            curr += 1
            
            if curr == steps:
                di, dj = dj, -di
                curr = 0
                dir_cnt += 1
            
                if dir_cnt % 2 == 0:
                    steps += 1
        
        return res
            