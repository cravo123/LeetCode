import collections
import heapq

# Solution 1, cache all frequencies
# Note the difference between LFU, LRU and this problem
class FreqStack:

    def __init__(self):
        self.d = collections.defaultdict(list)
        self.freq = collections.Counter() # key -> cnt
        self.max_freq = 0
        
    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.d[self.freq[x]].append(x)
        self.max_freq = max(self.max_freq, self.freq[x])
        
    def pop(self) -> int:
        x = self.d[self.max_freq].pop()
        if not self.d[self.max_freq]:
            del self.d[self.max_freq]
            self.max_freq -= 1
        self.freq[x] -= 1
        
        return x

# Solution 2, priority queue
# self.idx is used for returning most recent value if there
# is a tie in frequency
class FreqStack:

    def __init__(self):
        self.q = []
        self.idx = 0
        self.freq = collections.Counter() # key -> cnt
        
    def push(self, x: int) -> None:
        self.freq[x] += 1
        heapq.heappush(self.q, [-self.freq[x], -self.idx, x])
        self.idx += 1

    def pop(self) -> int:
        _, _, x = heapq.heappop(self.q)
        self.freq[x] -= 1
        
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()