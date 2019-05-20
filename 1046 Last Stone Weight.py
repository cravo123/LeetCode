import heapq

# Solution 1, priority queue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-s for s in stones]
        heapq.heapify(q)
        
        while len(q) > 1:
            x, y = heapq.heappop(q), heapq.heappop(q)
            if x == y:
                continue
            else:
                heapq.heappush(q, -abs(x - y))
        
        return -q.pop() if q else 0