import collections
import heapq

# Solution 1, Dijkstra's Algorithm
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        d = collections.defaultdict(dict)
        
        for u, v, w in flights:
            d[u][v] = w
        
        q = [[0, 0, src]]
        while q:
            cost, stops, curr = heapq.heappop(q)
            if curr == dst:
                return cost
            if stops <= K:
                for j in d[curr]:
                    heapq.heappush(q, [cost + d[curr][j], stops + 1, j])
        
        return -1