# Solution 1, more elegant
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        for c in nums:
            if i < 2 or c != nums[i - 2]:
                nums[i] = c
                i += 1
        return i

# Solution 2, array manipulation
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        idx = 0
        i = 0
        
        while i < n:
            cnt = 0
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
                cnt += 1
            cnt = min(cnt, 2)
            for k in range(idx, idx + cnt):
                nums[k] = nums[i]
            idx += cnt
            i = j
        return idx