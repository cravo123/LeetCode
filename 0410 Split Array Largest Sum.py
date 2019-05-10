# By Chong Chen, https://github.com/cravo123/LeetCode

# Solution 1, binary search on range value
class Solution:
    def feasible(self, nums, target, m):
        curr = 0
        
        for i, c in enumerate(nums):
            if curr + c > target:
                m -= 1
                curr = c
            else:
                curr += c
            
            if m < 1:
                return False
        return True
        
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if self.feasible(nums, mid, m):
                right = mid
            else:
                left = mid + 1
        
        return left

# Solution 2, DP,
# dp[i][j] means the minimum of maximum subarray sum from first i nums
# given j cuts
# t.b.c