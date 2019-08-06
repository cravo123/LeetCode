# Solution 1, simulation
# Similar idea as LC 448 Find All Numbers Disappeared in an Array
# Use abs(v) as index to toggle nums[abs(v) - 1]
# If nums[abs(v) - 1] < 0, then we know we see this value before
# so we can add abs(v) to result
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            v = abs(nums[i])
            
            if nums[v - 1] < 0:
                res.append(v)
            
            nums[v - 1] = - nums[v - 1]
        
        return res