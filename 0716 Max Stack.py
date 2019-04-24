# Solution 1, maintain current max
# but watch-out for popmax
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = [[float('-inf'), float('-inf')]]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curr_max = max(self.q[-1][1], x)
        self.q.append([x, curr_max])

    def pop(self):
        """
        :rtype: int
        """
        v, _ = self.q.pop()
        return v

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.q[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        v = self.q[-1][1]
        t = []
        
        while self.q and self.q[-1][0] != v:
            t.append(self.q.pop())
        self.q.pop()
        
        # got-cha 
        for x, _ in reversed(t):
            self.push(x)
        
        return v

# Solution 2


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()