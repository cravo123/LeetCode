import collections

# Solution 1, use set property (no-duplicate)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# Solution 2, running counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = collections.Counter()
        
        for c in nums:
            d[c] += 1
            if d[c] > 1:
                return True
        return False