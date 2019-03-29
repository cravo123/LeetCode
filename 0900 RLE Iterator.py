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
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)