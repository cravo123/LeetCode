# Solution 1, two-pointer
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = A[::]
        
        i, j = 0, len(A) - 1
        idx = len(A) - 1
        
        while i <= j:
            i_v, j_v = A[i] * A[i], A[j] * A[j]
            if i_v > j_v:
                res[idx] = i_v
                i += 1
            else:
                res[idx] = j_v
                j -= 1
            idx -= 1
        return res