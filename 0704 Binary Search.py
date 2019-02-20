class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        i, j = 0, len(nums) - 1
        
        while i < j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m
        return i if nums[i] == target else -1