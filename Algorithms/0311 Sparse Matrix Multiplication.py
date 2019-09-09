import collections

# Solution 1, simulation, hashmap
class Solution:
    def build_dict(self, matrix, m, n):
        d = collections.defaultdict(lambda: collections.defaultdict(int))
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    d[i][j] = matrix[i][j]
        
        return d
        
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0]) if A else 0
        p = len(B[0]) if B else 0
        
        a_d = self.build_dict(A, m, n) # d[row][col]
        b_d = self.build_dict(list(zip(*B)), p, n) # d[col][row]
        
        res = [[0 for _ in range(p)] for _ in range(m)]
        
        for i in a_d:
            for j in b_d:
                for k in a_d[i]:
                    res[i][j] += a_d[i][k] * b_d[j][k]
        return res