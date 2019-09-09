import collections

# Solution 1, use deque to maintain a list of values under consideration
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.max_size = size
        self.curr_size = 0
        self.curr_sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.curr_size += 1
        self.curr_sum += val
        
        if self.curr_size > self.max_size:
            self.curr_size -= 1
            self.curr_sum -= self.q.popleft()
        
        return self.curr_sum / self.curr_size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)