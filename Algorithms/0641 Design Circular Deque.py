class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k + 1
        self.q = [None for _ in range(k + 1)]
        self.head = 0
        self.tail = 1
    
    def index(self, i):
        return (i + self.size) % self.size
    
    def get_val(self, idx):
        return self.q[self.index(idx)]
    
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.q[self.head] = value
        self.head = self.index(self.head - 1)
        return True
    

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        self.q[self.tail] = value
        self.tail = self.index(self.tail + 1)
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head = self.index(self.head + 1)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = self.index(self.tail - 1)
        return True
        
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        
        return self.get_val(self.head + 1)

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.get_val(self.tail - 1)

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return (self.head + 1 - self.tail) % self.size == 0    

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.tail - self.head) % self.size == 0
        
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()