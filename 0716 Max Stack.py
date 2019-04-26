import heapq

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

# Solution 2, heapq
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []
        self.ls_d = set()
        self.q = []
        self.q_d = set()
        self.idx = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.ls.append([x, self.idx])
        heapq.heappush(self.q, [-x, -self.idx]) # got-cha, idx needs to be negative so that it is most recent value popped
        self.idx += 1
        

    def pop(self):
        """
        :rtype: int
        """
        self.top()
        x, idx = self.ls.pop()
        self.q_d.add(-idx)
        
        return x

    def top(self):
        """
        :rtype: int
        """
        while self.ls and self.ls[-1][1] in self.ls_d:
            _, idx = self.ls.pop()
            self.ls_d.discard(idx)
        
        v = self.ls[-1][0]
        return v
        

    def peekMax(self):
        """
        :rtype: int
        """
        while self.q and self.q[0][1] in self.q_d:
            _, idx = heapq.heappop(self.q)
            self.q_d.discard(idx)
        
        return -self.q[0][0]

    def popMax(self):
        """
        :rtype: int
        """
        self.peekMax()
        
        x, idx = heapq.heappop(self.q)
        x = -x 
        self.ls_d.add(-idx)
        return x

# Solution 2.1 my own implementation, abstract a "clean" function
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []
        self.ls_d = set()
        self.q = []
        self.q_d = set()
        self.idx = 0
    
    def clean(self):
        while self.ls and self.ls[-1][1] in self.ls_d:
            _, idx = self.ls.pop()
            self.ls_d.discard(idx)
        
        while self.q and self.q[0][1] in self.q_d:
            _, idx = heapq.heappop(self.q)
            self.q_d.discard(idx)
      
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.ls.append([x, self.idx])
        heapq.heappush(self.q, [-x, -self.idx])
        self.idx += 1

    def pop(self):
        """
        :rtype: int
        """
        self.clean()
        x, idx = self.ls.pop()
        self.q_d.add(-idx)
        
        return x

    def top(self):
        """
        :rtype: int
        """
        self.clean()
        return self.ls[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        self.clean()
        return -self.q[0][0]
        
    def popMax(self):
        """
        :rtype: int
        """
        self.clean()
        x, idx = heapq.heappop(self.q)
        self.ls_d.add(-idx)
        
        return -x

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()