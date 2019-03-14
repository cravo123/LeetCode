# Quick Select
class Solution:
    def quick_select(self, nums, start, end, k):
        if start > end:
            return 
        if start == end:
            return nums[start]
        
        mid = (start + end) // 2
        nums[mid], nums[end] = nums[end], nums[mid]
        i, j = start, start
        while i < end:
            if nums[i] > nums[end]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        nums[j], nums[end] = nums[end], nums[j]
        
        if j == k:
            return nums[j]
        if j < k:            
            return self.quick_select(nums, j + 1, end, k)
        return self.quick_select(nums, start, j - 1, k)
        
        
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k -= 1
        return self.quick_select(nums, 0, n - 1, k)