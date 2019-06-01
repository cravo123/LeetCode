# Solution 1, two pointer
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0]) if A else 0
        
        for i in range(m):
            j, k = 0, n - 1
            
            while j <= k:
                if A[i][j] == A[i][k]:
                    A[i][j] = A[i][k] = 1 - A[i][j]
                j += 1
                k -= 1
                    
        return A