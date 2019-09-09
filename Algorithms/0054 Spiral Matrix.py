# Solution 1, simulation
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        res = []
        
        r_start, r_end = 0, m - 1
        c_start, c_end = 0, n - 1
        
        while r_start <= r_end and c_start <= c_end:
            # move right
            for j in range(c_start, c_end + 1):
                res.append(matrix[r_start][j])
            r_start += 1
            if r_start > r_end:
                break
            
            # move down
            for i in range(r_start, r_end + 1):
                res.append(matrix[i][c_end])
            c_end -= 1
            if c_start > c_end:
                break
            
            # move left
            for j in range(c_end, c_start - 1, -1):
                res.append(matrix[r_end][j])
            r_end -= 1
            if r_start > r_end:
                break
            
            # move up
            for i in range(r_end, r_start - 1, -1):
                res.append(matrix[i][c_start])
            c_start += 1
            if c_start > r_end:
                break
        
        return res

# Solution 2, using seen matrix as delimitors
# t.b.c
