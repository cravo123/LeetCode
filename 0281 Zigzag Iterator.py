# SOlution 1, deque, this is more elegant that indexing
import collections
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = collections.deque()
        for v in [v1, v2]:
            if len(v) > 0:
                self.q.append([v, 0])

    def next(self):
        """
        :rtype: int
        """
        v, idx = self.q.popleft()
        if idx < len(v) - 1:
            self.q.append([v, idx + 1])
        
        return v[idx]

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0
        
# Solution 2, indexing-bases, error-prone
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = [v1, v2]
        self.row = 0
        self.cols = [0, 0]        

    def next(self):
        """
        :rtype: int
        """
        if self.cols[self.row] == len(self.v[self.row]):
            self.row = 1 - self.row
        
        res = self.v[self.row][self.cols[self.row]]
        self.cols[self.row] += 1
        self.row = 1 - self.row
        
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cols[0] < len(self.v[0]) or self.cols[1] < len(self.v[1])

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())