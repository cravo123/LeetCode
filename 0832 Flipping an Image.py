class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0]) if A else 0
        
        for i in range(m):
            left, right = 0, n - 1
            while left <= right:
                if A[i][left] == A[i][right]:
                    A[i][left] = A[i][right] = 1 - A[i][right]
                left += 1
                right -= 1
        return A