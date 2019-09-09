import collections

# Solution 1, XOR
# 0 ^ val = val ^ 0 = val
# val ^ val = 0
# a ^ b = b ^ a
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for c in nums:
            res ^= c
        return res

# Solution 2, hash table
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        
        res = [x for x, cnt in d.items() if cnt == 1]
        
        return res[0]