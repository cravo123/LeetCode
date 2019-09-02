# Solution 1, simulation using sliding-window
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = curr = 0
        
        for i, c in enumerate(calories):
            curr += c
            
            if i < k - 1:
                continue
            
            if i >= k:
                curr -= calories[i - k]
            
            if curr < lower:
                res -= 1
            elif curr > upper:
                res += 1
        
        return res