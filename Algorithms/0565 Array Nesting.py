# Solution 1, similar to find circle in a graph
class Solution:
    def dfs(self, idx, nums, seen):
        if idx in seen:
            return 0
        seen.add(idx)
        cnt = 1
        
        cnt += self.dfs(nums[idx], nums, seen)
        
        return cnt
        
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        res = 0
        for i, c in enumerate(nums):
            curr = self.dfs(c, nums, seen)
            res = max(res, curr)
        return res