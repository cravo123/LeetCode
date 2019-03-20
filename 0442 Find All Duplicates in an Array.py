# Similar idea as LC 448 Find All Numbers Disappeared in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            v = abs(nums[i])
            
            if nums[v - 1] < 0:
                res.append(v)
            
            nums[v - 1] = - nums[v - 1]
        
        return res