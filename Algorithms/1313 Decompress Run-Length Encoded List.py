# Solution 1, simulation
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        res = []
        
        for i in range(0, len(nums), 2):
            cnt = nums[i]
            val = nums[i + 1]
            
            res.extend(val for _ in range(cnt))
        
        return res