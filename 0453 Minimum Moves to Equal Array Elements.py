class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_val = min(nums)
        
        res = sum(v - min_val for v in nums)
        
        return res