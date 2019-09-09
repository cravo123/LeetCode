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

# Solution 1.1, similar idea, but using iterator is more elegant
# The reason why we add length counter is that there is not easy way to
# determine if an iterator is exhausted or not without using next().
# On the other hand, if we use next(), then we have already consume iterator.
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = collections.deque()
        
        for v in [v1, v2]:
            if v:
                self.q.append([iter(v), len(v)])

    def next(self):
        """
        :rtype: int
        """
        it, cnt = self.q.popleft()
        res = next(it)
        cnt -= 1
        if cnt > 0:
            self.q.append([it, cnt])
        
        return res

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
        self.q = collections.deque()
        self.vs = [v1, v2]
        self.ls = [len(v1), len(v2)]
        
        if len(v1) > 0:
            self.q.append([0, 0])
        if len(v2) > 0:
            self.q.append([0, 1])
        
    def next(self):
        """
        :rtype: int
        """
        i, idx = self.q.popleft()
        res = self.vs[idx][i]
        i += 1
        if i < self.ls[idx]:
            self.q.append([i, idx])
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())