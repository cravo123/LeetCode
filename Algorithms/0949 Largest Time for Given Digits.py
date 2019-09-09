# Again, permutation implemented by back-tracking

class Solution:
    def dfs(self, nums, seen, path, res):
        if len(path) == len(nums):
            res.append(path[::])
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and seen[i - 1] == False:
                continue
            if seen[i]:
                continue
            path.append(nums[i])
            seen[i] = True
            self.dfs(nums, seen, path, res)
            seen[i] = False
            path.pop()
            
    def permutations(self, nums):
        nums.sort()
        seen = [False for _ in nums]
        path = []
        res = []
        
        self.dfs(nums, seen, path, res)
        
        res = [(x[0] * 10 + x[1], x[2] * 10 + x[3]) for x in res]
        
        res = ['%02d:%02d' % x for x in res if 0 <= x[0] < 24 and 0 <= x[1] < 60]
        
        return res
    
    
    def largestTimeFromDigits(self, A: List[int]) -> str:
        res = self.permutations(A)
        res.sort()
        
        return res[-1] if res else ''