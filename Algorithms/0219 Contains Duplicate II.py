# Solution 1, hash map
# One disadvantage compared to Solution 2 is that,
# hash map d could hold O(n) elements
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        
        for i, c in enumerate(nums):
            if c in d and i - d[c] <= k:
                return True
            d[c] = i
        
        return False

# Solution 2,
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = set()
        
        for i, c in enumerate(nums):
            if i > k:
                d.discard(nums[i - k - 1])
            if c in d:
                return True
            d.add(c)
        return False