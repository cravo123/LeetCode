import collections

# Solution 1, deque
class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self._clean(t)
        self.q.append(t)
        
        return len(self.q)
    
    def _clean(self, t):
        while self.q and self.q[0] + 3000 < t:
            self.q.popleft()

# Solution 2, although TLE, it is actually a better solution for large-scale data
# Similar to LC 0362 Design Hit Counter
class RecentCounter:

    def __init__(self):
        self.size = 3001
        self.q = [float('-inf') for _ in range(self.size)]        

    def ping(self, t: int) -> int:
        # we are sure the original point at this position is outdated, so safe to update
        self.q[t % self.size] = t
        
        res = 0
        for v in self.q:
            if v + self.size - 1 >= t:
                res += 1
        return res


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
