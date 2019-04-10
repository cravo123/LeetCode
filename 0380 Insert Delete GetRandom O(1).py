class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.d = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.q.append(val)
        self.d[val] = len(self.q) - 1
        
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        
        last_val = self.q[-1]
        val_idx = self.d[val]
        last_idx = len(self.q) - 1
        
        self.q[val_idx], self.q[last_idx] = self.q[last_idx], self.q[val_idx]
        self.d[val] = last_idx
        self.d[last_val] = val_idx
        
        self.q.pop()
        del self.d[val]
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.q)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()