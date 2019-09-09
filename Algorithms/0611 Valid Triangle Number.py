# Solution 1, two-pointer
# three numbers(a < b < c), can constitute a triangle
# iff a + b > c
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        
        for k in range(2, len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] <= nums[k]:
                    i += 1
                else:
                    res += j - i
                    j -= 1
        
        return res