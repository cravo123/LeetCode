class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        n = len(A)
        
        while i < n and j < n:
            while i < n and A[i] % 2 == 0:
                i += 2
            while j < n and A[j] % 2 == 1:
                j += 2
            if i < n and j < n:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
        return A