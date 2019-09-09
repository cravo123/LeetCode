# hashmap has two ways to handle collision, open addressing and chaining.
# Chaining, each position in the array is a linked list to store (key, val) pair.
# Open addressing, when collision happens, it will move to next available position,
# and when we remove a (key, val) pair, it will set a tombstone to occupy the position.
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 10013
        self.q = [[] for _ in range(self.base)]
    
    def _hash(self, key):
        return key % self.base
    
    def add(self, key: int) -> None:
        if not self.contains(key):
            hash_val = self._hash(key)
            self.q[hash_val].append(key)

    def remove(self, key: int) -> None:
        
        if self.contains(key):
            hash_val = self._hash(key)
            self.q[hash_val].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_val = self._hash(key)
        return key in self.q[hash_val]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)