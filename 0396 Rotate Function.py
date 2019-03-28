class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if not A:
            return 0
        total = sum(A)
        curr = sum(i * c for i, c in enumerate(A))
        res = curr
        
        n = len(A)
        i = 1
        while i <= n:
            res = max(res, curr)
            curr = curr + total - n * A[n - i]
            i += 1
        
        return res