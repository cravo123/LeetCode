import heapq

# Solution 2, priority queue
# O(nlogn), not that efficient but easy to understand
class Solution:
    def candy(self, ratings: List[int]) -> int:
        q = [[r, i] for i, r in enumerate(ratings)]
        
        heapq.heapify(q)
        
        res = 0
        d = {}
        
        while q:
            r, i = heapq.heappop(q)
            curr = 1
            
            if i - 1 in d and ratings[i - 1] < r:
                curr = max(curr, d[i - 1] + 1)
            if i + 1 in d  and ratings[i + 1] < r:
                curr = max(curr, d[i + 1] + 1)
            
            res += curr
            d[i] = curr
        
        return res