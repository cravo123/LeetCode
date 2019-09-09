class Solution:
    def dfs(self, idx, nums, seen, target, path, res):
        if idx == len(nums) or target <= 0:
            if target == 0:
                res.append(path[::])
            return
        
        for i in range(idx, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and seen[i - 1] is False:
                continue
            seen[i] = True
            path.append(nums[i])
            self.dfs(i + 1, nums, seen, target - nums[i], path, res)
            path.pop()
            seen[i] = False
        
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        seen = [False for _ in candidates]
        
        path = []
        res = []
        
        self.dfs(0, candidates, seen, target, path, res)
        
        return res