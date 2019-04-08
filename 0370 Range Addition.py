# Solution 1, sweeping line algorithm
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0 for _ in range(length)]
        
        for left, right, inc in updates:
            res[left] += inc
            if right + 1 < length:
                res[right + 1] -= inc
        
        curr = 0
        
        for i in range(length):
            curr += res[i]
            res[i] = curr
        
        return res

# Solution 2, using heapq
# But actually no need to use heapq...
from heapq import *
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        q = []
        
        for left, right, inc in updates:
            q.append([left, inc])
            q.append([right + 1, -inc])
        
        heapify(q)
        
        res = [0 for _ in range(length)]
        
        while q:
            idx, val = heappop(q)
            if idx < length:
                res[idx] += val
        
        curr = 0
        for i in range(length):
            curr += res[i]
            res[i] = curr
        
        return res
        