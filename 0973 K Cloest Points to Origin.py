from heapq import *

class Solution:
    def distance(self, p, q):
        return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = []
        
        for p in points:
            heappush(q, [-self.distance(p, [0, 0]), p])
            if len(q) > K:
                heappop(q)
        
        res = [x[1] for x in q]
        return res