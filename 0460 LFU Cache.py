import collections
# Use DLL to store nodes for the same frequency
# Use collections.defaultdict(DLL) to maintain frequency list
# In order to do in O(1), we need to maintain min_freq
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def is_empty(self):
        return self.head.next == self.tail
    
    def extract_node(self, curr_node):
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
        
        curr_node.prev = None
        curr_node.next = None

    def append_node(self, curr_node):
        curr_node.prev = self.tail.prev
        curr_node.prev.next = curr_node
        curr_node.next = self.tail
        curr_node.next.prev = curr_node

    def remove_node(self):
        curr_node = self.head.next
        self.extract_node(curr_node)
        
        return curr_node
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.key_2_node = {}
        self.freq_2_dll = collections.defaultdict(DLL)
        self.min_freq = 0
    
    def get_node(self, key):
        curr_node = self.key_2_node[key]
        old_freq = curr_node.freq
        curr_node.freq = old_freq + 1
        dll = self.freq_2_dll[old_freq]
        dll.extract_node(curr_node)
        
        if dll.is_empty():
            del self.freq_2_dll[old_freq]
            if self.min_freq == old_freq:
                self.min_freq += 1
        
        new_freq = old_freq + 1
        dll = self.freq_2_dll[new_freq]
        dll.append_node(curr_node)
        
        return curr_node
    
    def get(self, key: int) -> int:
        if key not in self.key_2_node:
            return -1
        
        curr_node = self.get_node(key)
        
        return curr_node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_2_node:
            curr_node = self.get_node(key)
            curr_node.val = value
        else:
            if self.curr_size == self.capacity:
                dll = self.freq_2_dll[self.min_freq]
                remove_node = dll.remove_node()
                del self.key_2_node[remove_node.key]
                if dll.is_empty():
                    del self.freq_2_dll[self.min_freq]
            else:
                self.curr_size += 1
            new_node = Node(key, value)
            self.key_2_node[key] = new_node
            self.min_freq = 1
            self.freq_2_dll[self.min_freq].append_node(new_node)
                


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)