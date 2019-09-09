# Solution 1, cache suffix minimum
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        suffix = A[::]
        n = len(A)
        
        curr = A[-1]
        i = n - 1
        while i >= 0:
            curr = min(curr, A[i])
            suffix[i] = curr
            i -= 1
        
        i = 0
        curr = A[i]
        
        while i < n - 1:
            curr = max(curr, A[i])
            if curr <= suffix[i + 1]:
                return i + 1
            i += 1