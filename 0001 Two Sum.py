class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, c in enumerate(nums):
            if target - c in d:
                return [d[target - c], i]
            d[c] = i