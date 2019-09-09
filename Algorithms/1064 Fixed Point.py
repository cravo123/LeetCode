# Solution 1, binary search
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        i, j = 0, len(A) - 1
        
        while i < j:
            m = (i + j) // 2
            
            if A[m] < m:
                i = m + 1
            else:
                j = m
        
        return m if A[m] == m else -1