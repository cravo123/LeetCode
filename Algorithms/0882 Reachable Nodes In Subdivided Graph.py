import collections
import heapq

# Solution 1, Dijkstra's Algorithm
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        d = collections.defaultdict(dict)
        
        for i, j, k in edges:
            d[i][j] = d[j][i] = k
        
        res = 0
        seen = set()
        
        q = [[-M, 0]]
        
        while q:
            # Cuz we are using priority queue here
            # It is guaranteed that when we reach an unvisited point,
            # We have maximum remaining steps
            move, i = heapq.heappop(q)
            move = -move
            if i in seen:
                continue
            seen.add(i)
            res += 1
            
            for j in d[i]:
                # d[i][j] could be zero, meaning all interval nodes have been visited
                res += min(move, d[i][j])
                if j not in seen and move > d[i][j]:
                    heapq.heappush(q, [-(move - d[i][j] - 1), j])
                # gotcha, need to calculate this wheather reachable or not
                d[j][i] -= min(move, d[i][j]) # how many internal points remained
                
        
        return res