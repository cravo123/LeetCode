# Solution 1, not that elegant
class RLEIterator:

    def __init__(self, A: List[int]):
        self.q = A
        self.idx = 0
        self.curr = 0

    def next(self, n: int) -> int:
        while n > 0:
            if self.curr == 0:
                if self.idx >= len(self.q):
                    return -1
                self.curr += self.q[self.idx]
                self.idx += 2
            
            if n <= self.curr:
                self.curr -= n
                return self.q[self.idx - 1]
            else:
                n -= self.curr
                self.curr = 0
        

# Solution 2, simulation using stack
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

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)