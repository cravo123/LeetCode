# Solution 1, back-tracking
# Template problem
class Solution:
    def dfs(self, path, res, seen, nums):
        if len(path) == len(nums):
            res.append(path[::])
            return
        
        for i in range(len(nums)):
            if seen[i] == False:
                seen[i] = True
                path.append(nums[i])
                self.dfs(path, res, seen, nums)
                path.pop()
                seen[i] = False
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        seen = [False for _ in nums]
        
        self.dfs(path, res, seen, nums)
        
        return res