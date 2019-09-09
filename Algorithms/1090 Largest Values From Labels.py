import collections
import heapq

# Solution 1, sort
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        q = [[v, idx] for v, idx in zip(values, labels)]
        q.sort(reverse=True)
        
        res = 0
        used = collections.Counter()
        
        for v, idx in q:
            if num_wanted == 0:
                break
            if used[idx] < use_limit:
                res += v
                used[idx] += 1
                num_wanted -= 1
        
        return res

# Solution 2, priority queue
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        q = [[-v, idx] for idx, v in zip(labels, values)]
        heapq.heapify(q)
        
        d = collections.Counter()
        res = 0
        
        while q and num_wanted:
            v, idx = heapq.heappop(q)
            v = -v
            if d[idx] < use_limit:
                res += v
                d[idx] += 1
                num_wanted -= 1
        
        return res