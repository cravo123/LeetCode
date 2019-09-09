# Several sorting implementation

# Solution 1, built-in, amortized O(nlogn)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

# Solution 2, bubble-sorting, O(n ^ 2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        return nums

# Solution 3, insertion sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
        
        return nums

# Solution 4, quick-sort
class Solution:
    def pivot(self, start, end, nums):
        mid = (start + end) // 2
        nums[mid], nums[end] = nums[end], nums[mid]
        
        i = j = start
        v = nums[end]
        
        while i < end:
            if nums[i] <= v:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            i += 1
        nums[j], nums[end] = nums[end], nums[j]
        
        return j
    
    def quick_sort(self, start, end, nums):
        if start >= end:
            return
        
        idx = self.pivot(start, end, nums)
        self.quick_sort(start, idx - 1, nums)
        self.quick_sort(idx + 1, end, nums)
        
        
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.quick_sort(0, n - 1, nums)
        
        return nums

# Solution 5, merge-sort
# using tmp list is not compulsory. We use tmp here merely to avoid creating
# new list in every recursion
class Solution:
    def merge(self, start, mid, end, nums, tmp):
        i, j = start, mid + 1
        
        curr = start
        while i <= mid or j <= end:
            if i > mid:
                tmp[curr] = nums[j]
                j += 1
            elif j > end:
                tmp[curr] = nums[i]
                i += 1
            elif nums[i] < nums[j]:
                tmp[curr] = nums[i]
                i += 1
            else:
                tmp[curr] = nums[j]
                j += 1
            curr += 1
        
        for i in range(start, end + 1):
            nums[i] = tmp[i]
        
    def merge_sort(self, start, end, nums, tmp):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.merge_sort(start, mid, nums, tmp)
        self.merge_sort(mid + 1, end, nums, tmp)
        
        self.merge(start, mid, end, nums, tmp)
        
    def sortArray(self, nums: List[int]) -> List[int]:
        tmp = nums[::]
        
        self.merge_sort(0, len(nums) - 1, nums, tmp)
        
        return nums