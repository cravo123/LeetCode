# By Chong Chen, https://github.com/cravo123/LeetCode

# Solution 1, 0-1 knapsack
# dp[i][j] means if we can use first i nums to get value j
# so dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
# i.e. we don't use i-th num to get j or we use i-th num, then
# we need to use first (i - 1) nums to get value (j - nums[i - 1])
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        target = sum(nums)
        if target % 2 == 1:
            return False
        
        target //= 2
        n = len(nums)
        
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i - 1]] if j >= nums[i - 1] else False)
                
            if dp[i][-1]:
                return True
        return False

# Solution 2.1, pruning and early-termination
class Solution:
    def dfs(self, idx, target, nums, d):
        if target == 0:
            return True
        
        if target < 0:
            return False
        
        if (target, idx) in d:
            return d[target, idx]
        
        for i in range(idx, len(nums)):
            if self.dfs(i + 1, target - nums[i], nums, d):
                d[target, idx] = True
                return True
        
        d[target, idx] = False
        
        return False
        
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or sum(nums) % 2 != 0:
            return False
        nums.sort(reverse=True)
        target = sum(nums) // 2
        
        d = {}
        
        return self.dfs(0, target, nums, d)

# Solution 2.2, memoization (TLE)
class Solution:
    def dfs(self, idx, target, nums, d):
        if target == 0:
            return True
        
        if (target, idx) in d:
            return d[target, idx]
        
        for i in range(idx, len(nums)):
            if self.dfs(i + 1, target - nums[i], nums, d):
                d[target, idx] = True
                return True
        
        d[target, idx] = False
        
        return False
        
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        
        d = {}
        
        return self.dfs(0, target, nums, d)

# Solution 2.3, brute-force backtracking (TLE)
class Solution:
    def dfs(self, idx, target, nums):
        if target == 0:
            return True
        
        for i in range(idx, len(nums)):
            if self.dfs(i + 1, target - nums[i], nums):
                return True
        
        return False
        
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        
        return self.dfs(0, target, nums)