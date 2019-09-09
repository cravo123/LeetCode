# Solution 1, DFS
class Solution:
    def dfs(self, idx, nums, used, path, res, target):
        if len(path) == 4:
            if target == 0:
                res.append(path[::])
            return
        
        for i in range(idx, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False:
                continue
            path.append(nums[i])
            used[i] = True
            self.dfs(i + 1, nums, used, path, res, target - nums[i])
            path.pop()
            used[i] = False
            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        used = [False for _ in nums]
        
        path = []
        res = []
        
        self.dfs(0, nums, used, path, res, target)
        
        return res

# Solution 2
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                x, y = j + 1, n - 1
                while x < y:
                    v = nums[i] + nums[j] + nums[x] + nums[y]
                    
                    if v < target:
                        x += 1
                    elif v > target:
                        y -= 1
                    else:
                        res.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        y -= 1
                        while x < y and nums[x] == nums[x - 1]:
                            x += 1
                        while x < y and nums[y] == nums[y + 1]:
                            y -= 1
        return res