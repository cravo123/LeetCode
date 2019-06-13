# Solution 1, use a list of length 300 to cache hit history
# Similar to LC 0933 Number of Recent Calls
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 300
        self.times = [0 for _ in range(self.size)]
        self.hits = self.times[::]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % self.size
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 0
        self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for i in range(self.size):
            if self.times[i] + self.size > timestamp:
                res += self.hits[i]
        
        return res

# Solution 2, vanilla deque 
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.size = 300
        
    def _clean(self, timestamp):
        while self.q and self.q[0] + self.size <= timestamp:
            self.q.popleft()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self._clean(timestamp)
        
        return len(self.q)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)