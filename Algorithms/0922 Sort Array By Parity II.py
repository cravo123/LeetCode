# Solution 1, two-pointer
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        i, j = 0, 1
        
        while i < n and j < n:
            while i < n and A[i] % 2 == 0:
                i += 2
            while j < n and A[j] % 2 == 1:
                j += 2
            
            if i < n and j < n:
                A[i], A[j] = A[j], A[i]
        
        return A