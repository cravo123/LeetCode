class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float('inf')
        j = 0
        curr = 0
        
        for i, c in enumerate(nums):
            curr += c
            
            while curr >= s:
                res = min(res, i - j + 1)
                curr -= nums[j]
                j += 1
        return res if res < float('inf') else 0