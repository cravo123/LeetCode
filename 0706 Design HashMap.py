# Real solution should also consider resizing, and use linked list for each position.
# Here we use list as an alternative.
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 10000
        self.q = [[] for _ in range(self.base)]
    
    def _hash(self, key):
        return key % self.base
    
    def _contain(self, key):
        hash_val = self._hash(key)
        
        for i, c in enumerate(self.q[hash_val]):
            if c[0] == key:
                return i, hash_val
        return -1, hash_val
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx, hash_val = self._contain(key)
        
        if idx == -1:
            self.q[hash_val].append([key, value])
        else:
            self.q[hash_val][idx][1] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx, hash_val = self._contain(key)
        if idx == -1:
            return -1
        
        for key_, val in self.q[hash_val]:
            if key_ == key:
                return val
        
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx, hash_val = self._contain(key)
        if idx == -1:
            return
        
        for i, (key_, val) in enumerate(self.q[hash_val]):
            if key_ == key:
                self.q[hash_val].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)