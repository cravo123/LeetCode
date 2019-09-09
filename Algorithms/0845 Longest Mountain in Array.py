# Solution 1, O(n) traversing
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        i, n = 0, len(A)
        res = 0
        
        while i < n:
            # increase
            j = i
            while j < n - 1 and A[j] < A[j + 1]:
                j += 1
            # decrease
            k = j
            while k < n - 1 and A[k] > A[k + 1]:
                k += 1
            
            if i == j or j == k:
                i = max(i + 1, k)
                continue
            res = max(res, k - i + 1)
            i = k
        return res