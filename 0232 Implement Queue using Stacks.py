class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_s = []
        self.out_s = []
        
    def clean(self):
        if not self.out_s:
            while self.in_s:
                self.out_s.append(self.in_s.pop())
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_s.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.clean()
        
        return self.out_s.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.clean()
        
        return self.out_s[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.in_s) == 0 and len(self.out_s) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()