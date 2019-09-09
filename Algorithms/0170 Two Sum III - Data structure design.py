import collections

# If add operation is much more than find
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.Counter()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.d[number] = min(self.d[number] + 1, 2)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for c in self.d:
            v = value - c
            if c == v and self.d[c] > 1:
                return True
            elif c != v and v in self.d:
                return True
        return False

# If find operation is more
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()
        self.sums = set()
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        for c in self.nums:
            self.sums.add(c + number)
        self.nums.add(number)
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        return value in self.sums

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)