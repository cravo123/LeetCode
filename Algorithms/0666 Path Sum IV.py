# Solution 1, Use global variable, not decent solution
class Solution:
    def dfs(self, level, pos, curr, d):
        if (level, pos) not in d:
            return
        curr += d[level, pos]
        
        level += 1
        if (level, 2 * pos - 1) not in d and (level, 2 * pos) not in d:
            self.res += curr
            return
        
        self.dfs(level, 2 * pos - 1, curr, d)
        self.dfs(level, 2 * pos, curr, d)
        
    def pathSum(self, nums: List[int]) -> int:
        d = {}
        
        for c in nums:
            level = c // 100
            pos = c // 10 %  10
            val = c % 10
            d[level, pos] = val
        
        self.res = 0
        
        self.dfs(1, 1, 0, d)
        
        return self.res

# Solution 1.1, recursion, but not using global variable
class Solution:
    def dfs(self, level, pos, curr, d):
        if (level, pos) not in d:
            return 0
        
        curr += d[level, pos]
        level += 1
        
        L = self.dfs(level, pos * 2 - 1, curr, d)
        R = self.dfs(level, pos * 2, curr, d)
        
        if (level, pos * 2 - 1) not in d and (level, pos * 2) not in d:
            return curr
        
        return L + R
        
    def pathSum(self, nums: List[int]) -> int:
        d = {}
        
        for v in nums:
            level, pos, val = v // 100, v // 10 % 10, v % 10
            d[level, pos] = val
        
        return self.dfs(1, 1, 0, d)