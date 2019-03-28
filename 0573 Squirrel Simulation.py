class Solution(object):
    def distance(self, p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1])
    
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        
        total = sum(self.distance(tree, nut) for nut in nuts) * 2
        
        vs = min(self.distance(squirrel, nut) - self.distance(nut, tree) for nut in nuts)
        
        return total + vs