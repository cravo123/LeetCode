# Solution 1, two sum variant, using two-pointer
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        i, j = 0, len(A) - 1
        
        res = -1
        
        while i < j:
            v = A[i] + A[j]
            
            if v >= K:
                j -= 1
            else:
                res = max(res, v)
                i += 1
        
        return res