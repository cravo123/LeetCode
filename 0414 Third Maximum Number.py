# Solution 1, Manual 'heap'
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        
        for c in nums:
            if c in [first, second, third]:
                continue
            
            if c > first:
                first, second, third = c, first, second
            elif c > second:
                second, third = c, second
            elif c > third:
                third = c
        
        return third if third > float('-inf') else first

# Solution 2, heapq
from heapq import *

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        q = [float('-inf') for _ in range(3)]
        
        for c in nums:
            if c in q:
                continue
            heappush(q, c)
            heappop(q)
        
        res = heappop(q)
        heappop(q)
        first = heappop(q)
        
        return res if res > float('-inf') else first