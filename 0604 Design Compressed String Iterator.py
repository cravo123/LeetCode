import collections

# Solution 1, maintain pointer
class StringIterator:

    def __init__(self, compressedString: str):
        self.q = self.parse(compressedString)
        self.idx = 0
        self.curr = 0
    
    def parse(self, s):
        q = []
        i, n = 0, len(s)
        
        while i < n:
            c = s[i]
            i += 1
            v = 0
            while i < n and s[i].isdigit():
                v = v * 10 + int(s[i])
                i += 1
            q.append([c, v])
        return q

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        res = self.q[self.idx - 1][0]
        self.curr -= 1
        
        return res

    def hasNext(self) -> bool:
        self.move()
        
        if self.curr == 0 and self.idx >= len(self.q):
            return False
        return True

    def move(self):
        while self.curr == 0 and self.idx < len(self.q):
            self.curr = self.q[self.idx][1]
            self.idx += 1

# Solution 2, deque is more straigh-forward
class StringIterator:

    def __init__(self, compressedString: str):
        self.q = self.parse(compressedString)
        self.q = collections.deque(self.q)
    
    def parse(self, s):
        q = []
        i, n = 0, len(s)
        
        while i < n:
            c = s[i]
            i += 1
            v = 0
            while i < n and s[i].isdigit():
                v = v * 10 + int(s[i])
                i += 1
            q.append([c, v])
        return q

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        res = self.q[0][0]
        self.q[0][1] -= 1
        
        return res
            

    def hasNext(self) -> bool:
        self.move()
        
        return len(self.q) > 0

    
    def move(self):
        while self.q and self.q[0][1] == 0:
            self.q.popleft()

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()