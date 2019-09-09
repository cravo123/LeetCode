import collections
import heapq

# Solution 1, simulation
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        d = collections.Counter(hand)
        
        for c in sorted(d):
            v = d[c]
            if v == 0:
                continue
            for x in range(c, c + W):
                d[x] -= v
                if d[x] < 0:
                    return False
        return True

# Solution 2, heapq
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        d = collections.Counter(hand)
        
        q = [[c, v] for c, v in d.items()]
        heapq.heapify(q)
        
        while q:
            if len(q) < W:
                return False
            
            tmp = []
            for i in range(W):
                tmp.append(heapq.heappop(q))
                if i > 0 and tmp[i][0] != tmp[i - 1][0] + 1:
                    return False
            
            need = tmp[0][1]
            for i in range(len(tmp)):
                tmp[i][1] -= need
            
            for c, v in tmp:
                if v < 0:
                    return False
                if v > 0:
                    heapq.heappush(q, [c, v])
        
        return True