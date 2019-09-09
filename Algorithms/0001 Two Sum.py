# Solution 1, hash table to cache position
# Time Complexity, O(n)
# Space, O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, c in enumerate(nums):
            if target - c in d:
                return [d[target - c], i]
            d[c] = i

# Solution 2, sort and two pointers, 
# similar to LC 0167 Two Sum II - Input array is sorted
# Since we need to return index, so we maintain original index
# Time Complexity, O(n) if it is sorted
# Space, O(1), actually since we cache index, so should be O(n)...
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [[c, i] for i, c in enumerate(nums)]
        nums.sort()
        
        i, j = 0, len(nums) - 1
        
        while i < j:
            v = nums[i][0] + nums[j][0]
            if v == target:
                return [nums[i][1], nums[j][1]]
            if v < target:
                i += 1
            else:
                j -= 1