import collections

# Soltuion 1, greedy
# Because each garden has at most 3 neighbor gardens but we have 
# 4 colors available. 
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        
        for i, j in paths:
            d[i - 1].add(j - 1)
            d[j - 1].add(i - 1)
        
        res = [0 for _ in range(N)]
        
        for i in range(N):
            v = (set([1, 2, 3, 4]) - {res[j] for j in d[i]}).pop()
            res[i] = v
        
        return res