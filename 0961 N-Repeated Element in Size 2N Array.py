# Solution 1, hashtable
# Memory O(n)
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = set()
        for c in A:
            if c in seen:
                return c
            seen.add(c)

# Solution 2, sort
# Memory O(1)
# In the worst case, repeated element could be
# in the first half or the second half, otherwise
# it should cross two halves
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        
        n = len(A)
        idx = n // 2 - 1
        return A[idx] if A[idx] == A[idx - 1] else A[idx + 1]