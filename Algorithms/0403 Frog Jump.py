# Solution 1, BFS
class Solution:
    def dfs(self, curr, step, target, stones, d):
        if (curr, step) in d:
            return d[curr, step]
        if curr == target:
            return True
        if curr not in stones:
            return False
        
        for k in range(max(1, step - 1), step + 2):
            if self.dfs(curr + k, k, target, stones, d):
                d[curr, step] = True
                return True
        d[curr, step] = False
        return False
        
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        
        if 1 not in stones:
            return False
        
        d = {}
        
        return self.dfs(1, 1, target, stones, d)