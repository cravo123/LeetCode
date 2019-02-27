# Solution 1
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        q = []
        
        for v, cnt in d.items():
            heappush(q, [cnt, v])
            if len(q) > k:
                heappop(q)
        res = [x[1] for x in q]
        return res

# Solution 2, use built-in
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        
        res = nlargest(k, d.items(), key=lambda x: x[1])
        
        res = [x[0] for x in res]
        
        return res

# We can use bucket sort after get elements count 