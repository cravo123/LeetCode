# Solution 1, plain deque
import collections

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

# Solution 2, this one is much more elegant, similar to hit counter



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

