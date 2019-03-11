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


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)