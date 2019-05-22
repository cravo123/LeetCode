# Solution 1, two pointers
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        
        if not nums:
            return res
        
        i, n = 0, len(nums)
        
        while i < n:
            j = i
            while j < n - 1 and nums[j] + 1 == nums[j + 1]:
                j += 1
            
            if i == j:
                res.append('%d' % nums[i])
                i += 1
            else:
                res.append('%d->%d' % (nums[i], nums[j]))
                i = j + 1
        
        return res