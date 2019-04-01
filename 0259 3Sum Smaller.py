class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        nums.sort()
        res = 0
        
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr >= target:
                    k -= 1
                else:
                    res += k - j
                    j += 1
        
        return res