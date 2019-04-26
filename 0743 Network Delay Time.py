import heapq

# Solution 1, Best-First-Search with priority queue

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = collections.defaultdict(dict)
        
        for u, v, w in times:
            d[u][v] = w
        
        seen = {}
        
        q = [[0, K]]
        
        while q:
            t, i = heapq.heappop(q)
            if i not in seen:
                seen[i] = t        
                for j in d[i]:
                    heapq.heappush(q, [t + d[i][j], j])
        return -1 if len(seen) < N else max(seen.values())

# Solution 2, dijkstra's algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        d = collections.defaultdict(dict)
        
        for u, v, w in times:
            d[u][v] = w
        
        dist = {i:float('inf') for i in range(1, N + 1)}
        dist[K] = 0
        
        q = set(range(1, N + 1))
        
        while q:
            u = None
            
            for v in q:
                if u is None or dist[v] < dist[u]:
                    u = v
            q.discard(u)
            
            for v in q:
                dist[v] = min(dist[v], dist[u] + (d[u][v] if u in d and v in d[u] else float('inf')))
            
        res = max(dist.values())
        
        return res if res < float('inf') else -1