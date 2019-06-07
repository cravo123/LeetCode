import collections
import heapq

# Solution 1, count occurrence and sort
# Complexity, O(nlogn)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)
        
        res = [(-value, key) for key, value in d.items()]
        res.sort()
        res = [x[1] for x in res][:k]
        
        return res

# Solution 1.1, priority queue to reduce complexity
# O(nlogk)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.Counter(words)
        
        q = [(-cnt, word) for word, cnt in d.items()]
        
        heapq.heapify(q)
        
        res = [heapq.heappop(q)[1] for _ in range(k)]
        
        return res