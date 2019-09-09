import collections

# Solution 1, Sorting
class Solution:
    def frequencySort(self, s: str) -> str:
        d = collections.Counter(s)
        q = [[-cnt, c] for c, cnt in d.items()]
        q.sort()
        
        res = ''.join([c * (-cnt) for cnt, c in q])
        
        return res

# Solution 2, Bucket Sorting
class Solution:
    def frequencySort(self, s: 'str') -> 'str':
        d = collections.Counter(s)
        
        bucket = [[] for _ in range(len(s) + 1)]
        
        for c, cnt in d.items():
            bucket[cnt].append(c)
        
        res = []
        
        for i in range(len(bucket) - 1, -1, -1):
            for c in bucket[i]:
                res.append(c * i)
        res = ''.join(res)
        
        return res