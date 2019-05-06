import collections

# Solution 1, 
# two or three passes
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start = {} # c -> start index
        end = {} # c -> end index
        
        d = collections.Counter(nums)
        
        for i, c in enumerate(nums):
            if c not in start:
                start[c] = i
            end[c] = i
        
        v = max(d.values())
        
        res = float('inf')
        
        for c in d:
            if d[c] == v:
                res = min(res, end[c] - start[c] + 1)
        
        return res

# Solution 2, one-pass
# But still prefer Solution 1 as it is more straight-forward.
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        left = {}
        d = collections.Counter()
        res = float('inf')
        
        for i, c in enumerate(nums):
            if c not in left:
                left[c] = i
            
            d[c] += 1
            
            if d[c] == degree:
                res = min(res, i - left[c] + 1)
            elif d[c] > degree:
                degree = d[c]
                res = i - left[c] + 1
        return res