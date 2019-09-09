import collections

# Solution 1, Trie, similar to LC 0211
class Node:
    def __init__(self):
        self.val = 0
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, key, val):
        curr = self.root
        
        for c in key:
            curr = curr.children[c]
        curr.val = val
    
    def dfs(self, node):
        curr = node
        res = curr.val
        
        for p in curr.children:
            res += self.dfs(curr.children[p])
        
        return res
    
    def sum_prefix(self, prefix):
        curr = self.root
        
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        
        return self.dfs(curr)

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add_word(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.sum_prefix(prefix)

# Solution 2, Brute Force
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        res = sum(self.d[key] for key in self.d if key.startswith(prefix))
        return res



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)