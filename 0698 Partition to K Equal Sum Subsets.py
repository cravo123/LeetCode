
# Solution 3, brute force back-tracking (TLE)
class Solution:
    def dfs(self, seen, nums, curr, need, multi):
        if all(x for x in seen):
            return curr == need
        if curr > need:
            return False
        
        if curr == need:
            need += multi
        
        for i in range(len(seen)):
            if seen[i] == False:
                seen[i] = True
                if self.dfs(seen, nums, curr + nums[i], need, multi):
                    seen[i] = False
                    return True
                seen[i] = False
        return False
        
        
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        multi = total // k
        need = multi
        curr = 0
        seen = [False for _ in nums]
        nums.sort(reverse=True)
        return self.dfs(seen, nums, curr, need, multi)