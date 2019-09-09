import collections

# Solution 1, bit-mask...
# t.b.c

# Solution 2, brute-force counting
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        
        for c, cnt in d.items():
            if cnt == 1:
                return c