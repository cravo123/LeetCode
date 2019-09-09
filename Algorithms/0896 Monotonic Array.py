# Solution 1, using exclusion
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        is_increase = is_decrease = True
        
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                is_decrease = False
            if A[i] < A[i - 1]:
                is_increase = False
        
        return is_increase or is_decrease