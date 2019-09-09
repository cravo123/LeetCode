import collections
# Good application for hashmap
class Solution:
    def dist(self, p, q):
        return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])
    
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        
        for i in range(n):
            d = collections.Counter()
            for j in range(n):
                if i == j:
                    continue
                v = self.dist(points[i], points[j])
                d[v] += 1
                res += (d[v] - 1) * 2
        return res