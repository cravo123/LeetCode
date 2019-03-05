class Solution:
    def dfs(self, idx, nums, target, path, res):
        if idx == len(nums) or target <= 0:
            if target == 0:
                res.append(path[::])
            return
        
        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.dfs(i, nums, target - nums[i], path, res)
            path.pop()
        
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        
        self.dfs(0, candidates, target, path, res)
        
        return res