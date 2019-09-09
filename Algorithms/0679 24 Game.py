class Solution:
    def combination(self, nums):
        n = len(nums)
        
        for i in range(n):
            for j in range(i):
                t = [nums[c] for c in range(n) if c not in [i, j]]
                
                a, b = nums[i], nums[j]
                yield t + [a + b]
                yield t + [a - b]
                yield t + [b - a]
                yield t + [a * b]
                
                if b != 0:
                    yield t + [a / b]
                if a != 0:
                    yield t + [b / a]
        
    def dfs(self, nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) <= 1e-5
        
        for x in self.combination(nums):
            if self.dfs(x):
                return True
        
        return False
        
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.dfs(nums)