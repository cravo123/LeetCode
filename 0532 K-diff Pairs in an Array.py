import collections

# Solution 1, hash table
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums or k < 0:
            return 0
        
        d = collections.Counter(nums)
        
        if k == 0:
            res = sum(1 if d[c] > 1 else 0 for c in d)
        else:
            res = 0
            for c in sorted(d):
                if c + k in d:
                    res += 1
        
        return res