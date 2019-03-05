class Solution:
    def dfs(self, nums, seen, path, res):
        if len(path) == len(nums):
            res.append(path[::])
            return
        for i in range(len(nums)):
            if seen[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and seen[i - 1] is False:
                continue
            seen[i] = True
            path.append(nums[i])
            self.dfs(nums, seen, path, res)
            path.pop()
            seen[i] = False
        
                       
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        seen = [False for _ in nums]
        path = []
        res = []
        
        self.dfs(nums, seen, path, res)
        
        return res