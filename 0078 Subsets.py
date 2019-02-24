class Solution:
    def dfs(self, idx, nums, path, res):
        res.append(path[::])
        
        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.dfs(i + 1, nums, path, res)
            path.pop()
        
        
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        path = []
        res = []
        
        self.dfs(0, nums, path, res)
        
        return res