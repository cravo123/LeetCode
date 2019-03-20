# Using negative numbers to mark if we visit this position before is a common trick
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            v = abs(nums[i])
            nums[v - 1] = - abs(nums[v - 1])
        
        res = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
        return res