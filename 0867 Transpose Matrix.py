# Solution 1, simulation
class Solution:
    def transpose(self, A: 'List[List[int]]') -> 'List[List[int]]':
        m, n = len(A), len(A[0]) if A else 0
        
        res = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                res[j][i] = A[i][j]
        
        return res

# Solution 1.1, Python 1-line
class Solution:
    def transpose(self, A: 'List[List[int]]') -> 'List[List[int]]':
        return list(zip(*A))