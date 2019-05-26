# Solution 1, quick-select instead of sorting, O(n) complexity
# t.b.c

# Solution 2, greedy by sorting
# First fill all odd-position first since it is guaranteed that 
# a solution exists
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        v = sorted(nums)
        
        for i in range(1, len(nums), 2):
            nums[i] = v.pop()
        
        for i in range(0, len(nums), 2):
            nums[i] = v.pop()