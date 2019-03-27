class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j = 0
        
        for c in nums:
            if c != nums[j]:
                j += 1
                nums[j] = c
        
        return j + 1