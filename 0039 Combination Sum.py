# Solution 1, back-tracking
class Solution:
    def dfs(self, idx, candidates, target, path, res):
        if target == 0:
            res.append(path[::])
            return
        
        if target < 0:
            return
        
        for i in range(idx, len(candidates)):
            path.append(candidates[i])
            self.dfs(i, candidates, target - candidates[i], path, res)
            path.pop()
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        
        self.dfs(0, candidates, target, path, res)
        
        return res