from collections import deque

# Solution 1, simulation
# Step 1, append new val to the end of queue
# Step 2, pop every value from left except the new val from head of queue, 
#         and append them to the end.
# By doing this, we essentially reverse the order in the queue!
# [4, 3, 2, 1], add 5
# Step 1, [4, 3, 2, 1, 5]
# Step 2, [5, 4, 3, 2, 1]

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q =  deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        n = len(self.q)
        self.q.append(x)
        
        for _ in range(n):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()