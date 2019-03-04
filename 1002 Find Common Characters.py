import collections
class Solution:
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        d = collections.Counter(A[0])
        
        for a in A:
            d &= collections.Counter(a)
        
        res = list(d.elements())
        
        return res