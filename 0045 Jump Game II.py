# Solution 1, Breadth-First-Search
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        
        n = len(nums)
        tmp = right
        steps = 0
        for i in range(n):
            tmp = max(tmp, i + nums[i])
            if right >= n - 1:
                return steps
            
            if i == right:
                left, right = right + 1, tmp
                steps += 1

# Solution 2, optimized based on Solution 1
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        n = len(nums)
        tmp = right = 0
        steps = 0
        
        for i in range(n):
            tmp = max(tmp, i + nums[i])
            
            if tmp >= n - 1:
                return steps + 1
            
            if i == right:
                right = tmp
                steps += 1
        
        return steps

# Soltuion 3, same idea
class Solution:
    def jump(self, nums: List[int]) -> int:
        i = right = next_right = 0
        steps = 0
        
        n = len(nums)
        
        while right < n - 1:
            next_right = max(next_right, i + nums[i])
            if i == right:
                right = next_right
                steps += 1
            i += 1
        return steps