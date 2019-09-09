class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        q = []
        curr = 0
        
        for c in A:
            curr += c
            q.append(curr)
        
        res_max = float('-inf')
        res_min = float('inf')
        
        curr_min = curr_max = 0
        
        for c in q:
            res_max = max(res_max, c - curr_min)
            curr_min = min(curr_min, c)
            res_min = min(res_min, c - curr_max)
            curr_max = max(curr_max, c)
        
        return max(res_max, q[-1] - res_min) if res_max > 0 else res_max