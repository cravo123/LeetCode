# Solution 1, simulation
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_val = min(A)
        max_val = max(A)
        
        return max(max_val - min_val - 2 * K, 0)