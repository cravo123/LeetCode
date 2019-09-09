class Solution:
    def dfs(self, idx, path, res, nums, seen):
        res.append(path[::])
        
        for i in range(idx, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and seen[i - 1] is False:
                continue
            seen[i] = True
            path.append(nums[i])
            self.dfs(i + 1, path, res, nums, seen)
            path.pop()
            seen[i] = False
        
        
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = [False for _ in nums]
        
        path = []
        res = []
        
        self.dfs(0, path, res, nums, seen)
        
        return res
