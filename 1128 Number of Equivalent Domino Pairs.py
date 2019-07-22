import collections

# Solution 1, sort and count
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = collections.Counter()
        res = 0
        
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            d[a, b] += 1
            res += d[a, b] - 1
        
        return res

# Solution 1.1, better implementation
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = collections.Counter()
        res = 0
        
        for a, b in dominoes:
            k = tuple(sorted([a, b]))
            res += d[k]
            
            d[k] += 1
        
        return res