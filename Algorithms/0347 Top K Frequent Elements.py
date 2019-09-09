import collections
import heapq

# Solution 1, priority queue, O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        q = []
        
        for v, cnt in d.items():
            heapq.heappush(q, [cnt, v])
            if len(q) > k:
                heapq.heappop(q)
        res = [x[1] for x in q]
        return res

# Solution 2, use built-in
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        
        res = heapq.nlargest(k, d.items(), key=lambda x: x[1])
        
        res = [x[0] for x in res]
        
        return res

# We can use bucket sort after get elements count 