# Solution 1, simulation
# 3-reversal
class Solution:
    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n # notice k could be larger than n, so we need modulo
        
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)