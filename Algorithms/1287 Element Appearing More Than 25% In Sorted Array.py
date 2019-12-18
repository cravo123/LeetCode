import collections

# Solution 1, simulation
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        
        v = None
        cnt = 0
        
        for c in arr:
            if c == v:
                cnt += 1
            else:
                v = c
                cnt = 1
            
            if cnt > 0.25 * n:
                return v

# Solution 2, simulation using dict
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return collections.Counter(arr).most_common(1)[0][0]