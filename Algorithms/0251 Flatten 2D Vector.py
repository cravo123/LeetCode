# Solution 1, simulation
# Similar to LC 0900 RLE Iterator
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

# Solution 2, priority queue
# push (idx in v, idx in v[idx]) to heapq
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

# Solution 3, stack simulation
class RLEIterator:

    def __init__(self, A: List[int]):
        self.q = [[A[i], A[i + 1]] for i in range(0, len(A), 2)]
        self.q = self.q[::-1]

    def next(self, n: int) -> int:
        while self.q and self.q[-1][0] < n:
            n -= self.q[-1][0]
            self.q.pop()
        
        if not self.q:
            return -1
        
        self.q[-1][0] -= n
        res = self.q[-1][1]
        
        if self.q[-1][0] == 0:
            self.q.pop()
        
        return res

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()