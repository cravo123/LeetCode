# Similar to LC 1043

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
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # dp[i][j], minimum largest sum of first i elements separated to j subarrays
        # dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sum(nums[(k + 1):i]))
        
        n = len(nums)
        prefix = [0]
        curr = 0
        for v in nums:
            curr += v
            prefix.append(curr)
        
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        
        for j in range(m + 1):
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], prefix[i] - prefix[k]))
        
        return dp[-1][-1]