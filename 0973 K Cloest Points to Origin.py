from heapq import *

# Solution 1, maintain priority queue
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

# Solution 2, built-in function
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = nsmallest(K, points, key=lambda x: x[0] * x[0] + x[1] * x[1])
        return res

# Solution 3, quick select
class Solution:
    def dist(self, p):
        return p[0] * p[0] + p[1] * p[1]
    
    def quick_select(self, points, start, end, K):
        if start >= end:
            return
        
        mid = (start + end) // 2
        points[mid], points[end] = points[end], points[mid]
        i = j = start
        target = self.dist(points[end])
        
        while i < end:
            if self.dist(points[i]) <= target:
                points[j], points[i] = points[i], points[j]
                j += 1
            i += 1
        points[j], points[end] = points[end], points[j]
        
        if j == K:
            return
        if j < K:
            self.quick_select(points, j + 1, end, K)
        else:
            self.quick_select(points, start, j - 1, K)
        
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.quick_select(points, 0, len(points) - 1, K - 1)
        return points[:K]

# Solution 4, sort
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] * x[0] + x[1] * x[1])
        
        res = points[:K]
        
        return res