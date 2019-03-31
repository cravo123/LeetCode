# Solution 1, Binary Search on Value Range
class Solution:
    def count(self, val, m, n):
        res = 0
        for i in range(1, m + 1):
            res += min(val // i, n)
        
        return res
        
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n
        
        while left < right:
            mid = (left + right) // 2    
            cnt = self.count(mid, m, n)
            
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        
        return left
# Solution 2, priority queue(TLE though)
from heapq import heappush, heappop

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        q = [[i, 1] for i in range(1, n + 1)]
        
        idx = 0
        while idx < k:
            v, i = heappop(q)
            idx += 1
            if idx == k:
                return v
            if i + 1 <= m: # boundary condition
                heappush(q, [v // i * (i + 1), i + 1])