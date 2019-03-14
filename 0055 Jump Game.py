# Solution 1, BFS, good for shortest path
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        curr_min = curr_max = 0
        
        next_max = 0
        
        while True:
            for i in range(curr_min, curr_max + 1):
                next_max = max(next_max, i + nums[i])
            
            if next_max >= n - 1:
                return True
            if next_max == curr_max:
                return False
            
            curr_min, curr_max = curr_max + 1, next_max