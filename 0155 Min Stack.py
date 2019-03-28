# Two-stack solution
# One-stack solution is more complex.
# Another idea is save [curr_val, curr_min] as a single element to a stack
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.min_vals = []

    def push(self, x: int) -> None:
        self.q.append(x)
        
        if not self.min_vals or self.min_vals[-1] >= x:
            self.min_vals.append(x)

    def pop(self) -> None:
        x = self.q.pop()
        if x == self.min_vals[-1]:
            self.min_vals.pop()
        

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()