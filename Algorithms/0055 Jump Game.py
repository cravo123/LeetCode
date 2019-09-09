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

# Solution 2, same idea but more elegant solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = right = 0
        n = len(nums)
        
        while i < n and i <= right:
            right = max(right, i + nums[i])
            i += 1
        
        return right >= n - 1