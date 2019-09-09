# O(n) solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        
        res = 0
        for c in d:
            if c in d and c - 1 not in d:
                curr = 0
                while c in d:
                    curr += 1
                    c += 1
                res = max(res, curr)
        
        return res