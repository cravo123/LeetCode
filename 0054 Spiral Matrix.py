class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        res = []
        
        r_start, r_end = 0, m - 1
        c_start, c_end = 0, n - 1
        
        while r_start <= r_end and c_start <= c_end:
            for j in range(c_start, c_end + 1):
                res.append(matrix[r_start][j])
            r_start += 1
            if r_start > r_end:
                break
            
            for i in range(r_start, r_end + 1):
                res.append(matrix[i][c_end])
            c_end -= 1
            if c_start > c_end:
                break
            
            for j in range(c_end, c_start - 1, -1):
                res.append(matrix[r_end][j])
            r_end -= 1
            if r_start > r_end:
                break
            
            for i in range(r_end, r_start - 1, -1):
                res.append(matrix[i][c_start])
            c_start += 1
            if c_start > r_end:
                break
        
        return res