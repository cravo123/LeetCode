# Solution 1
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        is_increase = is_decrease = False
        
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                is_increase = True
            if A[i] < A[i - 1]:
                is_decrease = True
        
        return not (is_increase and is_decrease)

# Solution 2, more intuitive
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