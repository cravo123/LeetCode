# Solution 1, simulation
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        check = sorted(nums)
        d = {}
        
        for i, v in enumerate(check):
            if v not in d:
                d[v] = i
        
        res = [d[x] for x in nums]
        
        return res