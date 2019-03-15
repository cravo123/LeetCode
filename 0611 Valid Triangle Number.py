class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        res = 0
        
        for i in range(2, n):
            j, k = 0, i - 1
            
            while j < k:
                v = nums[j] + nums[k]
                if v > nums[i]:
                    res += k - j
                    k -= 1
                else:
                    j += 1
        return res