# Union Find Algorithm
class Solution:
    def find_parent(self, idx, d):
        if idx != d[idx]:
            d[idx] = self.find_parent(d[idx], d) # Path compression
        
        return d[idx]
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        d={i:i for i in range(1, n + 1)}
        
        for a, b in edges:
            pa, pb = self.find_parent(a, d), self.find_parent(b, d)
            if pa == pb:
                return [a, b]
            d[pa] = pb