# Solution 1
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        n = len(candies)
        kinds = len(set(candies))
        
        return min(n // 2, kinds)

# Solution 2, more elegant
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = curr = 0
        
        for c in nums:
            if c == 0:
                curr = 0
            else:
                curr += 1
                res = max(res, curr)
        
        return res