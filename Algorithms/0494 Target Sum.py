# Solution 1, Naive Back-tracking, O(2 ** n)
class Solution:
    def dfs(self, idx, nums, S):
        if idx == len(nums):
            if S == 0:
                return 1
            return 0
        res = self.dfs(idx + 1, nums, S - nums[idx]) + self.dfs(idx + 1, nums, S + nums[idx])
        
        return res
        
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        res = self.dfs(0, nums, S)
        
        return res

# Solution 2, memoization
class Solution:
    def dfs(self, idx, need, nums, d):
        if (idx, need) in d:
            return d[(idx, need)]
        if idx == len(nums):
            return 0 if need != 0 else 1
        
        res = self.dfs(idx + 1, need - nums[idx], nums, d) + self.dfs(idx + 1, need + nums[idx], nums, d)

        return res
        
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}
        res = self.dfs(0, S, nums, d)
        
        return res