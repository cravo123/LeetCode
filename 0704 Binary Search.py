# Solution 1, binary search
# There are several implementation of binary search.
# But the key point is m = (i + j) // 2 will equal to i if j = i + 1
# so we cannot set i = m, otherwise it will be infinite loop.
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        i, j = 0, len(nums) - 1
        
        while i < j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1 # gotcha
            else:
                j = m
        return i if nums[i] == target else -1

# Solution 1.1, another Binary Search implementation
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                return m
        
        return -1