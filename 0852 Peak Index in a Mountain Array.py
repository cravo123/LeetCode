# Solution 1, O(N)
class Solution:
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        i, j = 0, len(A) - 1
        
        while i < j and A[i] < A[i + 1]:
            i += 1
        
        return i

# Solution 2, Binary Search O(log N)
class Solution:
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        i, j = 0, len(A) - 1
        
        while i < j:
            m = (i + j) // 2
            if A[m] < A[m + 1]:
                i = m + 1
            else:
                j = m
        
        return i