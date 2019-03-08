# Solution 1
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.q = v
        self.q_idx = 0
        self.i_idx = 0
    
    def move_idx(self):
        while self.q_idx < len(self.q) and self.i_idx == len(self.q[self.q_idx]):
            self.i_idx = 0
            self.q_idx += 1
        
    def next(self) -> int:
        self.move_idx()
        res = self.q[self.q_idx][self.i_idx]
        self.i_idx += 1
        
        return res

    def hasNext(self) -> bool:
        self.move_idx()
        return self.q_idx != len(self.q)

# Solution 2
from heapq import *

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.q = []
        
        for i, c in enumerate(v):
            if c:
                heappush(self.q, [i, 0])
        
    def next(self) -> int:
        i, idx = heappop(self.q)
        res = self.v[i][idx]
        
        if idx + 1 < len(self.v[i]):
            heappush(self.q, [i, idx + 1])
        
        return res
        

    def hasNext(self) -> bool:
        return len(self.q) > 0

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()