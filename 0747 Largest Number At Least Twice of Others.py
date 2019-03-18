# Solution 1
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        val = max(nums)
        
        for i, c in enumerate(nums):
            if c == val:
                res = i
            elif c * 2 > val:
                return -1
        
        return res

# Solution 2, maintain priority queue of two largest number
from heapq import * 

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        q = []
        
        for i, c in enumerate(nums):
            heappush(q, [c, i])
            if len(q) > 2:
                heappop(q)
        
        small, large = heappop(q), heappop(q)
        
        if large[0] >= 2 * small[0]:
            return large[1]
        return -1