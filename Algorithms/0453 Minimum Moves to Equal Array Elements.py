# Solution 1, simulation
# increment n - 1 elements is the same as 
# decrementing only 1 element.
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_val = min(nums)
        
        res = sum(v - min_val for v in nums)
        
        return res