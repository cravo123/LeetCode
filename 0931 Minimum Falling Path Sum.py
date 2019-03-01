class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A[0])
        if n == 1:
            return sum(sum(row) for row in A)
        
        curr = [0 for _ in A[0]]
        
        for i, row in enumerate(A):
            tmp = curr[::]
            for j in range(n):
                mid = curr[j]
                if j == 0:
                    left = float('inf')
                    right = curr[j + 1]
                elif j == n - 1:
                    left = curr[j - 1]
                    right = float('inf')
                else:
                    left = curr[j - 1]
                    right = curr[j + 1]
                
                tmp[j] = row[j] + min(left, mid, right)
            curr = tmp
        return min(curr)
