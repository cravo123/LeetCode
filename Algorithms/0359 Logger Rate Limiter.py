import collections

# Solution 1, plain deque
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.d = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while self.q and self.q[0][0] + 10 <= timestamp:
            self.d.discard(self.q.popleft()[1])
        
        if message in self.d:
            return False
        self.d.add(message)
        self.q.append([timestamp, message])
        
        return True

# Solution 2, this one is much more elegant, 
# similar to LC 0362 Design Hit Counter
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10
        self.times = [0 for _ in range(self.size)]
        self.d = collections.defaultdict(set)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        t = timestamp % self.size
        if timestamp != self.times[t]:
            self.d[t] = set()
            self.times[t] = timestamp
            
        for i in range(self.size):
            if self.times[i] + 10 > timestamp and message in self.d[i]:
                return False
        
        self.d[t].add(message)
        
        return True

# Solution 2.1, similar idea
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10
        self.q = [[0, set()] for _ in range(self.size)]
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        for t, msgs in self.q:
            if abs(t - timestamp) < 10 and message in msgs:
                return False
        
        idx = timestamp % self.size
        if self.q[idx][0] == timestamp:
            self.q[idx][1].add(message)
        else:
            self.q[idx][0] = timestamp
            self.q[idx][1] = set([message])
        
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

