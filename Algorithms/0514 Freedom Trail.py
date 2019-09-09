import collections
import heapq

# Solution 1, DP, t.b.c


# Solution 2, brute force BFS implemented with priority queue
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        
        d = collections.defaultdict(list) # char -> idx
        for i, c in enumerate(ring):
            d[c].append(i)
        
        q = [[0, 0, 0]] # steps, idx of key, ring position
        
        while q:
            steps, idx, pos = heapq.heappop(q)
            if idx == len(key):
                return steps
            
            if ring[pos] == key[idx]:
                idx += 1
                steps += 1
                heapq.heappush(q, [steps, idx, pos])
            
            steps += 1
            for v in [-1, 1]:
                t = (pos + v) % n if pos + v >= 0 else (pos + v + n)
                heapq.heappush(q, [steps, idx, t])