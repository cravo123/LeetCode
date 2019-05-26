import collections

# Solution 1, prefix-sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.Counter()
        d[0] = 1
        
        curr = 0
        res = 0
        for c in nums:
            curr += c
            res += d[curr - k]
            d[curr] += 1
        
        return res