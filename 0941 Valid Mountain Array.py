class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        n = len(A)
        i = 0
        while i < n - 1 and A[i] < A[i + 1]:
            i += 1
        
        j = n - 1
        while j > i and A[j] < A[j - 1]:
            j -= 1
        
        return i == j and i != 0 and i != n - 1