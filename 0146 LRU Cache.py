# Use Double-Linked-List to implement LRU Cache
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def extract(self, curr_node):
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
        curr_node.prev = None
        curr_node.next = None
    
    def append(self, curr_node):
        curr_node.prev = self.tail.prev
        curr_node.prev.next = curr_node
        curr_node.next = self.tail
        curr_node.next.prev = curr_node

    def remove_oldest(self):
        curr_node = self.head.next
        self.extract(curr_node)
        
        return curr_node

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.curr_size = 0
        self.key_2_node = {}
        self.dll = DLL()
    
    def get_node(self, key):
        curr_node = self.key_2_node[key]
        self.dll.extract(curr_node)
        self.dll.append(curr_node)
        
        return curr_node
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key not in self.key_2_node:
            return -1
        
        curr_node = self.get_node(key)
        res = curr_node.val
        
        return res
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key_2_node:
            curr_node = self.get_node(key)
            curr_node.val = value
        else:
            self.curr_size += 1
            new_node = Node(key, value)
            self.key_2_node[key] = new_node
            self.dll.append(new_node)
            
            if self.curr_size > self.capacity:
                self.curr_size -= 1
                old_node = self.dll.remove_oldest()
                del self.key_2_node[old_node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)