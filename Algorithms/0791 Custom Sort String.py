import collections

# Solution 1, customized sorting
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        d = {c:i for i, c in enumerate(S)}
        
        T = list(T)
        T.sort(key=lambda x: d.get(x, -1))
        res = ''.join(T)

        return res

# Solution 2, Counting sort
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        d = collections.Counter(T)
        
        res = []
        
        for c in S:
            res.append(c * d[c])
            d[c] = 0
        
        for c in d:
            res.append(c * d[c])
        
        res = ''.join(res)
        
        return res