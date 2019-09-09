# Solution 1, combination problem
# Use back-tracking to generate all combinations
# Notice this is not permutation 
class Solution:
    def dfs(self, idx, n, path, res, candidates, seen):
        if n == 0:
            res.append(sum(path))
            return
        
        for i in range(idx, len(candidates)):
            if seen[i] == False:
                path.append(candidates[i])
                seen[i] = True
                self.dfs(i + 1, n - 1, path, res, candidates, seen)
                path.pop()
                seen[i] = False
    
    def combination(self, n, candidates):
        seen = [False for _ in candidates]
        
        path = [0]
        res = []
        
        self.dfs(0, n, path, res, candidates, seen)
        
        return res
    
    def generate_hours(self, n):
        res = self.combination(n, [1, 2, 4, 8])
        res = [x for x in res if 0 <= x < 12]
        return res
    
    def generate_mins(self, n):
        res = self.combination(n, [1, 2, 4, 8, 16, 32])
        res = [x for x in res if 0 <= x < 60]    
        print(n, res)
        return res
    
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        
        for i in range(num + 1):
            h, m = i, num - i
            
            for hh in self.generate_hours(h):
                for mm in self.generate_mins(m):
                    res.append('%d:%02d' % (hh, mm))
        res.sort()
        return res

# Solution 1.1, another implementation
class Solution:
    def dfs(self, curr, idx, n, nums, res):
        if n == 0:
            res.append(curr)
            return
        for i in range(idx, len(nums)):
            self.dfs(curr + nums[i], i + 1, n - 1, nums, res)
            
    def generate_nums(self, n, nums):
        res = []
        
        self.dfs(0, 0, n, nums, res)
        
        if len(nums) == 4:
            res = [x for x in res if 0 <= x < 12]
        else:
            res = [x for x in res if 0 <= x < 60]
        
        return res
        
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        
        for h in range(num + 1):
            m = num - h
            
            for hh in self.generate_nums(h, [1, 2, 4, 8]):
                for mm in self.generate_nums(m, [1, 2, 4, 8, 16, 32]):
                    res.append('%d:%02d' % (hh, mm))
        
        return res