# Solution 1, mathematic induction
# a/b/c/d = a/(b*c*d)
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) <= 2:
            return '/'.join(str(x) for x in nums)
        
        return str(nums[0]) + '/' + '(%s)' % ('/'.join(str(x) for x in nums[1:]))