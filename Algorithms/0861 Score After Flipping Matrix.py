# Solution 1
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0]) if A else 0
        
        v = int(2 ** (n - 1))
        res = m * v
        v //= 2
        
        for j in range(1, n):
            zeros = ones = 0
            for i in range(m):
                if A[i][j] == 1:
                    if A[i][j] == A[i][0]:
                        ones += 1
                    else:
                        zeros += 1
                else:
                    if A[i][j] == A[i][0]:
                        ones += 1
                    else:
                        zeros += 1
            res += max(ones, zeros) * v
            v //= 2
        
        return res

# Solution 2, According to Solution 1
# This can be simplified to below logic.
# if A[i][j] == A[i][0], then it will become 1 after toggling row i to make A[i][0] become 1
# if A[i][j] != A[i][0], it will become 0.
# We can then flip column j to maximize scores
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0]) if A else 0
        
        v = int(2 ** (n - 1))
        res = 0
        
        for j in range(n):
            zeros = ones = 0
            for i in range(m):
                if A[i][j] == A[i][0]:
                    ones += 1
                else:
                    zeros += 1
            res += max(ones, zeros) * v
            v //= 2
        
        return res