# By Chong Chen, https://github.com/cravo123/LeetCode

# Solution 1, 0-1 knapsack

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