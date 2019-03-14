import collections

class Solution:
    def build_dict(self, matrix):
        d = collections.defaultdict(dict)
        
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    d[i][j] = matrix[i][j]
        
        return d
        
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        da, db = self.build_dict(A), self.build_dict(list(zip(*B)))
        
        m = len(A)
        n = len(B[0])
        
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                for col in da[i]:
                    if col in db[j]:
                        res[i][j] += da[i][col] * db[j][col]
        return res