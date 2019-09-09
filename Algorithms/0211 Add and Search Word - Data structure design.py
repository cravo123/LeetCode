import collections
import string

# Similar to LC 0677 Map Sum Pairs
# Solution 1, Trie
# Delegation makes implementation easier.
# Delegate word_add and word_search to Trie()
class Node:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        curr = self.root
        
        for c in word:
            curr = curr.children[c]
        curr.is_word = True
    
    def dfs(self, curr, idx, word):
        if idx == len(word):
            return curr.is_word
        
        c = word[idx]
        if c != '.':
            if c not in curr.children:
                return False
            return self.dfs(curr.children[c], idx + 1, word)
        else:
            for c in curr.children:
                if self.dfs(curr.children[c], idx + 1, word):
                    return True
            return False
    
    def search(self, word):
        curr = self.root
        
        return self.dfs(curr, 0, word)

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.add_word(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word)

# Solution 2, DFS
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.d.add(word)
    
    def dfs(self, idx, path, word):
        if idx == len(word):
            return ''.join(path) in self.d
        
        if word[idx] != '.':
            path.append(word[idx])
            res = self.dfs(idx + 1, path, word)
            path.pop()
            return res
        else:
            for c in string.ascii_lowercase:
                path.append(c)
                if self.dfs(idx + 1, path, word):
                    path.pop()
                    return True
                path.pop()
        return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        path = []
        return self.dfs(0, path, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)