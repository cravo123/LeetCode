import bisect, collections

# Solution 1, binary search
# We can actually store (timestamp, value) instead of two lists
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[], []]
        self.d[key][0].append(timestamp)
        self.d[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ''
        
        idx = bisect.bisect_right(self.d[key][0], timestamp)
        
        if idx == 0:
            return ''
        
        return self.d[key][1][idx - 1]

# Solution 2, store (timestamp, value) pair
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ''
        
        idx = bisect.bisect_right(self.d[key], (timestamp, chr(255)))
        
        if idx == 0:
            return ''
        
        return self.d[key][idx - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)