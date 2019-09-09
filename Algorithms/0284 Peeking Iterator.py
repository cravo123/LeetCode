# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# self.q is a buffer to store next element
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.q = []
        self.it = iterator
        self._advance()

    def _advance(self):
        if not self.q and self.it.hasNext():
            self.q.append(self.it.next())
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        self._advance()
        
        return self.q[0]

    def next(self):
        """
        :rtype: int
        """
        res = self.q.pop()
        self._advance()
        
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        self._advance()
        return len(self.q) > 0

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].