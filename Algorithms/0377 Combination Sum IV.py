# Solution 1
class Solution:
    def dfs(self, nums, target, path):
        if target <= 0:
            return 1 if target == 0 else 0
        
        res = 0
        for i in range(len(nums)):
            path.append(nums[i])
            res += self.dfs(nums, target - nums[i], path)
            path.pop()
        return res
    
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        path = []
        
        res = self.dfs(nums, target, path)
        
        return res

# Solution 1.1
class Solution:
    def dfs(self, nums, target):
        if target <= 0:
            return 1 if target == 0 else 0
        
        res = 0
        for i in range(len(nums)):
            res += self.dfs(nums, target - nums[i])
            
        return res
    
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = self.dfs(nums, target)
        
        return res

# Solution 2, Memoization
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        
        nums.sort()
        
        # if you switch for i and for c
        # it will be count of combination instead of permutation
        for i in range(1, target + 1):
            for c in nums:
                if i - c >= 0:
                    dp[i] += dp[i - c]
        
        return dp[-1]