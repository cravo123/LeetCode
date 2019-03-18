import collections
# Solution 1, O(n) memory
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        
        res = [0, 0]
        
        for i in range(1, len(nums) + 1):
            if d[i] == 0:
                res[1] = i
            elif d[i] == 2:
                res[0] = i
        
        return res

# Solution 2, O(1) memory
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # diff = missing - duplicate
        diff = (1 + n) * n // 2 - sum(nums)
        
        # square_diff = missing ^ 2 - duplicate ^ 2
        square_diff = n * (n + 1) * (2 * n + 1) // 6 - sum(x * x for x in nums)
        
        # total_sum = missing + duplicate
        total_sum = square_diff // diff
        
        missing = (total_sum + diff) // 2
        duplicate = missing - diff
        
        return [duplicate, missing]

# Solution 3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        
        curr = 0
        
        for i, c in enumerate(nums):
            curr ^= (i + 1) ^ abs(c)
            
            if nums[abs(c) - 1] < 0:
                res[0] = abs(c)
            nums[abs(c) - 1] = - nums[abs(c) - 1]
        
        res[1] = curr ^ res[0]
        
        return res