import collections

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.d = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.q.append(val)
        self.d[val].add(len(self.q) - 1)
        
        return len(self.d[val]) == 1
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.d:
            return False
        
        # First switch val and last val
        # Then delete. This is error-proof
        val = val
        last_val = self.q[-1]
        val_idx = self.d[val].pop()
        last_idx = len(self.q) - 1
        
        self.d[last_val].discard(last_idx)
        self.d[last_val].add(val_idx)
        
        self.d[val].add(last_idx)
        self.q[val_idx], self.q[last_idx] = self.q[last_idx], self.q[val_idx]
        
        v = self.q.pop()
        self.d[v].discard(len(self.q))
        
        if not self.d[v]:
            del self.d[v]
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.q)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()