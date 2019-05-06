import collections

# Solution 1, use collections.defaultdict as children
class Node:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(Node)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        
        for c in word:
            p = p.children[c]
        
        p.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        
        return p.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True


# Solution 2, same idea, but use list as children
class Node:
    def __init__(self):
        self.is_word = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        
        for c in word:
            idx = ord(c) - ord('a')
            if p.children[idx] is None:
                p.children[idx] = Node()
            p = p.children[idx]
        
        p.is_word = True       

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        
        for c in word:
            idx = ord(c) - ord('a')
            if p.children[idx] is None:
                return False
            p = p.children[idx]
        
        return p.is_word
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for c in prefix:
            v = ord(c) - ord('a')
            if p.children[v] is None:
                return False
            p = p.children[v]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)