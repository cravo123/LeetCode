import collections

# Solution 1, Brute-Force, TLE
class Solution:
    def dfs(self, i, d, seen):
        seen.add(i)
        res = 1
        
        for j in d[i]:
            if j not in seen:
                res = max(res, self.dfs(j, d, seen) + 1)
        return res
        
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        
        for i, j in edges:
            d[i].add(j)
            d[j].add(i)
        
        h = {i:1 for i in range(n)}
        
        for i in d:
            seen = set()
            h[i] = self.dfs(i, d, seen)
        
        v = min(h.values())
        
        res = [i for i in h if h[i] == v]
        
        return res

# Solution 2
