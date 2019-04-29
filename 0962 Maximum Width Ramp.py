# Solution 1, elegant
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        q = [i for i in range(len(A))]
        q.sort(key=lambda x: A[x])
        
        curr = float('inf')
        res = 0
        
        for i in q:
            res = max(res, i - curr)
            curr = min(curr, i)
        
        return res