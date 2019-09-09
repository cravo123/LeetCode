class Solution:
    def dfs(self, idx, nums, path, res):
        if len(path) >= 2:
            res.append(path[::])
        if idx == len(nums):
            return
        seen = set()
        for i in range(idx, len(nums)):
            if nums[i] in seen:
                continue
            if not path or path[-1] <= nums[i]:
                seen.add(nums[i])
                path.append(nums[i])
                self.dfs(i + 1, nums, path, res)
                path.pop()
        
        
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        
        self.dfs(0, nums, path, res)
        
        return res