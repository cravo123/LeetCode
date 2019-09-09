class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                v = nums[i] + nums[j] + nums[k]
                if abs(v - target) < abs(res - target):
                    res = v
                if v < target:
                    j += 1
                else:
                    k -= 1
        return res